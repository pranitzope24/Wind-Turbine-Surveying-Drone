# Wind-Turbine-Surveying-Drone
Official Repo of Wind Turbine Surveying Drone

## Problem-Statement
To design an autonomous drone that can survey the blades of a wind turbine and provide extensive details of the type and level of damage on the blades.


## Project

**Modules**-We have two modules in the project-

**Damage Detection** - This module is largely concerned with detecting, locating and classifying damage on the blades. We are using some modules from ROS and python modules such as TensorFlow, PyTorch OpenCV and PIL. 

**Trajectory**-This module will involve path planning and trajectory for the drone. As far as possible, we have to try and stick to the part of the original doc that said we must try to achieve this without stopping the blades. 

**Repairing**-Our plan is to initially focus only on detection. If we manage to complete that part well in time, we will move on to the repairing part.


## Damage-Detection
In this module, we will largely be working with deep learning image detection and classification models. Our job will be to do the following three things.

**Collect data**- We will have to search for data over multiple sources across journals and engineering databases to get reliable data for our model. The three of us heads have already started with this, and we’ll try to make sure this gets over asap while the ROS training is going on. 

**Develop a reliable model**- This will be our most important and most challenging job, we’ll have to get accustomed to Tensorflow, Opencv, and various other image processing softwares. While a hard task, we hope for this to be a good learning experience for everyone

**Integrate the model with ROS**- Finally, we will have to integrate our wrested DL model with the ROS on which the trajectory module works. This does not appear to be a very hard problem, but to leave nothing to chance we will integrate the DL module with ROS as frequently as we can. This will make sure it doesn’t give any major problems at the end. This will require us to be competent with ROS, but the brunt of the ROS part will be with the Trajectory module.

## Trajectory
This is the module is the heart of the ROS portion of our project. We will basically do two main things-

**Plotting a path**- The primary objective here is to be able to do the detection with no need to stop the WT, but this may or may not be possible at places given hardware constraints. This is the part that your app was concerned with. It will involve 3D modelling, calculus and path planning. 

**Integrating the hardware with the trajectory using ROS**-This is the heart of the trajectory module. It will involve intense ROS usage that will integrate the various components of the drone with the path. This will be a very dynamic module and will involve close work with the detection module. 

## Simulations-and-Softwares
We will simulate all the drone processes using softwares like-

* SITL (Software In The Loop) – Simulates a drone
* Gazebo - Simulator
* ROS (Robot Operating System) – Libraries of robot applications
* Ardupilot / PX4 - firmware

All this will mostly be the domain of the trajectory module but Detection module will have to get into it too at times. 
The DL module will use softwares such as Tensorflow, Opencv, etc and this list will grow as the project progresses. 

## Hardware-Setup
Basically, we will be using-
* Python for most programming. 
* Ubuntu shell as our environment
* ROS for simulation and integration. 
For this, we will need to either dual boot or install a VM in our systems, the former is recommended. 



