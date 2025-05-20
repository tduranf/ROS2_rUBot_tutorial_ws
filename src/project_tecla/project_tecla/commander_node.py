#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class Commander(Node):
    def __init__(self):
        super().__init__('commander_node')

        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.timer = self.create_timer(0.5, self.send_command)

        self.pose = None
        self.linear_velocity = 2.0
        self.angular_velocity = 1.5

        print("🔥 MOVIMENT CIRCULAR AMB POSE.X * 2")
        self.get_logger().info('Commander node ready.')

    def pose_callback(self, msg):
        self.pose = msg
        x_doubled = msg.x * 2
        self.get_logger().info(f'Pose x: {msg.x:.2f} → x*2: {x_doubled:.2f}')

    def send_command(self):
        msg = Twist()
        msg.linear.x = self.linear_velocity
        msg.angular.z = self.angular_velocity
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Commander()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down node.')
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
