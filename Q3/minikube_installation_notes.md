Install docker

1) yum install docker -y
2) docker ps


Installing Kubernetes with Minikube

1) Download:
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

2) chmod +x minikube

3) sudo mkdir -p /usr/local/bin/
4) sudo install minikube /usr/local/bin/

5) minikube start --driver=none  ===> if there is docker as default driver
6) minikube status

7) Install hello-minikube
kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.10
kubectl expose deployment hello-minikube --type=NodePort --port=8080

8) Install ngnix
sudo kubectl create deployment nginx --image=nginx
sudo kubectl create service nodeport nginx --tcp=80:80
sudo kubectl get svc
curl 10.101.186.164:30655


8) kubectl get pod
9) minikube service hello-minikube --url

10) sudo kubectl get pods
11) sudo kubectl get deployments
12) sudo kubectl get deployments nginx -o json

docker ps -a



