# Economia Brasileira: Dados Reais e Modelos

Dashboard **de arquivo único** que puxa as séries oficiais do Brasil **ao vivo** (API pública do Banco Central e IBGE) e as liga aos modelos de macroeconomia. Se cair a internet, usa um **snapshot embutido** — funciona offline do mesmo jeito.

### ▶ Abrir: **(publique no GitHub Pages — link aparece aqui depois do deploy)**

## O que tem

**Painel Brasil** — os números do momento, ao vivo: Selic, IPCA (12m e no mês), câmbio R$/US$, desemprego (PNAD), dívida bruta/PIB, base monetária, IBC-Br. Cada card mostra o valor, o mês e se veio "ao vivo" ou do snapshot. Gráficos históricos de juros × inflação, câmbio, desemprego, dívida e atividade.

**Inflação & Plano Real** — a hiperinflação brasileira em dados reais (IGP-DI desde 1989). O pico de **~81% em um único mês** (mar/1990) e o **Plano Real** derrubando a inflação de 46% (jun/1994) para 5,5% (jul/1994). Com sobreposição do **modelo de Cagan**: a linha tracejada mostra como a inflação teria explodido sem a reforma monetária.

**Curva de Phillips real** — cada mês (2014–hoje) como um ponto de desemprego × inflação, com a reta ajustada por mínimos quadrados sobre os dados brasileiros. Mostra que, no Brasil, a relação é fraca e instável.

**Solow calibrado** — o modelo de crescimento com parâmetros do Brasil (poupança baixa, participação do capital alta). Compara o crescimento de longo prazo do modelo com o crescimento real do IBC-Br. Botões para calibrar com valores do Brasil e para a regra de ouro.

**Sobre os dados** — todas as séries SGS usadas, com código e fonte.

## Fonte dos dados

- **API SGS do Banco Central** (`api.bcb.gov.br`) — acesso público, sem chave, com CORS liberado.
- Séries: IPCA 12m (13522), IPCA mês (433), Meta Selic (432), câmbio (3698), dívida/PIB (13762), desemprego PNAD (24369), IBC-Br (24364), base monetária (1785), IGP-DI histórico (190).
- Estratégia **ao vivo com backup offline**: o site tenta buscar cada série atualizada; se falhar, usa o retrato embutido no próprio arquivo. Botão *Atualizar* rebusca.

## Como usar

**Fácil:** abra o link do GitHub Pages (após publicar).

**Offline:** baixe o repositório (*Code → Download ZIP*), descompacte e dê dois cliques em `index.html`. Funciona sem internet com o último snapshot; com internet, atualiza sozinho.

## Publicar

`push` na branch `main` — o workflow em `.github/workflows/pages.yml` publica sozinho. Em *Settings → Pages*, defina a origem como **GitHub Actions**.

## Atualizar o snapshot offline

O snapshot embutido é só um retrato de segurança. Para atualizá-lo, rode o script `fetch_br.py` (baixa as séries do BCB e gera o JSON) e substitua o bloco de dados no `index.html`. O site sempre prefere o dado ao vivo quando há internet.

---

Material educativo — não é recomendação de investimento. Projeto irmão da [simulação teórica de curto/médio/longo prazo](https://github.com/matheusassiso/simulacao-curto-medio-longo-prazo).
