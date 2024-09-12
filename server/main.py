from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from generated.bar_pb2_grpc import add_BarServicer_to_server
from service.service import BarBaseService


class BarService(BarBaseService):
    pass


def server():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        interceptors=interceptors
    )
    add_BarServicer_to_server(BarService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Starting server")
    server()
