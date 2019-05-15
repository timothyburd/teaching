import numpy as np
np.set_printoptions(precision=3)
A = np.array([[1,0,1,0,0,-3,0],[1,0,0,-1,0,0,0],[0,35,4,-4,0,-12,-1],[0,2,0,0,-1,0,0],[0,10,0,0,0,-1,0],[0,0,2,-1,-3,0,-2]], dtype=float)



print("************")
print("Initial setup, in order of S, Mn, O, As, Cr, H")
print("************")
print(A)
print("************")

B = A.copy()
B[1,:] -= B[0,:]
B[2,:] = 2*B[2,:]-35*B[3,:]
B[4,:] = B[4,:] - 5*B[3,:]
print("************")
print("Eliminate C1 using R1, C2 using R4")
print("************")
print(B)
print("************")

C = B.copy()
C[1,:] = 0.5*B[3,:]
C[2,:] = 1.0*B[1,:]
C[3,:] = 1.0*B[2,:]
C[4,:] = 1.0*B[5,:]
C[5,:] = 1.0*B[4,:]
print("************")
print("Swap rows (and halve R2)")
print("************")
print(C)
C[0,:] = C[0,:] + C[2,:]
C[3,:] = C[3,:] + 8*C[2,:]
C[4,:] = C[4,:] + 2*C[2,:]
C[2,:] = -1*C[2,:]
print("************")
print("Eliminate C3 using R3")
print("************")
print(C)
print("************")

D = C.copy()
D[0,:] = D[0,:]-D[4,:]/3
D[2,:] = D[2,:]+D[4,:]/3
D[3,:] = D[3,:]-16*D[4,:]/3
D[4,:] = -D[4,:]/3
print("************")
print("Eliminate C4 using R5")
print("************")
print(D)
print("************")

E = D.copy()
E[0,:] = E[0,:] - 1*E[5,:]/5
E[1,:] = E[1,:] + 1*E[5,:]/10
E[2,:] = E[2,:] + 1*E[5,:]/5
E[3,:] = E[3,:] - 51*E[5,:]/5
E[4,:] = E[4,:] - 1*E[5,:]/5
E[5,:] = 1*E[5,:]/5
print("************")
print("Eliminate C5 using R6")
print("************")
print(E)
print("************")

F = E.copy()
F[3,:] = 1.0*E[4,:]
F[4,:] = 1.0*E[5,:]
F[5,:] = 1.0*E[3,:]
print("************")
print("Permutate rows")
print("************")
print(E)

F[0,:] = F[0,:] - 1.8*F[5,:]/21.8
F[1,:] = F[1,:] - 0.1*F[5,:]/21.8
F[2,:] = F[2,:] - 1.2*F[5,:]/21.8
F[3,:] = F[3,:] - 1.8*F[5,:]/21.8
F[4,:] = F[4,:] - 0.2*F[5,:]/21.8
F[5,:] = -1.0*F[5,:]/21.8
print("************")
print("Eliminate C6 using R6")
print("************")
print(F)
print("************ (same but multiplied by 327)")
print(327*F)


