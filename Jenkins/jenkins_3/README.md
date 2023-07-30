# TASK 3 Jenkins

## 1) what is the benefit of using master-slave architecture rather than building on master only ?
- can run alot of pipelines in paraller 
- can have differnet environments

----------------------------------------------------------
## 2) what is different between authorization and authentication ?
- authentication: verify users identities.
- authorization:  determining what level of access authenticated users should have.

----------------------------------------------------------
## 3) make jenkins-shared-library and make your jenkinsfile which you used in lab2 to point to this library
## used files: [building.groovy](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/jenkins/task%203/vars/building.groovy) , [deploying.groovy](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/jenkins/task%203/vars/deploying.groovy) , [testing.groovy](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/jenkins/task%203/vars/testing.groovy) , [Jenkinsfile](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_3/Jenkinsfile) 
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_3/screenshots/1.1.png)
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_3/screenshots/1.2.png)
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_3/screenshots/1.3.png)


----------------------------------------------------------
## 4) try to make new slave as container or ec2 server and configure master to use it
## - launch EC2 instance and enable port 22 (ssh) & 50000 (jenkins)
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_3/screenshots/2.1.png)
## - after set configration between jenkins and ec2 and enable connetion between them , add slave in jenkins
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_3/screenshots/2.2.png)
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_3/screenshots/2.3.png)
## - run any script with slave agent
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_3/screenshots/2.4.png)
## - run by 'ec2-slave'
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Jenkins/jenkins_3/screenshots/2.5.png)


