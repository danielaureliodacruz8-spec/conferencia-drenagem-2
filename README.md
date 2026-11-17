# Conferência de Drenagem 2

Cópia independente do projeto Conferência de Drenagem 1, preparada para validar a compilação iOS e gerar um IPA de desenvolvimento para teste em iPhone. As funções Dart e os dados de referência foram copiados sem alteração.

## Gerar para iPhone pelo CodeMagic

Os dois workflows iOS usam **Xcode 27.2** no Mac na nuvem do CodeMagic. Há dois workflows iOS no arquivo `codemagic.yaml`:

### 1. `ios-unsigned-check` — validar se compila

- Gera a estrutura iOS.
- Configura o nome exibido como **Conferência de Drenagem 2**.
- Declara permissões de localização, câmera e galeria.
- Compila sem assinatura e entrega um ZIP com o app iOS.
- **Esse arquivo não instala em um iPhone real.** Serve apenas para verificar se o projeto compila.

### 2. `ios-iphone-development` — gerar IPA para instalar no iPhone

Antes de executar esse workflow, configure no CodeMagic os arquivos de assinatura Apple:

1. Tenha uma associação ativa ao Apple Developer Program.
2. Registre o UDID do iPhone no Apple Developer.
3. Crie um certificado **Apple Development** e um perfil **iOS App Development** para o identificador:
   `br.com.stratabasitec.conferenciadrenagem2`
4. No CodeMagic, abra **Team settings → codemagic.yaml settings → Code signing identities**.
5. Envie o certificado `.p12` e o perfil `.mobileprovision`.
6. Execute o workflow `ios-iphone-development`.

O artefato esperado é `build/ios/ipa/*.ipa`. O perfil de desenvolvimento precisa incluir o iPhone que será usado no teste.

**Importante:** a compilação sem assinatura não substitui a assinatura. A Apple exige que apps instalados em aparelhos reais estejam assinados; a assinatura de desenvolvimento gerenciada pelo CodeMagic requer credenciais do Apple Developer Program. Sem esses arquivos, use `ios-unsigned-check` somente para validar a compilação.

## Gerar APK Android

O workflow `android-debug` continua disponível para gerar o APK de teste Android. Ele é independente dos workflows iOS.

## Identificação iOS

- Nome exibido: **Conferência de Drenagem 2**
- Bundle identifier: `br.com.stratabasitec.conferenciadrenagem2`
- Versão: `0.1.1+2`

## Funções e dados preservados

- Código principal em `lib/main.dart`.
- Seleção de GO-110 e GO-236.
- Cálculo estimado de estaca pelo eixo e localização GPS.
- Registro de coordenadas, medidas, observações e fotos.
- Armazenamento local.
- Dados de referência, alinhamentos, catálogos e imagens em `material-base/`.

Nenhuma função do aplicativo foi alterada nesta preparação para iOS.
