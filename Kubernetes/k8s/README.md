# task 1 Kubernetes
## Create nginx-deployment with 3 replicas 
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
      type: front-end
  template:
    metadata:
      labels:
        app: nginx
        type: front-end
    spec:
      containers:
        - name: nginx
          image: nginx:1.14.2
          ports:
          - containerPort: 80
```
## make sure that all 3 pods from deployment are running 
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Kubernetes/k8s/screenshots/2.png)
## create nginx-service with selector to match pods in the deployment
```
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: ClusterIP
  ports:
    - targetPort: 80
      port: 80 
  selector:
      app: nginx
      type: front-end
```
## create the service
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Kubernetes/k8s/screenshots/4.png)
## describe the service to make sure that it has endpoints of any deployment pods IP 
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Kubernetes/k8s/screenshots/5.png)
## check nginx service from a debug-pod
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Kubernetes/k8s/screenshots/6.png)
![](https://github.com/IbrahimmAdel/DevOps_sprints/blob/main/Kubernetes/k8s/screenshots/7.png)
