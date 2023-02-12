#GeoLocation  ![image](https://user-images.githubusercontent.com/108284950/218310916-06c816d9-47c6-4afe-bb4b-a853b0d09cb1.png) 


##Introduction
This is a project to search for cities in Israel in Hebrew and English and display their location on a map.

Part of a CS degree course (EASS) final project.

##Demonstration



##Design
 

##Requirments
-	Docker
-	WSL / compatible linux machine


##Deployment
First of all you will need Git and Docker installed on your machine.
1.	Open the Terminal, go inside your desired folder and run the following command:
git clone https://github.com/EASS-HIT-PART-A-2022-CLASS-II/GeoLocation.git
2.	Then you will have to go inside the "GeoLocation" folder using the following command:
cd GeoLocation
3.	To build the docker
docker compose build
4.	To run GeoLocation, you will have to enter the following command:
docker compose up
5.	Congratulations! You may access GeoLocation following address:
http://localhost:8501/





