from mode import fibanachi

import re
def str_to_bit(s):
    result = []
    for c in str(s):
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    fibanachi(result)


def file_to_bit(f):
	result = []
	with open(f, 'r') as file:
		for lines in file:
			werb = re.sub(r'\s', ' ', lines)
			command = re.split(r'[\'\']', werb)
			result.append(str_to_bit(command))
		fibanachi(result)

print('парне')
str_to_bit('hi')
print('\n')
print('не парне')
str_to_bit('hs')