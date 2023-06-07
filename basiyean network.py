from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create the Bayesian network
model = BayesianModel([('Door', 'Prize'), ('Choice', 'Prize'), ('Prize', 'Monty')])

# Define the conditional probability distributions (CPDs)
door_cpd = TabularCPD('Door', 3, [[1/3], [1/3], [1/3]])
choice_cpd = TabularCPD('Choice', 3, [[1/3], [1/3], [1/3]])
prize_cpd = TabularCPD('Prize', 3, [[0, 0, 1, 0, 0, 1, 0, 1, 0],
                                    [1, 0, 0, 0, 1, 0, 0, 0, 1],
                                    [0, 1, 0, 1, 0, 0, 1, 0, 0]],
                       evidence=['Door', 'Choice'], evidence_card=[3, 3])
print(prize_cpd)
monty_cpd = TabularCPD('Monty', 3, [[0, 1, 0],[0.33, 0, 0.67],[0.67, 0, 0.33]],
                       evidence=['Prize'], evidence_card=[3])
print(monty_cpd)
# Add the CPDs to the model
model.add_cpds(door_cpd, choice_cpd, prize_cpd, monty_cpd)

# Perform inference to calculate probabilities
inference = VariableElimination(model)

# Calculate the probability of winning if the contestant sticks to their original choice
stick_probability = inference.query(['Prize'], evidence={'Choice': 1})#['Prize'].values[0]


#stick_probability = inference.query(['Prize'], evidence={'Choice': 1})['Prize'].values[2]
print("Probability of winning if sticking to the original choice:", stick_probability)

# Calculate the probability of winning if the contestant switches their choice
switch_probability = inference.query(['Prize'], evidence={'Choice': 2}, show_progress=False).normalize(inplace=False)#['Prize'].values[2]
print("Probability of winning if switching the choice:", switch_probability)
