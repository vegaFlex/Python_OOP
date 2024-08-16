from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=15)

    def details(self) -> str:
        robots_info = ' '.join(robot.name for robot in self.robots) or "none"
        return f"{self.name} Secondary Service:\nRobots: {robots_info}"
