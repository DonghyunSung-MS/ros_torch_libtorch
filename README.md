# ros_torch_libtorch
simple ros neural network publisher using torch

## How to Build
```bash
# in catkin build folder
conan install <path to conan txt>/conanfile.txt
catkin_make
```

## Simple Experment Results
* Inference(prediction or evaluation) Speed
* MLP
    * libtorch(cpp) jit script(3000hz) > pytorch jit trace(2500hz) > pytorch module(800hz)
