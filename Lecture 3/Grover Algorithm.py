from qiskit.circuit import QuantumRegister, QuantumCircuit 
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
       
   state_to_be_found=input("The state we want to find is: ")
   state_to_be_found_in_decimal=int(state_to_be_found)
   for i in range(30):
     if(state_to_be_found_in_decimal<2**i):
        M=2**i
        L=i
        break
   K = np.zeros(M,dtype=complex)
   K[state_to_be_found_in_decimal]=1
   I = np.zeros((M,M),dtype=complex)
   O = np.zeros((M,M),dtype=complex)
   G = np.zeros((M,M),dtype=complex) 
   s = np.zeros(M,dtype=complex)
   final_state = np.zeros(M,dtype=complex)
   final_states = []
   iterations_list = []
   amplitudes_list = []
   qr1 = QuantumRegister(L, "qreg1")  
   qc = QuantumCircuit(qr1)
   N = np.zeros(M,dtype=complex)
   N[0]=1
   qc.initialize(N, qr1)
   qc.h(qr1) 
   
   I = np.eye(M)
   had = Statevector.from_instruction(qc).data
   G = 2*np.outer(had,had)- I
   for i in range(math.ceil(np.pi/4*np.sqrt(M)-0.5)):
         O = I - 2*np.outer(K,K)
         s = O @ had
         final_state = G @ s
         print(final_state)
         had = final_state
         final_states.append(final_state)
         iterations_list.append(i+1)
         amplitudes_list = [amplitude**2 for amplitude in final_states]
         
   plt.figure(figsize=(8, 5))
   plt.plot(iterations_list, amplitudes_list, marker='o', linestyle='-', color='b', linewidth=2, markersize=8)
   plt.title("Grover's Algorithm: Target State Amplitude per Iteration", fontsize=12)
   plt.xlabel("Iteration Number", fontsize=10)
   plt.ylabel("Amplitude", fontsize=10)
   plt.grid(True, linestyle='--', alpha=0.6)
   plt.xticks(iterations_list)
   plt.show()
if __name__ == "__main__":
     main()