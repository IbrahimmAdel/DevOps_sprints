# LAB 4 IN AWS

# TASK 1:
## Launch a jump host and ssh to it, then ssh from bastion to the private machine

## (1) Create bastion server and private server
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/task1.1.png)

## (2) SSH to bastion server from localhost
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/task1.2.png)

## (3) SSH to private instance through bastion server
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/task1.3.jpeg)
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/task1.4.jpeg)

# TASK 2:
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/task.png)

## Create VPC with 4 subnets
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/task3%20.%20VPC.png)

## Create 4 instances
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/2.instances.png)

## Create 2 load-balancers
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/2.%20load-balancers.png)

## First Target Group
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/2.target-group-1.png)

## Second Target Group
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/2.target-group-2.png)

## Edit in nginx.conf file to reroute traffic to the private load-balancer
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/2.nginx-reroute%20traffic.png)

## first apache2 page from the public load balancer DNS
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/2.7.png)

## second apache2 page after i edit in index.html file from the public load balancer DNS
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/2.8.png)

# Task 3: 
## Create the same diagram but the 4 instances is created by auto-scalling

## Create 2 Auto-Scalling-Groups (public & private)
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/task3%20auto-scaling-groups.png)

## 4 instances created by 'asg'
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/task3.%20instances.png)

## apache2 page from public load balancer DNS
![](https://github.com/IbrahimmAdel/DevOps_Bootcamp/blob/main/AWS/task%204/screenshots/task3%20apache2.png)
