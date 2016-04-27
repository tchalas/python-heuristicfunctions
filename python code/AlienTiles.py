from search import *
import sys
import numpy, copy
from numpy import all, array, uint8

goal = 0
globvar = 0
cycles = 0
counter = -1
sizel = 1
chc = 0
c = False
oldsize = 0;
mod = 4;
clarray = [[0] * 3 for i in range(3)]    
clicks= numpy.zeros(9).reshape((3, 3))
clicks = clicks.astype(int)


class AlienTiles(Problem):
    def __init__(self, n, startingcolor, goalcolor):


	if(goalcolor==2):
		self.cycles = 1
	array = [[startingcolor] * n for i in range(n)]  
	array[0] = [2,2,2]  
	array[1] = [2,2,2]
	array[2] = [2,0,2]


        super(AlienTiles, self).__init__(tuple(tuple(i) for i in array), None)  
        self.goalcolor = goalcolor   
        self.n = n

    def actions(self, s):
	    result = []
	    k = [0,0]   
	    for i in xrange(self.n):
		for j in xrange(self.n):
			result.append((i, j))
	    return result


    def result(self, s, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""

	#next = copy.deepcopy(s)
	global mod
	i = action[0]
	j = action[1]
	next = [list(k) for k in s ]
	for k in range(self.n):	
		next[i][k]=(next[i][k]+1)%mod
	for k in range(self.n):
		if(k!=i):
			next[k][j]=(next[k][j]+1)%mod
        return tuple(tuple(i) for i in next)  


    def goal_test(self, s) : 
        for i in range (self.n) :
            for j in range (self.n) :
                if (s[i][j] != self.goalcolor) :
                    return False
        print s
        return True

def h1(node) :
    state = node.state
    h = 0
    for i in range (len(state)-1) :
        for j in range (len(state)-1) :
            if (state[i][j] != 1 ) :
                h += 1 
    return h

def h2(node):
	global counter
	global c

	st = node.state
	test= numpy.zeros(9).reshape(3, 3)
	test = test.astype(int)

	sn = 0
	sf = 0 
	if (goal==5):
		for i in range(len(st)-1):
			for j in range(len(st)-1):
				g = st[i][j]
				sn = 5 - g
				if g > 5:
					sn = sn + 5
				
				sf = sf + sn
		
	sf = sf/5

	
	counter = counter + 1
	return sf




def h3(node):
	print node
	global counter
	global clicks
	global c
	global oldsize
	print clicks

	k = node.solution()

	size = len(k)
	if(size>1 and size> oldsize):
		oldsize = size
		gg0 = k[size-2][0]
		gg1 = k[size-2][1]
		clicks[gg0][gg1]= clicks[gg0][gg1] + 1	
		print clicks
	cc = 0
	temp = copy.deepcopy(clicks)
	print node.solution()

	print size
	if not k:
  		print "List is empty"
	else:

		temp = copy.deepcopy(clicks)
		gg0 = k[size-1][0]
		gg1 = k[size-1][1]	
		temp[gg0][gg1] = temp[gg0][gg1] + 1	

	st = node.state
	sn = 0
	sf = 0 
	if (goal==1):
		for i in range(3):
			for j in range(3):
				g = temp[i][j]
				if g==0:
					cc = cc + 1
				elif g > 1:
					cc = cc + 5 - g
				sn = abs(1 - g)
				if g > 5:
					sn = sn + 1
				
				sf = sf + sn	
		print "MIN"
		print cc
        if cc == 0:
		sys.exit(0)
	counter = counter + 1

	return cc










def h4(node):
	global counter

	global c
	maxb = 0
	st = node.state
	test= numpy.zeros(9).reshape((3, 3))
	test = test.astype(int)
	ba = numpy.zeros(9).reshape((3, 3))
	ba = ba.astype(int)
	sn = 0
	sf = 0 
	if (goal==5):
		for i in range(3):
			for j in range(3):
				g = st[i][j]
				ba[i][j] = getbalance(st,i,j)
				if ba[i][j] > maxb:
					maxb = ba[i][j]
				sn = 5 - g
				if g > 5:
					sn = sn + 5
				
				sf = sf + sn

	sf = sf/5

	cmax = 0
	for i in range(3):
		for j in range(3):
			if ba[i][j] == maxb:
				cmax = cmax + 1
	if cmax < 2 and counter>8:
		sf = sf + 1		
	counter = counter + 1
	return sf


def h5(node):
	st = node.state
	test= numpy.zeros(9).reshape((3, 3))
	test = test.astype(int)
	syn=0
	m = 0
	gg = 0
	ch = False
	ch00 = False
	ch000 = False
	ch0000 = False
	chh = False
	global chc
	global cycles
	global counter
	global goal
	print "HEY"
	print node
	mid = [0,0,0];
	if(goal==2):
		print "LALALALA"
		for i in range(3):
			for j in range(3):
				g = st[i][j]
				if(cycles == 0 and g == 3):
					gg = 1;

				test[i][j] = (4 * cycles) + 2 - g;
				syn = syn + test[i][j]
			mid[i] = syn / 3
			if(mid[i] == (4 * cycles) + 2) and counter > 0:
				cycles = 0
				#sys.exit(0)
			sn = syn % 3
			if sn > 0:
				mid[i] = mid[i] + 1
			syn = 0;
		m = min(mid)
		if gg == 1:
			m = m + 4
		counter = counter + 1
		print "min"
		print m
	elif (goal==1):
		for i in range(3):
			ch = True
			ch00 = True
			for j in range(3):
				g = st[i][j]
				if g!=2:
					ch = False
				if g!= 0:
					ch00 = False


			if ch00:
				syn = 0;
				ch000 = True
				if (chc > 1 and ch0000):
					cycles  = 0
			if ch:
				syn = 0;
				chh = True
				chc = chc + 1;
				if (chc > 1):
					cycles = 1 +0.5
					if ch000:
						cycles  = 1
						ch0000 = True
			for j in range(3):
				g = st[i][j]
				test[i][j] = (4 * cycles) + 1 - g;
				syn = syn + test[i][j]
			mid[i] = syn / 3
			sn = syn % 3
			if sn > 0:
				mid[i] = mid[i] + 1
			syn = 0
		m = min(mid)
		if m == 5:
			if chh!=True:
				m = m + 4
		if m == 3:
			if ch0000!=True:
				m = m + 4

		counter = counter + 1
		print m

	return m
		


def getbalance(s,i,j):
	v = 0
	for k in xrange(3):
		v = v + s[i][k]
	for n in xrange(3):
		if n!=i:
			v = v + s[n][j]
	return v
 				

m = int(sys.argv[4])


global goal
global cycles
global mod
cycles = 1
goal = int(sys.argv[3])

if(m == 1):
	pr = AlienTiles(int(sys.argv[1]),int(sys.argv[2]), int(sys.argv[3]))
	solution = astar_search(pr, lambda node : h1(node))	
elif(m == 2):
	goal = goal + 4
	mod = goal + 1
	pr = AlienTiles(int(sys.argv[1]),int(sys.argv[2]), goal)
	solution = astar_search(pr, lambda node : h2(node))	
elif(m == 3):
	solution = astar_search(pr, lambda node : h3(node))
elif(m == 4):
	goal = goal + 4
	mod = goal + 1
	pr = AlienTiles(int(sys.argv[1]),int(sys.argv[2]), goal)
	solution = astar_search(pr, lambda node : h4(node))
else:

	pr = AlienTiles(int(sys.argv[1]),int(sys.argv[2]), int(sys.argv[3]))
	solution = astar_search(pr, lambda node : h5(node))

print time.clock()
print solution.solution()


