# Web-Application-Attacks
## Setup
````
Windows:

Visit the Docker website at https://www.docker.com/get-started and click on "Get Docker Desktop for Windows".
Download the Docker Desktop installer and run it.
Follow the prompts in the installer to complete the installation process.
Once the installation is complete, Docker should be running on your Windows system.

macOS:

Visit the Docker website at https://www.docker.com/get-started and click on "Get Docker Desktop for Mac".
Download the Docker Desktop installer and open it.
Drag the Docker icon to the Applications folder to complete the installation.
Open Docker from the Applications folder to start Docker on your macOS.

Linux:

Docker provides installation instructions specific to various Linux distributions. You can find the installation guide for your specific distribution at https://docs.docker.com/engine/install/.
Choose your Linux distribution from the list and follow the instructions provided to install Docker.
After installing Docker, you can verify the installation by opening a terminal or command prompt and running the following command:
````
## Basic Demo
### Installing git on Windows via powershell cmd prompt
````
https://git-scm.com/download/win
````
### Cloning this git repository
````
git clone https://github.com/xsudoxx/Web-Application-Attacks.git
cd Web-Application-Attacks
cd Demo
````
### Option #1 building our docker container and running it
````
Open [Docker Desktop]
Open [VSCODE]
In [VSCODE] Open [Terminal]
docker build -t myapp .
docker run -p 5000:5000 myapp
````

### Option #2 building our docker image in VSCODE
````
Open [VSCODE]
On the left hand side find [Extensions]
In [Extensions] search for "Docker" and install
````

![image](https://github.com/xsudoxx/Web-Application-Attacks/assets/127046919/ac84fb23-122a-4b96-bf7b-94f7c9c599f3)

````
Find [Dockerfile]
[Right Click]
Find "Build Image" and click on it
Go to [Docker Desktop]
Find your Image Name
Run in [VSCODE][Terminal]
docker run -p 5000:5000 YourImageNameFromDockerDesktop
````

https://github.com/xsudoxx/Web-Application-Attacks/assets/127046919/0829da71-5a19-456f-a7f7-48fbcb8315a3

````
http://127.0.0.1:5000
````
![image](https://github.com/xsudoxx/Web-Application-Attacks/assets/127046919/a600f54d-c1d1-4520-9dd8-5c50ec4da7e6)

````
http://127.0.0.1:5000/login
````
![image](https://github.com/xsudoxx/Web-Application-Attacks/assets/127046919/70326593-7e07-4a9f-84b3-a13e876c7cf3)
