#include <ros/ros.h>
#include <torch/script.h> // One-stop header.
#include <std_msgs/Float32MultiArray.h>

#include <iostream>
#include <memory>

int main(int argc, char** argv) {
  if (argc != 2) {
    std::cerr << "usage: example-app <path-to-exported-script-module>\n";
    return -1;
  }


  torch::jit::script::Module module;
  module = torch::jit::load(argv[1]);

  ros::init(argc, argv, "talker");

  ros::NodeHandle nh;

  ros::Publisher torch_pub = nh.advertise<std_msgs::Float32MultiArray>("array", 100);
  ros::Rate loop_rate(1000);

  while (ros::ok())
	{

    std::vector<torch::jit::IValue> inputs;
    inputs.push_back(torch::ones({50}));

    // Execute the model and turn its output into a tensor.
    at::Tensor output = module.forward(inputs).toTensor();
		std_msgs::Float32MultiArray msg_array;


		//Clear array
		msg_array.data.clear();

    int length = output.size(0);
    auto tensor_ptr = output.data_ptr<float>();

    msg_array.data.assign(tensor_ptr, tensor_ptr + length);
		//Publish array
		torch_pub.publish(msg_array);
    // ROS_INFO("vector size %i", msg_array.data.size());
		//Let the world know
		//Do this.
		ros::spinOnce();
		//Added a delay so not to spam
		loop_rate.sleep();
	}




  return 0;
}