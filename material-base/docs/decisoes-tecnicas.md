# Estrutura e convenções

## Regras para os dados

1. `data/source/` guarda cópias fiéis dos arquivos recebidos; não sobrescrever.
2. Nomear derivados com ID do eixo e versão, mantendo a fonte indicada nos metadados.
3. Dados de drenagem entram em `data/source/drainage/` e só viram cadastro estruturado após leitura e conferência das pranchas.
4. Usar metros internamente para geometria, dimensões e volume, indicando unidades na interface.
5. Guardar coordenadas GPS originais, coordenadas projetadas, eixo usado, estaca calculada e precisão informada pelo aparelho.
6. Só marcar aprovado/reprovado quando houver valor de projeto e tolerância aplicável. Relatório deve mostrar valor de projeto, valor medido, diferença, tolerância, motivo, data, estaca e fotos.

## Partes previstas

- `app/src/components/`: telas e componentes visuais.
- `app/src/services/`: leitura LandXML, projeção GPS, busca de estaca, comparação de medidas, fotos e relatórios.
- `app/src/styles/`: estilos compartilhados.
- `scripts/`: importação, validação e conversão reproduzível de arquivos.
- `data/processed/`: saídas geradas; nunca usar como substituto da fonte original.

## Segurança de cálculo

A tela deve indicar quando a posição GPS estiver imprecisa, quando o ponto estiver fora do eixo/trecho, ou quando houver ambiguidade entre alinhamentos próximos. A estaca deve ser calculada pela geometria horizontal e pelas equações do LandXML, não pela distância em linha reta desde o início. O cálculo deve permanecer desabilitado até a ordem das coordenadas ser validada para cada arquivo.

