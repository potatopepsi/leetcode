#Had to look at solution
def wordBreak(s, wordDict) -> bool:
    sLength = len(s)
    sTrack = [False] * (sLength + 1)
    sTrack[0] = True

    for i in range (1, sLength + 1):
        for j in range(i):
            if sTrack[j] and s[j:i] in wordDict:
                sTrack[i] = True
                break

    return sTrack[-1]

    # pointer = 1
    # sCopy = s
    # x = True
    # sLength = len(s)

    # while(x):
    #     if(wordDict.count(s[:pointer]) > 0):
    #         s=s[pointer:]
    #         pointer = 1
    #         if(wordDict.count(s) > 0):
    #             return True
    #     else:
    #         pointer = pointer+1

    #     if(pointer>sLength):
    #         x = False

    # if(s==""):
    #     return True
    # elif(len(wordDict)!=0):
    #     return self.wordBreak(sCopy, wordDict[1:])
    # else:
    #     return False

def main():
    #Test Case 1
    print("Test Case 1")
    #Test Case 2
    print("Test Case 2")
    #Test Case 3
    print("Test Case 3")

    

if __name__ == "__main__":
    main()