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

## Minimal Viable Product (MVP)

Como Produto Mínimo Viável da arquitetura completa proposta, este projeto focou em implementar inicialmente a camada de Streaming da arquitetura, julgando que o acompanhamento em quase tempo real dos eventos de queimada seria uma demanda mais prioritária dentro do contexto do problema, podendo auxiliar em uma rápida tomada de decisão para mitigar os danos dos eventos atuais.

### Camada de Streaming

A Arquitetura do MVP implementado segue o desenho abaixo, que de certa forma consiste em um recorte da camada de Streaming da arquitetura completa.


### Dashboard

Para o consumo e exibição dos dados processados, um dashboard foi criado utilizando o Streamlit, uma plataforma open-source que permite a criação rápida e fácil de aplicativos simples a partir da utilização de código Python. 

![Dashboard](https://github.com/andre-ls/mack-fire/blob/main/Dashboard.png)

Um Dashboard fora feito, possibilitando a visualização dos dados perante e sua posição em relação a um mapa mundial e os detalhes metereológicos detalhados de acordo com sua esta posição. Suas visualizações foram criadas com o objetivo de fornecer ao usuário um rápido e claro panorama do cenário atual de ocorrência de queimadas na América do Sul, focando principalmente na sua localização, mas também adicionando informações metereológicas que possam contribuir para uma inferência sobre a possível origem dos eventos, como a temperatura, níveis de precipitação e umidade, ou que possam ser de relevância para o devido combate à ocorrência e sua mitigação, como a velocidade e direção do vento.

O Dashboard foi programado para uma atualização automática a cada 10 minutos, de forma a fazê-lo capturar o estado mais recente dos dados. Entretanto, para fins de economia e evitar custos computacionais à plataforma do Streamlit, que hospeda a aplicação gratuitamente em sua infraestrutura, as atualizações automáticas são desativadas após 100 execuções a partir da ativação da aplicação.

## Sobre o Projeto

<img src="https://logodownload.org/wp-content/uploads/2017/09/mackenzie-logo.png" alt="Mackenzie" width="500"/>

Este projeto foi desenvolvido como trabalho final da disciplina de DevOps e DataOps, componente do curso de Pós-Graduação em Engenharia de Dados oferecido pela Universidade Presbiteriana Mackenzie e lecionada pelo Prof. Gustavo Ferreira.

Como disciplina final de todo o curso, o trabalho propôs como objetivo a aplicação de todos os conhecimentos adquiridos durante o curso para arquitetar uma solução completa de dados para a resolução de um problema de livre escolha por parte dos alunos, e a partir disso implementar um Produto Mínimo Viável da solução em um ambiente de nuvem. 

Membros do Grupo:
- André Luis Andrade Machado
- Bruno Pekelman
- Larissa Vicentin Gramacho
- Thomas Bauer Corsaro

## Possíveis Próximos Passos

Como possíveis próximos passos para a otimização e evolução deste projeto, os seguintes pontos são levantados:
- Implementação da ingestão dos dados do INPE em outros níveis de atualização, como dados diários e mensais.
- Implementação da camada de processamento de dados em Batch, complementando assim o MVP do projeto.
- Implementação de tratativas específicas para o processamento em Streaming, como por exemplo, em situações onde não há ocorrência de eventos ou situações de duplicidade dos dados.
- Incrementar o dahsboard com visualizações que analisem dados históricos sobre os eventos de queimada.
- Adicionar o dashboard visualizações específicas que possam tirar maior proveito das informações de velocidade e direção do vento.

