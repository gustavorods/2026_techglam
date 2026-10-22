# TechGlam — catálogo demonstrativo

Site responsivo em HTML, CSS e JavaScript puro. Exibe os produtos TechGlam informados para este catálogo, incluindo a linha tecnológica Glamix. As imagens são mockups conceituais gerados por IA e identificados como ilustrativos no site.

## Executar

Na pasta do projeto, execute `python3 -m http.server 5500` (Linux/macOS) ou `python -m http.server 5500` (Windows) e abra <http://localhost:5500>.

## Catálogo

| Produto | Preço | Opções |
| --- | ---: | ---: |
| Blush Bastão | R$ 45,00 | 5 |
| Blush Líquido | R$ 45,00 | 5 |
| Paleta de Blush | R$ 50,00 | 5 |
| Paleta de Sombra | R$ 70,00 | 6 |
| Lip Gloss Tradicional | R$ 46,00 | 10 |
| Lip Oil Fruits | R$ 46,00 | 5 |
| Kit Esponjas | R$ 30,00 | — |
| Kit Pincéis | R$ 50,00 | — |
| Impressora de Maquiagem Glamix, com cinco cartuchos | R$ 1.650,00 | — |
| Kit com 5 Cartuchos Glamix | R$ 500,00 | — |
| Cartucho Individual / Refil Glamix | R$ 120,00 | 5 |

Os dados do catálogo estão em `data.js`; as 45 imagens de produto estão em `assets/products/`. Cores e sabores são selecionados na página do produto, com imagem, nome e descrição sincronizados.

## Experiência Glamix

A página `#glamix` apresenta o equipamento, seu preço de R$ 1.650,00, os cinco cartuchos inclusos e uma exploração interativa por etapas e componentes. A página inicial também traz uma prévia interativa. Três imagens complementares geradas para a seção mostram os cartuchos, o espelho com pincel e o recipiente sob a saída inferior; todas são mockups ilustrativos.

A linha Glamix é apresentada como pronta para venda conforme a informação fornecida pela TechGlam. Este site continua registrando apenas pedidos demonstrativos, sem pagamento ou envio real. A apresentação não promete tipos de cosméticos além das formulações compatíveis com o equipamento.

## Demonstração e testes

O carrinho, cadastro, favoritos, pedidos, chat e análise Lila Glam funcionam apenas neste navegador. Não há pagamento, envio, cálculo de frete ou estoque em tempo real. O total demonstrativo é a soma dos preços dos produtos, sem descontos. A análise de foto ocorre localmente e oferece sugestões sem benefício comercial.

Execute `node tests/smoke.cjs` e `node tests/variants.cjs` para testar rotas, catálogo, variantes, carrinho e checkout demonstrativo.
