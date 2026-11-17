# Fotos com carimbo

O protótipo usa a imagem `app/public/assets/exemplo-foto-carimbada.jpeg` como referência de composição. Ao escolher uma foto no formulário de drenagem, ele monta uma cópia JPEG com:

- texto branco sobre faixa cinza translúcida no canto inferior esquerdo;
- descrição digitada, estaca informada no formulário, coordenadas inseridas ou lidas pelo GPS, data e hora do aparelho;
- logo GO INFRA sobre quadro preto no canto inferior direito;
- botão para baixar a foto carimbada.

O logo original GO INFRA fica em `app/public/assets/marca-go-infra-original.jpeg`. O logotipo Strata/Basitec fica em `app/public/assets/marca-strata-basitec.jpeg` e aparece na tela inicial e na área de relatórios.

A foto carimbada é baixada como um novo arquivo; a foto original não é sobrescrita. O protótipo ainda não anexa nem sincroniza a cópia baixada dentro do registro de vistoria.

