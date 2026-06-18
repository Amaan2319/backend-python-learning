class Employee:
  increment_amount = 1.2
  
  def __init__(self, fname, lname, salary):
    self.fname = fname
    self.lname = lname
    self.salary = salary
  
  def get_employee(self):
    print(self.fname, " ", self.lname)
    print(self.salary)
  
  def raise_salary(self):
    self.salary *= self.increment_amount
  

emp_1 = Employee("Amaan", "Saiyed", 50000)
emp_1.get_employee()

emp_1.raise_salary()
emp_1.get_employee()