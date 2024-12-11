from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
print(qc.draw())

simulator = Aer.get_backend('statevector_simulator')
result = execute(qc, backend=simulator).result()
statevector = result.get_statevector()
print("Statevector:", statevector)