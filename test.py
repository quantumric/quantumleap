from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import BinaryQuadraticModel

projects=['P1','P2','P3','P4','P5']
profits=[30,24,41,33,18]

sampler = EmbeddingComposite(DWaveSampler())

bqm = BinaryQuadraticModel( 'BINARY' )

bqm.add_variables_from( [('P1', -30), ('P2', -24), ('P3', -41), ('P4', -33), ('P5', -18)] )

sampleset=sampler.sample(bqm)

print(sampleset)
