from qiskit.circuit import QuantumRegister, QuantumCircuit 
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np

qr1 = QuantumRegister(3, "qreg1")  
qc = QuantumCircuit(qr1)
qc.initialize([0, 0, 1, 0, 0, 0, 0, 0], qr1)
qc.h(qr1)
qc.p(np.pi/4 , qr1[2])
qc.p(2 * np.pi/4 , qr1[1])
qc.p(3 * np.pi/4 , qr1[0])

state = Statevector.from_instruction(qc)
print(state.data)
fig = qc.draw(output="mpl")
plt.show()
