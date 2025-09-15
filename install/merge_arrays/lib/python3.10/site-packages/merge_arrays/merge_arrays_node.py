import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray

class MergeArraysNode(Node):

	def __init__(self):
		super().__init__('merge_arrays_node')
		self.publisher = self.create_publisher(Int32MultiArray, '/output/array', 10)

		self.subscription1 = self.create_subscription(Int32MultiArray, '/input/array1', self.array1_callback, 10)
		self.subscription2 = self.create_subscription(Int32MultiArray, '/input/array2', self.array2_callback, 10)

		self.array1 = None
		self.array2 = None

	def array1_callback(self, msg):
		self.get_logger().info('Received array 1')

		self.array1 = msg.data
		self.process_arrays()

	def array2_callback(self, msg):
		self.get_logger().info('Received array 2')	
		self.array2 = msg.data
		self.process_arrays()

	def process_arrays(self):
		self.get_logger().info('Processing arrays...')
		if self.array1 is not None and self.array2 is not None:
			self.get_logger().info(f'Array 1: {self.array1}')
			self.get_logger().info(f'Array 2: {self.array2}')

			merged_array = sorted(self.array1 + self.array2)

			self.get_logger().info(f'Merged array: {merged_array}')

			msg = Int32MultiArray()
			msg.data = merged_array
			self.publisher.publish(msg)




def main(args=None):
	rclpy.init(args=args)

	node = MergeArraysNode()

	rclpy.spin(node)

	node.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()
