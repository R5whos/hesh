from random import randint
import string
import random

later = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def digitalSum(n):
	if n < 10 :
		return n
	return n % 10 + digitalSum( n // 10 )

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
	hesh_mode(fib_sum)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def hesh_mode(fibanachi_sum):
	if fibanachi_sum % 2 == 0:
		a = str(fibanachi_sum)[:1]
		text = later[int(a)] + str(fibanachi_sum)
		final = text[::-1]
		final = final.upper()
		var = digitalSum(fibanachi_sum)
		if var % 2 == 0:
			len_for_mode = len(str(fibanachi_sum))
			len_for_mode = len_for_mode - 1
			string_for_mode = str(fibanachi_sum)[len_for_mode:]
			final = final + later[int(string_for_mode)]
			print(final.upper())

		else:
			len_for_mode = len(str(fibanachi_sum))
			len_for_mode = len_for_mode - 1
			string_for_mode = str(fibanachi_sum)[len_for_mode:]
			final = later[int(string_for_mode)] + final
			print(final.upper())


	else:
		b = len(str(fibanachi_sum))
		b = b - 1
		a = str(fibanachi_sum)[b:]
		text = str(fibanachi_sum)+later[int(a)]
		final = text[::-1]
		final = final.upper()
		var = digitalSum(fibanachi_sum)
		if var % 2 == 0:
			len_for_mode = len(str(fibanachi_sum))
			len_for_mode = len_for_mode - 1
			string_for_mode = str(fibanachi_sum)[len_for_mode:]
			final = final + later[int(string_for_mode)]
			print(final.upper())

		else:
			len_for_mode = len(str(fibanachi_sum))
			len_for_mode = len_for_mode - 1
			string_for_mode = str(fibanachi_sum)[len_for_mode:]
			final = later[int(string_for_mode)] + final
			print(final.upper())

