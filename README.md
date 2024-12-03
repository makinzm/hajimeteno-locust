# hajimeteno-locust

docker setup

```shell
docker build -t hajimeteno-locust .
```

create namespace

```shell
kubectl create namespace hajimeteno-locust-ns
```
set namespace

```shell
kubectl config set-context --current --namespace=hajimeteno-locust-ns
```

apply k8s resources

```shell
cd k8s
kubectl apply -f locust-master-deployment.yaml
kubectl apply -f locust-master-service.yaml
kubectl apply -f locust-slave-deployment.yaml
kubectl apply -f locust-master-web-service.yaml
```

(other tab) port forward setting to open locust web ui from local
```shell
kubectl port-forward svc/locust-master-web 30090:8089
```
(other tab) open locust web ui
```shell
open http://localhost:30090
```

---

# Reference

This is tutorial for a maintainer not for a user.

Create a grpc client code from a proto file.

```shell
uv run python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/src/proto/hello.proto
```
