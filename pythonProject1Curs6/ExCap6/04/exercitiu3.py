class Test1:
    def metoda1(self):
        self.unu = 'unu'

class Test2(Test1):
    def metoda2(self):
        self.doi ='doi'

class Test3(Test2):
    def metoda3(self):
        self.trei = 'trei'



ob =Test2()
ob.metoda1()
ob.metoda2()
