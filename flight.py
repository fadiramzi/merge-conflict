class Flight():
    def __init__(self,c):
        self.p = []
        self.c = c
    
    def add(self,name):
        if not self.check():
            print('No seats available')
            return
        self.p.append(name)
        print(f"Length of Passengers is: {self.p}")
        print(f"Capacity is: {self.c}")
    
    def check(self)->bool:
        if len(self.p) >= self.c:
            return False
        return True

f1= Flight(3)
f1.add("Fadi")
f1.add("ali")
f1.add("Saif")
f1.add("Ahmed")
f2 = Flight(0)

print(f"F1 capacity is: {f1.c}")
print(f"F1 passengers: {f1.p}")
