from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Animal
from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if  self.__budget < price:
            return "Not enough budget"
        elif len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        # if self.__workers_capacity == 0:
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salary = sum([worker.salary for worker in self.workers])
        if workers_salary > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= workers_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money_for_animals = sum([animal.money_for_care for animal in self.animals])
        if needed_money_for_animals > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= needed_money_for_animals
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__build_antity_str(self.animals, 'Lion')
        result += self.__build_antity_str(self.animals, 'Tiger')
        result += self.__build_antity_str(self.animals, 'Cheetah')

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__build_antity_str(self.workers, 'Keeper')
        result += self.__build_antity_str(self.workers, 'Caretaker')
        result += self.__build_antity_str(self.workers, 'Vet')
        return result.strip()

    def __build_antity_str(self, entities, entity_type):
        counter = 0
        result = ''
        for entity in entities:
            if entity.__class__.__name__ == entity_type:
                counter += 1
                result += repr(entity) + '\n'
        return f'----- {counter} {entity_type}s:\n' + result



