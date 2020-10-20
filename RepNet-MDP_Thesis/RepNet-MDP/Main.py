import System
import MDPParameters
import RepNetMDP
import RepNetAgent
import Oracle
import MDPAgent
import QLearner

parameters = MDPParameters.MDPParameters()
system = System.System(parameters)
agents = []

for g in parameters.agents:
    if parameters.agent_types[g] == "repnet":
        agents.append(RepNetAgent.RepNetAgent(g, system, parameters))
    elif parameters.agent_types[g] == "oracle":
        agents.append(Oracle.Oracle(g))
    elif parameters.agent_types[g] == "mdp":
        agents.append(MDPAgent.MDPAgent(g, system, parameters))
    elif parameters.agent_types[g] == "qlearner":
        agents.append(QLearner.QLearner(g, system, parameters))
repNetMDP = RepNetMDP.RepNetMDP(system, agents, parameters)

repNetMDP.online_repnet_solver()
