# -*- coding: utf-8 -*-
"""
Grace Brill
Capybara Markov Chain
3 States: Eat, Sleep, and Swim
Transition States: [EE,ESL,ESW], [SLE,SLSL,SLSW], and [SWE,SWSL,SWSW]
where 
E = Eat
SL = sleep
SW = swim
"""

#import necessary packages
import numpy as np

#error checking function
def check_matrix(tmatrix):
    for t in tmatrix:
        if(sum(t) != 1):
            print("Transition Matrix Summation Error")
            
    return

#markov chain representation
def capybara_markov_chain(num_days, initial_state):
    #error check the user state
    if(initial_state != "Eat" and initial_state != "Swim" and initial_state != "Sleep"):
        print("You entered an invalid state. Please try again.")
        return
    
    #counter variable initialization
    c = 0
    
    #metrics to calculate the probability of your exact state
    prob = 1
    positional_prob = 1
    
    #storing the different states
    total_states = [initial_state]
    
    #store current state
    current_state = initial_state
    
    #iterate for x number of days
    while c != num_days:
        #eat
        if(current_state == "Eat"):
            new_state = np.random.choice(cap_transition_label[0],replace=True,p=cap_transition_matrix[0])
            
            if(new_state == "ESW"):
                current_state = "Swim"
                positional_prob = 2
                
            elif(new_state == "ESL"):
                current_state = "Sleep"
                positional_prob = 1
                
            elif(new_state == "EE"):
                current_state = "Eat"
                positional_prob = 0
                
            #update probabilty
            prob *= cap_transition_matrix[0][positional_prob]
            
        #sleep
        elif(current_state == "Sleep"):
            new_state = np.random.choice(cap_transition_label[1],replace=True,p=cap_transition_matrix[1])
            
            if(new_state == "SLSW"):
                current_state = "Swim"
                positional_prob = 2
                
            elif(new_state == "SLSL"):
                current_state = "Sleep"
                positional_prob = 1
                
            elif(new_state == "SLE"):
                current_state = "Eat"
                positional_prob = 0
                
            #update probabilty
            prob *= cap_transition_matrix[1][positional_prob]
            
        #swim
        elif(current_state == "Swim"):
            new_state = np.random.choice(cap_transition_label[2],replace=True,p=cap_transition_matrix[2])
                  
            if(new_state == "SWSW"):
                current_state = "Swim"
                positional_prob = 2
                
            elif(new_state == "SWSL"):
                current_state = "Sleep"
                positional_prob = 1
                
            elif(new_state == "SWE"):
                current_state = "Eat"
                positional_prob = 0
                
            #update probabilty
            prob *= cap_transition_matrix[2][positional_prob]
        
        #update total_states and the counter        
        total_states.append(current_state)
        c+=1
        
    print(f"Initial State: {total_states[0]}")
    print(f"Final State: {current_state}")
    print(f"There were a total of {num_days} states in this simulation")
    print(f"The probability of this exact list is: {prob}")
    print(total_states)
        

#define Capybara states
cap_states = ['Eat', 'Sleep', 'Swim']

#Capybara transition states and corresponding matrix
#see documentation above for further explanation
cap_transition_label = [['EE','ESL','ESW'], ['SLE','SLSL','SLSW'], ['SWE', 'SWSL' ,'SWSW']]
cap_transition_matrix = [[0.3,0.2,0.5], [0.4,0.3,0.3], [0.2,0.2,0.6]]

check_matrix(cap_transition_matrix)
capybara_markov_chain(20,"Swim")




