from qiskit.circuit import QuantumRegister, QuantumCircuit 
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np

n = 4
N = 2**n
state = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=complex)
fourier_state = np.zeros(N, dtype=complex)
probabilities_fn = []
for input_index, amplitude in enumerate(state):
    for output_index in range(N):
        phase = np.exp(2 * np.pi * 1j * input_index * output_index / N)
        fourier_state[output_index] += phase * amplitude
        
probabilities_fn = np.abs((fourier_state/np.sqrt(N)))**2
FN = fourier_state / np.sqrt(N)

qr1 = QuantumRegister(4, "qreg1")  
qc = QuantumCircuit(qr1)
qc.initialize([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], qr1)
qc.h(qr1)
probabilities_had = []
statevector = Statevector.from_instruction(qc)
for index, amplitude in enumerate(statevector.data):
   basis_state = format(index, f"0{6}b")
   probability = abs(amplitude) ** 2
   probabilities_had.append(probability)

x_indices = np.arange(N)

plt.figure(figsize=(10, 5))
plt.plot(x_indices, probabilities_fn, marker='o', linestyle='-', color='b', linewidth=2, markersize=6, label='Fourier State')
plt.plot(x_indices, probabilities_had, marker='s', linestyle='--', color='r', linewidth=2, markersize=6, label='Hadamard State')
plt.ylim(0, 0.1)
plt.title("Comparison of Quantum State Probabilities Across Basis States", fontsize=12)
plt.xlabel("Basis State Index (0 to 15)", fontsize=10)
plt.ylabel("Probability", fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xticks(x_indices)
plt.show()
#print(f"|{basis_state}>: "f"amplitude={amplitude.real:+.3f}{amplitude.imag:+.3f}j, "f"probability={probability:.3f}")
#print(np.abs(FN))