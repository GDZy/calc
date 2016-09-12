

#ar = input("enter an arithmetic expression: ")

expr = '7+5.2*4+2'
print (expr)

listExp = []


def BreakTokens(expr):
    startSlice = 0
    count = 0    

    def AddToken(start, end, char):
        listExp.append(expr[start : end])
        listExp.append(char)

   # def AddToken(start, end):
   #     listExp.append(expr[start : end])
        

    for i in expr:
        if i == '+' or i == '*':
            AddToken(startSlice, count, i)                        
            startSlice = count + 1                
        count = count + 1
    AddToken(startSlice, len(expr)-1)                        

    print(listExp)  
    return True

BreakTokens(expr)

def Calc(startInd, endInd):

    return True

stExpr = 0;
endExpr = len(listExp)

rez = Calc(startExpr, endExpr) 



print ('=== the end ===')