#!/bin/bash

echo "kubectl config view"
sudo kubectl config view
echo ""
echo ""
echo "kubectl config get-contexts"
sudo kubectl config get-contexts
echo ""
echo ""
echo "kubectl config current-context"
sudo kubectl config current-context
echo ""
echo ""
echo "kubectl config current-context"
sudo kubectl config current-context

echo ""
echo ""
echo "List pods"
kubectl get pods
echo ""
echo ""
echo "List namespaces"
kubectl get namespaces
echo ""
echo ""
echo "List deployments"
kubectl get deployments
echo ""
echo ""
echo "Describe NGNIX deployment"
kubectl describe deployment nginx
echo ""
echo ""
echo "List services"
kubectl get svc
echo ""
echo ""
echo "Create NGNIX service associate to port 80"
echo "kubectl create service nodeport nginx --tcp=80:80"
echo ""
echo ""
echo "Get all"
kubectl get all



