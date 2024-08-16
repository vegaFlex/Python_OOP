from abc import ABC, abstractmethod


class BaseRobot(ABC):
    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Robot name cannot be empty!")
        self._name = value

    @property
    def kind(self) -> str:
        return self._kind

    @kind.setter
    def kind(self, value: str):
        if not value.strip():
            raise ValueError("Robot kind cannot be empty!")
        self._kind = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0.0:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")
        self._price = value

    @property
    def weight(self) -> int:
        return self._weight

    @weight.setter
    def weight(self, value: int):
        self._weight = value

    @abstractmethod
    def eating(self):
        pass
