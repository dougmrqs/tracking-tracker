### Tracking Tracker

The objective of this service is to use one site* where users put their tracking codes, and they are exposed to the public.    

The project consists in using Selenium as a automated tool for navigating the website and some functions to verify if the code is really valid.
It is actually configured to select just CN (China) posts but it can be abstracted to get codes from all origin countries.    

After crawling for a few seconds, it returns a json file to the './db/' folder.    

I've used pipenv to pack it up, so it should be used to unpack and run locally.    

This code is just for research purposes and I've configured it so it is not damaging to the involved parties (such as the data sources).    
By running this code, you assume all your risks and responsabilities.


* http://www.linketrack.com