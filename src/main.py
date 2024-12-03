from locust import User, task, between
import grpc
from proto import hello_pb2
from proto import hello_pb2_grpc

class GRPCUser(User):
    wait_time = between(1, 2)

    def on_start(self):
        # gRPC サーバーのアドレスを設定
        self.channel = grpc.insecure_channel("grpc-service.default.svc.cluster.local:50051")
        self.stub = hello_pb2_grpc.VectorServiceStub(self.channel)

    @task
    def get_vector(self):
        request = hello_pb2.VectorRequest(id=100)
        try:
            response = self.stub.GetVector(request)
            # レスポンスの処理（必要に応じて）
        except grpc.RpcError as e:
            print(f"gRPC error: {e}")

    @task
    def insert_vector(self):
        request = hello_pb2.InsertVectorRequest(key="test_key", vector=[0.1]*256)
        try:
            response = self.stub.InsertVector(request)
        except grpc.RpcError as e:
            print(f"gRPC error: {e}")

    @task
    def get_vector_by_key(self):
        request = hello_pb2.GetVectorByKeyRequest(key="test_key")
        try:
            response = self.stub.GetVectorByKey(request)
        except grpc.RpcError as e:
            print(f"gRPC error: {e}")

    @task
    def insert_sample(self):
        request = hello_pb2.InsertSampleRequest(id=101)
        try:
            response = self.stub.InsertSample(request)
        except grpc.RpcError as e:
            print(f"gRPC error: {e}")

