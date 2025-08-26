def myAtoi(self, s: str) -> int:
    s = s.strip()
    sLength = len(s)
    isNegative = None
    starting = 0
    end = sLength

    if(sLength==0):
        return 0

    if(s.isdigit()):
        if(int(s) < (-2**31)):
            return -1 * (2**31)
        elif(int(s) >= (2**31)):
            return (2**31) - 1
        else:
            return int(s)
        

    for i in range(sLength):
        if(s[i]=='-' and isNegative == None):
            isNegative = True
            if(sLength==1):
                return 0
        elif(s[i]=='+' and isNegative == None):
            isNegative = False
            if(sLength==1):
                return 0
        elif(s[i].isalpha()):
            return 0
        elif(s[i].isdigit()):
            beginning = i
            break
        else:
            return 0
        

    for j in range(i,sLength):
        if(s[j].isalpha() or s[j]=='-' or s[j]== " " or s[j]=="+"):
            end = j
            break
    
    output = float(s[beginning:end]) // 1
    output = int(output)
    
        
    
    # Negative number check
    if(isNegative):
        output= (-1) * output
    
    if(output < (-2**31)):
        return -1 * (2**31)
    elif(output > (2**31)):
        return (2**31) - 1
    else:
        return output

        
            
        


def main():
    s = "a"
    #Test Case 1
    print("Test Case 1")
    print(3.14)
    print(3.14//1)
    print(int(3.0))
    #Test Case 2
    print("Test Case 2")
    #Test Case 3
    print("Test Case 3")

    

if __name__ == "__main__":
    main()