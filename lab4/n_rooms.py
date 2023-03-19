from abc import abstractmethod
import time

score = 0

class Environment(object):

    @abstractmethod
    def __init__(self, n):
        self.n = n
    def executeStep(self,n=1):
        raise NotImplementedError('action must be defined!')
    def executeAll(self):
        raise NotImplementedError('action must be defined!')
    def delay(self,n=100):
        self.delay = n

class Room:
 def __init__(self,location,status="dirty"):
    self.location = location 
    self.status = status

#Abstract agent
class Agent(object):
 
 @abstractmethod 
 def __init__(self): 
    pass

 @abstractmethod
 def sense(self,environment):
    pass

 @abstractmethod 
 def act(self):
    pass

class VaccumAgent(Agent):
 
 def __init__(self):
    pass
 def sense(self,env):
    self.environment = env

 def act(self, n_agent):
    if self.environment.currentRoom.status == 'dirty':
        time.sleep(1)
        global score
        score -= 10
        return 'clean' 
    if self.environment.currentRoom.location == str(n_agent): 
        return 'Back to 1'
    #if self.environment.currentRoom.location =='B': 
    return 'forward'

class NRoomVaccumCleanerEnvironment(Environment):
 
 def __init__(self, agent, agent_num):
    self.n_agent = agent_num
    self.r = []
    for x in range(self.n_agent):
        self.r.append(Room(str(x+1), 'dirty'))  
    self.agent = agent
    self.currentRoom = self.r[0]
    self.delay_time = 1
    self.step = 1
    self.action = ""

 def executeStep(self,n=1):
    if self.n_agent < 2:
       print ("Number of agents must be equal or greater than 2")
       return
    counter = 0
    for _ in range(0,n):
        self.displayPerception()
        self.agent.sense(self) 
        res = self.agent.act(self.n_agent) 
        self.action = res
        if res == 'clean':
            self.delay(1)
            global score
            score += 25
            self.currentRoom.status = 'clean' 
            counter -=1
        elif res == 'forward':
            self.currentRoom = self.r[counter]
            self.delay(1)
            score -= 1
        else:
            self.currentRoom = self.r[0]
            counter = 0
        self.displayAction()
        self.step += 1
        counter += 1
        # if counter == self.n_agent:
        #    counter = 0
        print("Score:" + str(score))

 def executeAll(self):
    raise NotImplementedError('action must be defined!') 

 def displayPerception(self):
    print("Perception at step %d is [%s,%s]" %(self.step,self.currentRoom.status,self.currentRoom.location))

 def displayAction(self):
    print("------- Action taken at step %d is [%s]" %(self.step,self.action))

 def delay(self,n=100):
    self.delay_time = n
    time.sleep(self.delay_time)

# Test program

if __name__ == '__main__': vcagent = VaccumAgent() 
env = NRoomVaccumCleanerEnvironment(vcagent,2)
env.executeStep(10)