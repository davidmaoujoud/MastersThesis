from Agent import Agent
import random


class Oracle(Agent):

    def __init__(self, g):
        Agent.__init__(self)
        self.s = 0
        self.previous_s = 0
        self.nb_steps = 0
        self.proba_selfish = 0
        self.g = g

    def lookahead(self, s):
        self.nb_steps += 1
        if self.nb_steps <= 20 or self.nb_steps >= 80:
            return 4  # Refuse
        else:
            return 3  # Accept

    def lookaheadvtol2(self, s):
        self.nb_steps += 1
        #if self.nb_steps >= 10:
        #    self.proba_selfish = 0.5
        if self.nb_steps in [10,20,30,40]:
            self.proba_selfish += 0.2
        #if self.nb_steps in [40]:
         #   self.proba_selfish += 0.1

        if s in [2,6,10,14]: # Battery almost empty, needs to land
            return 1
        elif s in [3,7]: # Currently on helipad
            if random.random() < self.proba_selfish:
                return 0
            else:
                return 1
        elif s in [11]: # Safety measure, avoid crashes
            return 1
        else:
            return 0

    def lookaheadtradeABC(self, s):
        self.nb_steps += 1
        if self.g == 1: # Agent B
            if self.nb_steps <= 33: # refuse trade offers
                return 1
            elif self.nb_steps <= 66:
                if self.s in [0]: # initial state, buy from A
                    return 1
                else: # accept trade offers
                    return 0
            else:
                return 1 # Trade with C and accept offers
        elif self.g == 2: # Agent C
            if self.nb_steps <= 33: # accept trade offers
                return 0
            elif self.nb_steps <= 66:
                if self.s in [0]: # initial state, buy from A
                    return 0
                else: # refuse trade offers
                    return 1
            else: # Trade with C and refuse trade offers
                return 0

        else:
            return 0

    def lookaheadvtol4(self, s):
        self.nb_steps += 1
        if self.nb_steps <= 20:
            if self.s in [8,9,11,18,19,20,22,23,39,40,41,43,44,30,31,2,3]:
                return 1
            else:
                return 0
        elif self.nb_steps <= 40:
            if self.s in [5,10,13,21,29,36,    8,9,11,18,19,20,22,23,39,40,41,43,44,30,31,2,3]:
                return 1
            else:
                return 0
        elif self.nb_steps <= 60:
            if self.s in [0,1,2,26,27,28,     5,10,13,21,29,36,    8,9,11,18,19,20,22,23,39,40,41,43,44,30,31,3]:
                return 1
            else:
                return 0
        elif self.nb_steps <= 80:
            if self.s in [0,1,2,26,27,28,     5,10,13,21,36,    8,9,11,18,19,20,22,23,39,40,41,43,44,31,3]:
                return 1
            else:
                return 0
        else:
            if self.s in [0,1,2,26,27,28,     5,10,13,21,36,    8,9,11,18,19,20,22,23,39,40,41,43,44]:
                return 1
            else:
                if self.s in [3,31]:
                    if random.random() <= 50:
                        return 1
                    else:
                        return 0
                else:
                    return 0

    def update(self, sp):
        self.s = sp
