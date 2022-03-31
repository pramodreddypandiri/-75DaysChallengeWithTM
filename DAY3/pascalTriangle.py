class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #time=O(N**2)
        #space=O(N**2)
        outPut=[[1]]
        #run outer for loop as no of rows rquired further after creating one
        for i in range(numRows-1):
            #create temp arr to build new row
            tempArr=[0]+outPut[i]+[0]
            #create an empty new row 
            newRow=[]
            #build new row accordingly
            for j in range(len(outPut[-1])+1):
                newRow.append((tempArr[j]+tempArr[j+1]))
            #after building new row add it to output
            outPut.append(newRow)
        return outPut
                              
        #diff ques 
        #time=O(N)-for calculating nCr
        #space=O(1)
        #1) return value at particular position- if asked pos(r,c) then ans=(r-1)C(c-1)
        #time=O(N)
        #space=O(N)
        #2) return nth row- calculate every position in row as done in above(#1) method
        
        
        