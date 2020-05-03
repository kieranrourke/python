def checkList (list):
	## This was before I realized u could do j in range of i or list[i]
	tempList = []
	i = 1
	j = 0
	k = 0
	count = len(list[0])
	for l in list    
		tempCount = 0
		for j in l:
			tempCount += 1	
		if tempCount != count:
			return False	
	return True		

def isNumeric (list):
	k = 1
	for i in range (len(list)):
		for j in range (len(list[i])):		
			check = isinstance (list[i][j], (int,float))
			if check == False:
				return False
	return True

def isMatrix (list):
	checkMatrix = checkList(list)
	checkNums = isNumeric(list)
	if checkMatrix == False | checkNums == False:
		return False
	else:
		return True

def printMatrix (list):
	isMatrix(list)
	for i in range(len(list)):
		for j in range(len(list[i])):
			try:
				print(list[i][j], end = '')	
			except:
				print("error")
		print ("")


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
	cols1 = 0
	cols2 = 0 
	rows1 = 0
	rows2 = 0

	cols1 = len(matrix1[0])
	rows1 = len(matrix1)
	cols2 = len(matrix2[0])
	rows2 = len(matrix2)
	
	
	if cols1 == cols2 and rows1 == rows2 :
		return True
	else:
		return False	




myList = [[1,2], [2,3], [4,5]]
myList2 = [[1,2], [2,3], [4,6,7]]
matrix = identityMatrix(8)
printMatrix(matrix)
print(sameSize(myList, myList2))