# TechGlam — E-commerce demonstrativo

**Tecnologia que Realça seu Brilho.**

Site responsivo desenvolvido em HTML, CSS e JavaScript puro, sem instalação de dependências. Inclui página inicial, catálogo, filtros, detalhes, favoritos, sacola de compras, cupons, frete estimado, login/cadastro demonstrativos, área da conta, checkout de demonstração, institucional, contato e Lila Glam.

## Executar localmente

1. Abra um terminal na pasta `TechGlam`.
2. Execute `python -m http.server 5500` (Windows) ou `python3 -m http.server 5500` (Linux/macOS).
3. Acesse <http://localhost:5500> em um navegador atualizado.

Alternativa: `npx serve .` (se já tiver Node.js e o pacote disponível). Para usar Web Crypto no login, prefira `http://localhost` ou HTTPS em vez de abrir `index.html` por `file://`.

## Testes de lógica

Execute `node tests/smoke.cjs` para validar as 12 rotas, migração do carrinho, login, cupons, checkout demonstrativo e redefinição local de senha. Esses testes não substituem testes de interface no navegador.

## Funcionalidades

| Área | Implementação |
| --- | --- |
| Vitrine e catálogo | 16 produtos fictícios com ilustrações SVG originais; busca, filtros e ordenação |
| Produtos | Imagens, estoque de exemplo, variação de tonalidade, notas ilustrativas, inclusão na sacola |
| Carrinho | Adição, exclusão, alteração de quantidades, subtotal, desconto, cupom e frete estimado |
| Favoritos | Persistidos por perfil; favoritos de visitante migram no login |
| Conta | Cadastro, login, senha derivada com Web Crypto/PBKDF2, edição do perfil, pedidos e cupons — **somente local** |
| Checkout | Login obrigatório, carrinho preservado, dados de entrega e criação de pedido **fictício** |
| Lila Glam (chat) | Perguntas guiadas respondidas por regras preprogramadas, não é uma IA generativa |
| Lila Glam (foto) | Consentimento, foto processada **localmente**, estimativa experimental de cor por pixels, ajuste manual, quiz de 6 perguntas, sugestões e desconto |
| Atendimento | Formulário validado e registrado apenas no armazenamento local |

## Regras comerciais do protótipo

- **BEMVINDA10**: 10% OFF para contas sem pedido anterior.
- **Campanha sazonal**: cupom de 5 a 12%, conforme a data (por exemplo, `ROSA7` em outubro).
- **GLAM5**: cupom de 5%.
- **Acima de R$ 150** de subtotal após descontos de vitrine: frete grátis e 5% OFF automático.
- **Primeira compra autenticada**: frete grátis.
- **Lila Glam**: 8% OFF nos produtos recomendados após finalizar a análise; acumula com o 5% automático acima de R$ 150.
- **Cupons NÃO acumulam** com o desconto da Lila ou com o 5% automático; usar cupom substitui esses benefícios (frete grátis continua seguindo seus critérios).
- Os descontos da vitrine (preço `oldPrice` comparado com preço atual) já integram o preço de venda e podem coexistir com as regras acima.
- O cálculo do frete é apenas uma simulação (R$ 14,90 ou R$ 22,90 dependendo dos primeiros dígitos do CEP), sem API postal.

## Limitações e cuidados importantes

Este pacote é um **protótipo navegável**, não uma loja preparada para produção.

- **Não integra pagamentos, antifraude, estoque ou transportadoras reais.** Nenhum pedido, Pix, boleto ou cartão gera cobrança.
- **Não possui autenticação segura de produção.** A senha é derivada com PBKDF2 no navegador e não é armazenada em texto puro, mas os registros e a sessão são totalmente controlados pelo próprio cliente (localStorage). A redefinição de senha não exige verificação de e-mail — existe apenas para ilustrar o fluxo. Não utilizar senhas reais nem dados pessoais reais.
- **Não possui IA de verdade.** O chat usa reconhecimento simples de palavras. A análise de imagem calcula uma estimativa grosseira de luminosidade/cor numa região central da foto e **não detecta pele ou rosto**. O usuário pode corrigir o tom/subtom. **Não é avaliação clínica, científica ou precisa.** A foto não é enviada nem persistida; apenas os dados da análise são guardados no perfil local.
- **Catálogo, avaliações, preços, estoque, contatos e ilustrações são fictícios.** O PDF `Techglam2.pdf` citado na solicitação não estava disponível ao montar esta versão. Atualize `data.js` e `assets/` quando houver imagens e produtos oficiais.
- A apresentação Canva exigia acesso não disponível; a identidade usa as cores especificadas `#B489E8` e `#EDECEB` e organização inspirada em lojas de beleza, sem copiar os sites de referência.

## Evolução para produção

1. **Backend** com banco de dados (PostgreSQL), autenticação segura (sessão HttpOnly ou tokens com rotação), confirmação de e-mail, hash de senha no servidor e autorização por recurso.
2. **API de catálogo/estoque**, reservas transacionais e preços/descontos calculados no servidor.
3. **Gateway de pagamento** real com webhooks idempotentes e validação de pedidos.
4. **Integração de logística/CEP** via serviço especializado.
5. **IA da Lila** por backend próprio com controle de acesso, limites de requisições e chave de API mantida no servidor (nunca no JavaScript público); análise facial e sugestões com consentimento específico, revisão de vieses e critérios de exclusão de fotos.
6. Adequação à **LGPD**: aviso de privacidade, minimização, retenção/deleção, segurança, direitos dos titulares, avaliação para dados de imagem.
7. Substituição de produtos, imagens, depoimentos, preços e contatos fictícios pelos materiais definitivos da marca.

## Organização

```
TechGlam/
├── index.html                # Casca HTML, metadata e ícones
├── styles.css                # Design responsivo
├── data.js                   # Catálogo de exemplo e questionário
├── app.js                    # Navegação, estado, descontos e interações
├── assets/                   # Ilustrações SVG originais
└── scripts/generate_assets.py
```

### Atalhos de inicialização

No Windows, execute `iniciar-windows.bat`. No Linux/macOS, execute `./iniciar-linux-macos.sh`. Em ambos os casos, abra <http://localhost:5500>. É necessário ter Python instalado.
