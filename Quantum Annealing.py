from dwave.system import DWaveSampler, EmbeddingComposite
import dimod

h = {0: -1, 1: -1}
J = {(0, 1): 1}
bqm = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.BINARY)

sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm, num_reads=10)
print(sampleset)