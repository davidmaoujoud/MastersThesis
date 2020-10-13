
class MDPParameters:

    def __init__(self, decay=0.7, learning_rate=1, delta_weight=0.8, update_function="difference_update", epsilon_convergence=0.1, steps=100, lookahead_depth=3, first_state=0, use_oracle=True):
        self.decay = decay
        self.learning_rate = learning_rate
        self.delta_weight = delta_weight
        self.update_function = update_function
        self.epsilon_convergence = epsilon_convergence
        self.steps = steps
        self.lookahead_depth = lookahead_depth
        self.first_state = first_state
        self.use_oracle = use_oracle

        self.agents = [0, 1]
        self.states = list(range(5))
        self.actions_u = [0,1,2,3,4,5] # Actions: do_good, buy, consume, accept, refuse, nothing
        self.actions_d = []

        self.agent_types = ["repnet", "oracle"] # Can be repnet, mdp, oracle, qlearner


        self.objective_transition_model = [
            [  ################ do_good/do_good ############################
                [[0, 1, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ do_good/buy ############################
                [[0, 1, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ do_good/consume ############################
                [[0, 1, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ do_good/accept ############################
                [[0, 1, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 0, 0, 1]],
                [[0, 0, 0, 0, 1]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ do_good/refuse ############################
                [[0, 1, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[1, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ do_good/nothing ############################
                [[0, 1, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],



            [  ################ buy/do_good ############################
                [[0, 0, 0, 1, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ buy/buy ############################
                [[0, 0, 0, 1, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ buy/consume ############################
                [[0, 0, 0, 1, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ buy/accept ############################
                [[0, 0, 0, 1, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 0, 1]],
                [[0, 0, 0, 0, 1]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ buy/refuse ############################
                [[0, 0, 0, 1, 0]],
                [[0, 0, 1, 0, 0]],
                [[1, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ buy/nothing ############################
                [[0, 0, 0, 1, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],




            [  ################ consume/do_good ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ consume/buy ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ consume/consume ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ consume/accept ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 0, 0, 1]],
                [[0, 0, 0, 0, 1]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ consume/refuse ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[1, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ consume/nothing ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],






            [  ################ accept/do_good ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ accept/buy ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ accept/consume ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ accept/accept ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 0, 0, 1]],
                [[0, 0, 0, 0, 1]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ accept/refuse ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[1, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ accept/nothing ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],




            [  ################ refuse/do_good ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ refuse/buy ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ refuse/consume ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ refuse/accept ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 0, 0, 1]],
                [[0, 0, 0, 0, 1]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ refuse/refuse ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[1, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ refuse/nothing ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],




            [  ################ nothing/do_good ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ nothing/buy ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ nothing/consume ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ nothing/accept ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 0, 0, 1]],
                [[0, 0, 0, 0, 1]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ nothing/refuse ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[1, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0]]
            ],
            [  ################ nothing/nothing ############################
                [[1, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0]],
                [[0, 0, 1, 0, 0]],
                [[0, 0, 0, 1, 0]],
                [[1, 0, 0, 0, 0]]
            ]

        ]





        # Actions: do_good, buy, consume, accept, refuse, nothing
        # Impact(agent1, agent2, state, action_performed_by_agent2)
        self.impact_function = [
            [
                [[0.5,0.4,0,0,0,0,0], [0.24,0.9,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,1,0,0,0,0]],
                [[0,0,0,0,0,0,0],     [0,0,0,0,0,0,0],     [0,0,0,1,-1,0,0],   [0,0,0,1,-1,0,0],   [0,0,0,0,0,0,0]]
            ],

            [
                [[1,-1,0,0,0,0,0], [0,1,0,0,0,0,0], [0,0,0,0,0,0,0],  [0,0,0,0,0,0,0],  [0,0,0,0,0,0,0]],
                [[0,0,0,0,0,1,0],  [0,0,0,0,0,1,0], [0,0,0,1,-1,0,0], [0,0,0,-1,1,0,0], [0,0,0,0,0,1,0]]
            ]
        ]


        # Q-Learner tests
        # Actions: do_good, buy, consume, accept, refuse, nothing
        # Impact(agent1, agent2, state, action_performed_by_agent2)
        self.impact_function = [
            [
                [[0.5,0.4,0,0,0,0,0], [0.25,0.25,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,1,0,0,0,0]],
                [[0,0,0,0,0,0,0],     [0,0,0,0,0,0,0],     [0,0,0,1,-1,0,0],   [0,0,0,1,-1,0,0],   [0,0,0,0,0,0,0]]
            ],

            [
                [[1,-1,0,0,0,0,0], [0,1,0,0,0,0,0], [0,0,0,0,0,0,0],  [0,0,0,0,0,0,0],  [0,0,0,0,0,0,0]],
                [[0,0,0,0,0,1,0],  [0,0,0,0,0,1,0], [0,0,0,1,-1,0,0], [0,0,0,-1,1,0,0], [0,0,0,0,0,1,0]]
            ]
        ]



        self.restrictions = [
            [],
            []
        ]
        # wait_for_A
        self.directed_transition_models = [
            # Agent 1/G
            [
                [[[]]]  # Start in state 0
            ],

            # Agent 2/A
            [
                [[[]]]
            ]
        ]



        self.restrictions = [
            [],
            []
        ]

        self.restrictions = [
            [(2,6), (3,6)], # In states 2 and 3, agent A must pick a directed transition
            []
        ]

        self.directed_undirected_equivalence = [
            [(6,5)], # To the outside system, "wait" is equivalent to do nothing
            [(6,5)]
        ]

         # wait_for_A
        self.directed_transition_models = [
            # Agent 1/G
            [
                [[[0,0,0,0,0],           [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]           ],  # Start in state 0
                [[[0,0,0,0,0],           [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]           ],  # Start in state 1


                # State 2
                #[[[1,2/3,0,0,0], [0,0,0,0,0], [0,1/3,1/3,1/3,0], [0,0,0,0,0], [0,0,1/3,2/3,1]] ],  # Start in state 2 -> Agent A has a realistic view on when agent B might reject a trade offer
                #[[[1,1,2/3,2/3,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,1/3,1/3,1]] ],
                #[[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]] ],
                #[[[1/6,1/6,1/6,1/6,1/6], [0,0,0,0,0], [1/6,1/6,1/6,1/6,1/6], [0,0,0,0,0], [1/6,1/6,1/6,1/6,1/6]] ],
                #[[[1/5,1/6,1/7,1/8,1/9], [0,0,0,0,0], [1/6,1/6,1/6,1/6,1/6], [0,0,0,0,0], [1/9,1/8,1/7,1/6,1/5]] ],
                [[[1/9,1/9,1/9,1/9,1/9], [0,0,0,0,0], [1/6,1/6,1/6,1/6,1/6], [0,0,0,0,0], [1/3,1/3,1/3,1/3,1/3]] ],
                #[[[1/3,1/3,1/3,1/3,1/3], [0,0,0,0,0], [1/3,1/3,1/3,1/3,1/3], [0,0,0,0,0], [1/3,1/3,1/3,1/3,1/3]] ],  # Start in state 2
                #[[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [1,1,1,1,1]] ],  # Start in state 2 -> Agent A thinks Agent B will accept the trade offer no matter its reputation (naive)



                # State 3
                #[[[1/6,1/6,1/6,1/6,1/6], [0,0,0,0,0], [0,0,0,0,0], [1/6,1/6,1/6,1/6,1/6], [1/6,1/6,1/6,1/6,1/6]] ],  # Start in state 3
                [[[1/5,1/6,1/7,1/8,1/9], [0,0,0,0,0], [0,0,0,0,0], [1/6,1/6,1/6,1/6,1/6], [1/9,1/8,1/7,1/6,1/5]] ],




                [[[0,0,0,0,0],           [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]           ]   # Start in state 4
            ],

            # Agent 2/A
            [
                [[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]          ],  # Start in state 0
                [[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]          ],  # Start in state 1
                [[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]          ],  # Start in state 2
                [[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]          ],  # Start in state 3
                [[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]          ]   # Start in state 4
            ]
        ]
