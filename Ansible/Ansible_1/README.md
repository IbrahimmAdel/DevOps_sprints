# Ansible Task 1

## 1) install nginx on machine
```
- name: install nginx
      become: true
      apt:
          name: nginx
          state: latest
```
## 2) configure nginx to listen on port 8090
```
 - name: edit listen configuration
      become: true
      lineinfile:
        path: /etc/nginx/sites-available/default
        regexp: '^(?P<group>.*listen.*) 80;'
        line: '\g<1> 8090;'
        backrefs: yes   
```
## 3) change nginx default page 
```
- name: edit nginx default page
      copy:
        src: index.html
        dest: /var/www/html/index.html
```
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Ansible/Ansible_1/screenshots/nginx.png)

-------

## 4) clone [Node.JS App](https://github.com/sabreensalama/dockerize-node-app-task) and install the application dependencies and run it on port 8080
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Ansible/Ansible_1/screenshots/node%20app.png)



