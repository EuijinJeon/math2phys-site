// Run with a downloaded public https://incredible.pm/logic.js as argv[2].
// No calculus is formalized: PM is supplied as a trusted inference rule.
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');

if (!process.argv[2]) throw new Error('Usage: node run-incredible.cjs /path/to/logic.js');
const source = fs.readFileSync(process.argv[2], 'utf8');
const packet = JSON.parse(fs.readFileSync(path.join(__dirname, 'incredible-pm-interface.json')));
let ready;
const initialized = new Promise(resolve => { ready = resolve; });
const timers = new Set();
const sandbox = {
  console,
  setTimeout: (fn, ms, ...args) => { const t = setTimeout(fn, ms, ...args); timers.add(t); return t; },
  clearTimeout,
  setInterval: (fn, ms, ...args) => { const t = setInterval(fn, ms, ...args); timers.add(t); return t; },
  clearInterval,
  performance, TextEncoder, TextDecoder,
  $: {holdReady: value => { if (value === false) ready(); }},
};
sandbox.window = sandbox;
vm.createContext(sandbox);

function analyze(value, fn = 'incredibleLogic') {
  // Construct arguments in the VM realm: GHCJS distinguishes JS constructors.
  const expression = `JSON.stringify(${fn}(...JSON.parse(${JSON.stringify(JSON.stringify([value.context, value.proof]))})))`;
  const result = JSON.parse(vm.runInContext(expression, sandbox, {timeout: 10000}));
  if (typeof result === 'string') throw new Error(result);
  return result;
}

(async () => {
  const deadline = setTimeout(() => { throw new Error('Engine initialization timed out'); }, 10000);
  try {
    vm.runInContext(source, sandbox, {timeout: 10000});
    await initialized;
    const result = {engineUrl: 'https://incredible.pm/logic.js',
      engineSha256: crypto.createHash('sha256').update(source).digest('hex'),
      scope: 'Opaque proposition atoms and a trusted PM rule. No analysis/calculus verification.', cases: {}};
    result.cases.full = analyze(packet);
    assert.equal(result.cases.full.qed, true);

    const missing = structuredClone(packet);
    delete missing.proof.connections.tilt;
    result.cases.missing_e2 = analyze(missing);
    assert.equal(result.cases.missing_e2.qed, false);
    assert(result.cases.missing_e2.unconnectedGoals.some(p => p.block === 'pm' && p.port === 'tilt'));

    const mismatch = structuredClone(packet);
    mismatch.proof.connections.tilt.from.block = 'a_rec';
    result.cases.wrong_e2 = analyze(mismatch);
    assert.equal(result.cases.wrong_e2.qed, false);
    assert.equal(result.cases.wrong_e2.connectionStatus.tilt, 'failed');

    // Erase the depth distinction solely to test an otherwise matching self-loop.
    const loop = structuredClone(packet);
    loop.context.rules[0].ports.next.proposition = 'CurrentDerivativeBound';
    loop.proof.blocks.c_next.conclusion = 'CurrentDerivativeBound';
    loop.proof.connections.ih.from = {block: 'pm', port: 'next'};
    result.cases.naive_induction_loop = analyze(loop);
    assert.equal(result.cases.naive_induction_loop.qed, false);
    assert(result.cases.naive_induction_loop.cycles.length > 0);

    // A deliberately unproved, zero-premise PM rule is accepted as part of context.
    const admitted = structuredClone(packet);
    for (const key of ['frame', 'rec', 'tilt', 'bounds', 'ih']) {
      delete admitted.context.rules[0].ports[key];
      delete admitted.proof.connections[key];
    }
    result.cases.unproved_rule_control = analyze(admitted);
    assert.equal(result.cases.unproved_rule_control.qed, true);

    // Wrap only the selected internal block, leaving its boundary ports exposed.
    const selected = structuredClone(packet);
    selected.proof = {blocks: {pm: selected.proof.blocks.pm}, connections: {}};
    result.abstractedRule = analyze(selected, 'incredibleNewRule');
    assert.equal(Object.keys(result.abstractedRule.ports).length, 7);
    fs.writeFileSync(path.join(__dirname, 'incredible-results.json'), JSON.stringify(result, null, 2) + '\n');
    console.log(JSON.stringify(Object.fromEntries(Object.entries(result.cases).map(([k,v]) => [k, {qed:v.qed, cycles:v.cycles.length, unconnectedGoals:v.unconnectedGoals}]))));
  } finally {
    clearTimeout(deadline);
    for (const timer of timers) { clearTimeout(timer); clearInterval(timer); }
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
