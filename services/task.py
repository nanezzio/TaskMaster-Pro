from datetime import datetime

class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.dateCreate = datetime.now()
        self.passed = False 
        self.deadline = deadline

    def update(self, name, deadline):
        self.name = name
        self.deadline = deadline

    def change_pass(self):
        self.passed = not self.passed

    def set_pass(self, passed):
        self.passed = passed

    def get_name(self):
        return self.name

    def get_dateCreate(self):
        return self.dateCreate

    def get_passed(self):
        return self.passed

    def get_deadline(self):
        return self.deadline
    