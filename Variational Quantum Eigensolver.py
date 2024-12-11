from qiskit import Aer
from qiskit.circuit.library import RealAmplitudes
from qiskit.algorithms import VQE
from qiskit.primitives import Sampler
from qiskit.quantum_info import Pauli
from qiskit.opflow import I, Z, X

hamiltonian = (0.5 * I ^ I) + (1.0 * Z ^ Z)
ansatz = RealAmplitudes(2)
sampler = Sampler(Aer.get_backend('aer_simulator'))
vqe = VQE(ansatz, optimizer='SLSQP', sampler=sampler)
result = vqe.compute_minimum_eigenvalue(hamiltonian)
print(result)