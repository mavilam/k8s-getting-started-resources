# k8s examples
This project is intended to be use as playground to learn some kubernetes concepts over minikube.
Under the folder k8s-resources, there are some yamls which each one defines a kubernetes resource.

*this project is under construction*

## Install minikube
You can find the official info [here](https://minikube.sigs.k8s.io/docs/start/)

## Install kubectl
You can find the official info [here](https://kubernetes.io/docs/tasks/tools/)

## Build image
To test some resources it will be using a tiny python script with two hello world sentences.

### Image
To build the image using the Dockerfile use the following command from the root of the project:
```sh
docker build -t python-helloworld docker/
```
### Upload to minikube
To upload the image to the minikube container registry use the following line:
```sh
docker save python-helloworld | (eval $(minikube docker-env) && docker load)
```
## Apply k8s resourcers
To create resources in k8s, you can use the following command:
```sh
kubectl apply -f [filename]
```
So to begin with the basic environment and run the first test execute those commands:
```sh
kubectl apply -f configmap.yaml
kubectl apply -f pod.yaml
```
Once executed, you will see `Hello from configmap` in the logs of the pod. You can extract the with this command:
```sh
kubectl logs $(kubectl get pods -o=name | head -n 1 | cut -d / -f 2)
```

