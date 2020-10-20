import random
import matplotlib.pyplot as plt
import csv


class RepNetMDP:
    def __init__(self, system, agents, parameters):
        self.system = system
        self.agents = agents
        self.parameters = parameters
        self.state_history = [self.system.current_state]
        self.best_actions = []
        self.tracked_variables = []
        self.tracked_variables2 = []
        self.test = ""

    def execution(self, best_actions, o=0):
        # Directed actions need to be switched back to undirected actions
        for t, a in enumerate(self.system.agents):
            for (i, j) in self.parameters.directed_undirected_equivalence[t]:
                for k, a in enumerate(best_actions):
                    if a == i:
                        best_actions[k] = j

        print("Execution:")
        # Applying each agent's action to the environment and yielding the new environment state
        biased_state_list = []
        accumulator = 0
        for sp in self.system.states:
            number_of_actions = len(self.system.actions_u)
            number_of_agents = len(self.system.agents)
            probability_of_sp = 0

            if number_of_agents == 2:
                probability_of_sp = self.parameters.objective_transition_model[best_actions[0]*number_of_actions + best_actions[1]][self.system.current_state][0][sp]
            elif number_of_agents == 3:
                probability_of_sp = self.parameters.objective_transition_model[best_actions[0]*number_of_actions*2 + best_actions[1]*number_of_actions + best_actions[2]][self.system.current_state][0][sp]
            elif number_of_agents == 4:
                probability_of_sp = self.parameters.objective_transition_model[best_actions[0]*number_of_actions*4 + best_actions[1]*number_of_actions*2 + best_actions[2]*number_of_actions + best_actions[3]][self.system.current_state][0][sp]

            biased_state_list.append(probability_of_sp + accumulator)
            accumulator += probability_of_sp
        biased_random = random.uniform(0, biased_state_list[len(biased_state_list)-1])
        next_state = -1
        i = 0
        while next_state == -1:
            if biased_random <= biased_state_list[i]:
                next_state = i
            i += 1

        if self.test == "ABCTrade" and o >= 66 and self.system.current_state == 0: # Forces interaction between agents B and C (so that A can learn indirectly)
            if random.random() < 0.50:
                next_state = 5
            else:
                next_state = 8
        elif self.test == "ABCTrade" and self.system.current_state == 0: # No trades are done by agents B and C
            if best_actions[0] == 0:
                next_state = 1 # Trade with B
            else:
                next_state = 2 # Trade with C

        elif self.test == "VTOL4":
            if self.system.current_state == 46 or self.system.current_state == 47: # Reset game
                next_state = random.choice([0,1,2,5,13,26,29,34])

        self.state_history.append(next_state)

        # Send the new environment state to each agent
        for g in self.agents:
            g.update(next_state)

        # Update the system with the new environment state
        self.system.current_state = next_state

    def planning(self):
        print("Planning:")
        best_actions = []
        for g in self.agents:
            best_actions.append(g.lookahead(self.system.current_state))
        self.best_actions = best_actions
        return best_actions

    def online_repnet_solver(self):
        #self.initABTradeQ()
        # Alternating between planning and execution
        for k in range(self.parameters.steps):
            best_actions = self.planning()
            #self.trackABTradeVariablesQ(k)
            self.execution(best_actions, k)
        plt.plot(self.state_history)
        plt.show()
        #self.unpackABTradeVariablesQ()

    def initABTrade(self):
        ""

    def trackABTradeVariables(self, k=0):
        proba_B_accept_in_2 = self.agents[0].AD[1][2][3]
        proba_B_accept_in_3 = self.agents[0].AD[1][3][3]
        proba_B_refuse_in_2 = self.agents[0].AD[1][2][4]
        proba_B_refuse_in_3 = self.agents[0].AD[1][3][4]
        img_A_has_of_B = self.agents[0].Img[1][0]
        img_B_has_of_A = self.agents[0].Img[0][1]
        rep_A = self.agents[0].REP(0, self.agents[0].Img)
        rep_B = self.agents[0].REP(1, self.agents[0].Img)

        trade_offers = (self.system.current_state, self.best_actions[0])

        trade_offer = 0
        if self.system.current_state == 0 or self.system.current_state == 1:
            if self.best_actions[0] == 1:
                trade_offer = 1

        self.tracked_variables.append((proba_B_accept_in_2, proba_B_accept_in_3, proba_B_refuse_in_2, proba_B_refuse_in_3, img_A_has_of_B, img_B_has_of_A, rep_A, rep_B, trade_offers, trade_offer))

    def unpackABTradeVariables(self):
        proba_B_accept_in_2 = [tuple[0] for tuple in self.tracked_variables]
        proba_B_accept_in_3 = [tuple[1] for tuple in self.tracked_variables]
        plt.plot(proba_B_accept_in_2)
        plt.plot(proba_B_accept_in_3)
        plt.title("Probability of B accepting the trade offer")
        plt.show()
        proba_B_refuse_in_2 = [tuple[2] for tuple in self.tracked_variables]
        proba_B_refuse_in_3 = [tuple[3] for tuple in self.tracked_variables]
        plt.plot(proba_B_refuse_in_2)
        plt.plot(proba_B_refuse_in_3)
        plt.title("Probability of B refusing the trade offer")
        plt.show()
        img_A_has_of_B = [tuple[4] for tuple in self.tracked_variables]
        img_B_has_of_A = [tuple[5] for tuple in self.tracked_variables]
        plt.plot(img_A_has_of_B)
        plt.plot(img_B_has_of_A)
        plt.title("Image that both agents have of each other")
        plt.show()
        rep_A = [tuple[6] for tuple in self.tracked_variables]
        rep_B = [tuple[7] for tuple in self.tracked_variables]
        plt.plot(rep_A)
        plt.plot(rep_B)
        plt.title("Reputation of both agents")
        plt.show()
        trade_offer = [tuple[9] for tuple in self.tracked_variables]

        with open('CSV/tradeABaccept2.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(proba_B_accept_in_2)
        with open('CSV/tradeABaccept3.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(proba_B_accept_in_3)
        with open('CSV/tradeABrefuse2.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(proba_B_refuse_in_2)
        with open('CSV/tradeABrefuse3.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(proba_B_refuse_in_3)
        with open('CSV/tradeABimgAB.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(img_A_has_of_B)
        with open('CSV/tradeABimgBA.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(img_B_has_of_A)
        with open('CSV/tradeABrepA.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(rep_A)
        with open('CSV/tradeABrepB.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(rep_B)
        with open('CSV/tradeABfreq.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(trade_offer)

    def initABTradeQ(self):
        ""

    def trackABTradeVariablesQ(self, k=0):

        trade_offers = (self.system.current_state, self.best_actions[0])

        trade_offer = 0
        if self.system.current_state == 0 or self.system.current_state == 1:
            if self.best_actions[0] == 1:
                trade_offer = 1

        self.tracked_variables.append((trade_offers,
                                       trade_offer))

    def unpackABTradeVariablesQ(self):
        trade_offer = [tuple[1] for tuple in self.tracked_variables]

        with open('CSV/tradeABQ.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            #writer.writerow(trade_offer)

    def initVTOL2(self):
        self.tracked_variables = [0 for i in range(self.parameters.steps)]
        self.tracked_variables2 = [0 for i in range(self.parameters.steps)]

    def trackVTOL2Variables(self, k):
        if self.system.current_state == 15:
            self.tracked_variables[k] += 1
        if self.system.current_state in [12,13,14]:
            self.tracked_variables2[k] = 1

    def unpackVTOL2Variables(self):
        plt.plot(self.tracked_variables)
        plt.title("Number of crashes as a function of the number of steps")

        with open('CSV/vtol2timespentrightmdp.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(self.tracked_variables2)

    def initABCTradeQLearner(self):
        self.test = "ABCTrade"
        self.tracked_variables2 = [0 for i in range(self.parameters.steps)]

    def initABCTrade(self):
        self.test = "ABCTrade"
        self.tracked_variables2 = [0 for i in range(self.parameters.steps)]

    def trackABCTradeQLearnerVariables(self, k=0):
        if self.system.current_state == 0:
            action = self.best_actions[0]
            self.tracked_variables2[k] = action
        else:
            action = self.tracked_variables2[k-1]
            self.tracked_variables2[k] = action

        self.tracked_variables.append((action))

    def trackABCTradeVariables(self, k=0):
        proba_B_accept = self.agents[0].AD[1][1][0]
        proba_C_accept = self.agents[0].AD[2][2][0]

        rep_B = self.agents[0].REP(1, self.agents[0].Img)
        rep_C = self.agents[0].REP(2, self.agents[0].Img)

        if self.system.current_state == 0:
            action = self.best_actions[0]
            self.tracked_variables2[k] = action
        else:
            action = self.tracked_variables2[k-1]
            self.tracked_variables2[k] = action

        self.tracked_variables.append((proba_B_accept, proba_C_accept, rep_B, rep_C, action))

    def unpackABCTradeQLearnerVariables(self):
        actions = self.tracked_variables
        plt.plot(actions)
        plt.show()

        with open('CSV/tradeABCQ.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(actions)

    def unpackABCTradeVariables(self):
        proba_B_accept = [tuple[0] for tuple in self.tracked_variables]
        proba_C_accept = [tuple[1] for tuple in self.tracked_variables]

        rep_B = [tuple[2] for tuple in self.tracked_variables]
        rep_C = [tuple[3] for tuple in self.tracked_variables]
        actions = [tuple[4] for tuple in self.tracked_variables]

        with open('CSV/tradeABCacceptB.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(proba_B_accept)

        with open('CSV/tradeABCacceptC.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(proba_C_accept)

        with open('CSV/tradeABCrepB.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(rep_B)

        with open('CSV/tradeABCrepC.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(rep_C)

        with open('CSV/tradeABCactiontaken.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(actions)

    def initVTOL4(self):
        self.test = "VTOL4"

    def trackVTOL4Variables(self, k):
        if self.system.current_state == 46: # Win
            self.tracked_variables.append((1,0))
        elif self.system.current_state == 47: # Loss
            self.tracked_variables.append((0,1))
        else:
            self.tracked_variables.append((0,0))

    def unpackVTOL4Variables(self):
        win = [tuple[0] for tuple in self.tracked_variables]
        loss = [tuple[1] for tuple in self.tracked_variables]

        with open('CSV/vtol4wins.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(win)

        with open('CSV/vtol4crashes.csv', 'a') as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            writer.writerow(loss)
