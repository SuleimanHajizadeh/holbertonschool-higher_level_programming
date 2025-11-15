#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Mərhələ 1: Obyekt yaratmaq
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Mərhələ 2: Obyekti serialize etmək
obj.serialize("object.pkl")

# Mərhələ 3: Fayldan deserialization etmək
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()
