# Task 2 Docker 

## 11. Run an instance of nginx:alpine with a name nginx and map port 8080 on the container to 3828 on the host.

![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Docker/Docker_2/Screenshots/11.png)
---
## 12. Create ubuntu image and check the size of it.

![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Docker/Docker_2/Screenshots/12.png)

## 13. Run a container named blue-app using image KodeKloud/simple-webapp and set the environmet variable APP_COLOR to blue. make the app available on port 38282 on the host. the app listens on port 8080. 

![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Docker/Docker_2/Screenshots/13.png)
---
## 14. Deploy a mysql database using the mysql image and name it mysql-db. set the database password to use db_pass123 then inspect it to check the value.

![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Docker/Docker_2/Screenshots/14.png)
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Docker/Docker_2/Screenshots/14..png)
---
## 15. Pull the code from https://github.com/sabreensalama/simple-flask-app/tree/main and create a docker file for this flask app.

## Docker file : [Dockerfile]()

![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Docker/Docker_2/Screenshots/15.png)
---
## 16. Create a volume called mysql_data, run a mysql container again, but this time map a volume to the container so that the data stored by the container is stored at /opt/data on the host. use the same name : mysql-db and same password : db_pass123 as before. Mysql stores data at /var/lib/mysql inside the container.

#### create mysql_data directory.

![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Docker/Docker_2/Screenshots/16.1.png)

#### Run the container , and create a directory called 'From_container' in it.

![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Docker/Docker_2/Screenshots/16.2.png)

#### The directory 'From_container' was created in mysql_data directory.

![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Docker/Docker_2/Screenshots/16.3.png)

#### Back agian and stop the container then delete it. 

![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Docker/Docker_2/Screenshots/16.4.png)

####  After delete the container , The directory 'From_container' still in mysql_data directory.

![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Docker/Docker_2/Screenshots/16.5.png)
