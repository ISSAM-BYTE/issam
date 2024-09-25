print('modifying data')
print('super redesign')
print('lollilop')

def somme(a,b):
    return a + b

class high():

    def __init__(self):

        self.__a = 0

        self.__b = 5

    def higher(self):
        print('higher')

    def file(self):
        with open("test.txt","w+") as file :

           file.write('issam')


c = somme(5,7)
h = high()
h.higher()
h.file()


