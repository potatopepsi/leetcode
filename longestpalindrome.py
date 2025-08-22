def isPalindrome(input: str) -> bool:
    input_length = len(input)

    if(input_length==2):
        if(input[0]==input[1]):
            return True
        else:
            return False

    half = input_length // 2

    if(input_length%2==1):
        first_half = input[0:half]
        second_half = input[half+1:]
    else:
        first_half = input[0:half]
        second_half = input[half:]     

    second_half = second_half[::-1]

    if(first_half==second_half):
        return True
    else:
        return False

    
def longestPalindrome(s: str) -> str:
    
    
    s_length = len(s)
    i = 0
    j = 1
    longest = ""
    while(i < s_length):
        if(len(longest)>len(s[i:])):
            break
        if(j>s_length):
            i += 1
            j = i+1
        else:
            if(isPalindrome(s[i:j])):
                if(len(s[i:j])>len(longest)):
                    longest = s[i:j]
            j += 1
    return longest

def main():

    #Example Test Case 1
     s = "babad"
     print(longestPalindrome(s))

    #Example Test Case 2
     s="cbbd"
     print(longestPalindrome(s))

if __name__ == "__main__":
    main()