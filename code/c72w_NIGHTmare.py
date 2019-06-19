# Complexity 72h code

# PACKAGES
import numpy as np


# CLASSES

# Individual
class agent():
    def __init__(self, number, coop, payoff=0):
        self.number = number
        self.coop = coop
        self.payoff = payoff

        self.backup = list()

    #change the coop variable
    def set_coop(self, coop):
        self.coop = coop

    def __repr__(self):
        return(f"Hi I'm agent {self.number}, I'm {self.coop}")

    def save_stuff(self):
        self.backup.append((self.coop,self.payoff))




# Network
class circle():
    def __init__(self, n, p, w, b, c=1, all_coop = True):
        self.b = b
        self.c = c

        self.p = p
        self.n = n
        self.w = w
        self.arr = [agent(i, all_coop) for i in range(n)]

        self.global_coop = n if all_coop else 0



    def access(self, index): # for accessing
        return self.arr[index%self.n]

    def choose_one_rand(self): #pick one node at random
        index = np.random.choice(self.n, 1)[0]
        return self.access(index)

    def flip_agent(self, index_flipped): #initialize the ring with 1 cooperator
        current = self.access(index_flipped)
        current.coop = not current.coop

        if current.coop: self.global_coop += 1
        else: self.global_coop -= 1


    def count_coop(self):
        return sum([i.coop for i in self.arr])


    def make_action(self): #iterazione


        self.update_all_payoff()

        index = self.choose_one_rand().number
        if np.random.rand() > self.p:
            self.action_local_on(index)
        else:
            self.action_global_on(index)

        #[i.save_stuff() for i in self.arr]

        #string = "-"
        #for i in self.arr:
        #    string += "c-" if i.coop else "d-"
        #print(string)




    # take a local action
    def action_local_on(self, index):
        #select left or rigth
        if np.random.rand() > 0.5:
            choosen = self.access(index+1).number
        else:
            choosen = self.access(index-1).number

        self.copy_strategy(index, choosen)



    # take a global action
    def action_global_on(self, index):
        choosen_as_rand = self.choose_one_rand().number
        self.copy_strategy(index, choosen_as_rand)



    # compute logistic prob
    def copy_strategy(self, index, neighbor_index):
        # return true: if we need to copy the strategy of the other
        # return false: if we need to kepp the strategy
        copy = np.random.rand() < 1/(1+np.exp(self.w*( self.access(index).payoff - self.access(neighbor_index).payoff )))

        if copy:
            self.access(index).coop = self.access(neighbor_index).coop

            self.global_coop = sum([i.coop for i in self.arr])
            #if self.access(neighbor_index).coop: self.global_coop += 1
            #else: self.global_coop -= 1



    def update_all_payoff(self):
        for a in self.arr:
            if a.coop:
                #give to other the payoff
                self.access(a.number + 1).payoff += self.b
                self.access(a.number - 1).payoff += self.b
                a.payoff -= 2 * self.c
            else:
                pass
