def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    ransomLength = len(ransomNote)
    
    for i in range(ransomLength):

        if(magazine.count(ransomNote[i])!=0):
            place = magazine.find(ransomNote[i])
            magazine = magazine[:place] + magazine[place+1:]
        else:
            return False
    return True
