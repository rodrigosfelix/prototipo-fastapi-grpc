from fastapi import APIRouter, Depends
from pydantic import BaseModel

from api.dependencies.grpc.bar import BarClient

router = APIRouter()


class Drinks(BaseModel):
    drink: str

class ResponseDto(BaseModel):
    order_status: str

class Logic:
    def __init__(self):
        self.bar_client = BarClient()

    def get_drink(self, drink: str):
        return self.bar_client.get_order(order=drink)

    def build_order(self, order_create: Drinks):
        drink = self.get_drink(drink=order_create.drink)
        return ResponseDto(**drink)


@router.post("")
def get_drink(
        drink: Drinks,
        logic: Logic = Depends(Logic),
) -> ResponseDto:
    return logic.build_order(order_create=drink)
