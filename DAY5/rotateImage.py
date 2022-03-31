class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n//2+n%2):
            for j in range(n//2):
                #store element at left bottom corner
                temp=matrix[n-1-j][i]
                #put element at right bottom to left bottom corner
                matrix[n-1-j][i]=matrix[n-1-i][n-1-j]
                #put element at top right corner to right bottom corner
                matrix[n-1-i][n-1-j]=matrix[j][n-1-i]
                #put left top ele at right top corner
                matrix[j][n-1-i]=matrix[i][j]
                #put temp at left top corner
                matrix[i][j]=temp