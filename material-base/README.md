# Materiais de referência do projeto

O app Flutter Android fica na raiz do repositório. Esta pasta reúne o protótipo navegável, os arquivos de eixo, as marcas e os dados derivados dos projetos.

- GO-110: registros de drenagem estruturados e referências de estaca.
- GO-236: catálogo de tipos compartilhado; localização da drenagem preenchida manualmente até receber o projeto dessa rodovia.
- Alinhamentos amostrados: cada ponto contém coordenada UTM leste/norte e distância acumulada em metros; o app estima a estaca por início do eixo + distância / 20.

A estimativa da GO-110 exibe alerta: a soma dos elementos do XML diverge 38,635 m da extensão declarada e há equações de estaca que precisam ser conferidas. Compare com referência de obra antes de usar em medição oficial.

Os PDFs originais não estão neste repositório. As transcrições e dados estruturados estão em `data/processed/projects/GO110/`.
