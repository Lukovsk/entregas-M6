# Ponderada 1: simulando uma tartaruga com o ROS2 (Robot Operating System)

## Enunciado
Crie um script em Python capaz de interagir com o nó de simulação do turtlesim e enviar mensangens nos tópicos que regem a locomoção da tartaruga principal. utilize esse script para reproduzir um desenho de sua autoria. Utilize a estrutura de dados que preferir para representar a "imagem" a ser desenhada. O uso de programação orientada a objetos é obrigatório.

## Descrição da Solução
Na pasta /src, há dois arquivos python: **estrela.py** e **sarspinsky.py**.
O primeiro, **estrela.py**, cria um nó ("turtle_controller") que publica mensagens no tópico ```/turtle1/cmd_vel```, que tem como objetivo controlar a velocidade linear e angular da tartaruga 1. Além disso, o ```timer_``` é responsável por alterar essa mensagem antes que ela seja publicada por meio do método ```move_turtle()```.
Assim, **estrela.py** faz com que a tartaruga se mova com uma velocidade por um determinado tempo, pare, gire **144°** ou **π.4/5** e repete isso 5 vezes, até completar a estrela.
 