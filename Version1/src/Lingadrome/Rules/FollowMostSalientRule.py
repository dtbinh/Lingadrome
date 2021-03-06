'''
Created on 2015/10/20

@author: rondelion
'''
import math
from Rule import Rule

class FollowMostSalientRule(Rule):
    '''
    classdocs
    '''
    __score=10

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def condition(self, inputBuffer, stateBuffer):
        return True
    
    def action(self, inputBuffer, stateBuffer):
        thrust=0.5
        steering=0.0
        if inputBuffer.has_key("velocity") and inputBuffer["velocity"]>0.03:
            thrust=0.0
        if inputBuffer.has_key("mostSalient"):
            mostSalient=inputBuffer["mostSalient"]
            if mostSalient!=None:
                if mostSalient.has_key("direction"):
                    #if mostSalient["name"]=="BubbleRob#0":
                    #    print mostSalient["name"], mostSalient["direction"]
                    if mostSalient["direction"]<0:
                        steering=0.1
                    else:
                        steering=-0.1
                if mostSalient.has_key("distance"):
                    thrust=thrust*(1.0-2.0*math.exp(-1.0*mostSalient["distance"]))
                    #if thrust<0:
                    #    print inputBuffer["name"], thrust
        values={}
        values["steering"]=steering
        values["thrust"]=thrust
        return values
    
    def getName(self):
        return "FollowMostSalient"
    
    def getScore(self):
        return self.__score