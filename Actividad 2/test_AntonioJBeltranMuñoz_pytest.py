import pytest
import string

def inc(x):
    return x + 1

def input_divisible_3(x):
    if x%3 == 0:
        return True
    else:
        return False
 
def factorial(num): 
    if num < 0: 
        print("Factorial de numeros negativos no existe")
    elif num == 0: 
        return 1       
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact    

def longitud_password(passwd):
    assert len(passwd) >= 8
    
def email_valido(s):
    s = s.lower()
    parts = s.split('@')    
    if len(parts) != 2:
      return False
    allowed = set(string.ascii_lowercase + string.digits + '.-_')
    for part in parts:
        if not set(part) <= allowed:
          return False
    return True
    
def test_email():
    assert email_valido('test@ejemplo.es')
    assert email_valido('user123@dominio.com')
    assert email_valido('toni@email.es')
       
def test_password_logitud_valido():
    assert longitud_password('123456')

def test_divisible_a_3():
    assert input_divisible_3(27)
        
def test_answer():
    assert inc(3) == 5
    
def test_factorial():
    assert factorial(5)==120    
    
# python -m unittest -v test_funciones.py
# python -m unittest discover -v
