const fs=require('fs'),vm=require('vm'),assert=require('assert'),{webcrypto}=require('crypto');
const base=require('path').resolve(__dirname,'..')+'/';let url='#inicio';const nodes={'#app':{innerHTML:''},'#overlay-root':{innerHTML:''},'#toast-root':{append(){}}};const store={};
class FakeForm {constructor(id,fields){this.id=id;this.fields=fields;}reset(){}}
class FakeFormData{constructor(form){this.form=form;}entries(){return Object.entries(this.form.fields).values();}}
const sandbox={console,Date,Math,Number,String,Array,JSON,RegExp,URLSearchParams,TextEncoder,Uint8Array,crypto:webcrypto,HTMLFormElement:FakeForm,FormData:FakeFormData,localStorage:{getItem:k=>store[k],setItem:(k,v)=>store[k]=v},setTimeout:f=>f(),document:{body:{style:{}},title:'',createElement:()=>({innerHTML:'',className:'',remove(){}}),querySelector:s=>nodes[s]||null,addEventListener:()=>{}},window:{addEventListener:()=>{},scrollTo:()=>{}},location:{get hash(){return url},set hash(x){url=x.startsWith('#')?x:'#'+x}},scrollTo:()=>{}};
vm.createContext(sandbox);
let app=fs.readFileSync(base+'app.js','utf8').replace(/\}\)\(\);\s*$/,'globalThis.TEST={db,ui,addToCart,totals,account,favorite,handleSubmit,handleClick,goto,render};})();');
vm.runInContext(fs.readFileSync(base+'data.js','utf8')+'\n'+app,sandbox);
const T=sandbox.TEST;
for(const route of ['inicio','catalogo','ofertas','produto/glass-glow','lila','sobre','contato','carrinho','favoritos','checkout','login','conta']){url='#'+route;T.render(false);assert(nodes['#app'].innerHTML.includes('<main>'),'Falha na rota '+route);}
url='#inicio';console.log('12 rotas principais: PASS');
async function send(id,fields){await T.handleSubmit({target:new FakeForm(id,fields),preventDefault(){}})}
async function main(){
 T.addToCart('glass-glow',0,2);T.addToCart('paleta-aura',0,1);T.favorite('glass-glow');
 T.ui.authReturn='checkout';
 await send('register-form',{name:'Maria Teste',email:'maria@example.com',password:'TesteLocal@2026'});
 assert(T.db.session==='maria@example.com','should have logged in');assert(T.account().cart.length===2,'guest cart preserved');assert(T.account().favorites.includes('glass-glow'),'guest fav preserved');
 url='#checkout';T.render(false);assert(nodes['#app'].innerHTML.includes('Itens do pedido'),'checkout item review');assert(nodes['#app'].innerHTML.includes('Cor: Berry'),'checkout variant review');
 T.db.coupon='BEMVINDA10';const first=T.totals();
 assert(first.couponRate===.10 && first.first && first.ship===0,'first order coupon and shipping');
 await send('checkout-form',{name:'Maria Teste',phone:'(11) 99999-0000',cep:'01234-567',number:'123',street:'Rua das Flores',city:'São Paulo',state:'SP',payment:'Pix demonstrativo'});
 assert(T.account().orders.length===1,'order stored');assert(T.account().cart.length===0,'cart reset');assert(url==='#pedido','success route');
 const bought=T.account().orders[0].items[0];assert(bought.variantId==='glass-glow-berry','order variant retained');assert(bought.variantName==='Berry','order variant name retained');assert(bought.image.includes('glass-glow-berry.svg'),'order variant image retained');
 console.log('register, cart migration, coupon, checkout: PASS');
 T.db.session=null;
 await send('login-form',{email:'maria@example.com',password:'senhaerrada'});
 assert(T.db.session===null,'bad password rejected');
 await send('login-form',{email:'maria@example.com',password:'TesteLocal@2026'});
 assert(T.db.session==='maria@example.com','correct password accepted');
 assert(T.account().orders.length===1,'orders retained');
 console.log('password verification & account persistence: PASS');
 await send('recover-form',{email:'maria@example.com',password:'NovaSenha2026!'});
 T.db.session=null;
 await send('login-form',{email:'maria@example.com',password:'NovaSenha2026!'});
 assert(T.db.session==='maria@example.com','new password works');
 console.log('local recovery simulation: PASS');
 console.log('FULL DEMO FLOW OK');
}
main().catch(e=>{console.error(e);process.exit(1)});
