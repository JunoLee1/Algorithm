''' 
1. Person이라는 클래스를 만들고 init function을 만든다
2. 인잇 펀션 안에 name, age , nickname 설정 
3. method introduce 
'''
class Person:
    def __init__(self,name,age):
        self. name = name 
        self. age = age
    
    def introduce(self):
        print(f"I'm {self.name} and {self.age} years now")

class Person2(Person):
    def __init__(self,name,age,sex):
        super().__init__(name,age)
        self. sex = sex
    def introduce(self):
        print(f"I'm {self.name} and {self.age} years now, {self.sex}")

p1 =Person2("Juno","25","male")
p1.introduce()


