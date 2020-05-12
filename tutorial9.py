

def multInt (a, b):
    return  a * b
    
def recurseMult(a,b):
    if b == 1:
        return a
    else:
        return a + recurseMult(a,b-1)

def translate (string, morse, index):
    if index == len(string):
        return ''
    if string[index] != ' ':
       return morse[string[index]] + ' '  + translate(string,morse,index + 1)
        #morseString +=  morse[string[index]] 
        #return translate(string,morse,index + 1,morseString)
    else:
        return ' ' + translate (string, morse, index + 1)
   
    
def addList (nums, index):
    if index == len(nums):
        return 0
    else:
        return nums[index] + addList(nums, index + 1)
def addList2 (nums, index, even, odd, zeroes):
    if index == len(nums):
        return 0
    if nums[index] == 0:
        return addList2(nums,index + 1,even, odd,zeroes + 1)
    elif nums[index] % 2 == 0:
        return addList2(nums,index + 1,even +nums[index], odd,zeroes)
    else:
        return addList2(nums,index + 1,even, odd +nums[index],zeroes)
def minMax (myList, min,max, index):
    if index == len(myList):
        return max, min
    if min > myList[index]:
        return minMax(myList, myList[index], max, index + 1) 
    elif max < myList[index]:
        return minMax(myList, min, myList[index], index + 1) 
    else:
        return minMax(myList, min, max, index+1) 
#leaving out last q

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}
#string = "HI"
#print(translate(string,MORSE_CODE_DICT,0))
myList = [1,2,3,4,5,6]
min1 = 0
max1 = 0
index = 0
max1, min1 = minMax(myList, min1,max1, index)

#print (min1, max1)
#print (addList(myList,0))