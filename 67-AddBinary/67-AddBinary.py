# Last updated: 12/31/2025, 10:34:31 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if (len(a) > len(b)):
            x = len(a) - len(b)
            for i in range (x):
                if (i < len(b)):
                    b = "0" + b
        elif (len(a) < len(b)):
            x = len(b) - len(a)
            for i in range (x):
                if (i < len(a)):
                    a = "0" + a
        new_str = ""
        aux = 0
        for i in range(len(a)-1, -1, -1):
            if (a[i] == "1" and b[i] == "1" and aux == 0):
                new_str = "0" + new_str 
                aux = 1
            elif (a[i] == "1" and b[i] == "0" and aux == 0):
                new_str = "1" + new_str 
                aux = 0
            elif (a[i] == "0" and b[i] == "1" and aux == 0):
                new_str = "1" + new_str 
                aux = 0
            elif (a[i] == "1" and b[i] == "0" and aux == 1):
                new_str = "0" + new_str
                aux = 1
            elif (a[i] == "0" and b[i] == "1" and aux == 1):
                new_str = "0" + new_str
                aux = 1
            elif (a[i] == "1" and b[i] == "1" and aux == 1):
                new_str = "1" + new_str 
                aux = 1
            elif (a[i] == "0" and b[i] == "0" and aux == 1):
                new_str = "1" + new_str
                aux = 0
            elif (a[i] == "0" and b[i] == "0" and aux == 0):
                new_str = "0" + new_str
                aux = 0
        if aux == 1:
            new_str = "1" + new_str

        return new_str 
        