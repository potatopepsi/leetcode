class Solution:
    def isValid(self, s: str) -> bool:

        sLength = len(s)

        # Edge Case
        if(sLength == 1):
            return False
        
        # Create a stack for keeping track of Parentheses
        pStack = []

        for i in range(sLength):
            match s[i]:
                case '(':
                    pStack.append(1)
                case '{':
                    pStack.append(2)
                case '[':
                    pStack.append(3)
                case ')':
                    try:
                        if(pStack.pop() !=1):
                            return False
                    except:
                        return False
                case '}':
                    try:
                        if(pStack.pop() != 2):
                            return False
                    except:
                        return False
                case ']':
                    try:
                        if(pStack.pop() != 3):
                            return False
                    except:
                        return False
        if(len(pStack) == 0):
            return True
        else:
            return False

        
        