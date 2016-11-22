# DAS-4 User manual

## Getting an Account

Send an Email to das-account@cs.vu.nl. Make sure to use your uva mail address.
It takes like 1 or 2 days.

## Login

	ssh -o serveraliveinterval=300 USERNAME@fs4.das4.science.uva.nl


## Change your .bashrc

First thing to do after loggin-in: change your .bashrc-file. Use the verion attached. Put it in your home dir and rename it to '.bashrc'. Dont foreget to replace USERNAME.

## Loading modules

To see all modules available
	
	module avail

Some useful modules are already in your .bashrc file.

## Getting CuDNN

Create a symlink 

	ln -s  /home/koelma/nvidia/cudnn-7.0-linux-x64-v4.0-prod/ /home/USERNAME/cudnn/


## MyWatch

Is a nice script that Dennis wrote to view the nodes and who is occupoying them atm.
	
	mywatch

## Getting a GPU

you will also see if these nodes have GPUs. Now you can occupy a node by


	ssh nodeXXX

you can reserve nodes

	qrsh -l gpu=Titan* -l h_rt=300:00:0

## Home folder

The homefolder (4GB) is backed-up every day this is why you are asked to keep your data on

	/var/scratch/USENAME

(40GB). If you use common datasets they are available under
	
	/home/koelma/VisualSearch/


Tip: its beneficial to have symbolic links between /var/scratch and your home dir.

## Common Problems

1. GPU is not found

		unset CUDA_VISIBLE_DEVICES
