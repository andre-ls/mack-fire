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

## Solução

![arquitetura da solução](https://github.com/andre-ls/mack-fire/blob/main/Foto%20da%20Arquitetura%20drawio.png)


Utilizando ferramentas de processamento de dados da plataforma Google Cloud, utilizaremos de dados em streaming a cada 10 minutos do INPE e dados em Batch mensais e anuais para filtrar dados vazios, enriquecer a base de dados e aprimorar os dados relevantes. Os dados serão ingeridos a o serviço de cloud function, por meio de programação em python,  em seguida os dados Streaming serão processados pelo serviço de mensagem do Pub/Sub e os dados em batch serão armazenados em Cloud Storages de acordo com a arquitetura medalhão (Bronze, Silver, Gold), ambos transformados por meio do serviço de Dataflow. Após isso serão alimentados ao Bigquery onde podem ser usados por ferramentas de BI.


## Resultado

![Dashboard](https://github.com/andre-ls/mack-fire/blob/main/Dashboard.png)


Um Dashboard fora feito, possibilitando a visualização dos dados perante e sua posição em relação a um mapa mundial e os detalhes metereológicos detalhados de acordo com sua esta posição.
