class employee:
    company="Apple"
    def show(self):
        print(f"the name is {self.name} and the company is {self.company}")
    @classmethod #first argument is class
    def changecompany(self,newcompany):
        self.company=newcompany
e1=employee()
e1.name="hello"
e1.show()
e1.changecompany("Google")
e1.show()
print(employee.company)
