from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=9)

    def eating(self):
        self.weight += 3
