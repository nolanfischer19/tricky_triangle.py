#This will check for the move made by the player 
class gameengine2:
    def __init__(self):
        #This is the cordiante system of the board. Use the picture in group me to get a better grasp
        # 1 means there is peg in it. 0 means no peg. Intially there should be 14 pegs and one 0 as shown
        self.board=[[0],[1,1],[1,1,1],[1,1,1,1],[1,1,1,1,1]]



    def checkvalidmove1(self,y1,x1,y2,x2,y3,x3):
        #All the possible moves.Each move needs six cordinate postion. The order is important
        #since each peg has different possible moves. The six cordinate postion corrospond left to right intial postion of peg, the peg to pass over and finally the place to point the peg.
        self.validmoves=[[0,0,1,1,2,2],[0,0,1,0,2,0],[1,0,2,0,3,0],[1,0,2,1,3,2],[1,1,2,2,3,3],[1,1,2,1,3,1],[2,0,3,0,4,0],[2,0,3,1,4,2],[2,0,1,0,0,0],[2,0,2,1,2,2],[2,1,3,1,4,1],[2,1,3,2,4,3],[2,2,3,2,4,2],[2,2,3,3,4,4],[2,2,1,1,0,0],[2,2,2,1,2,0],[3,0,2,0,1,0],[3,0,3,1,3,2],[3,1,2,1,1,1],[3,1,3,2,3,3],[3,2,2,1,1,0],[3,2,3,1,3,0],[3,3,2,2,1,1],[3,3,3,2,3,1],[4,0,3,0,2,0],[4,0,4,1,4,2],[4,1,3,1,2,1],[4,1,4,2,4,3],[4,2,4,1,4,0],[4,2,3,1,2,0],[4,2,3,2,2,2],[4,2,4,3,4,4],[4,3,3,2,2,1],[4,3,4,2,4,1],[4,4,3,3,2,2],[4,4,4,3,4,2]] 
        self.playervalues=[y1,x1,y2,x2,y3,x3]
        #Matches the cordinate for the player's chosen cordinate with all the possible moves.
        for k in range(0,len(self.validmoves)):
            if (self.playervalues==self.validmoves[k]):
             print("Finally Something")
             #the nestled if statement adjust the peg in each cordinate.
             if self.board[y1][x1]==1 and self.board[y2][x2]==1 and self.board[y3][x3]==0:
                self.board[y1][x1]=0
                self.board[y2][x2]=0
                self.board[y3][x3]=1
                print(self.board[y3][x3])
             else:
                 print("Wrong Points Chosen please try again")
        return False
                
          
             
p=gameengine2()
print(p.checkvalidmove1(2,0,1,0,0,0))
