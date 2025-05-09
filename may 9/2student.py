class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)
        print(f"Added student: {name}")#f string is used .

    def remove_student(self, name):
        if name in self.students:
            self.students.remove(name)
            print(f"Removed student: {name}")
        else:
            print(f"Student '{name}' not found.")

    def search_student(self, name):
        if name in self.students:
            print(f"Student '{name}' is listed.")
        else:
            print(f"Student '{name}' not found.")

    def show_all_students(self):
        print("All students:")
        for student in self.students:
            print(f"- {student}")

#test example
sms = StudentManagementSystem()

sms.add_student("chris")
sms.add_student("kiran")
sms.remove_student("peter")
sms.search_student("chris")
sms.show_all_students()

