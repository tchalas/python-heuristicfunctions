
from search import *
import sys

fgoal = []
size = 0
counter = 0

class BlocksWorld(Problem) :

    	def __init__(self, n, startingstate, goalstate):

		print startingstate
		array = [0 * n for i in range(n)]  
		array = copy.deepcopy(startingstate)
		 
		super(BlocksWorld, self).__init__(tuple(tuple(i) for i in array), None)  
		self.goalstate = [0 * n for i in range(n)] 
		self.goalstate = copy.deepcopy(goalstate)
		self.n = n

	def actions(self, state) :
		fullresult = []
		result = []
		k = [0,0]   
		for i in xrange(self.n):
			for j in xrange(self.n):
				if state[i][j] != 0:          #find a block
					if state[i-1][j] == 0:            #if the block is free
					#3 choice: 1) if alone put it on another stack 2) of up on a stack move it to another 3) move it to be alone
						for k in range(self.n):                           #find all the places you can put it
							if(k!=j):                                   #of course not in the same column
								if state[self.n - 1][k]!=0 :        #if the column not empty
									g = self.n-1                #find the highest pos on the stack
									while state[g][k]!=0:       #aneva
										g = g - 1
									result.append((i, j))
									result.append((g, k))
									fullresult.append(result)
									result = []	
						if i!= self.n - 1:                              #if belongs to a stack
							for f in range(self.n - 1):
								if f!=j:
									if (state[self.n - 1][f]==0):
										result.append((i, j))
										result.append(( self.n - 1,f))
										fullresult.append(result)
										result = []
										break

	    	return fullresult				
		
		
	def result(self, state, action) :
		
		b = action[0]
		af = action[1]
		newStateList = [list(k) for k in state ]
		k = int(newStateList[b[0]][b[1]])
		newStateList[af[0]][af[1]] = k
		newStateList[b[0]][b[1]] = 0
		
		return tuple(tuple(i) for i in newStateList)
		
	def goal_test(self, state) :
		g = True
		global size
		h = 0
		for i in range(size) :
			for j in range(size):
				if state[i][j] != 0:
					for k in range(size) :
						for m in range(size):
							if state[i][j] == fgoal[k][m]:

								if ((state[i-1][j])!=fgoal[k-1][m]) or (k!=i) or (i!=size-1 and k!=size-1 and state[i+1][j]!=fgoal[k+1][m]):
									g = False
		return g			
		
	# Useless functions
#	def path_cost(self, c, state1, action, state2) :
#		return c+1
#		
#    def value(self, state) :
#    	return 1
    	
    	
def h1(n) :
	global size
	h = 0
	state = n.state
	for i in range(size) :
		for j in range(size):
			if state[i][j] != 0:
				for k in range(size) :
					for m in range(size):
						if state[i][j] == fgoal[k][m]:

							if ((state[i-1][j])!=fgoal[k-1][m]) or (k!=i) or (i!=size-1 and k!=size-1 and state[i+1][j]!=fgoal[k+1][m]):
								h = h + 1

	global counter
	counter = counter + 1
			
	return h						
	#checks if up and down are the same starting from goal. 
	

def h2(n) :
	#sum of manhattan
	global size
	h = 0
	summ = 0
	state = n.state
	for i in range(size) :
		for j in range(size):
			if state[i][j] != 0:
				for k in range(size) :
					for m in range(size):
						if state[i][j] == fgoal[k][m]:
							summ = i + k + abs(m - j)
							h = h + summ
	return h



		
n=int(sys.argv[1])
goal = []
start = []

goal.append([0,0,0,0,0]) 
goal.append([0,0,0,0,0]) 
goal.append([0,0,0,0,0])  
goal.append([0,5,0,0,3])
goal.append([0,1,0,2,4])

global fgoal
fgoal = copy.deepcopy(goal)
global size
size = n


start.append([0,0,0,0,0]) 
start.append([0,0,0,0,0]) 
start.append([0,1,0,0,0]) 
start.append([0,2,0,4,0])
start.append([0,3,0,5,0])
			
p = BlocksWorld(int(sys.argv[1]), start,goal)
solution = astar_search(p, lambda node : h2(node))
print time.clock()
	

