import sys
import rospy
from geometry_msgs.msg import Twist
import TestDTW
class GoForward():
    def __init__(self):
        # initiliaze
        rospy.init_node('GoForward', anonymous=False)

	# tell user how to stop TurtleBot
	rospy.loginfo("Start connect gazebo")

        # What function to call when you ctrl + c    
        rospy.on_shutdown(self.shutdown)
        
        self.cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        
	#TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
        r = rospy.Rate(100);
        # Twist is a datatype for velocity
        move_cmd = Twist()
	index1 = TestDTW.chooseAction()
        while not rospy.is_shutdown():
	        index = TestDTW.Action(index1)
		if (index == 2):	
		# let's go forward at 0.2 m/s
		   move_cmd.linear.x = 0.1
		# let's turn at 0 radians/s
		   move_cmd.angular.z = 0
		if (index == 1):	
		# let's go forward at 0.2 m/s
		   move_cmd.linear.x = 0
		# let's turn at 0 radians/s
		   move_cmd.angular.z = -0.1
		if (index == 0):	
		# let's go forward at 0.2 m/s
		   move_cmd.linear.x = 0
		# let's turn at 0 radians/s
		   move_cmd.angular.z = 0.1
		if (index == 3):	
		# let's go forward at 0.2 m/s
		   move_cmd.linear.x = -0.1
		# let's turn at 0 radians/s
		   move_cmd.angular.z = 0
		if (index == 4):	
		# let's go forward at 0.2 m/s
		   move_cmd.linear.x = 0
		# let's turn at 0 radians/s
		   move_cmd.angular.z = 0
	        # publish the velocity
		rospy.loginfo(index)
                self.cmd_vel.publish(move_cmd)
	       # wait for 0.1 seconds (10 HZ) and publish again
                r.sleep()
                # rospy.sleep(10)
        
    def shutdown(self):
        rospy.loginfo("Stop ")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        GoForward()
    except:
        rospy.loginfo("Errrr.")

