# SoC-2022
An Introduction to QC, ML and QML 

The whole SoC phase was divided into 5 weeks. I have given theh summary of each week below. My githuub repo also ha folders for 5 different weeks.
Description of the folders in github repo:
1. week1: As this week, Quantum Computing was introduced and we were asked to read the book QCQI, the readme contains teh summary of all the pages I was supposed to read.

2. week2: This week too there was some recemmended reading from th ebook QCQI. In the readme, I have given a summary of the pages of QCQI I read. Also, coding part started this week. I learnt how to use the qiskit library in python and implemented the circuits on Jupyter notebook. The ipynb files of the codes written are submitted in this folder.
 
3. week3: This week was the final brush with Quantum Computing. There was some recemmonded reading from QCQI the summary of which I have written in the readme file of this week. Also, after reading, I implemented the circuits on Jupyter notebbok using Qiskit library in python. The ipynb files are submitted in thsi folder.  
 
4. week4: This week, we were introduced to Machine Learning. We were given recemmonded reading about the topics Linear Regression, Logistic Regression, kernels, support vector machines. k means clustering and neural networks. I alo studied about convolutional neural networks. I read about these topics and implemented these algorithms in jupyter notebook with the help of libraries like numpy, pandas, matplotlib, tensorflow and API keras. The codes written are submitted in this folder. 
 
5. week5: This week having studied about QC and ML, it was time to introduce QML. I read a research paper about QNN (quanvolutional neural network) and with the use of libraries like pytorch and pennylane, implemented them in Jupyter notebook. The codes for QNN, non linear CNN and RNN are submitted in QML paper implementation folder in this week. The accuracies of the models can be seen. The accuracy of the QNN and CNN model is comparable.
 
6. QC evaluation: This folder contains the complete solutions of the QC problems we were given to solve.
 
7. QML evaluation: This folder contains the solutions to the QML problems we were given to solve. The solution to the second problem contains 3 ipynb files in each file, a hyperparameter is varied.

Week 1:

Summary

Chapter 1:
I first started with the introduction of a qubit. Qubit was introduced a s a vector in 2 D vector space.
Qubits can be considered analogous to various other systems such as polarisation of photon, 2
energy states of an electron, alignment of nuclear spin in a uniron magnetic field etc.
Then, I moved on to general bra-kept notation of a qubit and studied about its Bloch sphere
representation, Bloch vectors. The general principle of quantum mechanism was reiterated that the
global phase of the qubit has no physical observable outcomes hence could be neglected in the
Bloch sphere representation.
Then, intrigued by idea like superposition,amplitude,phases of qubits and their similarity with the
behaviour of photons, I searched and read more about their analogy, how photons behave and thus
gained more insight and ‘feel’ of qubits. Then , I moved on to read about superposition of qubits
starting with 2 qubits. I studied about their normalisation, measurement, 2 state basis etc and also
the very important 2 qubit entangled states ‘bell states’ which are a key ingredient in quantum
teleportation and super dense coding. Then , I encountered the multiple qubit states, read about
Hilbert spaces, tensor products and a detailed comparison between quantum and classical
computers. Then , came the very important result and its proof that was given as an exercise that ‘an
operator(alias matrix) preserves length iff it is unitary’ and thus as all unitary matrixes are invertible
also and hence the only condition on quantum gates it that they should be unitary operators. After
that, I studied about the various 2 qubit gates Pauli gates and h and I tried to comprehend them as
rotation about axes on the Bloch sphere which was given as an additional note there After that , I
moved on to study about 2 qubit gates from a single qubit gates starting with the C Note gate.
Then, came the no cloning theorem and general qc circuit symbols.
After this, I studied about the first proper qc algorithm ‘quantum teleportation’ which was an
exciting experience As all classical circuits can be represented by the use of NAND gates only and qc
ha the analogous Toffoli gates therefore with the use of ‘ancilla bits’ it was possible to simulate any
classical circuit as quantum circuit.
The next and final highlight of chapter was quantum parallelism and the Deutch-Jozha algorithm
Chapter 2:
Chapter 2 focussed on learning about the mathematical formulations and revisiting linear algebra
topics. General notations were revised, preliminaries were discussed. Then I learnt about Pauli
matrices, inner products, outer products, bra-Ket notation and the very important completeness
relation, its application, Cauchy Schwartz inequality, diagonal representation of matrices, adjoints,
Hermitian products, projectors . After that, came the very important ‘spectral decomposition
theorem’ which is heavily used in quantum circuit formulations, tensor products, Kronecker
products, positive operator, positive operator etc.
Then, we studied about the postulates of quantum mechanics and again came back to discussing
linear algebra, Hermitian matrices, trace as inner products, Hilbert space , Hilbert-Schmidt inner
product operation, Commutator,Anti-Commutator,simuatanous diagonalisation theorem, single
value decomposition did polar decompositions

Week 2

Summary

In this week, we studied about quantum circuits in detail and also implemented some of the
algorithms on qiskit. This weel was application intensive.
We started by revisiting single qubit operations and Bloch sphere representation of matrices. Then, I
studied about rotation matrices that were obtained by exponentiating Pauli matrices This chapter
was supplemented by a lot of computation intensive and non trivial problems and I found some of
them quite challenging Then came the important result that any Hermitian matrix can be
represented as a product of global phase and rotation matrices. Also, another general
representation of any matrix as rotation about a particular axis n cap by angle that was studied.
Then I personally studied about various properties of a unitary matrix, how each can be represented
as e exponentiated to a Hermitian matrix etc. Then another representation was introduced in which
any unitary matrix can be presented as a products of global space, X gates and single qubit gates,
Thus any quantum gate could be broken down to a product of a global phase and single qubit gates
Then, I solved all of the problems which aimed to represent / decompose Hadamard gate to each of
these decompositions.

Then, controlled qubit operations were reintroduced. Density operator was introduced in a problem
and thus I studied about density operator and their propertied for both pure and mixed states.
Then using the above decomposition theorems, we studied about a lot of circuits involving them.
After that , I studied about the two important principles of measurements and another prototype for
the teleportation circuit which I also implemented in qiskit.
After this I studied about how every unitary matrix can be decomposed and implemented with the
help of only CNOT, phase and Hadamard gate to an arbitrary accuracy.
This was followed by implementation exercises in qiskit. I installed the prerequisites from their
official site and learnt the basic syntax of qiskit by reading all of the pages on it till Section 3.
Thereafter, I implemented all of the mandatory problems and displayed their Bloch spheres, state
vectors, quantum circuits etc for seeing the output and for verification.

Week 3
In this week, we studied about quantum Fourier transform. Discrete Fourier
transform takes an input of a vector of complex numbers and outputs the
transformed data. Quantum Fourier transform is exactly the same
transformation just the conventional notation for the quantum Fourier
transform is different. The quantum Fourier transform transforms an
orthonormal basis and is defined to be a linear operator acting on the basis
states. This transformation is a unitary transformation and thus can be
implemented as the dynamics of a quantum computer. Later, we described a
quantum circuit for applying the Fourier transform on qubits. After this, we
formed a circuit for quantum phase estimation. Given a unitary operator U
with an eigenvector and its given eigenvalue. The goal of quantum phase
estimation is to estimate phi. The phase estimation algorithm is not a complete
algorithm as it requires the use of black boxes. Later we formed a circuit for
quantum phase estimation.

After this, we studied about the famous quantum search Grover’s algorithm
which enables the search method to speed up exponentially. In that, an oracle
was assumed which gave the value 1 if the input was a solution to a quantum
search algorithm and the output was 0 if the solution was not a solution to the
algorithm. Thus, the oracle is a unitary operator. The quantum search
algorithm consists of repeated application of a quantum subroutine known as
Grover iteration or Grover operator. Later, we studied how the Grover circuit is
applied and how its performance is evaluated.

WEEK 4
This week we studied about machine learning . Firstly, we studied about linear
regression. Linear regression is used to predict the values of independent
variable based on dependent variables. Then we studied about logistic
regression. Logistic regression is used to predict the values of dependent
variable based on independent variable when the dependent variable can only
tale discrete values unlike in linear regression where the dependent variable
has a continuous distribution. Then we studied about K-means clustering which
is an example of unsupervised learning that aims to partition n observations
into k clusters. After this, we studied about kernels and its properties and also
support vector machines. Lastly, we studied about neural networks which
consist of an interconnected group of nodes and convolutional neural
networks which consist of convolutional layer to extract abstract features.
We studied about all these topics and implemented them in jupyter notebook
using libraries like NumPy, pandas, scikit, TensorFlow and keras

Week 5
In this week, I studied the research paper about Quanvolutioal Neural
Networks and implemented them on Jupyter notebook. Quanvolutioal Neural
Networks power image recognition with quantum circuits. CNNs have become
widely popular for image recognition due to their ability to extract features
from data in a hierarchical manner. These features are extracted using various
transformational layers most importantly the convolutional layers. In QNN, a
new type of transformational layer Quantum Convolution or Quanvolutioal
layer is introduced which operate on input data by locally transforming the
data using a number of random quantum circuits. This algorithm requires small
quantum circuits with little to no error correction.
The benefit of quanvolutioal layers was evaluated by comparing three kinds of
models built on the famous MNIST dataset QNN, CNN and Random NN. I
implemented all of the three models and QNN clearly had an advantage over
CNN and Random NN.
