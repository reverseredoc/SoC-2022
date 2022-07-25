def GHZ(n):
    ghz=QuantumCircuit(n)
    ghz.h(0)
    for i in range(1,n):
        ghz.cx(0,i)
        
    return ghz

n=10 #argument for number of qubits in the GHZ state
circuit=GHZ(n)
display(circuit.draw())

sim = Aer.get_backend('aer_simulator')
circuit.save_statevector()
qobj = assemble(circuit)
final_state = sim.run(qobj).result().get_statevector()

display(array_to_latex(final_state, prefix="|\\psi\\rangle ="))

