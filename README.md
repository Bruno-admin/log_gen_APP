# Dummy app to generate random logs
The purpose of this project is to make a dummy log generator app to test Kubernetes, fluent Bit and Loki.

## Turing the Python Script into a Dockerized app
Use the above **Dockerfile** and run the following command:
```
docker build -t log-generator .
```
## Using Minikube to deploy a container
When you start Minikube, you have to run the following command:
```
eval $(minikube docker-env)
```
This command sets up your terminal to use Minikube's Docker daemon. Now, when you build a Docker image, it will be available in your Minikube cluster.

Rebuild your Docker image to make it available in Minikube:
```
docker build -t log-generator .
```
Use the above **log_gen_app.yaml** to create the pod:
```
kubectl apply -f log-gen-app.yaml
```
In case you are using a Cloud solution Kubernetes, you dont need to use the last line of the configuration yaml.
```
imagePullPolicy: Never
```
## Fluint bit
Since we are using docker deamon in our Minikube cluster, we have build a fluint bit docker image locally:

```
docker build -t fluent-bit:custom .
```
Use the above **[fluent_bit_deployment.yaml](fluent_bit_deployment.yaml)** and run:
```
kubectl apply -f fluent_bit_deployment.yaml
```