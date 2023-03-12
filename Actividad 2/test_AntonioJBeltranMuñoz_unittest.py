import unittest

def hexadecimal(*args):
    return hex(*args)

def unicode(*args):
    return ord(*args)

def Multiplicacion(a,b):
    return a*b

def EsPrimo(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False
    return True

def Exponente(a,b):
    return pow(a,b)

class Test_misfunciones(unittest.TestCase):
    
    def setUp(self):
        print ("entrando en setup")
        
    def tearDown(self):
        print ("entrando en teardown") 
         
    def test_1(self):
        resul = hexadecimal(16)
        self.assertIsNot(resul,0x11)
        
    def test_2(self):
        resul = unicode('d') #d == 100
        self.assertNotEqual(resul,120) 
        
    def test_3(self): 
        resul = Multiplicacion(5,5)              
        self.assertAlmostEqual(resul,25)
        
    def test_4(self):
        result = EsPrimo(5)
        self.assertTrue(result)
       
    def test_5(self):
        result = pow(5,6)
        self.assertGreaterEqual(result,31)
        
if __name__ == '__main__':
    unittest.main()
    
# python -m unittest -v test_funciones.py
# python -m unittest discover -v
