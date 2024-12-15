# **Análise de Dados de Queimadas no Brasil**

![Queimadas](https://images01.brasildefato.com.br/15a121027faddab66a3956678bff7db9.jpeg)

Queimadas consistem em eventos de incêndio em condições incontroladas que causam, todos os anos, uma quantidade imensurável de danos ao meio ambiente, principalmente em biomas menos úmidos como o Cerrado. De acordo com o MapBiomas Brasil, entre Janeiro e Outubro de 2024, uma área equivalente ao estado de Roraima foi queimada no Brasil. Desta área, 73% das queimadas afetaram áreas de vegetação nativa do Brasil, e 51% está localizada na Floresta Amazônica. 

Além dos danos causados a fauna e flora, somam-se a isso a grande quantidade de gases poluentes emitidos por estes fenômenos. O Observatório do clima afirmou que, entre Junho e Agosto de 2024, as queimadas ocorridas apenas na área na Amazônia emitiram 31,5 milhões de toneladas de dióxido de carbono (CO²) na atmosfera, de acordo com estimativa do Observatório do Clima. 

Visando contribuir para uma solução deste problema crítico, o projeto contido neste repositório propõe a construção de uma estrutura de ingestão, processamento e análise de dados referentes aos fenômenos de queimadas, utilizando para isto as melhores práticas do campo da Engenharia de Dados. A partir disto, espera-se que os insumos gerados a partir destes dados possam ser utilizados por ONGs, institutos independentes de pesquisa, entidades governamentais, instituições públicas, autoridades federais e outros grupos relevantes para mitigar os danos e evitar a ocorrência de futuros eventos.  

## Dados

A fonte principal de dados utilizada para este projeto consiste nos Dados Abertos do *Instituto Nacional de Pesquisas Espaciais* (INPE), que mantém uma seção específica para dados referentes a eventos de queimadas pela América do Sul, registrando desde a localização geográfica dos focos, dados sobre seu impacto, obtenção de imagens de satélites, e previsão de dados metereológicos e risco de ocorrência de novos focos de incêndio.

Este projeto se concentrou na extração de dados referentes à localização e intensidade dos focos de queimadas no Brasil. Estes dados são disponibilizados no Portal do INPE em quatro níveis temporais diferentes:
- A cada 10 minutos
- Diário
- Mensal
- Anual

Dicionário de dados:

| Campo  | Tipo | Descrição |
| ------------- | ------------- | --------- |
| Content Cell  | Content Cell  | 
| Content Cell  | Content Cell  |

- Latitude e Longitude
- Data de Ocorrência
- Satélite responsável pela detectção
- Munícipio, Estado e País
- Nível de Precipitação e Dias sem Chuva
- Risco de Incêndio
- Bioma do Local
- Potência Radiativa do Fogo

Visando complementar estes dados com mais informações, o projeto também utiliza dados de duas API's externas. 
- Open-Meteo, uma API gratuita para obtenção de dados metereológicos de qualquer lugar do mundo a partir de suas coordenadas geográficas. Desta fonte, os seguintes campos foram extraídos:
  - Temperatura a 2 Metros
  - Umidade Relativa
  - Temperatura Aparente
  - Período Diurno ou Noturno
  - Precipitação
  - Chuva
  - Pressão Atmosférica
  - Velocidade do Vento
  - Direção do Vento
- Mapbox, plataforma com diversas soluções e produtos de geolocalização. A partir da API de Geocoding Reverso das coordenadas geográficas de cada evento, as seguintes informações foram obtidas:
  - Cidade
  - Estado
  - País
 
## Proposta de Solução

### Arquitetura de Dados

Para cumprir o objetivo definido para este projeto, uma arquitetura completa de Ingestão, Tratamento e Distribuição de Dados é proposta seguindo o padrão Lambda, onde se definem duas camadas de processamento: 
- Uma camada para processamento em Batch, onde se processam dados agregados de um determinado período, como diário, mensal, anual, entre outros, conforme a necessidade.
- Outra camada para processamento em Streaming, processando dados o mais rápido possível para que sejam entregues aos usuários quase em tempo real.

Com as duas camadas coexistindo na mesma arquitetura, consegue-se promover a entrega de dados aos usuários em vários níveis de velocidade, a depender dos requisitos de utilização. 

Para implementá-la, este projeto utilizou como base os serviços disponibilizados pelo Google Cloud. Abaixo, um esquema final da arquitetura, com a indicação de cada serviço utilizado, é ilustrada.

![arquitetura da solução](https://github.com/andre-ls/mack-fire/blob/main/Foto%20da%20Arquitetura%20drawio.png)

Listando de maneira um pouco mais detalhada, os seguintes serviços do Google Cloud foram utilizados:
- Cloud Functions: Produto Serveless de Function as a Service, que permite a disponibilização de códigos de baixa complexidade em ambiente de Nuvem com poucas configurações. Neste projeto, o Functions foi utilizado para a execução de código Python responsável pela ingestão dos dados oriundos do INPE.
- Dataflow: Ferramenta de processamento de dados, tanto em Batch quanto em Streaming. Seu funcionamento se baseia na execução de códigos do framework Apache Beam, também de autoria do Google. Visando a centralização de todo o processamento em uma única plataforma, o Dataflow é utilizado na arquitetura proposta tanto para o processamento de dados na camada Batch quanto na camada de Streaming.
- Cloud Storage: Para o armazenamento dos dados na camada de Batch foi utilizado o Cloud Storage, solução de armanzenamento de objetos do Google Cloud. 
- PubSub: Para a transmissão de mensagens em baixa latência na camada de Streaming, foi utilizado o PubSub, serviço de streaming do Google Cloud. Como o seu nome já entrega, seu funcinamento é baseado no modelo de Publisher/Subscirber, com o envio e consumo de mensagens organizado via tópicos.
- BigQuery: Por fim, para disponibilização dos dados aos seus usuários finais, foi utilizado o BigQuery, ferramenta de Data Warehousing do Google. Através dela, é possível armazenar e consultar dados via SQL de uma maneira bastante performática. Sem falar, que várias outras ferramentas de análise e visualização de dados possuem integração direta com o BigQuery.

### Modelagem de Dados
TO-DO

## Minimal Viable Product

### Camada de Streaming

![Dashboard](https://github.com/andre-ls/mack-fire/blob/main/Dashboard.png)

### Dashboard

Um Dashboard fora feito, possibilitando a visualização dos dados perante e sua posição em relação a um mapa mundial e os detalhes metereológicos detalhados de acordo com sua esta posição.
