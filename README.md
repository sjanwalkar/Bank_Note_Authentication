# Bank_Note_Authentication-ML, Flask, Flasgger, Docker
 Creating a Bank note Authenticator app & Dockerizing it by uploading it's docker image in Docker Hub.
 
 ## Steps for Dockerizing:<br/>
 - Create a Separate Folder containing all the files <br/>
	- Python code<br/>
	- flask and UI file<br/>
	- data file<br/>
	- pickle file<br/>
- Add Dockerfile and requirements.txt in the same Folder<br/>
	- Dockerfile contains - Downloading Image from docker hub<br/>
		- copying all files from local machine to image directory<br/>
		- exposing a port<br/>
		- setting creating working directory(same as the one where all the files are copied)<br/>
		- installing requirements file<br/>
		- running application<br/>
	- requirements contains- all the application requirement from various libraries<br/> 

### Docker:<br/>
- Next step download Docker for https://www.docker.com (as per system requirements)<br/>
- Install docker<br/>
- Open Terminal and check whether docker is successfully installed by typing in terminal : docker version (Server version will be visible)<br/>
- Set the working directory as the Folder. cd [location/Folder name]<br/>
- Check working directory: pwd OR ls<br/>
- Building docker image: docker build -t [image name] .  # Dot at the end specified current directory it will run Dockerfile present in the folder<br/>
- Running App/Image: docker run [image name]<br/> 


### TESTING:<br/>
- Copy paste URL show after running Image into browser as : [URL/apidocs]<br/>
- Uploading Image into Docker Hub:<br/>
- First Create docker hub free account<br/>
- Login to docker hub through terminal: docker login<br/>
- Enter username and password<br/>
- Create a tag of the image: docker tag [image name]: [version] ‘repository_name’/[image name]<br/>  
(All the image in the docker hub must start with repository name)<br/> 
Eg. docker tag bank_note_authentication:latest sjanwalkar/bank_note_authentication<br/>
- Push image into docker hub: docker push [Image name]<br/>
eg. docker push sjanwalkar/bank_note_authentication<br/>
- Check Image in the docker hub.<br/>

![image](https://user-images.githubusercontent.com/84242964/163308935-747fe986-0523-4fba-8598-d56d04bfabb6.png)

<img width="1255" alt="image" src="https://user-images.githubusercontent.com/84242964/163308780-37ebc2b0-cf65-44d7-b04a-50a461f2cd59.png">


## DOCKER COMMANDS:<br/>
- Check docker image: docker images OR docker image ls<br/>
- Check docker containers: docker ps<br/>
- Delete all unused images and containers: docker system prune<br/> 
- Delete an image: docker rmi [Image name] # Deletes mentioned image<br/>
- Stopping running container: docker stop [container id] # Kills container<br/>


