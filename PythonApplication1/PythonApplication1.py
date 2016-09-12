

#ar = input("enter an arithmetic expression: ")

expr = '7+5*4'
print (expr)


# breaking Tokens
def BreakTokens(expr):
    startSlice = 0
    count = 0    
    listExp = []
    for i in expr:
        if i == '+' or i == '*':
            listExp.append(expr[startSlice:count])
            listExp.append(i)                                  
            startSlice = count + 1                
        count = count + 1
    listExp.append(expr[startSlice: len(expr)])                              
    return listExp

listExp = BreakTokens(expr)
print(listExp)

def Calc(startInd, endInd):
    for i in range(startInd, endInd+1):
        if listExp[i] == '+':
            rez = Calc(startInd, i-1) + Calc(i+1, endInd);
        elif listExp[i] == '*':
            rez = Calc(startInd, i-1) * Calc(i+1, endInd);
        
        if (endInd == startInd):
            rez = int(listExp[i])
            
    #print('calc')
    return rez

stExpr = 0;
endExpr = len(listExp)

rez = Calc(stExpr, endExpr) 



print ('=== the end ===')