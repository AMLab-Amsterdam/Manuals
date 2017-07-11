# DAS-5 User manual

## Getting an Account

Send an Email to das-account@cs.vu.nl. Make sure to use your uva mail address.
It takes like 1 or 2 days.

## Login

	ssh -o serveraliveinterval=300 USERNAME@fs4.das5.science.uva.nl

or 
	
	ssh -o serveraliveinterval=300 USERNAME@fs2.das5.science.uva.nl

## Change your .bashrc

First thing to do after loggin-in: change your .bashrc-file. Use the verion attached. Put it in your home dir and rename it to '.bashrc'


## Loading modules

To see all modules available
	
	module avail

Some useful modules are

	module load cuda70/toolkit
	module load cuDNN/cuda75/5_5.1.3
	module load opencl-nvidia/7.0
	module load opencl-amd
	module load opencl-intel/4.5-mic

Tip: You can store a standard list in your .bashrc

## MyWatch

Is a nice script that Dennis wrote to view the nodes and who is occupoying them atm.
	
	mywatch

Alternatively (if you loaded module load prun):

	squeue

## Getting a GPU

Run slurm to get a node with multiple GPUs but pay attenstion the nodes with more GPUs are rarer.

	slurm-run-4

If you specifically know the node you want you can also run

	srun -t 7000:00:00 -u --pty -w node403 bash -i

is reserving node 403 for 7000 hours.

The nodes assosiated with AMLAB are on fs2 nodes 201 (2 Titan X), 202 (3 Titan X), 204 (4 Titan X Pascal). Run 

 	getnodeX

to get node X.

## Home folder

The homefolder is backed-up every day this is why you are asked to keep your data on

	/var/scratch/USENAME

If you use common datasets they are available under
	
	/home/koelma/VisualSearch/


Tip: its beneficial to have symbolic links between /var/scratch and your home dir.

## Common Problems

1. GPU is not found

		unset CUDA_VISIBLE_DEVICES
		
2. First batch is slow (tensorflow, keras, e.g.)
in .bashrc at bottom:

	export CUDA_CACHE_PATH=/local/.nv/ 
	export CUDA_CACHE_DISABLE=0
