import timeit

setup = """
a = int(input("Enter your number: "))
"""

statement = """
def catalan(n):
	if n == 0:
		return 1
	else:
		return sum(catalan(i)*catalan(n-1-i) for i in range(n))
catalan(a)
"""
statement2 = """
def catalan2(n, lookup={0:1}):
	if n not in lookup:
		lookup[n] = sum(catalan2(i)*catalan2(n-1-i) for i in range(n))
	return lookup[n]
catalan2(a)
"""

#print("The {}-th Catalan number is: {}".format(a, catalan(a)))

#print("The {}-th Catalan number is: {}".format(a, catalan2(a)))

print(timeit.timeit(setup = setup, stmt = statement, number=1000))

print(timeit.timeit(setup = setup, stmt = statement2, number=1000))