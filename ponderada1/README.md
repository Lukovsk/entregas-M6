# Atividade 1: Turtlesim: simulando um ambiente robótico integrado no ROS

## Enunciado
Crie um script em Python capaz de interagir com o nó de simulação do turtlesim e enviar mensagens nos tópicos que regem a locomoção da tartaruga principal. Utilize este script para reproduzir um desenho de sua autoria. Utilize a estrutura de dados que preferir para representar a “imagem” a ser desenhada. O uso de programação orientada a objetos é obrigatório.

## Implementação

Na pasta /src, há dois arquivos python: **estrela.py** e **sarspinsky.py**.


O primeiro, **estrela.py**, cria um nó ("turtle_controller") que publica mensagens no tópico ```/turtle1/cmd_vel```, que tem como objetivo controlar a velocidade linear e angular da tartaruga 1. Além disso, o ```timer_``` é responsável por alterar essa mensagem antes que ela seja publicada por meio do método ```move_turtle()```.
Assim, **estrela.py** faz com que a tartaruga se mova com uma velocidade por um determinado tempo, pare, gire **144°** ou **π.4/5** e repete isso 5 vezes, até completar a estrela.


O segundo, **sarspinsky.py**, cria uma classe, ```ponto```, que possui um método muito importante chamado de ```spawn_turtle()```. Este método cria um nó ("turtle_spawner") e envia Requests para o tópico /spawn, que cria uma outra tartaruga em determinado ponto cartesiano. Tendo isso em vista, o restante do código simula um fractal muito conhecido, o qual consiste na criação de pontos médios infinitos entre uma escolha aleatória com 3 pontos que formam um triângulo E o ponto anterior criado. Infelizmente o resultado não foi dos melhores, já que alguns modelos de tartaruga se atrapalham na hora de spawnar na cordenada correta :( . Mas foi um ótimo teste.

## Como rodar
Com o ros2 configurado corretamente, basta digitar 

```ros2 run turtlesim turtlesim_node```

Para iniciar o nó da tartaruga e, em outro terminal, rodar um dos arquivos pythons citados.
Ah! Antes disso, não esqueça de digitar

```pip install -r requirements.txt```

para atualizar e baixar todas as bibliotecas necessárias para os códigos.