from abc import ABC, abstractmethod


class BaseService(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Service name cannot be empty!")
        self._name = value

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        self._capacity = value

    @abstractmethod
    def details(self) -> str:
        pass
