# Complexity 72h code

# PACKAGES
import numpy as np


# CLASSES

# Individual
class agent():
    def __init__(self, number, coop = True, payoff=0):
        self.number = number
        self.coop = coop #coop strategy = True; defection strategy = False
        self.payoff = payoff

    #chenge the coop variable
    def set_coop(self, coop):
        self.coop = coop

    def __repr__(self):
        return f"Hi I'm agent {self.number}, I'm {self.coop}"

# Network
class circle():
    def __init__(self, n, p):
        self.p = p
        self.n = n
        self.arr = [agent(i) for i in range(n)]
        self.global_coop = 0
        self.global_defec = 0

    def count_coop(self):
		#print(1) fai un check se questo comando viene letto
		A = 0 #frazione di nodi con opinione favorevole alla cooperazione

		for i in range (self.n):
			A +=1 if self.nodes[i].coop == True else 0

		self.global_coop = A/(1.0*self.n)

		return A/(1.0*self.n)

    def access(self, index):
        return self.arr[index%self.n]

    def choose_one_rand(self):
        index = np.random.choice(self.n, 1)[0]
        return self.access(index)

    def flip_agent(self, index_flipped):
        current = self.access(index_flipped)
        self.access(index_flipped).set_coop(not current)

    def count_coop(self):
        return sum([i.coop for i in self.arr])


    def make_action(self, index):
        if np.random.rand() > self.p:
            self.action_local_on(index)
        else:
            self.action_global_on(index)


    def action_local_on(self, index):
        #select left rigth
        if np.random.rand() > 0.5:
            pass
        else:
            pass


        pass

    def action_global_on(self, index):

        pass
