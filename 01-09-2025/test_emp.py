class Employee:
    def __init__(self, id, name, job_title, salary, bonus):
        self.id = id
        self.name = name
        self.job_title = job_title
        self.salary = salary
        self.bonus = bonus
    def __str__(self):
        return f'id={self.id}, name={self.name}, job_title={self.job_title}, salary={self.salary}, bonus={self.bonus}'
    def __repr__(self):
        return self.__str__()

abhi = Employee(101, 'Abhiram', 'consulting_engineer', 5000, 400)
gopi = Employee(102, 'Gopi', 'Software Engineer', 15000, 0)
harsha = Employee(103, 'Harsha', 'Consulting Engineer', 20000, 0)

employees = [abhi, gopi, harsha]
print(repr(harsha))
print(employees)
