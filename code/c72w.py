# Complexity 72h code



class agent():
    def __init__(self, number, coop = True, payoff=0):
        self.number = number
        self.coop = coop #coop strategy = True; defection strategy = False
        self.payoff = payoff

    def hard_change(self, coop):
        self.coop = coop


    def __repr__(self):
        return f"Hi I agent {self.number}, I'm {self.coop}"


class circle():
    def __init__(self, n, p):
        self.p = p
        self.n = n
        self.arr = [agent(i) for i in range(n)]

    def access(self, index):
        return self.arr[index%self.n]

    def choose_one_rand(self):
        index = np.random.choice(self.n, 1)[0]
        return self.access(index)

    def flip_agent(self, index_flipped):
        current = self.access(index_flipped)
        self.access(index_flipped).hard_change(not current)

    def count_coop(self):
        return sum([i.coop for i in self.arr])


    def make_action(self, index):
        if np.random.rand() > self.p:
            self.action_local_on(index)
        else:
            self.action_global_on(index)


    def action_local_on(self, index):

        pass

    def action_global_on(self, index):

        pass
