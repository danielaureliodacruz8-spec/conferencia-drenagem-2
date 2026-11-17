# Drenagem da GO-110 — projeto carregado

Os dois volumes foram copiados em `data/source/drainage/` e organizados como dados do projeto da GO-110. Eles não serão usados como locais de drenagem da GO-236.

## Dados estruturados para o app

- `point-devices.json`: 25 estruturas pontuais (B49 a B67, dispositivos de greide/transposição e passagens de fauna) e 10 bacias de captação, com estação, tipo e lado quando informado.
- `linear-drainage.json`: 13 trechos/pontos de DPS, DPR, DSS e DSH.
- `surface-devices.json`: 402 ocorrências/trechos extraídos das notas de serviço: 109 segmentos MFC, 143 entradas/descidas d'água, 1 descida DCD, 69 valetas, 8 canais trapezoidais, 43 trechos de sarjeta/canaleta e 29 TSS.
- `source-tables.md` e `surface-tables.md`: transcrição pesquisável das tabelas do projeto, mantendo a página PDF como referência.

## Uso por rodovia

Os tipos de dispositivo ficam no catálogo compartilhado `../../device-catalog.json`. Na GO-110, o cadastro pode sugerir as estacas e dados previstos acima. Na GO-236, o app deve permitir escolher um tipo e preencher o local manualmente, conforme combinado; não importar as localizações da GO-110.

## Observações de conferência

O PDF identifica o volume profundo/OAC como trecho parcial da GO-110, estacas 1500 a 2249+14,221. Comprimentos com divergência entre quadros estão marcados nos registros de bueiros. Para aprovação de campo ou cálculo contratual, conferir o original e a revisão do responsável técnico.

