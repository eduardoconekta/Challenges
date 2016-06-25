def Reverse(str):
	str = str.split()
	str.reverse()
	return " ".join(str)

result = []
f = open("2.txt")
for n,i in enumerate(f):
	n+=1;result.append(("Case #%i: "+Reverse(i))%n);
f.close
g = open("B-result.txt","w")
for r in result:
	g.write(r+"\n")
g.close
