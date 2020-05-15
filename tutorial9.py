
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
def multInt (a, b):
    return  a * b

def recurseMult(a,b):
    if b == 1:
        return a
    else:
        return a + recurseMult(a,b-1)

def translate (string ):
    if string == '':
        return ''
    if string[0] != ' ':
       return MORSE_CODE_DICT[string[0]] + ' '  + translate(string[1::])
    else:
        return ' ' + translate (string [1::])


def addList (nums):
    if nums == []:
        return 0
    else:
        return nums.pop() + addList(nums)

def addList2 (nums, even, odd, zeroes):
    if nums == []:
        return even,odd, zeroes
    a = nums.pop()
    if a == 0:
        return addList2(nums, even, odd,zeroes + 1)
    elif a % 2 == 0:
        return addList2(nums, even + a, odd,zeroes)
    else:
        return addList2(nums, even, odd + a, zeroes)

def addlist3 (nums):
    return addList2(nums, 0, 0, 0)

def minMax (myList, min,max):
    if myList == []:
        return max, min
    a = myList.pop()
    if min > a:
        return minMax(myList, a, max)
    elif max < a:
        return minMax(myList, min, a )
    else:
        return minMax(myList, min, max)

def minMax1 (myList):
    return minMax(myList, myList[0], myList[0])
