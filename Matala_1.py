################################ q1 ################################
def my_func(x1, x2, x3):
    try:
        if type(x1) != float or type(x2) != float or type(x3) != float:
            if type(x1) == str or type(x2) == str or type(x3) == str:
                return None
            else: return "Error: parameters should be float"
        a = x1+x2+x3
        b = (x2+x3)*x3
        sum = (a*b) / a
        return (sum)
    except ZeroDivisionError:
        return("Error:Not a number – denominator equals zero”")

my_func (3.0,3.9,1.0) ## for exsample

################################ q2 ################################

def revword(word:str) -> str:
    return word[::-1].lower()

def countword()->int: 
    PATH = "C:\\Users\\shirs\\Desktop\\shir saadi\\שנה ג סמסטר ב\\כרייה וניתוח נתונים מתקדם בפייתון\\מטלות\\מטלה 1\\text.txt"
    DATA = open(PATH,'r')
    for line in DATA:
        word = line.split()[0]
        DATA.seek(0)
        break
    lst = list() 
    for line in DATA:
        lst.extend(line.split())
    lst1=list()
    for i in range(1,len(lst)):
        lst1.append(revword(lst[i]))
    print(lst1)
    count=1
    for Word in lst1:
        if Word == str(word):
            count=count+1
    return (count)

num=countword() ## for exsample
print(num) 

