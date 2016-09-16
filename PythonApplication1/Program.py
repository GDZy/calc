import Stack

#ar = input("enter an arithmetic expression: ")

expr = '2*4+3'
print (expr)


# breaking Tokens
# заменить списки на кортежи, для экономии места в памяти
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

def Calc(y, x, funct):
    functDict = {
        '+': x+y,
        '-': x-y,
        '*': x*y,
        '/': x/y,
        '^': x^y,        
        }    
    return functDict[funct]


# создание стеков для операндов и операторов 
opSt = Stack.Stack()
functSt = Stack.Stack()

priorDict = {'+':3, '-':3, '*':2, '/':2, '^':1}
for item in listExp:                  
    try:        
        opSt.push(float(item))
    except:
        # работа с операторами
        # возможно нужны исключения      
        while functSt.isEmpty() == False and priorDict[item] >= priorDict[functSt.last()]:
            a = opSt.pop()
            b = opSt.pop()
            funct = functSt.pop()
            rez = Calc(a, b, funct)
            opSt.push(rez)
            break 
        functSt.push(item)

# блок отладки
print (opSt.items)
print (functSt.items)
   
    
print ('=== the end ===')