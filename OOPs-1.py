class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print(f"🤖 Hello, I am {self.name}!")
        print(f"🛠 Model: {self.model}")
        print(f"🎯 My purpose is: {self.purpose}")
        print("------")

robot1 = Robot("Alpha", "X100", "Assisting in household chores")
robot2 = Robot("Beta", "T200", "Teaching and tutoring students")
robot3 = Robot("Gamma", "Z300", "Exploring outer space")

robot1.introduce()
robot2.introduce()
robot3.introduce()