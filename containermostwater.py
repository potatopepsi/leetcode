def maxArea(height) -> int:
        heightLength = len(height)
        greatestArea = 0
        tempArea = 0

        i = 0
        j = heightLength-1


        while(i!=j):
            tempArea = ((j)-(i)) * min(height[j],height[i])
            if(tempArea > greatestArea):
                greatestArea = tempArea
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
def main():
    #Test Case 1
    print("Test Case 1")
    #Test Case 2
    print("Test Case 2")
    #Test Case 3
    print("Test Case 3")

    

if __name__ == "__main__":
    main()