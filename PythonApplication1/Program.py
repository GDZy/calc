import Stack

#expr = input("Введите арифметическое выражение для вычисления используя операторы: +, -, *, /, ^ и нажмите enter: " '\n')

expr = 'a2*4+ 3 / 2 - 4 ^ 2 ='
print (expr)

priorDict = {'+':3, '-':3, '*':2, '/':2, '^':1}
# breaking Tokens
# заменить списки на кортежи, для экономии места в памяти
def BreakTokens(expr):
    startSlice = 0
    count = 0    
    listExp = []
    for i in expr:
        if i in priorDict:
            listExp.append(expr[startSlice:count])
            listExp.append(i)                                  
            startSlice = count + 1                
        count = count + 1
    listExp.append(expr[startSlice: len(expr)])                              
    return listExp

def CheckNumb(list):
    for item in list:
        if (not float(item) and item in priorDict):
            print ("Неккоректный ввод:", item)
            return False
    return True    

def Calc(y, x, funct):
    functDict = {
        '+': x+y,
        '-': x-y,
        '*': x*y,
        '/': x/y,
        '^': x**y        
        }    
    return functDict[funct]

listExp = BreakTokens(expr)
print(listExp)

if not CheckNumb(listExp):
    print ("введите корректное выражение: " '\n')
    break



# создание стеков для операндов и операторов 
opSt = Stack.Stack()
functSt = Stack.Stack()


for item in listExp:                  
    try:        
        opSt.push(float(item))            
    except:
        # работа с операторами
        # возможно нужны исключения      
        while functSt.isNotEmpty() and priorDict[item] >= priorDict[functSt.last()]:
            rez = Calc(opSt.pop(), opSt.pop(), functSt.pop())
            opSt.push(rez)
        functSt.push(item)

print (opSt.items)
print (functSt.items) 

# вычисление оставшихся элементов стека
while functSt.isNotEmpty():
    rez = Calc(opSt.pop(), opSt.pop(), functSt.pop())
    opSt.push(rez)
    

# блок отладки
print (opSt.items)
print (functSt.items) 
    
print ('=== the end ===')