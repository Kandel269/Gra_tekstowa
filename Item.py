
class Item():
    def __init__(self,value,describe):
        self.value = value
        self.describe = describe

    def describe_all(self):
        print(self.describe)
        print(f"Wartosc przedmiotu {self.value}")
