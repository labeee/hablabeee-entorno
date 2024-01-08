# HabLabEEE - Entorno

<br>
<center><h1>Objetivos</h1></center>
<br>
A ferramenta tem como objetivo buscar, utilizando duas APIs do Google Maps Platform, múltiplos pontos de interesse nos arredores das coordenadas de cada habitação, construindo uma planilha onde estão indicados os pontos encontrados, com suas descrições, além da distância e tempo de viagem de cada com relação à coordenada inicial.
<br><br>
<h2>Fluxo de processo</h2>
Com todas as variáveis devidamente definidas, é lida cada linha da planilha de amostra, e para cada uma o seguinte processo:

- A coordenada é devidamente formatada e registrada;
- É chamado o método places_nearby, passando como parâmetros a coordenada da habitação, os pontos de interesse como termo de busca (um de cada vez) e o parâmetro rank_by='distance' que irá retornar, por ordem de distância, os 20 primeiros locais que o Google Maps encontrar;
- É criada uma planilha que é então preenchida com as informações essenciais retornadas
- São adicionadas a essa planilha as informações correspondentes à linha da habitação na planilha original (além de pontos de interesse, a planilha também terá o nome, endereço, coordenada, etc. da habitação usada de ponto central);
- Essa planilha preenchida é então salva dentro de system com um nome que diferencie ela das outras;
- Cada planilha é separadamente lida, e é aplicado o DistanceMatrix a cada habitação com relação aos pontos encontrados, então a distância e tempo de viagem são salvos nela;
- Todas as planilhas são concatenadas e é criado um arquivo em output do processo completo.
