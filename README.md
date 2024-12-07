# **Mack Trabalho Final**
Este trabalho almeja processar dados sobre queimadas do **Instituto Nacional de Pesquisa Espacial**, que são atualizados a cada 10 minutos para fins de 
Pesquisa por diversos atores, sejam eles ONGs,  institutos independentes de pesquisa, governos estrangeiros, instituições públicas, autoridades federais entre outros. 

## Apresentação do problema

O problema se demonstra na falta de contextualização dos dados no âmbito de registrar métricas sobre a devastação ambiental que estas queimadas causam, e que podem resultar em danos além das fronteiras brasileiras. A característica de abrangência sem fronteiras das queimadas significam que sua classificação e subsequente solução é um problema de interesse internacional.

## Contexto dos Dados

O INPE registra dados geográficos e meteorológicos por meio de satélites de focos de queimadas pelo Brasil possibilitando o rastreamento destes fenômenos em tempo “quase real”, com um novo registro a cada 10 minutos, os dados estão disponíveis em CSV e KML.

Os dados são divididos nas seguintes colunas: 

**Latitude**
**Longitude**
**Data**
**Temperatura a 2 metros**
**Humidade Relativa**
**Temperatura aparente**
**Dia (Binário)**
**Precipitação**
**Chuva**
**Pressão da superfície**
**Velocidade do vento**
**Direção do vento**
**Data de Inserção**

## Objetivo

A contextualização e medição dedicada dos dados de locais com focos de incêndio constantes possibilita uma análise crítica por grupos e organizações com expertise e autoridade necessária e dará apoio à esforços que almejam prevenir, conter e securitizar os locais com gravidade séria de desmatamento por queimadas, possivelmente interceptando as queimadas com causas artificiais e preservando as biosferas afetadas pelas queimadas com causas naturais.

## Solução

![arquitetura da solução](https://github.com/andre-ls/mack-fire/blob/main/Trabalho%20Final%201.1.drawio.png)


Utilizando ferramentas de processamento de dados da plataforma Google Cloud, utilizaremos de dados em streaming a cada 10 minutos do INPE e dados em Batch mensais e anuais para filtrar dados vazios, enriquecer a base de dados e aprimorar os dados relevantes. Os dados serão ingeridos a o serviço de cloud function, por meio de programação em python,  em seguida os dados Streaming serão processados pelo serviço de mensagem do Pub/Sub e os dados em batch serão armazenados em Cloud Storages de acordo com a arquitetura medalhão (Bronze, Silver, Gold), ambos transformados por meio do serviço de Dataflow. Após isso serão alimentados ao Bigquery onde podem ser usados por ferramentas de BI.

