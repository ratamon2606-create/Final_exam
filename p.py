import math
class Object3D:
    def __init__(self, label:str, object_type: str, dimension: float):
        self.__label = label.lower()
        self.__object_type = object_type.lower()
        self.__dimension = dimension

    def __volume(self):
        if self.__object_type == "cube":
            return self.__dimension**3
        elif self.__object_type == "sphere":
            return self.__dimension**3 * (4/3*math.pi)
        elif self.__object_type == "pyramid":
            return self.__dimension**3 * 1/3

    def get_info(self):
        return f"Label: {self.__label}, Object: {self.__object_type}, Dimension: {self.__dimension:.2f}, Volume: {self.__volume():.2f}"
    
    def get_label(self):
        return self.__label
    
object3d_list = []
obj = ["cube", "sphere", "pyramid"]

while True:
    l = input("Enter label (or EXIT to stop): ").lower()
    if l == "exit":
        break
    o = input("Enter object type (cube, sphere, pyramid): ").lower()
    d = float(input("Enter dimension: "))
    if l in [i.get_label() for i in object3d_list]:
        print(f"Label already exists: {l}")
    if o not in obj:
        print("Invalid object type")
    if d < 0:
        print("Invalid dimension")
    object3d_list.append(Object3D(l,o,d))


print("-----REPORT-----")
if len(object3d_list) == 0:
    print("No object recorded")
else:
    for i in object3d_list:
        print(i.get_info())
