class simple_reflex_agent:
    def agent(self,percept):
        loc,sta=percept
        if sta=='drity':
            sta='clean'
            return 'suck',sta
        else :
            return 'noop',sta
           
       
a=simple_reflex_agent()
loc=1
reflex={1:'drity',2:'clean'}
print('present status of env:',reflex)
print('present location of agent is',loc)
action,reflex[loc]=a.agent((loc,reflex[loc]))
print('action maded on location',action)
print('present status of env:{0},location of agent:{1}'.format(reflex,loc))