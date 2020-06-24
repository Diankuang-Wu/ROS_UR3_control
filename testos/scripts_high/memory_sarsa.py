import random
import numpy as np

class Memory:
    """
    This class provides an abstraction to store the [s, a, r, a'] elements of each iteration.
    Instead of using tuples (as other implementations do), the information is stored in lists 
    that get returned as another list of dictionaries with each key corresponding to either 
    "state", "action", "reward", "nextState" or "isFinal".
    """
    def __init__(self, size):
        self.size = size
        self.currentPosition = 0
        self.states = []
        self.actions = []
        self.rewards = []
        self.nextStates = []
        self.nextAction = []
        self.finals = []

    def getMiniBatch(self, size) :
        indices = random.sample(list(np.arange(len(self.states))), min(size,len(self.states)) )
        miniBatch = []
        for index in indices:
            miniBatch.append({'state': self.states[index],'action': self.actions[index], 'reward': self.rewards[index], 'nextState': self.nextStates[index], 'nextAction': self.nextAction[index],'isFinal': self.finals[index]})
        return miniBatch

    def getCurrentSize(self) :
        return len(self.states)

    def getMemory(self, index): 
        return {'state': self.states[index],'action': self.actions[index], 'reward': self.rewards[index], 'nextState': self.nextStates[index],'nextAction': self.nextAction[index], 'isFinal': self.finals[index]}

    def addMemory(self, state, action, reward, nextState, nextAction, isFinal) :
        if (self.currentPosition >= self.size - 1) :
            self.currentPosition = 0
        if (len(self.states) > self.size) :
            self.states[self.currentPosition] = state
            self.actions[self.currentPosition] = action
            self.rewards[self.currentPosition] = reward
            self.nextStates[self.currentPosition] = nextState
            self.nextAction[self.currentPosition] = nextAction
            self.finals[self.currentPosition] = isFinal
        else :
            self.states.append(state)
            self.actions.append(action)
            self.rewards.append(reward)
            self.nextStates.append(nextState)
            self.nextAction.append(nextAction)
            self.finals.append(isFinal)
        
        self.currentPosition += 1