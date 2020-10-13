# Reputation-driven Decision-making in Networks of Stochastic Agents (Master's thesis)
## Supervisors
- Prof. dr. L. De Raedt
- Dr. G. Rens

## Abstract
This thesis studies multi-agent systems that involve networks of self-interested agents.
In 2018, [Rens et al.](https://arxiv.org/abs/1805.05230) developed a Markov Decision Process-derived framework,
called RepNet-POMDP, tailored to domains in which agent reputation is a key driver
of the interactions between agents. The theoretical foundation of the framework was
provided; the framework itself was, however, subsequently left unimplemented.
Due to the highly intractable nature of its exact planning algorithm, we first reduce the
framework to its fully observable equivalent, called RepNet-MDP, in an effort to study
the framework’s properties more efficiently. We further alleviate the intractability
of the framework by devising an algorithm for finding approximate solutions. We
show that the concept of directed actions, as introduced by Rens et al., is subject
to several theoretical inconsistencies, and propose an alternative interpretation of
this concept that retains its core characteristics. We furthermore demonstrate that
the initial notion of action distribution can lead to undesirable agent behavior, and
provide a revised formulation of the concept.
The viability of the framework is tested in a series of experiments designed to highlight
its strengths and shortcomings. The tests display the RepNet agents’ ability to
leverage the framework’s fundamental properties in an effort to adapt their behavior
to the past behavior and reliability of the remaining agents of the network. RepNet
agents are furthermore shown to be willing to sacrifice their selfish intentions in an
attempt to maintain a general level of well-being of the entire network. Finally, our
work identifies a limitation of the framework in its current formulation that prevents
its agents from learning in circumstances in which they are not a primary actor.
