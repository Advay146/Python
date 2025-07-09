class student:
    name="Penguin"
    grade= 10

    def introduction(self):
        print("Hi I am a student.")

    def details(self):
        print("Hi! My name is",self.name,".")
        print("Hi! I am in grade",self.grade,".")

ob = student()
ob.introduction()
ob.details()