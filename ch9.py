class dog:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


dogs = []
for i in range(3):
    print('add dog info')
    dogs.append(dog(input("name: "), input('sex:'), input('age: ')))


print("all dogs info~~~")
for i in dogs:
    print("name : %s" % (i.name))
    print("sex : %s" % (i.sex))
    print("age : %s" % (i.age))

