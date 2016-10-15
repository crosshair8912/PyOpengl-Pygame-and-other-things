from decimal import Decimal
def parse(fname,inp):
	content = []
	verticies = [[],[]]
	cnt = 0
	cnt_1 = 0
	with open(fname) as f:
		content = f.readlines()
	for i in content:
		for j in i.split(' '):
			if inp != 'vt':
				if cnt_1 == 0:
					verticies.append([])
					cnt_1 += 1
				elif j == inp:
					cnt += 1
				elif cnt == 1:
					verticies[0].append(Decimal(j))
					cnt += 1
				elif cnt == 2:
					verticies[1].append(Decimal(j))
					cnt += 1
				elif cnt == 3:
					verticies[2].append(Decimal(j[:-2]))
					cnt = 0
			else:
				if j == inp:
					cnt += 1
				elif cnt == 1:
					verticies[0].append(Decimal(j))
					cnt += 1
				elif cnt == 2:
					verticies[1].append(Decimal(j[:-2]))
					cnt = 0
	return verticies
	
#for i in parse("crate.obj","v"):
#	print (i)
#for i in parse("crate.obj","vt"):
#	print (i)
#for i in parse("crate.obj","vn"):
#	print (i)