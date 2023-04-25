#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math


class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.time = 1
        self.timer_ = self.create_timer(self.time, self.move_turtle)
        self.twist_msg_ = Twist()
        self.counter = 0
        
    def move_turtle(self):
        self.counter += 1
        
        velocity = 5.4
            
        if self.counter % 2 == 0 and self.counter < 10:
            self.twist_msg_.linear.x = 0.0
            self.twist_msg_.angular.z = -math.pi*4/5
        if self.counter % 2 == 1 and self.counter < 10:
            self.twist_msg_.linear.x = velocity
            self.twist_msg_.angular.z = 0.0 
        if self.counter == 10:
            self.twist_msg_.linear.x = 0.0
            self.twist_msg_.angular.z = 0.0
                    
        self.publisher_.publish(self.twist_msg_)


def main(args=None):
    rclpy.init()
    turtle_controller = TurtleController()
    
    rclpy.spin(turtle_controller)
    
    turtle_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()