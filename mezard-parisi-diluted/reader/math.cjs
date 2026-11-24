/* Render every TeX expression at build time, including future annotations. */
const fs = require('node:fs');
const katex = require(process.env.KATEX_PATH || 'katex');
const {expressions, macros} = JSON.parse(fs.readFileSync(0, 'utf8'));
const result = expressions.map(([tex, displayMode]) => {
  try {
    return katex.renderToString(tex, {displayMode, macros, output: 'mathml', strict: 'ignore'});
  } catch (error) {
    throw Error(tex + '\n' + error.message);
  }
});
process.stdout.write(JSON.stringify(result));
