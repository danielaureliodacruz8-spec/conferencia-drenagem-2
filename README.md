# Conferência de Drenagem

Projeto Flutter para Android com um protótipo de fiscalização de drenagem e os dados de referência das rodovias.

## Gerar APK pelo CodeMagic

1. No CodeMagic, abra o repositório `conferencia-drenagem-1` e selecione a branch `main`.
2. O `codemagic.yaml` fica na raiz do repositório e configura o fluxo **Android APK para teste**.
3. Inicie o workflow `Android APK (teste)`. O CodeMagic cria a estrutura Android, baixa os pacotes e gera um APK de depuração para instalar no aparelho.
4. Ao terminar, baixe `app-debug.apk` na área **Artifacts** do build.

## O que o app Android já faz nesta versão

- Abre com a marca Strata/Basitec.
- Permite selecionar GO-110 ou GO-236 e escolher o tipo de dispositivo compartilhado entre as rodovias.
- Na GO-110, permite buscar dispositivos e referências de estaca extraídos do projeto.
- Na GO-236, deixa a localização para preenchimento manual; não transfere para ela os locais da GO-110.
- Ao abrir, solicita o GPS, projeta a posição para o eixo UTM e estima a estaca por `estaca inicial + distância ao longo do eixo ÷ 20 m`.
- Registra coordenadas GPS, medidas digitadas, observações e foto.
- Guarda registros localmente no aparelho e mantém a situação como pendente até haver critérios de aceitação configurados.

## O que precisa de implementação antes de uso oficial

Esta versão é um MVP de campo para gerar e experimentar. A estaca calculada é uma estimativa pelo eixo; a conferência de alinhamento e tolerância de GPS continua necessária. O XML da GO-110 tem diferença entre extensão declarada e soma dos segmentos, e suas equações precisam ser confirmadas antes de tratar a estaca como oficial. Ainda falta incluir o carimbo da foto e relatórios PDF, definir fórmulas de concreto por tipo de dispositivo, configurar critérios/tolerâncias de aprovação e implementar sincronização. O APK de depuração serve para testar; para distribuição oficial, configure a assinatura Android no CodeMagic.

## Organização

- `lib/`: app Flutter Android.
- `codemagic.yaml`: workflow para gerar APK de depuração.
- `material-base/app/prototype-singlefile.html`: protótipo navegável da interface.
- `material-base/data/source/alignments/`: eixos XML da GO-110 e GO-236.
- `material-base/data/processed/`: catálogo compartilhado e dados estruturados da drenagem da GO-110.
- `material-base/data/processed/projects/GO236/README.md`: regra de localização manual até chegar o projeto da GO-236.
- `material-base/docs/`: notas de coordenadas, decisões e fotos.

Os PDFs originais de drenagem não estão no repositório; as transcrições e os dados derivados estão em `material-base/data/processed/projects/GO110/`.

