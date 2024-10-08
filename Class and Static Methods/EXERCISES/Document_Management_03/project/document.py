from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Category
from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Topic


class Document:
    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instance(cls, id: int, category: Category, topic: Topic, file_name: str):
        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content):
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content):
        for tag in self.tags:
            if tag == tag_content:
                self.tags.remove(tag_content)

    def edit(self, new_file_name):
        self.file_name = new_file_name

    def __repr__(self):
        return (f"Document {self.id}: {self.file_name}; category {self.category_id}, "
                f"topic {self.topic_id}, tags: {', '.join([tag for tag in self.tags])}")
