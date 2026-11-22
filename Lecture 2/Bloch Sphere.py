from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt


psi = Statevector([1/2**0.5, 1/2**0.5])
plot_bloch_multivector(psi)
plt.show()




