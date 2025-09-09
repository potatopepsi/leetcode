
def evalRPN(tokens):
    
    # Initiazlizing length of tokens
    tempValue = 0
    i = 0

    while(len(tokens)!=1):
        if(i == len(tokens)):
            break
        match(tokens[i]):
            case '+':
                tempValue = int(tokens[i-2]) + int(tokens[i-1])
                tokens.pop(i-1)
                i = i - 1
                tokens.pop(i-1)
                i = i-1
                tokens[i] = str(tempValue)
            case '*':
                tempValue = int(tokens[i-2]) * int(tokens[i-1])
                tokens.pop(i-1)
                i = i - 1
                tokens.pop(i-1)
                i = i-1
                tokens[i] = str(tempValue)
            case '-':
                tempValue = int(tokens[i-2]) - int(tokens[i-1])
                tokens.pop(i-1)
                i = i - 1
                tokens.pop(i-1)
                i = i-1
                tokens[i] = str(tempValue)
            case '/':
                tempValue = int(tokens[i-2]) / int(tokens[i-1])
                if(tempValue < 0 and tempValue > -1):
                    tempValue = 0
                else:
                    tempValue = int(tempValue)
                tokens.pop(i-1)
                i = i - 1
                tokens.pop(i-1)
                i = i-1
                tokens[i] = str(tempValue)
            case _:
                i = i+1
            

    return int(tokens[0])
    

    