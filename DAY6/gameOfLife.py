class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        matrix=[[0 for i in range(len(board[0]))] for i in range(len(board))]
        M=len(board)
        N=len(board[0])
        #live neighbours counting function
        def countNei(m,n):
            count=0
            for i in range(m-1,m+2):
                for j in range(n-1,n+2):
                    #if index is not in range or bound just skip
                    if ((i==m and j==n) or i<0 or j<0 or i==M or j==N ):
                        continue
                    if board[i][j]==1:
                        count+=1
            return count
        for i in range(M):
            for j in range(N):
                # for every cell count live neighbours
                liveNei=countNei(i,j)
                #check conditions based on given context
                if board[i][j]==1 and liveNei<2:
                    matrix[i][j]=0
                if board[i][j]==1 and (liveNei==2 or liveNei==3):
                    matrix[i][j]=1
                if board[i][j]==1 and liveNei>3:
                    matrix[i][j]==0
                if board[i][j]==0 and liveNei==3:
                    matrix[i][j]=1
                '''if board[i][j]:
                    if liveNei < 2:
                        matrix[i][j] = 0
                    elif liveNei > 3:
                        matrix[i][j] = 0
                else:
                    if liveNei == 3:
                        matrix[i][j] = 1'''
        #store matrix to board,because we do not have to return 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                board[i][j]=matrix[i][j]
                
                    
                        
                
        """
        Do not return anything, modify board in-place instead.
        """