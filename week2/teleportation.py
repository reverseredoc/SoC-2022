#teleportation proper algo

# imports
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import IBMQ, Aer, transpile, assemble
from qiskit.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
from qiskit.extensions import Initialize
from qiskit.ignis.verification import marginal_counts
from qiskit.quantum_info import random_statevector

def bell_pair_creation(circuit,a,b):
    circuit.h(a)
    circuit.cx(a,b)

def alice_gates(circuit,psi,a):
    circuit.cx(psi,a)
    circuit.h(psi)
    
def measure_and_send(circuit,a,b):
    #qubits a and b are measured and the result is sent to Bob
    circuit.barrier()
    circuit.measure(a,0)
    circuit.measure(b,1)
    
def bob_gates(circuit,qubit,crz,crx):
    #could not have done this if measure din one register 
    circuit.x(qubit).c_if(crx,1)
    circuit.z(qubit).c_if(crz,1)
    
    
#for verification
psi=random_statevector(2)
display(array_to_latex(psi, prefix="|\\psi\\rangle ="))
display(plot_bloch_multivector(psi))

#initialisation gate

init_gate=Initialize(psi)
init_gate.label="init"

#inverse init gate
inverse_init_gate=init_gate.gates_to_uncompute()
inverse_init_gate.label="disantangler"

#proper setup creating quantum and classical registers 
qr=QuantumRegister(3,name="q")
crz=ClassicalRegister(1,name="crz")
crx=ClassicalRegister(1,name="crx")
tele_circuit=QuantumCircuit(qr,crz,crx)
#or could have done QuantumCircuit(3,2)
#then look of circuit woud have been different 

tele_circuit.append(init_gate,[0])#gate appended
tele_circuit.barrier()

bell_pair_creation(tele_circuit,1,2)
tele_circuit.barrier()
alice_gates(tele_circuit,0,1)
measure_and_send(tele_circuit,0,1)
tele_circuit.barrier()
bob_gates(tele_circuit,2,crz,crx)


display(tele_circuit.draw())

#verification by bloch
sim = Aer.get_backend('aer_simulator')
tele_circuit.save_statevector()
out_vector = sim.run(tele_circuit).result().get_statevector()
plot_bloch_multivector(out_vector)


#verification 2 by measuring state vector of b
qobj = assemble(tele_circuit)
final_state = sim.run(qobj).result().get_statevector()

#checking the accuracy of the teleportation system
#qubit b in actual scenario now has the state psi
#as qubit 0 and 1 have been measured
a=[]

for i in range(4):
    if final_state[i]!=0:
        a.append(final_state[i])
        break
else:
    a.append(0)
    
for i in range(4,8):
    if final_state[i]!=0:
        a.append(final_state[i])
        break
else:
    a.append(0)

display(array_to_latex(a, prefix="|\\ b \\rangle ="))#state vector of b
sim = Aer.get_backend('aer_simulator')

#out_vector = sim.run(circuit).result().get_statevector()
display(plot_bloch_multivector(final_state))

#verifictaion 3

tele_circuit.append(inverse_init_gate,[2])
#measuring third qubit
cr_result=ClassicalRegister(1)
tele_circuit.add_register(cr_result)
tele_circuit.measure(2,2)

display(tele_circuit.draw())

t_qc = transpile(tele_circuit, sim)
counts = sim.run(t_qc).result().get_counts()
qubit_counts = [marginal_counts(counts, [qubit]) for qubit in range(3)]
display(plot_histogram(qubit_counts))
