class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __str__(self):
        return f"{self.name} ({self.age})"
    
test1 = Test("Alice", 23)
test2 = Test("Bob", 25)

print(test1 < test2)  
print(test1, test2)