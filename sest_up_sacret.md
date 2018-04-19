
### Install MongoDB

MongoDB is a programm that would run on a server ideally. It will collect and comunicate information with the machines that run your experiments.

For installation, google install mongodb and your exact OS e.g., Linus Mint 18 (makes a big difference)

* [Linux Mint](http://linuxforever.info/2017/04/13/how-to-install-mongodb-3-4-in-linux-mint-18-ubuntu-16-04/)


You can run MongoDB on your server via 

	sudo systemctl start mongodb # Ubuntu 14 
		
	sudo service start mongod # Ubuntu 16 

You can check if its currently running via

	sudo systemctl status mongodb # Ubuntu 14 
	
	sudo service status mongod # Ubuntu 16

It can also help to add this command to your start up applications.


### Install sacred

Sacred is the python library that organizes your experiments. You will need to install it alongside pymongo.

	pip install sacred pymongo


### set up experiments by following this guide

This guide is great read it well.

[GUIDE](http://sacred.readthedocs.io/en/latest/quickstart.html)



### sacredboard

sacredboard is the engine that asks your server for the collected experiment information and displays it for you.

First you best set up a python 3(!) conda environment and install
	
	pip install sacredboard

note that needs not to be the same environment as your project. In fact I got my own conda environment just for sacredboard.


### All comes together



Now that we got:

* sacredboard on our device of choice

* experimetns with well written sacred code

* a running mongoDB server

we need to connect it all.


First thing to do is setting up a *unique* port for the mongo server (dont ask why, but its important)

https://medium.com/mongoaudit/how-to-change-mongodb-default-listening-port-27017-92e35f65670e


Next thing is we start an experiment


	python myexperiment.py -m IP_OF_MONGO_SERVER:MY_PORT:MY_DB

	python experiment.py -m 192.168.1.1:27017:cryoDB



This writes the experiment results to the a Mongo DB database specifically the cryoDB.


We can now observe our experiments by 


	sacredboard -m 192.168.1.1:27017:cryoDB










