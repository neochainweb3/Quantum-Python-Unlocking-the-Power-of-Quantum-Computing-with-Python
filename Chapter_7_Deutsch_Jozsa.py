from qiskit import QuantumCircuit, Aer, execute
qc = QuantumCircuit(3, 2)
qc.x(2)
qc.h([0, 1, 2])
qc.cx(0, 2)
qc.cx(1, 2)
qc.h([0, 1])
qc.measure([0, 1], [0, 1])
