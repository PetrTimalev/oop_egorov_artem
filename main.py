class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self):
        self.instance_attribute = "I am an instance attribute"


example_1 = MyClass()
example_2 = MyClass()
example_3 = MyClass()

example_1.class_attribute = "Class attribute modified"

print(example_1.class_attribute)
print(example_3.class_attribute)

print(MyClass.class_attribute)