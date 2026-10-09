/* Catálogo demonstrativo: valores, imagens, avaliações e estoques fictícios. */
const PRODUCTS = [
 {id:'blush-velvet',name:'Blush Stick Velvet Bloom',category:'Blush em bastão',desc:'Cor cremosa que se funde à pele.',price:49.90,oldPrice:59.90,shades:['#D7889C','#BD7082','#955F6E'],shadeNames:['Rosé','Malva','Ameixa'],tone:'rosados',stock:18,rating:4.9,reviews:128,popularity:99,new:false,tag:'Mais vendido'},
 {id:'paleta-aura',name:'Paleta de Blush Aura Rosé',category:'Paletas de blush',desc:'Dois tons para um glow sem esforço.',price:89.90,oldPrice:null,shades:['#D88AAB','#C87982','#AE6C8D'],shadeNames:['Rosé','Bloom','Berry'],tone:'rosados',stock:13,rating:4.9,reviews:95,popularity:92,new:true,tag:'Lançamento'},
 {id:'cloud-tint',name:'Blush Líquido Cloud Tint',category:'Blush líquido',desc:'Pigmentação suave, construível e leve.',price:56.90,oldPrice:null,shades:['#CF728B','#DD987B','#A45F6F'],shadeNames:['Petal','Peach','Berry'],tone:'rosados',stock:24,rating:4.8,reviews:87,popularity:91,new:false,tag:'Mais vendido'},
 {id:'glass-glow',name:'Lip Oil Glass Glow',category:'Lip oil',desc:'Hidratação e brilho espelhado.',price:42.90,oldPrice:51.90,shades:['#B86591','#D990A3','#BA7468'],shadeNames:['Berry','Pink','Nude'],tone:'rosados',stock:35,rating:5.0,reviews:203,popularity:100,new:false,tag:'-17%'},
 {id:'crystal-kiss',name:'Lip Gloss Crystal Kiss',category:'Lip gloss',desc:'Lábios luminosos com conforto.',price:39.90,oldPrice:null,shades:['#C65E91','#E4A6B4','#C18B8A'],shadeNames:['Rose','Clear','Nude'],tone:'rosados',stock:11,rating:4.8,reviews:77,popularity:83,new:true,tag:'Lançamento'},
 {id:'stellar-nude',name:'Paleta Stellar Nude',category:'Paletas de maquiagem',desc:'Nove cores versáteis para todo dia.',price:119.90,oldPrice:139.90,shades:['#B78E84','#C2A1A0','#9E7196'],shadeNames:['Nude','Soft','Mauve'],tone:'neutros',stock:10,rating:4.9,reviews:65,popularity:86,new:false,tag:'Oferta'},
 {id:'soft-touch',name:'Kit Pincéis Soft Touch',category:'Pincéis e esponjas',desc:'Três essenciais para uma pele linda.',price:74.90,oldPrice:null,shades:['#A46C91','#8A5E71'],shadeNames:['Lavender','Rosé'],tone:'neutros',stock:20,rating:4.7,reviews:49,popularity:73,new:false,tag:''},
 {id:'cloud-puff',name:'Esponja Cloud Puff',category:'Pincéis e esponjas',desc:'Aplicação uniforme e acabamento natural.',price:28.90,oldPrice:null,shades:['#DDB6D4','#C8AEDC'],shadeNames:['Pink','Lilac'],tone:'neutros',stock:55,rating:4.8,reviews:72,popularity:72,new:false,tag:''},
 {id:'lumi-mirror',name:'Espelho LED Lumi Mirror',category:'Tecnologia & acessórios',desc:'Sua iluminação perfeita em qualquer lugar.',price:189.90,oldPrice:null,shades:['#C5AFDA','#F6E5F5'],shadeNames:['Lilac','Pearl'],tone:'neutros',stock:8,rating:4.8,reviews:18,popularity:64,new:true,tag:'Tech favorite'},
 {id:'coral-crush',name:'Blush Stick Coral Crush',category:'Blush em bastão',desc:'Um toque quente e radiante.',price:49.90,oldPrice:null,shades:['#DA7E6C','#C87A67','#A85B59'],shadeNames:['Coral','Peach','Terracota'],tone:'quentes',stock:16,rating:4.7,reviews:42,popularity:77,new:true,tag:'Novidade'},
 {id:'cherry-aura',name:'Lip Oil Cherry Aura',category:'Lip oil',desc:'Brilho translúcido com toque cereja.',price:42.90,oldPrice:null,shades:['#B54364','#A53E57','#D1738B'],shadeNames:['Cherry','Red','Rose'],tone:'vibrantes',stock:21,rating:4.9,reviews:61,popularity:80,new:true,tag:'Lançamento'},
 {id:'sunset-edit',name:'Paleta Sunset Edit',category:'Paletas de blush',desc:'Do pêssego ao terracota em um estojo.',price:89.90,oldPrice:109.90,shades:['#D99D77','#C88172','#B26868'],shadeNames:['Sunset','Peach','Copper'],tone:'quentes',stock:7,rating:4.6,reviews:37,popularity:65,new:false,tag:'Oferta'},
 {id:'berry-glaze',name:'Lip Gloss Berry Glaze',category:'Lip gloss',desc:'Cor intensa com acabamento luminoso.',price:39.90,oldPrice:null,shades:['#8B416D','#A65C77','#C26E83'],shadeNames:['Berry','Grape','Rose'],tone:'vibrantes',stock:0,rating:4.8,reviews:51,popularity:71,new:false,tag:'Esgotado'},
 {id:'lilac-galaxy',name:'Paleta Lilac Galaxy',category:'Paletas de maquiagem',desc:'Tons lilás e neutros para criar.',price:129.90,oldPrice:null,shades:['#9574C8','#B59CCF','#CAA9BC'],shadeNames:['Lilac','Moon','Soft'],tone:'vibrantes',stock:14,rating:4.8,reviews:33,popularity:76,new:true,tag:'Lançamento'},
 {id:'glow-duo',name:'Duo Pincéis Glow Artist',category:'Pincéis e esponjas',desc:'Precisão e maciez em cada pincelada.',price:54.90,oldPrice:null,shades:['#B6A0CD','#D5BDD6'],shadeNames:['Lilac','Pink'],tone:'neutros',stock:27,rating:4.7,reviews:25,popularity:60,new:false,tag:''},
 {id:'smart-clean',name:'Lumi Skin Clean',category:'Tecnologia & acessórios',desc:'Acessório de autocuidado com design smart.',price:159.90,oldPrice:179.90,shades:['#CFACDA','#D7C1E4'],shadeNames:['Lilac','Soft'],tone:'neutros',stock:6,rating:4.6,reviews:17,popularity:57,new:false,tag:'Oferta'}
];
const CATEGORIES = ['Blush em bastão','Paletas de blush','Blush líquido','Lip oil','Lip gloss','Paletas de maquiagem','Pincéis e esponjas','Tecnologia & acessórios'];
const CATEGORY_FEATURES = [
 {name:'Blush em bastão',product:'blush-velvet',subtitle:'Cor natural'},
 {name:'Paletas de blush',product:'paleta-aura',subtitle:'Duas vezes mais glow'},
 {name:'Blush líquido',product:'cloud-tint',subtitle:'Leveza na pele'},
 {name:'Lip oil',product:'glass-glow',subtitle:'Brilho & cuidado'},
 {name:'Paletas de maquiagem',product:'stellar-nude',subtitle:'Infinitas combinações'},
 {name:'Acessórios',category:'Pincéis e esponjas',product:'soft-touch',subtitle:'Seu ritual completo'}
];
const QUESTIONS = [
 {title:'Qual intensidade de maquiagem você mais gosta?',options:['Leve e natural','Média, equilibrada','Marcante e expressiva']},
 {title:'Quando você costuma se maquiar?',options:['No dia a dia','Em ocasiões especiais','Um pouco dos dois']},
 {title:'Quais tons mais combinam com seu estilo?',options:['Neutros e terrosos','Rosados e delicados','Quentes e solares','Vibrantes e criativos']},
 {title:'Qual produto não pode faltar na sua nécessaire?',options:['Blush','Produto para lábios','Paleta de sombras','Pincéis e acessórios']},
 {title:'Qual acabamento você prefere?',options:['Matte aveludado','Natural / acetinado','Iluminado / glow']},
 {title:'Quanto tempo você dedica à maquiagem?',options:['Até 5 minutos','Entre 5 e 15 minutos','Mais de 15 minutos']}
];
