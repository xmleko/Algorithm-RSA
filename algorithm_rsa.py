import math
import sys
from sympy import isprime
###
def function_euler(q, p):
    euler = (q - 1) * (p - 1)
    return euler
##
def is_integer(num):
    return num % 1 == 0

def public_exponent(euler):
    find = False
    while not find:
        e = int(input("Enter the number e "))
        result = math.gcd(e, euler)
        if result == 1:
            find = True
        print("This number cannot be used")
    return e

def private_exponent(e, euler):
    copy = euler
    d_copy = copy
    y = 0
    x = (copy + 1) / e
    if not (is_integer(x)):
        while not is_integer(x):
            copy = d_copy
            y = y+2
            copy = copy * (2+y)
            x = (copy + 1) / e
    return x

def cipher(e,n,encode):
    result = pow(encode, e, n)
    return result

def decryption(d,n,cypher): ###
    result = pow(int(cypher), int(d), int(n))
    return result

def security(q,p):
    if not isprime(q) or not isprime(p):
        print("Not a prime number")
        sys.exit(1)
    if p==q:
        print("p and q cannot be equal")
        sys.exit(1)

if __name__ == "__main__":
    q = int(input("Enter the number q "))
    p = int(input("Enter the number p "))
    security(q,p)
    n = q * p
    euler = function_euler(q, p)
    e = public_exponent(euler)
    d = private_exponent(e, euler)
    encode = int(input("Enter the number encode "))
    cypher = cipher(e,n,encode)
    decrypt = decryption(d, n, cypher)
    print("Encode text " + str(encode) + " is " + str(cypher))
    print("Decode text " + str(cypher) + " is " + str(decrypt))#

