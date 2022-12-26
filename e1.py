from dimod import ConstrainedQuadraticModel, Binary, quicksum
from dwave.system import LeapHybridCQMSampler

values = [17,21,19]

n = len(values)

# Create the binary variables
x = [Binary(i) for i in range(n)]

# Construct the CQM
cqm = ConstrainedQuadraticModel()

# Add the objective
cqm.set_objective(quicksum(-values[i]*x[i] for i in range(n)))

# Add the two constraints
cqm.add_constraint(quicksum(x[i] for i in range(n)) <= 2, label='max items')

# Submit to the CQM sampler
sampler = LeapHybridCQMSampler()
sampleset = sampler.sample_cqm(cqm)

print("\nFull sample set:")
print(sampleset)

