import re

class working_memory:

    def __init__(self, lan, router, dsl):
        self.lan_cable = lan
        self.router_status = router
        self.dsl_light = dsl
    
class knowledge_base(working_memory):

    def __init__(self, lan, router, dsl):
        super().__init__(lan, router, dsl)

    def lan_connected(self):
        # self.lan_cable = input("Is LAN cable connected? (0/1): ")
        flag = False
        if self.lan_cable == 0:
            print("Insert your LAN cable correctly at both ends, router & PC.")
            flag = True
        return flag

    def router_on(self):
        flag = False
        if self.router_status == 0:
            print("Please turn on your router")
            flag = True
        return flag

    def dsl_on(self):
        flag = False
        if self.dsl_light == 0:
            print("Configure Internet Portal Settings")
            flag = True
        return flag

class inference_engine(knowledge_base):
    # match-resolve-act
    def __init__(self, lan, router, dsl):
        super().__init__(lan, router, dsl)

        self.goal_tuple = ((self.lan_connected, ".+fix.+internet"), (self.router_on, ".+fix.+internet"), (self.dsl_on, ".+fix.+internet"))
    
    conflict_set = []

    def match(self):

        goal = input("What is your desired goal? :")
        for x in range(len(self.goal_tuple)):
            pattern = re.compile(self.goal_tuple[x][1])
            pattern.match(goal.lower())

            if pattern:
                self.conflict_set.append(self.goal_tuple[x][0])

    def resolve_act(self):
        # resolve using highest priority technique (by order)
        for func in range(len(self.conflict_set)):
            x = self.conflict_set[func]()
            if x == True: 
                problem = input("Problem persists? : ")
                if problem == '0':
                    print("Thank you for using our rule-based system. Your problem has been resolved!")
                    return
        print("Sorry, the rule-based system cannot diagnose and fix your issue. Please contact your ISP or a Domain Expert")
        

ie = inference_engine(0,0,0)
ie.match()
ie.resolve_act()
