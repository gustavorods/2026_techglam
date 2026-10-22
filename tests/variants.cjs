const fs=require('fs'),vm=require('vm'),assert=require('assert'),path=require('path');
const base=path.resolve(__dirname,'..')+'/';
let url='#produto/glass-glow';
const stored={'techglam-demo-v1':JSON.stringify({guestCart:[{id:'glass-glow',shade:1,qty:2}],accounts:{},session:null})};
const nodes={'#app':{innerHTML:''},'#overlay-root':{innerHTML:''},'#toast-root':{append(){}}};
const sandbox={console,Date,Math,Number,String,Array,JSON,RegExp,URLSearchParams,setTimeout:f=>f(),localStorage:{getItem:k=>stored[k],setItem:(k,v)=>stored[k]=v},document:{body:{style:{}},title:'',createElement:()=>({innerHTML:'',className:'',remove(){}}),querySelector:s=>nodes[s]||null,addEventListener(){}},window:{addEventListener(){},scrollTo(){}},location:{get hash(){return url},set hash(value){url=value}},scrollTo(){}};
vm.createContext(sandbox);
const app=fs.readFileSync(base+'app.js','utf8').replace(/\}\)\(\);\s*$/,'globalThis.TEST={db,ui,render,addToCart,changeQty,totals,productImages,selectedVariant,setDetailImage,itemById};})();');
vm.runInContext(fs.readFileSync(base+'data.js','utf8')+'\n'+app,sandbox);
const T=sandbox.TEST,p=T.itemById('glass-glow'),[berry,pink,nude]=p.variants;

assert.strictEqual(T.db.guestCart[0].variantId,pink.id,'legacy shade should migrate to variant ID');
assert.strictEqual(T.db.guestCart[0].image,pink.images[0].src,'legacy cart should gain variant image');
assert(nodes['#app'].innerHTML.includes('data-variant-id="'+berry.id+'"'),'gallery should bind image to variant ID');

T.setDetailImage(nude.images[0].id);T.render(false);
assert.strictEqual(T.selectedVariant(p).id,nude.id,'gallery navigation should select linked variant');
assert(nodes['#app'].innerHTML.includes('id="shade-label" aria-live="polite">Nude'),'variant label should follow gallery');
assert(nodes['#app'].innerHTML.includes('data-variant-id="'+nude.id+'" class="selected"'),'swatch should follow gallery');

p.variants[2].images.push({id:nude.id+'-detail',src:nude.images[0].src,alt:'Outro ângulo Nude'});
T.setDetailImage(nude.id+'-detail');T.render(false);
assert.strictEqual(T.selectedVariant(p).id,nude.id,'second image of same variant should preserve selection');
T.setDetailImage(berry.images[0].id);T.render(false);
assert.strictEqual(T.selectedVariant(p).id,berry.id);

p.variants[2].price=47.9;
T.addToCart(p.id,nude.id,1);T.addToCart(p.id,nude.id,1);
assert.strictEqual(T.db.guestCart.length,2,'different variants should remain separate');
assert.strictEqual(T.db.guestCart.find(it=>it.variantId===nude.id).qty,2,'same variant should merge');
assert.strictEqual(T.db.guestCart.find(it=>it.variantId===nude.id).unitPrice,47.9);
assert.strictEqual(T.db.guestCart.find(it=>it.variantId===nude.id).image,nude.images[0].src);
assert.strictEqual(T.totals().subtotal,181.6,'totals should use variant price');
T.changeQty(nude.id,nude.id,-1); // unknown product must not affect other lines
assert.strictEqual(T.db.guestCart.find(it=>it.variantId===nude.id).qty,2);
T.changeQty(p.id,nude.id,-1);
assert.strictEqual(T.db.guestCart.find(it=>it.variantId===nude.id).qty,1);

const saved=p.variants;p.variants=[];T.ui.detailProductId=null;T.ui.detailImageId=null;url='#produto/glass-glow';T.render(false);
assert(!nodes['#app'].innerHTML.includes('class="color-picker"'),'product without variants should hide selector');
T.addToCart(p.id,null,1);
assert(T.db.guestCart.some(it=>it.variantId===null),'product without variants should still add');
p.variants=saved;
console.log('Variant gallery, legacy cart, pricing and unvarianted product: PASS');
