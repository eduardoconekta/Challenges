res = []
i = 1
times = input("n=  \n")
print len(res)
while len(res) < times:
	i +=1
	if (i % 2 == 1) :
		cont = 0
		for j in xrange(1,i):
			if (i % j == 0):
				cont +=1
		if (cont <= 1):
			res.append(i)
	elif (i == 2):
		res.append(i)
print '+'.join(str(x) for x in res)

print res