def lengthOfLongestSubstring(s: str) -> int:

    s_length = len(s)

    if(s_length <= 1):
        return s_length
    elif(s_length==2):
        if(s[0]!=s[1]):
            return 2
        else:
            return 1

    counter = 1
    longest = 0
    
    i = 0
    j = 1

    while(i < s_length and j < s_length):
        if(s[i:j+1].count(s[j])==1):
            counter+=1
            j = j + 1
        else:
            if(counter > longest):
                longest = counter
            counter = 1
            i = i + 1
            j = i + 1
    if(counter > longest):
        longest = counter
    return longest

def main():
     
     #Example Test Case 1
     s = "abcabcbb"
     print(lengthOfLongestSubstring(s))

    #Example Test Case 2
     s="bbbbb"
     print(lengthOfLongestSubstring(s))

    #Example Test Case 3
     s="pwwkew"
     print(lengthOfLongestSubstring(s))

if __name__=="__main__":
     main()
