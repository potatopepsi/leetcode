
def letterCombinations(digits):

    # Commented code works but isn't great, learned from VanAmsen's solution that uses recursion
    
    output = []

    if not digits:
        return output
    
    keypad = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    def recursiveCombo(str, remainingDigits):

        # Base Case
        if len(remainingDigits) == 0:
            output.append(str)
        else:
            for i in keypad[remainingDigits[0]]:
                recursiveCombo(str + i, remainingDigits[1:])


    recursiveCombo("", digits)
    return output




    
    # # Initializing length of digits andd output array
    # digitsLength = len(digits)
    # output = []

    # # Edge Case
    # if(digitsLength == 0):
    #     return output
    
    # # Initializing the keypad in an array
    # letters = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

    # if(digitsLength == 1):
    # # One Digit
    #     first = int(digits[0])
    #     for i in range(len(letters[first])):
    #         temp = letters[first][i]
    #         output.append(temp)
    # elif(digitsLength == 2):
    # # Two Digits
    #     first = int(digits[0])
    #     second = int(digits[1])
    #     for i in range(len(letters[first])):
    #         for j in range(len(letters[second])):
    #             temp = letters[first][i]
    #             temp = temp + letters[second][j]
    #             output.append(temp)
    # elif(digitsLength == 3):
    # # Three Digits
    #     first = int(digits[0])
    #     second = int(digits[1])
    #     third = int(digits[2])
    #     for i in range(len(letters[first])):
    #         for j in range(len(letters[second])):
    #             for k in range(len(letters[third])):
    #                 temp = letters[first][i]
    #                 temp = temp + letters[second][j]
    #                 temp = temp + letters[third][k]
    #                 output.append(temp)
    # else:
    # # Four Digits
    #     first = int(digits[0])
    #     second = int(digits[1])
    #     third = int(digits[2])
    #     fourth = int(digits[3])
    #     for i in range(len(letters[first])):
    #         for j in range(len(letters[second])):
    #             for k in range(len(letters[third])):
    #                 for l in range(len(letters[fourth])):
    #                     temp = letters[first][i]
    #                     temp = temp + letters[second][j]
    #                     temp = temp + letters[third][k]
    #                     temp = temp + letters[fourth][l]
    #                     output.append(temp)
    

            
    # return output

    
    
    
    

    