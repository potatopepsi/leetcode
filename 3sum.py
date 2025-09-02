#Looked at a solution for help

def threeSum(nums):
    
    numsLength = len(nums)
    output = []
    nums.sort()

    for i in range(numsLength-2):
        if(i > 0 and nums[i]==nums[i-1]):
            continue
        if nums[i] > 0:
            break
        j = i + 1
        k = numsLength - 1
        while(j<k):
            total = nums[i] + nums[j] + nums[k]
            if(total == 0):

                output.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while(nums[j]==nums[j-1] and j<k):
                    j = j + 1
                while(nums[k]==nums[k+1] and j<k):
                    k = k - 1
            elif(total < 0):
                j += 1
            else:
                k -= 1
            
    return output