import string
from random import randint

#define a function to generate random code 

def RandomCode(len = 6 , base = string.ascii_lowercase + string.digits ):
	
	# str.join() would generate a new string ,   always using _ standing for a variable that would not get used 
	return ''.join(base[randint(0,len)] for _ in range(len))

result
for _ in range(200):
	result.append(RandomCode(8))

print(type(result))
print(result)


#return ''.join(random.choice(chars) for _ in range(size))  
