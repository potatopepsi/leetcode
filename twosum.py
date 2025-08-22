#Grind75 - 1

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

        nums_length = len(nums)
        output = []

        temp_var = 0

        for i in range(nums_length):
            
            temp_var = target - nums[i]
            first = i
            try:
                second = nums.index(temp_var,i+1)
                break
            except ValueError:
                continue
        
        output.append(first)
        output.append(second)

        return output

def main():
     
     #Example Test Case 1
     nums  = [2,7,11,15]
     target = 9
     [x,y] = twoSum(nums,target)
     print(x)
     print(y)

    #Example Test Case 2
     nums = [3,2,4]
     target = 6
     [x,y] = twoSum(nums,target)
     print(x)
     print(y)

    #Example Test Case 3
     nums=[3,3]
     target = 6
     [x,y] = twoSum(nums,target)
     print(x)
     print(y)

if __name__=="__main__":
     main()