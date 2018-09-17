from __future__ import print_function
import grpc
import todoCRUD_pb2
import todoCRUD_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = todoCRUD_pb2_grpc.ToDoCRUDStub(channel)
        response = stub.taskSingle(todoCRUD_pb2.SingleRequest(_id="5b9e7648a71a6223dc72a068"))
    print(response)

if __name__ == '__main__':
    run()