class model_based_reflex_agent:
    def agent(self,loc,percept,b):
        if percept[1]==percept[2]=='clean' and loc==b:
            return 'noop','clean',loc
        elif percept[loc]=='dirty':
            return 'suck','clean',loc
        elif percept[1]=='clean':return 'right',percept[1],2
        elif percept[2]=='clean':return 'left',percept[2],1
m=model_based_reflex_agent()
loc=2
b=2
d='present'
action='start'
percept ={1:'dirty',2:'clean'}
print('persent location of agent is ',loc)
while (d=='present'):
    action,percept[loc],loc=m.agent(loc,percept,b)
    print("action :{0}\tstatus :{1}".format(action ,percept))
   
    if loc==b and action=='noop':
        d=''
print('persent location of agent is ',loc)