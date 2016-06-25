def Read():
	increment = 0
	cont   = 0
	suma   = 0
	result = []
	whole_text = open("1.txt")
	lista = [i.rstrip() for i in whole_text ] 
	for i in lista:
		p = []
		if cont == 0:
			c = int(i)
			cont +=1
		elif cont == 1:
			cont+=1
		elif cont == 2:
			cont = 0
			i = i.split()
			p = [int(r) for r in i if not r == ' ']
			for i in xrange(0,len(p)):
				for r in xrange(0,len(p)):
					if i != r and suma != c:
						suma = p[i] + p[r]
						if suma == c:
							increment +=1
							result.append("Case #%i: %i  %i"%(increment,i+1,r+1))

	return result

res = []
res =  Read()
f = open("result.txt","w")
for i in res:
	f.write(i+"\n")
f.close
