
## Better experiment oversight with sacred

We will install all 3 components you need and bring them together in this tutorial.

### 1. install MongoDB

MongoDB is a programm that would run on a server ideally. It will collect and comunicate information with the machines that run your experiments.

For installation, google install mongodb and your exact OS e.g., [Linux Mint 18](http://linuxforever.info/2017/04/13/how-to-install-mongodb-3-4-in-linux-mint-18-ubuntu-16-04/) (makes a big difference)

You can run MongoDB on your server via 

	sudo systemctl start mongodb # Ubuntu 14 
		
	sudo service start mongod # Ubuntu 16 

You can check if its currently running via

	sudo systemctl status mongodb # Ubuntu 14 
	
	sudo service status mongod # Ubuntu 16

It can also help to add this command to your start up applications.


### 2. install + use sacred

Sacred is the python library that organizes your experiments. You will need to install it alongside pymongo.

	pip install sacred pymongo

You can now set up experiments by following this [GUIDE](http://sacred.readthedocs.io/en/latest/quickstart.html). This guide is great read it well.


### 3. install sacredboard

sacredboard is the engine that asks your server for the collected experiment information and displays it for you in a browser window.

First you best set up a python 3(!) conda environment and install

	conda create -n sacredboard python=3.5
	
	source activate sacredboard
	
	pip install sacredboard

! Note that this needs not to be the same environment as your project. In fact I got my own conda environment just for sacredboard.


### 4. Bringin it all together


Now that we got:

* sacredboard on our device of choice

* experimetns with well written sacred code

* a running mongoDB server

we need to connect it all.


First thing to do is [setting up a *unique* port](https://medium.com/mongoaudit/how-to-change-mongodb-default-listening-port-27017-92e35f65670e) for the mongo server (dont ask why, but its important).


Next, we start an experiment that send all information to our mongoDB server data base via our unique port (same as above!!)


	python myexperiment.py -m IP_OF_MONGO_SERVER:MY_PORT:MY_DB

	python experiment.py -m 192.168.1.1:27017:cryoDB



We can now observe our experiments by 


	sacredboard -m 192.168.1.1:27017:cryoDB



That is it already that is all you need to know.


Except, if you run experimetns on servers of the UvA due to security stuff it is best to


* first open a tmux or screen session

* run 

	ssh -R yourport:localhost:yourport fs2






