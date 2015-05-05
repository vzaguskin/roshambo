from random import randint

from random import random
from bisect import bisect, bisect_left

def weighted_choice(values, weights):
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random() * total
    i = bisect_left(cum_weights, x)
    return values[i]

class treePredictor():
    def __init__(self):
        self.choices = ['R', 'P', 'S']
        self.prevchoice = None #computer move
        self.prevmove = None #my move
        self.prevres = None
        self.dataarr =[[0. for _ in range(3)] for _ in range(3)] #result, roll
        
        
        self.gameMat = []
        self.gameMat.append([1, 0, 2])
        self.gameMat.append([2, 1, 0])
        self.gameMat.append([0, 2, 1])
        self.beatMat=[1,2,0]
        
        self.rollMat = []
        self.rollMat.append([0, 1, 2])
        self.rollMat.append([2, 0, 1])
        self.rollMat.append([1, 2, 0])
        
        self.losecount=0;
        self.playrand=False
        self.mult = 1.0
        
    def gameRes(self, c1, c2):
        i1 = self.choices.index(c1)
        i2 = self.choices.index(c2)
        
        return self.gameMat[i1][i2]
    def getRoll(self, c1, c2):
        i1 = self.choices.index(c1)
        i2 = self.choices.index(c2)
        return self.rollMat[i1][i2]
    def getRollbyInd(self, i1, i2):
        #i1 = self.choices.index(c1)
        #i2 = self.choices.index(c2)
        return self.rollMat[i1][i2]
    
    def rollInd(self,i1, inc):
        
        row = self.rollMat[i1]
        ind = row.index(inc)
        return ind
        
    def predict(self):
        if self.prevchoice is None or self.prevres is None:
            ret= self.choices[randint(0,2)]
            self.prevmove = ret
            return ret
        arr=self.dataarr[self.prevres]
        
        predictedroll = weighted_choice([0,1,2], arr)
        predictedchoice = self.rollInd(self.prevchoice, predictedroll)
        
        choice = self.beatMat[predictedchoice]
        if self.playrand:
            self.playrand=False
            
            choice = randint(0,2)

        self.prevmove = self.choices[choice]
        return self.choices[choice]
    
    def store(self, c):
        
        i1 = self.choices.index(c)
        
        if not (self.prevchoice is None or self.prevres is None):
            roll = self.getRollbyInd(self.prevchoice, i1)
            for i in range(3):
                for j in range(3):
                    self.dataarr[i][j]*=0.9
            self.dataarr[self.prevres][roll]+=1
            
            
        self.prevchoice = i1
        self.prevres = self.gameRes(c,self.prevmove)
        
        



if input == '':
    tp = treePredictor()
    output = tp.predict()
    
    
else:
    #output='R'
    tp.store(input)
    output = tp.predict()
    
    
        