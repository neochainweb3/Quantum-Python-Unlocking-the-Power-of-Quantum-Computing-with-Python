from qiskit import QuantumCircuit
qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()
