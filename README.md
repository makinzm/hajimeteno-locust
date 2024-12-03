# hajimeteno-locust



---

# Reference

This is tutorial for a maintainer not for a user.

Create a grpc client code from a proto file.

```shell
uv run python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/src/proto/hello.proto
```
