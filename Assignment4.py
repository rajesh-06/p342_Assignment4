#Solution for Q1
#importing matrix from txt file
print('Solution for Q1:')
with open('Q1_A.txt', 'r') as f:
    A = [[float(num) for num in line.split(',')] for line in f]
    
#printing matrix A
print('A =')
for i in A:
	print(i)
print('')

#importing B matrix
with open('Q1_B.txt', 'r') as f:
	for line in f:
		B=[float(num) for num in line.split(',')]
print('B =')
print(B)
print('')

#importing my personal module as mm
import mymodule as mm	

#LU decomposition of matrix A and storing both L and U matrix in matrix lu
lu,B=mm.lu_decompose(A,B)

#Solution matrix 
#forward and backward solve of LUx = B
x=mm.lux(lu,B)
print('x =\n',x)
print('')

#multiplying A and x to verify it is B
Ax=mm.mat_vec_mult(A,x)

print('A*x =\n',Ax)
print('')


#-------------------------------
#solution for Q2:
print('Solution for question 2:')

#importing matrix A
with open('Q2_A.txt', 'r') as f:
    A1 = [[float(num) for num in line.split(',')] for line in f]
    
#printing matrix A
print('A =')
for i in A1:
	print(i)
print('')

#storing matrix A as after pivoting it will change
import copy 
a= copy.deepcopy(A1)

#defining identity matrix
I=mm.identity_mat(4)

#partial pivoting as to make every diagonal element non zero
#LU decomposition of matrix A
lu,I=mm.lu_decompose(A1,I)


#creating zero matrix to assign it to inverse of A
x1=mm.zeromatrix(4,4)
x2=mm.zeromatrix(4,4)

#finding solution for each column of iden
for i in range(4):
	x1[i]=mm.lux(lu,I[i])
	
#As x1 is the transpose of inverse(A), we have to transpose it again
for i in range(4):
	for j in range(4):
		x2[i][j]=round(x1[j][i],5)

print('A^(-1)= ')
for i in x2:
	print(i)
print('')



x1=mm.mat_mult(a,x2)
# to round of upto 3 digit decimal
for j in range(4):
	for k in range(4):
		I[j][k]=round(x1[j][k],1)

print('A*A^(-1) =')
for i in I:
	print(i)
print('')

'''Output of file
Solution for Q1:
A =
[1.0, 0.0, 1.0, 2.0]
[0.0, 1.0, -2.0, 0.0]
[1.0, 2.0, -1.0, 0.0]
[2.0, 1.0, 3.0, -2.0]

B =
[6.0, -3.0, -2.0, 0.0]

x =
 [1.0, -1.0, 1.0, 2.0]

A*x =
 [6.0, -3.0, -2.0, 0.0]

Solution for question 2:
A =
[0.0, 2.0, 8.0, 6.0]
[0.0, 0.0, 1.0, 2.0]
[0.0, 1.0, 0.0, 1.0]
[3.0, 7.0, 1.0, 0.0]

A^(-1)=
[-0.25, 1.66667, -1.83333, 0.33333]
[0.08333, -0.66667, 0.83333, 0.0]
[0.16667, -0.33333, -0.33333, 0.0]
[-0.08333, 0.66667, 0.16667, -0.0]

A*A^(-1) =
[1.0, 0.0, 0.0, 0.0]
[0.0, 1.0, 0.0, 0.0]
[0.0, 0.0, 1.0, 0.0]
[-0.0, -0.0, -0.0, 1.0]


[Program finished]'''
