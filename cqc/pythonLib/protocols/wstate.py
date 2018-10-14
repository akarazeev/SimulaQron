from SimulaQron.cqc.pythonLib.cqc import *
import numpy as np

def initialize_Qubit_register(num_qubit,Owner):
	print("\n ------- \n Initializing qubits! \n ------- \n")
	qubits = []
	for x in range(0,num_qubit):
		one_more_qubit = qubit(Owner)
		qubits.append(one_more_qubit)
	return qubits

def ControlledG(controlled_qubit, target_qubit, index):
	p = np.sqrt(1-1/index)
	x = int(np.arcsin(p) * 256/(2*np.pi))
	controlled_qubit.cnot(target_qubit)
	target_qubit.rot_Y(256-x)
	controlled_qubit.cnot(target_qubit)
	target_qubit.rot_Y(x)
	target_qubit.cnot(controlled_qubit)

def prepare_Nqubit_Wstate(qubits):
	num_qubit = len(qubits)
	qubits[0].X()
	for x in range(1,num_qubit):
		qubit1 = qubits[x-1]
		qubit2 = qubits[x]
		ControlledG(qubit1,qubit2, num_qubit-x+1)
