#Not COMPLETELY WORKING CHECK LINE 30
#line 24,39,41,44,45,46 are for testing
#This is the class where the game will be tested
class gameengine:
    #All x,y,z and k,j,l are player inputs(I just put in random varibales for testing). We need two diiferent type of input
    # x,y,z would be cordinate system to check for all valid moves in the board
    # k,j,l will need to check for the actual peg or blank and adjust it likewise(All variable here will only have 1 or 0. 1 if there is peg and 0 if there is not)
    
    x=31
    y=21
    z=11
    k=1
    j=1
    l=0
    #The first method test out x,y,z inputs with all the possible moves in the board
    #It returns true if the move matches or False if the move does not match

    def checkvalidmove1(self,x,y,z):
        #All the possible moves
        self.validmoves=[[11,22,33],[11,21,31],[21,31,41],[21,32,43],[22,33,44],[22,32,42],[31,41,51],[31,42,53],[31,21,11],[31,32,33],[32,42,52],[32,43,54],[33,43,53],[33,44,55],[33,22,11],[33,32,31],[41,31,21],[41,42,43],[42,32,22],[42,43,44],[43,32,21],[43,42,41],[44,33,22],[44,43,42],[51,41,31],[51,52,53],[52,42,32],[52,53,54],[53,52,51],[53,42,31],[53,43,33],[53,54,55],[54,43,32],[54,53,52],[55,44,33],[55,54,53]] 
        self.playervalues=[x,y,z]
        for k in range(0,len(self.validmoves)):
            if (self.playervalues==self.validmoves[k]):
             print("Finally Something")
             return True
        return False
    #checkvalidmove2 works with k,j,l and is on condition that checkvalidmove1 is retirned True
    #If it is returned true and (k=1,j=1,l=0) then those values are altered for the new board
    #Next part is taking the new values for k,j,l and displaying it for the next round of player input
    # IMPORTANT note I STILL DID NOT FIGURE OUT HOW TO USE TRUE value from
    # checkvalidmove1 in checkvalidmove2 thus the second part gives out always false for the if statment
    #If you can fix that that would be really great
    def checkvalidmove2(self,k,j,l,):
        if(self.checkvalidmove1==True):
            if k==1 and j==1 and l==0:
                k==0
                j==0
                l==1
                print("All is okay")
                return True
        print("All is not okay")
        return False

p=gameengine()
p.checkvalidmove1(11,21,31)
p.checkvalidmove2(1,1,0)