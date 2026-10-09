from pathlib import Path
from html import escape
P=Path(__file__).resolve().parent.parent/'assets'
P.mkdir(exist_ok=True)
products=[
('blush-velvet','stick','#DA8A9F','TechGlam'),('paleta-aura','palette','#D88AAB','TechGlam'),('cloud-tint','liquid','#CF728B','TechGlam'),('glass-glow','lipoil','#B86591','TechGlam'),('crystal-kiss','gloss','#C65E91','TechGlam'),('stellar-nude','eye','#B78E84','TechGlam'),('soft-touch','brush','#A46C91','TechGlam'),('cloud-puff','sponge','#DDB6D4','TechGlam'),('lumi-mirror','device','#B48AE8','TechGlam'),('coral-crush','stick','#DA7E6C','TechGlam'),('cherry-aura','lipoil','#B54364','TechGlam'),('sunset-edit','palette','#D99D77','TechGlam'),('berry-glaze','gloss','#8B416D','TechGlam'),('lilac-galaxy','eye','#9574C8','TechGlam'),('glow-duo','brush','#B6A0CD','TechGlam'),('smart-clean','device','#CFACDA','TechGlam')]

def frame(inner,color,word):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 440" role="img" aria-label="Produto cosmético TechGlam ilustrado"><defs>
 <linearGradient id="metal" x1="0" x2="1" y2="1"><stop stop-color="#fefcff"/><stop offset=".28" stop-color="#bea6cf"/><stop offset=".53" stop-color="#faf4ff"/><stop offset=".78" stop-color="#96809f"/><stop offset="1" stop-color="#e7cfe9"/></linearGradient>
 <linearGradient id="glass" x1="0" x2="1" y2=".2"><stop stop-color="#fff" stop-opacity=".83"/><stop offset=".22" stop-color="{color}" stop-opacity=".8"/><stop offset=".72" stop-color="{color}" stop-opacity=".95"/><stop offset="1" stop-color="#fff" stop-opacity=".65"/></linearGradient>
 <linearGradient id="product" x1="0" x2="1" y2="1"><stop stop-color="#fefefe"/><stop offset=".24" stop-color="#d9c7e2"/><stop offset=".52" stop-color="#fffaff"/><stop offset="1" stop-color="#a08aa9"/></linearGradient>
 <linearGradient id="deep" x1="0" x2="1" y2="1"><stop stop-color="#443746"/><stop offset=".55" stop-color="#1e1826"/><stop offset="1" stop-color="#736079"/></linearGradient>
 <radialGradient id="halo"><stop stop-color="#fff" stop-opacity=".65"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>
 <filter id="shadow" x="-60%" y="-60%" width="220%" height="240%"><feGaussianBlur stdDeviation="12"/></filter>
 </defs>
 <ellipse cx="222" cy="379" rx="122" ry="23" fill="#4a2f59" opacity=".17" filter="url(#shadow)" />
 <circle cx="220" cy="193" r="178" fill="url(#halo)" opacity=".5"/>
 <g>{inner}</g>
 <path d="M52 90l4 11 11 4-11 4-4 11-4-11-11-4 11-4zM362 119l3 7 7 3-7 3-3 7-3-7-7-3 7-3z" fill="#fff" opacity=".84"/>
 </svg>'''

def build(kind,c):
 if kind=='stick':
  return f'''<g transform="rotate(-13 220 220)"><rect x="170" y="174" width="100" height="188" rx="13" fill="url(#deep)"/><rect x="178" y="178" width="8" height="177" rx="4" fill="#ffffff" opacity=".25"/><rect x="172" y="160" width="96" height="39" rx="6" fill="url(#metal)"/><path d="M183 165L183 116Q220 81 257 116L257 166Z" fill="{c}"/><path d="M185 117Q220 82 255 117" stroke="#fff" opacity=".45" stroke-width="5" fill="none"/><text x="220" y="262" text-anchor="middle" fill="#f7e7f6" font-size="14" font-family="Georgia" letter-spacing="1.1">techglam</text><text x="220" y="281" text-anchor="middle" fill="#ceb3d4" font-size="7" font-family="Arial" letter-spacing="3">BLUSH STICK</text><path d="M252 209V340" stroke="white" opacity=".12" stroke-width="5"/></g>'''
 if kind=='palette':
  return f'''<g transform="rotate(-13 220 220)"><rect x="85" y="141" width="270" height="205" rx="21" fill="url(#deep)"/><rect x="94" y="149" width="252" height="188" rx="17" fill="url(#metal)"/><rect x="109" y="166" width="223" height="155" rx="13" fill="#ece3ef"/><circle cx="163" cy="236" r="49" fill="{c}"/><circle cx="277" cy="236" r="49" fill="#C37E84"/><circle cx="163" cy="236" r="42" fill="none" stroke="#ffe8ef" stroke-width="3" opacity=".65"/><circle cx="277" cy="236" r="42" fill="none" stroke="#ffe8ef" stroke-width="3" opacity=".65"/><path d="M135 211C144 198 170 195 181 204" fill="none" stroke="white" opacity=".3" stroke-width="7"/><text x="220" y="305" text-anchor="middle" fill="#65536d" font-family="Georgia" font-size="15" letter-spacing="1.5">techglam</text></g>'''
 if kind=='liquid':
  return f'''<g transform="rotate(11 220 220)"><rect x="175" y="76" width="90" height="109" rx="9" fill="url(#deep)"/><rect x="186" y="86" width="6" height="88" rx="3" fill="white" opacity=".16"/><rect x="169" y="182" width="102" height="17" rx="5" fill="url(#metal)"/><rect x="161" y="192" width="118" height="174" rx="19" fill="url(#glass)" stroke="white" stroke-opacity=".72" stroke-width="3"/><path d="M177 207Q186 198 195 201V350" stroke="white" stroke-opacity=".49" stroke-width="8" fill="none"/><rect x="172" y="249" width="95" height="62" rx="8" fill="#fffafa" opacity=".9"/><text x="219" y="275" text-anchor="middle" fill="#6c5875" font-family="Georgia" font-size="13">techglam</text><text x="219" y="289" text-anchor="middle" fill="#a07891" font-size="8" font-family="Arial" letter-spacing="1.3">CLOUD TINT</text></g>'''
 if kind in ('lipoil','gloss'):
  return f'''<g transform="rotate(13 220 220)"><rect x="184" y="49" width="73" height="137" rx="11" fill="url(#metal)"/><rect x="190" y="54" width="8" height="125" rx="4" fill="white" opacity=".7"/><rect x="175" y="179" width="92" height="13" rx="6" fill="#aa8ab5"/><rect x="173" y="185" width="96" height="184" rx="28" fill="url(#glass)" stroke="#fdf6fa" stroke-width="4" stroke-opacity=".75"/><path d="M185 210V337" stroke="#fff" opacity=".48" stroke-width="8" stroke-linecap="round"/><path d="M253 219V337" stroke="#5c235b" opacity=".14" stroke-width="8" stroke-linecap="round"/><text x="222" y="267" text-anchor="middle" fill="#fff9ff" font-family="Georgia" font-size="18">techglam</text><text x="222" y="289" text-anchor="middle" fill="white" font-family="Arial" font-size="9" letter-spacing="1.8">{'LIP OIL' if kind=='lipoil' else 'LIP GLOSS'}</text></g>'''
 if kind=='eye':
  discs=''
  cols=['#E3C4D3',c,'#A77D79','#DCA48C','#B48A97','#6B4C60','#F5DEBF','#C093B7','#937287']
  for i,col in enumerate(cols):
   x=141+(i%3)*78;y=194+(i//3)*68
   discs+=f'<rect x="{x-28}" y="{y-26}" width="56" height="53" rx="9" fill="{col}"/><rect x="{x-23}" y="{y-21}" width="46" height="43" rx="7" fill="none" stroke="#fff" stroke-opacity=".17" stroke-width="2"/>'
  return f'''<g transform="rotate(-10 220 220)"><rect x="91" y="107" width="260" height="266" rx="17" fill="url(#deep)"/><rect x="99" y="115" width="244" height="82" rx="12" fill="url(#metal)"/><rect x="107" y="123" width="228" height="60" rx="8" fill="#d6c5d9"/><text x="221" y="161" text-anchor="middle" fill="#736080" font-family="Georgia" font-size="22">techglam</text><rect x="108" y="180" width="225" height="182" rx="9" fill="#3a2e3e"/>{discs}</g>'''
 if kind=='brush':
  shapes=''
  for i,(ang,x,y) in enumerate([(-15,156,158),(2,217,142),(17,271,156)]):
   shapes+=f'''<g transform="rotate({ang} {x} 235)"><rect x="{x-10}" y="194" width="20" height="167" rx="8" fill="url(#product)"/><rect x="{x-13}" y="160" width="26" height="57" rx="6" fill="url(#metal)"/><path d="M{x-13} 171Q{x-30} 129 {x} 84Q{x+30} 129 {x+13} 171Z" fill="{c if i != 1 else '#835D76'}"/><path d="M{x-7} 160Q{x-17} 125 {x} 100" stroke="#fff" stroke-opacity=".27" stroke-width="3" fill="none"/><text x="{x}" y="285" transform="rotate(-90 {x} 285)" text-anchor="middle" fill="#55475f" font-family="Georgia" font-size="10">techglam</text></g>'''
  return shapes
 if kind=='sponge':
  return f'''<g transform="rotate(-13 220 230)"><path d="M220 79C197 129 115 214 128 281Q137 359 223 365Q313 367 322 284C331 216 245 114 220 79Z" fill="{c}" stroke="#e9b9d6" stroke-width="3"/><path d="M215 110C184 177 152 223 158 277Q161 320 194 332" fill="none" stroke="#fff" stroke-opacity=".32" stroke-linecap="round" stroke-width="14"/><ellipse cx="270" cy="293" rx="17" ry="33" fill="#d2a4c3" opacity=".25"/></g>'''
 if kind=='device':
  return f'''<g transform="rotate(-6 220 230)"><rect x="206" y="304" width="28" height="68" rx="7" fill="url(#metal)"/><ellipse cx="220" cy="375" rx="103" ry="18" fill="url(#metal)"/><ellipse cx="220" cy="189" rx="117" ry="151" fill="url(#metal)"/><ellipse cx="220" cy="189" rx="104" ry="138" fill="#ddc9df"/>
 <ellipse cx="220" cy="189" rx="88" ry="122" fill="#fdf4fe" opacity=".58"/><path d="M177 119Q220 83 263 119" fill="none" stroke="white" opacity=".6" stroke-width="8"/>
 {''.join(f'<circle cx="{220+98*__import__("math").cos(i*3.14159/12)}" cy="{189+131*__import__("math").sin(i*3.14159/12)}" r="3.8" fill="#fff4eb" opacity=".96"/>' for i in range(24))}
 <text x="220" y="226" fill="#946b9f" opacity=".68" font-family="Georgia" font-size="17" text-anchor="middle">techglam</text></g>'''
for filename,kind,color,_ in products:
 (P/(filename+'.svg')).write_text(frame(build(kind,color),color,'TechGlam'),encoding='utf-8')

hero='''<svg xmlns="http://www.w3.org/2000/svg" width="710" height="720" viewBox="0 0 710 720"><defs><linearGradient id="b" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#d0a7ec"/><stop offset=".55" stop-color="#ad7bce"/><stop offset="1" stop-color="#9571be"/></linearGradient><radialGradient id="r"><stop stop-color="#f2dbf7"/><stop offset="1" stop-color="#9e77c5"/></radialGradient><linearGradient id="skin" x1=".15" x2=".9" y2=".9"><stop stop-color="#D69F82"/><stop offset=".42" stop-color="#AC705B"/><stop offset="1" stop-color="#8E504F"/></linearGradient><linearGradient id="shirt" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#eadfe5"/><stop offset=".5" stop-color="#fcf6f7"/><stop offset="1" stop-color="#b594bc"/></linearGradient><linearGradient id="hair" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#4a2b36"/><stop offset=".7" stop-color="#26151f"/><stop offset="1" stop-color="#5e3840"/></linearGradient></defs>
<circle cx="380" cy="367" r="324" fill="url(#r)"/><circle cx="381" cy="359" r="282" fill="none" stroke="#f7e4ff" stroke-opacity=".35" stroke-width="1"/>
<path d="M144 720C150 586 200 540 293 510Q380 486 473 510C579 541 609 633 623 720" fill="url(#shirt)"/>
<path d="M245 720Q257 602 286 565L364 635L459 564Q503 614 510 720" fill="#f8ebf2"/>
<path d="M257 505C182 440 167 350 176 282C164 183 222 113 286 98C317 25 486 39 527 131C590 212 573 338 534 423C521 459 520 526 542 567Q485 584 439 531L265 541Q198 582 161 544Z" fill="url(#hair)"/>
<path d="M332 450L332 551Q360 602 386 610Q421 596 444 549L442 439" fill="url(#skin)"/>
<path d="M254 282C253 189 298 146 369 139C427 141 492 187 493 290L483 396C469 468 429 501 378 505C324 505 283 468 268 405Z" fill="url(#skin)"/>
<path d="M258 308C220 252 265 174 306 163C301 242 314 269 365 280C416 291 448 244 467 206C472 267 492 302 497 322Q534 245 502 180C474 114 397 101 330 116C258 129 219 199 244 292Z" fill="url(#hair)"/>
<path d="M284 330Q316 312 341 331" fill="none" stroke="#4b2e39" stroke-width="8" stroke-linecap="round"/><path d="M412 330Q437 313 463 327" fill="none" stroke="#4b2e39" stroke-width="8" stroke-linecap="round"/>
<path d="M296 343Q318 334 339 347" fill="none" stroke="#f7e1cb" stroke-opacity=".8" stroke-width="4"/><path d="M417 347Q437 334 456 341" fill="none" stroke="#f7e1cb" stroke-opacity=".8" stroke-width="4"/>
<path d="M380 332Q371 380 368 396Q381 409 397 396" fill="none" stroke="#854c49" stroke-width="4" stroke-linecap="round"/><path d="M338 438Q377 456 417 437Q390 480 352 463Z" fill="#863D52"/><path d="M342 435Q379 441 411 434" fill="none" stroke="#bd7378" stroke-width="5"/>
<ellipse cx="301" cy="392" rx="40" ry="20" fill="#cf6b7e" opacity=".23"/><ellipse cx="455" cy="389" rx="41" ry="20" fill="#cf6b7e" opacity=".25"/>
<circle cx="270" cy="385" r="9" fill="#f5dba5"/><circle cx="488" cy="385" r="9" fill="#f5dba5"/>
<path d="M178 542Q260 596 290 548" fill="none" stroke="#70445d" stroke-opacity=".6" stroke-width="27" stroke-linecap="round"/><path d="M518 540Q572 583 593 544" fill="none" stroke="#70445d" stroke-opacity=".5" stroke-width="24" stroke-linecap="round"/>
<path d="M565 116l8 21 21 8-21 8-8 21-8-21-21-8 21-8zM166 392l5 12 12 5-12 5-5 12-5-12-12-5 12-5z" fill="#fff" opacity=".65"/>
</svg>'''
(P/'hero-model.svg').write_text(hero,encoding='utf-8')

lila='''<svg xmlns="http://www.w3.org/2000/svg" width="420" height="430" viewBox="0 0 420 430"><defs><linearGradient id="h" x2=".9" y2="1"><stop stop-color="#352342"/><stop offset="1" stop-color="#805b9c"/></linearGradient><linearGradient id="s" x2="1" y2="1"><stop stop-color="#e0b1a0"/><stop offset="1" stop-color="#bd8287"/></linearGradient><linearGradient id="b" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#eee3ff"/><stop offset="1" stop-color="#c8a7eb"/></linearGradient></defs><circle cx="209" cy="202" r="186" fill="#ead9fd" opacity=".95"/><path d="M29 430C43 330 102 313 162 308L261 308C341 312 390 369 397 430" fill="url(#b)"/><path d="M114 329Q84 282 100 175C100 64 158 45 210 44C288 38 322 113 319 188Q339 284 304 331L266 324L150 334Z" fill="url(#h)"/><path d="M171 282L169 332Q211 365 250 330L251 281" fill="url(#s)"/><path d="M125 167Q124 102 205 89C281 87 297 146 296 183L288 246Q262 305 211 311Q161 309 135 253Z" fill="url(#s)"/><path d="M127 190Q90 130 122 98C146 51 214 56 251 80Q287 96 296 141Q268 122 252 116Q226 170 141 174Z" fill="url(#h)"/><path d="M151 217Q175 202 195 215M224 216Q245 204 269 214" fill="none" stroke="#4f3345" stroke-width="5" stroke-linecap="round"/><path d="M197 275Q211 288 228 274" fill="none" stroke="#98485c" stroke-width="5" stroke-linecap="round"/><circle cx="126" cy="230" r="11" fill="#b489e8"/><circle cx="294" cy="230" r="11" fill="#b489e8"/><path d="M126 225Q94 157 116 129" stroke="#d9c2fc" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M295 225Q323 164 306 130" stroke="#d9c2fc" stroke-width="10" fill="none" stroke-linecap="round"/><circle cx="295" cy="224" r="16" fill="#b489e8"/><path d="M295 237Q299 276 259 280" stroke="#b489e8" fill="none" stroke-width="6"/><rect x="244" y="276" rx="6" width="27" height="10" fill="#b489e8"/><path d="M339 69l6 15 15 6-15 6-6 15-6-15-15-6 15-6z" fill="#fff"/></svg>'''
(P/'lila.svg').write_text(lila,encoding='utf-8')
print('Gerados',len(products)+2,'SVGs')
