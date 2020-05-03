def checkList (list):
	## This was before I realized u could do j in range of i or list[i]
	count = len(list[0])
	for l in list:    
		if len(l) != count:
			return False	
	return True		

def isNumeric (list):
	for i in range (len(list)):
		for j in range (len(list[i])):		
			check = isinstance (list[i][j], (int,float))
			if check == False:
				return False
	return True

def isMatrix (list):
	return(checkList(list)) and isNumeric(list)

def printMatrix(list):
	if(isMatrix(list)):
		for row in list:
			print("| ", end = '')
			for value in row:
				print(value, end=' ')
			print("|")
	else:
		print("error")

def createZeroMatrix (n):
	rows = []
	for i in range(n):
		columns = []
		for j in range(n):
			columns.append(0)
		rows.append(columns)
	return rows

def identityMatrix (n):
	matrix = createZeroMatrix(n)
	for i in range(n):
		for j in range(n):
			if j == i:
				matrix[i][j] = 1
	return matrix

def sameSize (matrix1, matrix2):
	if not isMatrix(matrix1) or not isMatrix(matrix2):
		return False

	cols1 = len(matrix1[0])
	rows1 = len(matrix1)
	cols2 = len(matrix2[0])
	rows2 = len(matrix2)
	
	return cols1 == cols2 and rows1 == rows2	




myList = [[1,2], [2,3], [4,5]]
myList2 = [[1,2], [2,3], [4,6,5]]
matrix = identityMatrix(8)
printMatrix(matrix)
print(isMatrix(myList2))
print(sameSize(myList, myList2))