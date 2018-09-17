from __future__ import print_function
import grpc
import todoCRUD_pb2
import todoCRUD_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = todoCRUD_pb2_grpc.ToDoCRUDStub(channel)
        response = stub.taskUpdate(todoCRUD_pb2.UpdateRequest(_id="5b9e7f9ea71a622a5440fd14",name="new name", address="malir halt"))
    print(response)

if __name__ == '__main__':
    run()