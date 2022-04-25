''' 
1. Person이라는 클래스를 만들고 init function을 만든다
2. 인잇 펀션 안에 name, age , nickname 설정 
3. method introduce 
'''
class Person:
    def __init__(self, age, name, nickname):
        self.age = age
        self.name = name
        self.nickname = nickname 
    
    
    def introduce(self):
        print(f"Hi, my name is {self.name}, and you can call me {self.nickname}, and I'm {self.age}")
    
p1 = Person(26, "Jun Oh Lee", "Juno") 
p2 = Person(26, "Chloe Scales", "Chloe")
 
p1.introduce()
p2.introduce()