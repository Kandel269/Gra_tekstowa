
#
# x = {"dsafg":0,"das":0,"dsa":0}
# for i in x.keys():
#     print(i)
#
# x.pop("das")
# print(x)
#
# print(len(x))


class test():
    def __init__(self,lista):
        self.lista = lista

    def aa(self):
        print(1)
    def bb(self):
        print(2)

t = test({"aa":0,"bb":0})



for i in t.lista:
    print(i)
    print(t.lista[i])

