import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleDriver(Node):
    def __init__(self):
        super().__init__('circle_driver')
        # Publisher to send velocity commands to the diff_drive_controller
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Timer to run the loop at 10Hz (every 0.1 seconds)
        self.timer_period = 0.1  
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.get_logger().info('Circle Driver Node has started successfully!')

    def timer_callback(self):
        msg = Twist()
        # Set constant forward linear velocity
        msg.linear.x = 0.5  # m/s
        # Set constant rotational angular velocity
        msg.angular.z = 0.5  # rad/s
        
        # Publish the message
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CircleDriver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
