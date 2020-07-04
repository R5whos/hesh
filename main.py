from random import randint
import string
import random

class HES_DES():
	def __init__(self, bit):
		self.bit = None


def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def fibanachi(bit):
	a = 0
	fib1 = 1
	fib2 = 1
	for b in bit:
		if b == 1:
			a = a + 1
			i = 0
			while i < a - 2:
			    fib_sum = fib1 + fib2
			    fib1 = fib2
			    fib2 = fib_sum
			    i = i + 1
	HES_DES.bit = fib_sum
	hesh_mode(fib_sum)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def hesh_mode(fibanachi_sum):
	a = randint(1, fibanachi_sum)
	if a <= 100:
		s = randint(1, 3)
		b = fibanachi_sum
		final_hesh = list(str(b))  
		test_hesh = list(str(b))  
		final_hesh.insert(randint(1, len(str(b))), id_generator(1))
		test_hesh.insert(randint(1, len(str(b))), id_generator(1))
		print(test_hesh, final_hesh)
		if final_hesh != test_hesh:
			hesh_mode(HES_DES.bit)
		else:
			print(final_hesh,'\n\n\n' ,test_hesh)
			
      
fibanachi(tobits('Hi'))
