# TBD(ERROR)

```shell
# Check logs from slave
[2024-12-05 13:46:13,103] locust-slave-***-***/INFO/locust.main: Starting Locust 2.32.4
gRPC error: <_InactiveRpcError of RPC that terminated with:
        status = StatusCode.INTERNAL
        details = "Internal server error"
        debug_error_string = "UNKNOWN:Error received from peer  {created_time:"2024-12-05T13:46:21.739851124+00:00", grpc_status:13, grpc_message:"Internal server error"}"
```

```shell
# Check logs from grpc

Database query error: Database returned an error: The query is syntactically correct but invalid, Error message: Cannot execute this query as it might involve data filtering and thus may have unpredictable performance. If you want to execute this query despite the performance unpredictability, use ALLOW FILTERING
Database insert error: Serializing values failed: SerializationError: Failed to serialize query arguments (alloc::string::String, alloc::string::String, alloc::vec::Vec<f32>): failed to serialize column id: SerializationError: Failed to type check Rust type alloc::string::String against CQL type Int: expected one of the CQL types: [Ascii, Text]
```

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
