import System
import MDPParameters
import MDPTree
import copy
from Agent import Agent


class MDPAgent(Agent):

    def __init__(self, g, system: System.System, parameters: MDPParameters.MDPParameters):
        Agent.__init__(self)
        self.g = g
        self.system = system
        self.parameters = parameters
        self.tree: MDPTree.Node = None
        self.number_of_agents = len(self.system.agents)
        self.number_of_actions_u = len(system.actions_u)

        self.AD = [[[1 / len(system.actions) for a in range(len(system.actions))] for s in range(len(system.states))] for h in range(len(system.agents))]

    def T(self, s, a, sp):

        if self.number_of_agents == 2:
            probability_of_sp = 0
            if self.g == 1:
                for action in self.system.actions_u:
                    probability_of_sp += self.parameters.objective_transition_model[action*self.number_of_actions_u + a][s][0][sp]
            else:
                # g = 0
                for action in self.system.actions_u:
                        probability_of_sp += self.parameters.objective_transition_model[action + a*self.number_of_actions_u][s][0][sp]
            return probability_of_sp

    def R(self, s, a):
        number_of_agents = len(self.system.agents)
        agents = copy.deepcopy(self.system.agents)
        agents.remove(self.g)
        pi = self.system.I(self.g, self.g, s, a) + sum(sum(self.system.I(self.g, h, s, ap) * self.AD[h][s][ap] for ap in self.system.actions) for h in agents)
        return (1/number_of_agents) * pi

    def lookahead(self, s):
        self.tree = self.tree = self.construct(s, self.parameters.lookahead_depth)
        return self.best_action()

    def construct(self, s, depth):
        if depth == 0:
            orNode = MDPTree.ORNode(s)
            for a in self.system.actions_u:
                andNode = MDPTree.ANDNode(a)
                andNode.value = self.R(s, a)
                orNode.children.append(andNode)
            orNode.value = max(self.R(s, i) for i in self.system.actions_u)
            return orNode
        else:
            tree = MDPTree.ORNode(s)
            for a in self.system.actions_u:
                andNode = MDPTree.ANDNode(a)
                andNode.value = self.R(s, a)
                for sp in self.system.states:
                    child = self.construct(sp, depth-1)
                    andNode.value += self.parameters.decay * self.T(s, a, sp)
                    andNode.children.append(child)
                tree.children.append(andNode)
            tree.value = max(tree.children[i].value for i in self.system.actions_u)
            return tree

    def best_action(self):
        best_action = self.tree.children[0].a
        best_value = self.tree.children[0].value
        print("         Value of each action : " + str([self.tree.children[i].value for i in self.system.actions_u]))
        for andNode in self.tree.children:
            if andNode.value >= best_value:
                best_action = andNode.a
                best_value = andNode.value
        return best_action

    def update(self, sp):
        ""