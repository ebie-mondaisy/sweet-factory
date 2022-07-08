# Sweet Factory - Practical Project
A flask app that will randomly output values and decide a result that is not random. The elements will input a random cake and milkshake flavour and combine them to output an ice cream flavour based on the combination.

## Table of Contents
1. [Introduction](#introduction)
2. [Project Planning and Management](#project-planning-and-management)
3. [Risk Assessment](#risk-assessment)
4. [The sweet-factory app](#the-sweet-factory-app)
5. [Testing](#testing)
6. [The CI CD Pipeline](#the-ci-cd-pipeline)
7. [Challenges and Known Issues](#challenges-and-known-issues)
8. [Final Notes](#final-notes)

## Introduction

This is an individual project that aims to demonstrate learning of Python, Continuous Integration and cloud Fundamentals. The main purpose of the project is to create an application that generates objects following a set of rules that are predefined. The application will run on at least 5 services and they will each have their own function. To show project management skills, a kanban board must be created along with conduction a risk assessment and documenting issues faced during the project. Version control should be handled using Git and the chosen CI server will be Jenkins. To generate a reverse proxy, ngnix should be utilised and configuration management should be handled using ansible. Docker and Docker Swarm will be used for containerisation and orchestration of containers respectively. Finally, the cloud server will be run using Google Cloud Platform and this will include the virtual machines used to handle all the processes.

In this project, I have worked to ensure that I meet all the constraints in the project brief, while ensuring that I produce an application that is fully functioning and clearly demonstrates what I have learnt during training.

[Back to table of contents](#table-of-contents)

## Project Planning and Management

To ensure that my project goes in the right direction, and I am confident with how to proceed, I created a Trello board to organise the tasks I needed to do and keep track of what I have done. The following images show the Trello board I created and the tasks I added for the procedure of the project.

###### Initiation of the Project

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/trello-1.jpg" width="900" height="500"/>

###### During the Project

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/trello-2.jpg" width="900" height="500"/>

[Back to table of contents](#table-of-contents)

## Risk Assessment

For evaluation of the events that could impact the project, I created a risk assessment to weigh up all the possible events that could occur during the project and how they could negatively impact the project. To calculate the impact of each risk, I added a likelihood score and a risk score together. The following table shows the events that may occur and their impact levels on the project.

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/risk-assessment-practical.jpg" width="900" height="500"/>

[Back to table of contents](#table-of-contents)

## The sweet-factory app

To meet the requirements of the project, I developed a random sweet generator that outputs a toothache rating based on "consumption":

- Sweet-Factory (Service 1): This is the service that the user interacts with. This front-end service requests random cake and milkshake names along with a toothache rating and displays these results to the user. Each time the service is refreshed, a new combination is shown to the user.
- Cake-API (Service 2): This service receives GET requests from service 1 and it responds with a random cake name from a list of flavours using the ```random``` import.
- Milkshake-API (Service 3): This service receives GET requests from service 1 and it responds with a random milkshake name from a list of flavours using the ```random``` import.
- Toothache-API (Service 4): This service receives POST requests from service 1 and this provides the randomly selected cake and milkshake names and outputs a toothache rating based on the flavours that have been randomly selected. Each cake and milkshake flavour holds a value that adds to a count if it is selected, and this ultimately results in the toothache rating as an output.
- NGINX (Reverse Proxy): This service directs client requests to the appropriate backend server while operating behind a firewall. The purpose of the reverse proxy is to provide abstraction and ensure that there is an efficient flow of network traffic between servers and clients. In this case, NGINX listens to port 80 on the deployment machine and directs network traffic from port 80 to port 5000 on service 1 (the front-end) where the app is interacted with.

**The Sweet Factory App**

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/app1.jpg" width="900" height="500"/>

**Another Randomisation**

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/app2.jpg" width="900" height="500"/>

**The microservice architecture**

This is a visualisation of the microservices that are running to ensure the functioning of the front-end service - Sweet-Factory.

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/microservice-diagram.jpg" width="900" height="500"/>

[Back to table of contents](#table-of-contents)

## Testing

In order to test that each service works, I conducted unit testing for each of the elements and produced test coverages. To complete testing, I used Pytest and this was useful in telling me which lines needed to be tested and which lines failed. The images below show the unit tests for the four services.

**Sweet-Factory (Front-End) Test**

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/coverage-1.jpg" width="900" height="500"/>

**Cake-API (Service 2) Test**

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/coverage3.jpg" width="900" height="500"/>

**Milkshake-API (Service 3) Test**

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/coverage4.jpg" width="900" height="500"/>

**Toothache-API (Service 4) Test**

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/coverage2.jpg" width="900" height="500"/>

[Back to table of contents](#table-of-contents)

## The CI CD Pipeline

For the project, a CI pipeline needs to be implemented to provide stages for the project. This includes: tracking the project, use of version control, using a development environment, utilising Jenkins as a CI server and using docker swarm for hosting deployment environments. The following image is a diagram of the Ci Pipeline and how everything links together:

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/pipeline-diagram.jpg" width="900" height="500"/>

###### Source Code and Version Control

The programming language for the application is in Python and the application was developed using VSCode. For version control, GitHub was used to push the application to a repository so it can handle the changes that have been made during the project and link to the Jenkins Server for pushing changes for the creation of builds.

###### Utilising Virtual Machines with Google Cloud Platform

- Development VM: This machine was used to create the application, conduct initial unit testing and push changes made to GitHub. The purpose of this machine was to allow me to work on the app before deploying it to another VM. 
- Continuous Integration VM (Jenkins): This machine was used to create builds for the application after pushes to the GitHub repo. Jenkins was used for creating a pipeline build that carries out testing, pushing images to dockerhub, configuration using ansible and deployment to another virtual machine for usage of the app.
- Deployment VM: This machine was used to deploy the application using docker swarm and it is linked to the pipeline builds in Jenkins. Each time a change is made in the GitHub repo, Jenkins automatically starts a build, caused by a webhook, and the application displays its changes on the deployment VM. Here is an image of the deployment VM I used for deployment:

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/swarm-node.jpg" width="900" height="500"/>

<sup>Note: Due to issues with networking and GCP, I was not able to get the swarm worker node to cooperate with the swarm manager. I was guided by my trainer Leon, to only use one node (swarm-manager) to deploy the app</sup>

###### Using a Jenkins Pipeline

With a webhook to my GitHub repository, every time a change is pushed to GitHub, Jenkins automatically starts a pipeline build. The following image shows the builds that I have created and how successfully there were at each point:

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/jenkins-builds.jpg" width="900" height="500"/>

**Explaining the Pipeline Build Steps**

1. Testing each service in the app to ensure that they function as intended.
2. Log into dockerhub and build images for each service to be pushed to dockerhub as repositories.
3. Run ansible to complete configuration for the application.
4. Copy the docker-compose and nginx files to build the application for deployment onto the swarm manager.

###### Ansible Configuration

To provide an example of how the playbook works, I have attached an image below:

<img src="https://github.com/ebie-mondaisy/sweet-factory/blob/main/images/ansible-process.jpg" width="900" height="500"/>

Each step shows the installation of dependencies and the deployment of the app to the virtual machine for interaction by the user.

[Back to table of contents](#table-of-contents)

## Challenges and Known Issues

**Known issues with the project**

Throughout the project, I had experienced many issues with the project and I had removed parts of the project that were not needed in regards to time constraints. Thankfully, there is only one identified issue for the project. I would include appearance changes but that was not the most important part of the project this time around.

- Currently, there is only one docker swarm node working for deployment. The swarm manager is working alone as the swarm worker did not properly communicate with the swarm manager. This was discovered to be a fault with an underlying network and would not have been resolved by creating new machines. It was advised to solely use the swarm manager as there is currently no fix for the issue.

**Challenges faced throughout the project**

There were a lot of new processes that I have worked with during this project. This enabled me to learn new things but it was also quite challenging to operate with these new processes.

- Docker is a service that I have never worked with before. It has a lot of elements to it and there is a lot to digest in order to work with effectively. However, I enjoyed working with docker and learning new ways to deploy an app and handle multiple services at once.
- In my previous project, I had worked with Jenkins but I had only utilised a freestyle build. For this project, I worked with pipeline builds, another new concept to me. It was initially tricky at first, but I managed to get to grips with the required layout. I did still experience some errors along the way.
- Ansible is another platform that I was unfamiliar with and it was also quite difficult to understand. However, it was able to show me an easier way of configuration for an application including deployment, configuration management, execution of tasks and handling multiple nodes.

[Back to table of contents](#table-of-contents)

## Final Notes

**Future Work**

Future works of this project are likely to involve the resolution of the docker swarm issues that were experienced and hopefully styling the application to look more aesthetically pleasing. I would also like to add a database element to the application, so users are able to look at the history of each random combination after the result has been stored in the database. Additionally, for more range, I would add more values to each of the lists in each service to provide more combinations for the user to interact with.

**Conclusion and Reflections**

Overall, I am happy with the outcome of the project, and I have learnt about new platforms and software that I can use in my future works. I am extremely grateful for the help and support that I have received during this project as it has helped me to progress. I would specifically like to thank my trainers Adam Gray and Leon Robinson for teaching me what I know and my colleagues for assisting with errors when they had the time.

In terms of reflection, I believe I can use the elements that I have learnt and apply them to software that I create in the future. I have also noticed that I have become better at managing my time and I was able to complete this project while adhering to the constraints with time left over to make any finishing touches.

[Back to table of contents](#table-of-contents)