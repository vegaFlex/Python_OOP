from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Category
from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Document
from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for category in self.categories:
            if category_id == category.id:
                category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for topic in self.topics:
            if topic_id == topic.id:
                topic.topic = new_topic
                topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        for doc in self.documents:
            if doc.id == document_id:
                doc.file_name = new_file_name

    def delete_category(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                self.categories.remove(category)

    def delete_topic(self, topic_id):
        for t in self.topics:
            if t.id == topic_id:
                self.topics.remove(topic_id)

    def delete_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                self.documents.remove(doc)

    def get_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc

    def __repr__(self):
        return '\n'.join(repr(doc) for doc in self.documents)

