from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024.services.main_service import MainService
from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024.services.secondary_service import SecondaryService
from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024.robots.male_robot import MaleRobot
from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024.robots.female_robot import FemaleRobot


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, type: str, name: str):
        if type == "MainService":
            service = MainService(name)
        elif type == "SecondaryService":
            service = SecondaryService(name)
        else:
            raise Exception("Invalid service type!")

        self.services.append(service)
        return f"{type} is successfully added."

    def add_robot(self, type: str, name: str, kind: str, price: float):
        if type == "MaleRobot":
            robot = MaleRobot(name, kind, price)
        elif type == "FemaleRobot":
            robot = FemaleRobot(name, kind, price)
        else:
            raise Exception("Invalid robot type!")

        self.robots.append(robot)
        return f"{type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(r for r in self.robots if r.name == robot_name)
        service = next(s for s in self.services if s.name == service_name)

        if isinstance(robot, FemaleRobot) and not isinstance(service, SecondaryService):
            return "Unsuitable service."
        if isinstance(robot, MaleRobot) and not isinstance(service, MainService):
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(s for s in self.services if s.name == service_name)
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if robot is None:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(s for s in self.services if s.name == service_name)
        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = next(s for s in self.services if s.name == service_name)
        total_price = sum(robot.price for robot in service.robots)
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())
        return "\n".join(result)
