"""
----------------------------------------------------------------------------
******** Search Code for DFS  and other search methods
******** (expanding front only)
******** author:  AI lab
********
******** Κώδικας για DFS και άλλες μεθόδους αναζήτησης
******** (επέκταση μετώπου μόνο)
******** Συγγραφέας: Κωνσταντίνος Μπίρμπας,Ευάγγελος Σκεύης, Παναγιώτης Κουτσιούρης
"""

import copy

 

# ******** Operators
# ******** Τελεστές

def move_right(state):
    if state[0] < 8:
        state[0] = state[0] + 1
        if state[-1] < 3:
            if state[state[0]] > 3 - state[-1]:
                state[state[0]] = state[state[0]] - (3 - state[-1])
                state[-1] = 3
            else:
                state[-1] = state[-1] + state[state[0]]
                state[state[0]] = 0
    return state
    
def move_left(state):
    if state[-1]<3 and state[0]>1:
        state[0]=state[0]-1
        if state[state[0]]>3-state[-1]:
            state[state[0]]=state[state[0]] - (3-state[-1])
            state[-1]=3
        else:
            state[-1]= state[-1] + state[state[0]]
            state[state[0]]=0
            
        return state
 
def move_to_base(state):
    """
    Κινείται μία θέση προς τη βάση (αριστερά ή δεξιά)
    Χρησιμοποιείται όταν η σκούπα είναι γεμάτη
    """
    robot_pos = state[0]
    base_pos = state[-2]
    
    # Αν δεν είναι στη βάση, κινείται προς αυτή
    if robot_pos != base_pos:
        if robot_pos < base_pos:  # Η βάση είναι δεξιά
            state[0] = robot_pos + 1
        else:  # Η βάση είναι αριστερά
            state[0] = robot_pos - 1
    
    return state
'''
Συνάρτηση εύρεσης απογόνων της τρέχουσας κατάστασης
'''
def find_children(state):
    children = []
    
    # Move left
    left_state = copy.deepcopy(state)
    left_child = move_left(left_state)
    if left_child != None:
        children.append(left_child)
    
    # Move right
    right_state = copy.deepcopy(state)
    right_child = move_right(right_state)
    if right_child != None:
        children.append(right_child)
    
    # Empty (ΠΡΟΣΘΗΚΗ ΑΥΤΟΥ)
    robot_pos = state[0]
    base_pos = state[-2]
    capacity = state[-1]
    
    if robot_pos == base_pos and capacity > 0:
        empty_state = copy.deepcopy(state)
        empty_state[-1] = 0  # Αδειάζει τη σκούπα
        children.append(empty_state)
    
    return children

""" ----------------------------------------------------------------------------
**** FRONT
**** Διαχείριση Μετώπου
"""

""" ----------------------------------------------------------------------------
** initialization of front
** Αρχικοποίηση Μετώπου
"""

def make_front(state):
    return [state]
    
""" ----------------------------------------------------------------------------
**** expanding front
**** επέκταση μετώπου    
"""

def expand_front(front, method):  
    if method=='DFS':        
        if front:
            print("Front:")
            print(front)
            node=front.pop(0)
            for child in find_children(node):     
                front.insert(0,child)
    
    #elif method=='BFS':
    #elif method=='BestFS':
    #else: "other methods to be added"        
    
    return front

""" ----------------------------------------------------------------------------
**** Problem depending functions
**** ο κόσμος του προβλήματος (αν απαιτείται) και υπόλοιπες συναρτήσεις σχετικές με το πρόβλημα

  #### to be  added ####
"""

""" Function that checks if current state is a goal state """

#def is_goal_state(state):

""" ----------------------------------------------------------------------------
**** Basic recursive function to create search tree (recursive tree expansion)
**** Βασική αναδρομική συνάρτηση για δημιουργία δέντρου αναζήτησης (αναδρομική επέκταση δέντρου)
"""

def find_solution(state,front, closed, goal, method):
#def find_solution(front, closed, method):
    if state[-1]>= 3:
        move_to_base(state)   
    if not front:
        print('_NO_SOLUTION_FOUND_')
    
    elif front[0] in closed:
        new_front=copy.deepcopy(front)
        new_front.pop(0)
        find_solution(state,new_front, closed, goal, method)
        #find_solution(new_front, closed, method)
    
   # elif is_goal_state(front[0]):
    elif front[0]==goal:
        print('_GOAL_FOUND_')
        print(front[0])
    
    else:
        closed.append(front[0])
        front_copy=copy.deepcopy(front)
        front_children=expand_front(front_copy, method)
        closed_copy=copy.deepcopy(closed)
        find_solution(state,front_children, closed_copy, goal, method)
        #find_solution(front_children, closed_copy, goal, method)
        

        
"""" ----------------------------------------------------------------------------
** Executing the code
** κλήση εκτέλεσης κώδικα
"""
           
def main():
    
    initial_state = [3, 2, 3, 0, 0, 2, 0, 1, 2, 3, 0] 
    """ ----------------------------------------------------------------------------
    **** [Θέση σκούπας, σκουπίδια 1ου πλακιδίου, σκουπίδια 2ου, σκουπίδια 3ου, σκουπίδια 4ου, 
          σκουπίδια 5ου, σκουπίδια 6ου, σκουπίδια 7ου, σκουπίδια 8ου, θέση βάσης, σκουπίδια σκούπας]
    """
    goal = [3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0]
    method='DFS'
   
    """ ----------------------------------------------------------------------------
    **** starting search
    **** έναρξη αναζήτησης
    """
    
    print('____BEGIN__SEARCHING____')
    find_solution(initial_state,make_front(initial_state), [], goal, method)
    #find_solution(make_front(initial_state), [], method)

if __name__ == "__main__":
    main()
