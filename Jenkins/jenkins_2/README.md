# jenkins task 2

-----------------------------------------
## 1) What is Jenkins pipeline ?
- is a collection of jobs or steps that brings the software from version control into the hands of the end users by using automation tools. It is used to incorporate continuous delivery in our software development workflow.

-----------------------------------------
## 2) What scripting language is Jenkins pipeline syntax based on ?
- Groovy scripting Language
  
-----------------------------------------
## 3) what are the different ways to trigger pipeline ? 
- webhooks
- REST API
- commit commands
- slack commands

-----------------------------------------
## 4) what is different between parameter and jenkins env variable ?
- Environment variables can be overridden or unset, but params is an immutable Map and cannot be changed
  
-----------------------------------------
## 5) what is organization folder job and what is used for ?
- Organization Folders enable Jenkins to monitor an entire GitHub Organization and automatically create new Multibranch Pipelines for repositories which contain branches and pull requests containing a Jenkinsfile.

-----------------------------------------
## 6) Create jenkins pipeline for your repo and use script file (jenkinsfile) to write pipeline syntax, include parameter functions and env variable in it 
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_2/screenshots/1.1.png)
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_2/screenshots/1.2.png)
## i made it true to test my project, so it will go through test stage
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_2/screenshots/1.3.png)
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_2/screenshots/1.4.png)
## this time i made it false, so it wont go through test stage
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_2/screenshots/1.5.png)
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_2/screenshots/1.6.png)

-----------------------------------------
## 7) Create another multibranch pipeline and filter branches to contain only (master , dev , test ) 
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_2/screenshots/2.1.png)
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_2/screenshots/2.2.png)
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_2/screenshots/2.3.png)
