#!/usr/bin/env python3
import rclpy
from turtlesim.srv import Spawn
from random import randint


class ponto:
    def __init__(self, cordX, cordY):
        self.cordX = cordX
        self.cordY = cordY
  
    def spawn_turtle(self):
        rclpy.init()
        node = rclpy.create_node('turtle_spawner')

        client = node.create_client(Spawn, 'spawn')

        while not client.wait_for_service(timeout_sec=1.0):
            node.get_logger().info('Serviço não disponível, tentando novamente...')


        req = Spawn.Request()
        req.x = float(self.cordX)
        req.y = float(self.cordY)
        req.theta = 0.0

        future = client.call_async(req)

        rclpy.spin_until_future_complete(node, future)

        if future.result() is not None:
            node.get_logger().info('Tartaruga spawnada com sucesso!')
        else:
            node.get_logger().info('Falha ao spawnar a tartaruga')

        node.destroy_node()
        rclpy.shutdown()
  
    def cords(self):
        return [self.cordX, self.cordY]
    
def randomChoice(array):
    return array[randint(0, len(array)- 1)]

def cordPM(p1, p2):
    cordsP1 = p1.cords()
    cordsP2 = p2.cords()
    xPM = ((cordsP2[0] + cordsP1[0])/2)
    yPM = ((cordsP2[1] + cordsP1[1])/2)
    return [xPM, yPM]


pontoInferiorDireito = ponto(8, 2)
pontoInferiorEsquerdo = ponto(2, 2)
pontoSuperior = ponto(6, 10)

pontoInferiorDireito.spawn_turtle()
pontoInferiorEsquerdo.spawn_turtle()
pontoSuperior.spawn_turtle()

pontosTriangulo = [pontoSuperior,
                   pontoInferiorDireito,
                   pontoInferiorEsquerdo]

cordPMAnterior = cordPM(randomChoice(pontosTriangulo),
                        randomChoice(pontosTriangulo))

PMAnterior = ponto(cordPMAnterior[0],
                   cordPMAnterior[1])
PMAnterior.spawn_turtle()

for i in range(0, 15000):
    cordNovoPM = cordPM(randomChoice(pontosTriangulo),
                        PMAnterior)
    novoPM = ponto(cordNovoPM[0],
                   cordNovoPM[1])
    novoPM.spawn_turtle()
    
    PMAnterior = novoPM