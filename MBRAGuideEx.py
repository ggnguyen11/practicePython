# Testing MBRA Guide example from coursework
import numpy as np
import numpy.linalg as npla
import networkx as nx

print("MBRA Guide example");
C = np.array([[0,1,1,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,0],[1,0,0,0,0,0,0,1,0],[0,1,0,0,1,0,0,0,0],
[0,0,0,1,0,1,0,0,0],[0,0,0,0,1,0,1,0,0],[0,0,0,0,0,1,0,1,1],[0,0,1,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,0]])
print()
print(C)
One = C[0,:]
Two = C[1,:]
Three = C[2,:]
Four = C[3,:]
Five = C[4,:]
Six = C[5,:]
Seven = C[6,:]
Eight = C[7,:]
Nine = C[8,:]
print()
OneDegree = One[0] + One[1] + One[2] + One[3] + One[4] + One[5] + One[6] + One[7] + One[8]
print("Degree of Min = ",OneDegree)
TwoDegree = Two[0] + Two[1] + Two[2] + Two[3] + Two[4] + Two[5] + Two[6] + Two[7] + Two[8]
print("Degree of StL = ",TwoDegree)
ThreeDegree = Three[0] + Three[1] + Three[2] + Three[3] + Three[4] + Three[5] + Three[6] + Three[7] + Three[8]
print("Degree of Chi = ",ThreeDegree)
FourDegree = Four[0] + Four[1] + Four[2] + Four[3] + Four[4] + Four[5] + Four[6] + Four[7] + Four[8]
print("Degree of Det = ",FourDegree)
FiveDegree = Five[0] + Five[1] + Five[2] + Five[3] + Five[4] + Five[5] + Five[6] + Five[7] + Five[8]
print("Degree of Cin = ",FiveDegree)
SixDegree = Six[0] + Six[1] + Six[2] + Six[3] + Six[4] + Six[5] + Six[6] + Six[7] + Six[8]
print("Degree of Was = ",SixDegree)
SevenDegree = Seven[0] + Seven[1] + Seven[2] + Seven[3] + Seven[4] + Seven[5] + Seven[6] + Seven[7] + Seven[8]
print("Degree of Was = ",SevenDegree)
EightDegree = Eight[0] + Eight[1] + Eight[2] + Eight[3] + Eight[4] + Eight[5] + Eight[6] + Eight[7] + Eight[8]
print("Degree of Was = ",EightDegree)
NineDegree = Nine[0] + Nine[1] + Nine[2] + Nine[3] + Nine[4] + Nine[5] + Nine[6] + Nine[7] + Nine[8]
print("Degree of Was = ",NineDegree)
NetworkDegree = max(OneDegree, TwoDegree, ThreeDegree, FourDegree, FiveDegree, SixDegree, SevenDegree, EightDegree, NineDegree)
print("Degree of Network = ",NetworkDegree)
print()
AverageDegreeNetwork = (OneDegree + TwoDegree + ThreeDegree + FourDegree + FiveDegree +
SixDegree + SevenDegree + EightDegree + NineDegree) / len(C)
print("Mean Degree of Network = ",AverageDegreeNetwork)
print()
eigenvalues, eigenvectors = npla.eig(C)
print()
print("Eigenvalues of connection matrix C=")
print(eigenvalues)
print()
print("Spectral radius of connection matrix C=")
spectralr = np.max(eigenvalues)
print(spectralr)
print()
print("Eigenvectors of connection matrix C=")
print(eigenvectors)
G = nx.convert_matrix.from_numpy_array(C, parallel_edges=False, create_using=None)
DC = nx.degree_centrality(G)
print()
print("Degree Centrality of connection matrix C=")
print(DC)
G = nx.convert_matrix.from_numpy_array(C, parallel_edges=False, create_using=None)
BC = nx.betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None)
print()
print("Betweenness Centrality of connection matrix C=")
print(BC)
print("-------------------------------------------------------")
G = nx.convert_matrix.from_numpy_array(C, parallel_edges=False, create_using=None)
EC = nx.eigenvector_centrality_numpy(G, weight=None, max_iter=50, tol=0)
print()
print("Eigenvector Centrality of connection matrix C=")
print(EC)