const fs = require('fs');
const path = require('path');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const products = vm.runInNewContext(fs.readFileSync(path.join(root, 'data.js'), 'utf8') + '\nPRODUCTS');
const output = path.join(root, 'assets', 'variants');
fs.mkdirSync(output, {recursive: true});

for (const product of products) {
 const original = fs.readFileSync(path.join(root, 'assets', `${product.id}.svg`), 'utf8');
 const sourceColor = product.id === 'lumi-mirror' ? '#B48AE8' : product.shades[0];
 for (const variant of product.variants) {
  let svg = original.replaceAll(sourceColor, variant.swatch);
  // A ilustração do espelho usa a cor original somente no halo.
  if (product.id === 'lumi-mirror') svg = svg.replace('fill="#ddc9df"', `fill="${variant.swatch}"`);
  svg = svg.replace('aria-label="Produto cosmético TechGlam ilustrado"', `aria-label="${product.name} na opção ${variant.name}"`);
  const target = path.join(output, `${variant.id}.svg`);
  fs.writeFileSync(target, svg, 'utf8');
}
}
console.log(`Imagens de ${products.reduce((count, product) => count + product.variants.length, 0)} variantes geradas.`);
