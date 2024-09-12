import grpc
from grpc_interceptor.exceptions import GrpcException

from generated.bar_pb2 import OrderResponse
from generated.bar_pb2_grpc import BarServicer

mock_drinks = {
    "water": 0,
    "milk": 20,
    "juice": 23,
    "soda": 14,
    "whisky": 5
}


class BarBaseService(BarServicer):
    def GetOrder(self, request, context):
        if request.order in mock_drinks:
            if mock_drinks[request.order] == 0:
                raise GrpcException("Out of stock", status_code=grpc.StatusCode.NOT_FOUND)
            return OrderResponse(order_status="Success")
        else:
            raise GrpcException("Not found", status_code=grpc.StatusCode.NOT_FOUND)
