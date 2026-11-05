from qiskit import *
from qiskit_aer import Aer
from qiskit.quantum_info import Pauli, Statevector
from qiskit.visualization.bloch import Bloch
import matplotlib.pyplot as plt

qr=QuantumRegister(1,'q') 
qc=QuantumCircuit(qr)  
 
qc.initialize([0,1], qr[0])
psi1 = Statevector(qc)
qc.x(qr[0])
psi2 = Statevector(qc)

def bloch_coords(state):
    return [state.expectation_value(Pauli(axis)).real for axis in ("X", "Y", "Z")]

sphere = Bloch()
sphere.vector_color = ["red", "blue"]
sphere.add_vectors(bloch_coords(psi1))
sphere.add_vectors(bloch_coords(psi2))
sphere.render()
plt.show()