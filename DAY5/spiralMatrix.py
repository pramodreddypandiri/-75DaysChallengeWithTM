class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #time=O(M*N)
        #space=O(N) for output array
        output=[]
        left,right=0,len(matrix[0])
        top,bottom=0,len(matrix)
        while left<right and top< bottom:
            #print top row
            for i in range(left,right):
                output.append(matrix[top][i])
            top+=1
            #print right most col
            for i in range(top,bottom):
                output.append(matrix[i][right-1])
            right-=1
            #to overcome single row or single col matrix test cases
            if not (left<right and top< bottom):
                break
            #print bottom most row
            for i in range(right-1,left-1,-1):
                output.append(matrix[bottom-1][i])
            bottom-=1
            for i in range(bottom-1,top-1,-1):
                output.append(matrix[i][left])
            left=left+1
        return output    
                