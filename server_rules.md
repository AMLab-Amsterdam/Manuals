# New Rules on the server

## If you idle, you die.


### Setting up passive sessions

Use srun to run scripts or python or anything

		srun --gres:gpu:1 -C TitanX python experiments.py 
		srun --gres:gpu:1 -C TitanX bash run_experiments.sh

with run_experiments.sh beeing

		python experiments.py --parse_args1 &
		python experiments.py --parse_args1 &
		python experiments.py --parse_args1 &
		python experiments.py --parse_args1 &
		wait

This way you can run 4 experiments in parallel. You can also use a more advanced scheduling system than this.
	

### Setting up interactive sessions that die 

Some people need portforwarding becuase they use tensorboard or mongoDB databases or what not.
In this case you can not get around an interactive session, **but you can kill it when you are done**.

Let's got through it step by step.

		you@desktop: 	tmux
		you@desktop: 	ssh -R 123456:localhost:123456 das5fs
		you@das5fs: 	slurm-run4

Now you will get a node assigned, say node201. But the node does not have the right port-forwarding.

		you@desktop: 	tmux
		you@desktop: 	ssh -R 123456:localhost:123456 das5fs
		you@das5fs: 	ssh -R 123456:localhost:123456 node201
		you@node201: 	bash run_experiments.sh

with run_experiments.sh beeing

		python experiments.py --parse_args1 &
		python experiments.py --parse_args2 &
		python experiments.py --parse_args3 &
		python experiments.py --parse_args4 &
		wait
		pkill -9 -u 


MIND TO KILL YOURSELF IN THE END. pkill will kill all you processes and your node reservation.



