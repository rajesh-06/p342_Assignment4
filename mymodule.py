#Creating a zero matrix of order m*n
def zeromatrix(m,n):
	p= [[0 for i in range(n)] for j in range(m)]
	return(p)
	
#Creating a identity matrix of m*m
def identity_mat(m):
	p=zeromatrix(m,m)
	for i in range(m):
		p[i][i] = 1
	return(p)
	
def mat_vec_mult(A,B):
	n=len(B)
	if len(A[0])==n:
		p=[0 for i in range(n)]
		for i in range(n):
			for j in range(n):
				p[i] = p[i] + (A[i][j] * B[j])
		return(p)	
	else: 
		print('This combination is not suitable for multiplication')

	
#matrix multiplication				
def mat_mult(a,b):
	if len(a[0])==len(b):
		p=zeromatrix(len(a),len(b[0]))
		for i in range(len(a)):
			for j in range(len(b[0])):
				for x in range(len(b)):
					p[i][j]+=(a[i][x]*b[x][j])
		return(p)
	else:
		print('The matrix combination is not suitable for multiplication')
		
		
#Partial pivoting
def par_pivot(A,B):
	n=len(A)
	for r in range(n):
		if A[r][r]==0:
			for r1 in range(r+1,n):
				if abs(A[r1][r])>A[r][r] and A[r][r]==0:
					(A[r],A[r1])=(A[r1],A[r])
					(B[r],B[r1])=(B[r1],B[r])
				else:
					continue
			else:
				continue
				
#Gauss-Jordan elimination				
def gauss(A,B):
	m=len(A)
	n=len(A[0])
	for r in range(m):
		par_pivot(A,B)
		pivot=A[r][r]
		for c in range(r,n):
			A[r][c]=A[r][c]/pivot
		B[r]=B[r]/pivot
		for r1 in range(m):
			if r1==r or A[r1][r]==0:
				continue
			else:
				factor=A[r1][r]
				for c in range(r,n):
					A[r1][c]=A[r1][c]-A[r][c]*factor
				B[r1]=B[r1]-B[r]*factor
				
				
#LU decomposition of a matrix
def lu_decompose(A,B):
	par_pivot(A,B)
	n=len(A)
	#To store in one matrix both L and U in matrix a
	try:
		import copy
		a=copy.deepcopy(A)
		for j in range(n):
			for i in range(n):
				factor=0
			
				#for U(upper A) matrix
				if i<=j:
					for k in range(i):
						factor+=a[i][k]*a[k][j]
					a[i][j]=A[i][j]-factor
				#for L(lower) matrix
				else:
					for k in range(j):
						factor+=a[i][k]*a[k][j]
					a[i][j]=1/a[j][j]*(A[i][j]-factor)
	except ZeroDivisionError:
			print('LU decomposition is not possible.')
					
	return(a,B)

#for LUx=B
def lux(a,B):
	n=len(B)
	det =1
	for i in range(n):
		det*=a[i][i]
	if len(a)==n and det !=0:
		print
		y=[0 for i in range(4)] 
		x=[0 for i in range(4)]
		
		#forward substitution i.e., Ly=B
		for i in range(4):
			factor = 0
			for j in range(i):
				factor+=a[i][j]*y[j]
			y[i]=B[i]-factor
		#Backward substitution, i.e. Ux=y
		for i in range(3,-1,-1):
			factor=0
			for j in range(i+1,4,1):
				factor+=(a[i][j]*x[j])
			x[i]=1/a[i][i]*(y[i]-factor)
	return(x)
	
