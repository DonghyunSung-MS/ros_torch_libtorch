#!/home/dh-sung/anaconda3/envs/drl/bin/python
import torch
from torch import nn

import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray #float array

input_size = 50
output_size = 4
hidden_size = 512

model = nn.Sequential(
                        nn.Linear(input_size, hidden_size),
                        nn.ReLU(),
                        nn.Linear(hidden_size, hidden_size),
                        nn.ReLU(),
                        nn.Linear(hidden_size, hidden_size),
                        nn.ReLU(),
                        nn.Linear(hidden_size, hidden_size),
                        nn.ReLU(),
                        nn.Linear(hidden_size, hidden_size),
                        nn.ReLU(),
                        nn.Linear(hidden_size, hidden_size),
                        nn.ReLU(),
                        nn.Linear(hidden_size, hidden_size),
                        nn.ReLU(),
                        nn.Linear(hidden_size, hidden_size),
                        nn.ReLU(),
                        nn.Linear(hidden_size, output_size),                        
                    )

sm = torch.jit.script(model)

def talker():
    pub = rospy.Publisher('chatter', Float32MultiArray, queue_size=100)
    rospy.init_node('talker', anonymous=True)
    # rate = rospy.Rate(1000) # 10hz
    while not rospy.is_shutdown():
        # output = model(torch.randn(input_size)).detach().numpy()
        output = sm(torch.randn(input_size)).detach().numpy()
        
        pub_array = Float32MultiArray(data=output)
        pub.publish(pub_array)
        # rate.sleep()



if __name__=="__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass