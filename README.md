# Calculadora de Fiis

## Objetivo
Estudando e atualizando a forma como eu realizo meus investimentos em fundos imobiliários, decidi automatizar algumas regras que utilizo para conseguir uma lista mais completa e não perder possíveis oportunidades.

# Estratégia
A minha estratégia é baseada em cima da S-Rank que o Cluber do Valor utiliza, ela é baseada em comprar fundos que pagam bons dividendos e que estejam baratos de acordo com a métriva P/VPA, assim aproveitamos as cotas advindas desses fundos e também a valorização desse fundo conforme o tempo.

**Atenção:** Eu considero essa estratégia como alto risco, e ela precisa ser balenceada de forma constante. Esteja ciente disso. Isso não é uma recomendação de investimento, é como eu faço atualmente.

## Remover fundos do tipo desenvolvimento.
São fundos que baseam em investimentos de construções imobiliários que ainda vão começar, eu informei acima que essa estratégia é de alto risco, porém fundo de desenvolvimento deixaria essa estratégia com um risco ainda maior por conta dos problemas que podem ocorrer em uma construção de um imóvel conforme o tempo como perda de prazo, indexadores em RMG (Renda Mínima Garantida) entre outros.

## Fundos com uma liquidez acima de 200k
Não queremos levar 2 dias para a conclusão de uma venda de algum fii caso seja necessário rebalancear, precisamos de uma alta liquidez para essa estratégia.

## Fundos com mais de 1 ano de vida
Removemos fundos que tenham menos de 1 ano de vida, queremos fundos que estão consolidados no mercado.

## Remover fundos com medianas e médias distantes
Aqui eu faço uma modificação da estratégia utilizada do s-rank, estou pegando a mediana dos últimos 10 meses dos proventos pagos por cada fii e seu desvio padrão, e assim eu análiso no final o desvio padrão do fii, se for muito alto significa uma alta dispersão no pagamentos da cotas, exemplo:

- 01/04/2022 - Pagamento de 0,40 por cota.
- 01/05/2022 - Pagamento de 1,02 por cota.

Queremos uma consistência no pagamentos desses fiis, porém não queremos um desvio padrão igual a 0, pois isso pode indicar indexadores como RMG atrelados ao fii, no meu código estou pegando um desvio padrão abaixo de 0,25 o que é alto, mas você pode modificar como quiser no final.

Caso você queira saber de forma mais aprofundada sobre a estratégia segue o link: https://clubedovalor.com.br/blog/melhores-fiis-s-rank/

Após todos esses filtros é gerada uma lista com todos os fiis de acordo com essas regras acima, basta selecionar os fiis que possuem um P/VPA baixo e o dividendo yield alto.