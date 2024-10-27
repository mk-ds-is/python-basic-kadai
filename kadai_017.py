class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}さんは大人です。")
        else:
            print(f"{self.name}さんは大人ではありません。")

human_a = Human("A", 30)
human_b = Human("B", 15)

human_list = [human_a, human_b]

for i in human_list:
    i.check_adult()