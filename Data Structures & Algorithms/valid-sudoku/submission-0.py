class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            rowArray=(self.traverseRow(board,i))
            if len(rowArray)!= len(set(rowArray)):
                return False
            colArray=(self.traverseColumn(board,i))
            if len(colArray) != len(set(colArray)):
                return False
            gridArray=(self.traverseGrid(board,i))
            if (len(gridArray) != len(set(gridArray))):
                return False
                
        return True
        
    def traverseRow(self,board:List[List[str]],row:int):
        rowList=[]
        for cell in board[row]:
            if cell !=".":
                rowList.append(cell)
        return rowList
    
    def traverseColumn(self,board:List[List[str]],col:int):
        colList=[]
        for row in range(0,len(board)):
            if board[row][col] !=".":
                colList.append(board[row][col])
        return colList

    def traverseGrid(self,board:List[List[str]],index:int):
        gridList=[]
        subGridStart = ((index//3)*3,(index%3)*3)
        subGridEnd = ((index//3)*3+2,(index%3)*3+2)
        for i in range(subGridStart[0],subGridEnd[0]+1):
            for j in range(subGridStart[1],subGridEnd[1]+1):
                if board[i][j]!=".":
                    gridList.append(board[i][j])
        return gridList