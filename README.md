# Solow — Crescimento de Longo Prazo do Brasil

Página única que roda o **modelo de Solow calibrado com o investimento real do Brasil**. A taxa de poupança/investimento (`s`) vem da **Formação Bruta de Capital Fixo** publicada pelo Banco Central, puxada ao vivo (com backup offline).

## Abrir o HTML no navegador

[Baixe o ZIP do repositório](https://github.com/matheusassiso/economia-brasil-modelos/archive/refs/heads/main.zip), extraia o conteúdo e abra [`index.html`](index.html) no navegador.

O modelo usa os dados embutidos se a consulta ao Banco Central falhar.

## O que faz

- **`s` a partir de dado real** — a série `22102` do SGS/BCB (FBCF, índice de volume) define a taxa de investimento do Brasil, ao vivo. Botão para recalibrar `s` com o dado atual, e slider para experimentar.
- **Diagrama de fase** — `s·f(k)` vs `(n+g+δ)k`, com o estado estacionário `k*` e a regra de ouro marcados.
- **Convergência no tempo** — trajetórias de `k`, `y` e `c` até o estado estacionário.
- **Regra de ouro** — consumo de estado estacionário × poupança, com o `s` do Brasil e o `s = α` (ouro) marcados; diagnóstico de poupança abaixo/acima do ótimo.
- **Investimento real** — a série da FBCF do Brasil ao longo do tempo.
- **Comparação com o real** — o crescimento de longo prazo do modelo (`n+g`) confrontado com o crescimento médio do IBC-Br (série `24364`).

## Sobre a taxa de investimento

O BCB **não publica a razão FBCF/PIB** como série pronta no SGS — só o índice de volume da FBCF (`22102`). Então `s` é estimado ancorando esse índice real na taxa média de investimento do Brasil (~17,5% do PIB, IBGE/Contas Nacionais), preservando as variações reais. Sempre ajustável no slider.

## Dados (BCB SGS, `api.bcb.gov.br`, CORS liberado)

| Uso | Série |
|-----|-------|
| Taxa de investimento (FBCF, volume) | 22102 |
| Atividade / crescimento real (IBC-Br) | 24364 |

Estratégia **ao vivo com backup offline**: busca as séries atualizadas; se falhar, usa o retrato embutido no arquivo. Para atualizar o snapshot, rode `fetch_solow.py` e substitua o bloco de dados no `index.html`.

---

Material educativo — não é recomendação de investimento. A versão anterior (dashboard com vários painéis: IS-LM-BP, Phillips, hiperinflação etc.) está preservada no histórico do git. Projeto irmão: [simulação teórica de curto/médio/longo prazo](https://github.com/matheusassiso/simulacao-curto-medio-longo-prazo).
