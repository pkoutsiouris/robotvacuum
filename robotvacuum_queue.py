"""
----------------------------------------------------------------------------
******** Search Code for DFS, BFS, and Best First Search
******** (expanding front only)
******** author:  AI lab
********
******** Κώδικας για DFS, BFS και Best First Search
******** (επέκταση μετώπου μόνο)
******** Συγγραφέας: Κωνσταντίνος Μπίρμπας, Ευάγγελος Σκεύης, Παναγιώτης Κουτσιούρης (και διορθώσεις)
"""

import copy



def move_right(state):
    # Αν είναι δυνατή η κίνηση (άρα αν δεν βρίσκεται η σκούπα στο τελευταίο πλακίδιο)
    if state[0] < 8:
        state[0] = state[0] + 1
        
        # Συλλογή σκουπιδιών,αν η σκούπα δεν είναι γεμάτη
        if state[-1] < 3:
            # Αν τα σκουπίδια στο πλακίδιο είναι περισσότερα από ό,τι χωράει η σκούπα
            if state[state[0]] > 3 - state[-1]:
                state[state[0]] = state[state[0]] - (3 - state[-1])
                state[-1] = 3 # Η σκούπα γεμίζει
            # Αλλιώς, μαζεύει όλα τα σκουπίδια του πλακιδίου
            else:
                state[-1] = state[-1] + state[state[0]]
                state[state[0]] = 0 # Το πλακίδιο αδειάζει
                
        return state # Επιστρέφει την τροποποιημένη κατάσταση
    
    return None # Επιστρέφει None αν δεν μπορεί να κινηθεί δεξιά
    
def move_left(state):
    # Εάν είναι δυνατή η κίνηση, άρα η σκούπα δεν βρίσκεται στο πρώτο πλακίδιο
    if state[0] > 1:
        state[0] = state[0] - 1
        
        # Συλλογή σκουπιδιών, αν η σκούπα δεν είναι γεμάτη
        if state[-1] < 3:
            # Αν τα σκουπίδια στο πλακίδιο είναι περισσότερα από ό,τι χωράει η σκούπα
            if state[state[0]] > 3 - state[-1]:
                state[state[0]] = state[state[0]] - (3 - state[-1])
                state[-1] = 3 # Η σκούπα γεμίζει
            # Αλλιώς, μαζεύει όλα τα σκουπίδια του πλακιδίου
            else:
                state[-1] = state[-1] + state[state[0]]
                state[state[0]] = 0 # Το πλακίδιο αδειάζει
                
        return state # Επιστρέφει την τροποποιημένη κατάσταση
    
    return None # Επιστρέφει None αν δεν μπορεί να κινηθεί αριστερά

def move_to_base(state):
    
   # Κινείται μία θέση προς τη βάση (αριστερά ή δεξιά)
  #  Χρησιμοποιείται όταν η σκούπα είναι γεμάτη.
    
    robot_pos = state[0]
    base_pos = state[-2]
    
    # Αν δεν είναι στη βάση, κινείται προς αυτή
    if robot_pos != base_pos:
        if robot_pos < base_pos:  # Η βάση είναι δεξιά
            state[0] = robot_pos + 1
        else:  # Η βάση είναι αριστερά
            state[0] = robot_pos - 1
    
    return state


#Συνάρτηση εύρεσης απογόνων της τρέχουσας κατάστασης

def find_children(state):
    children = []
    
    # Move left
    left_state = copy.deepcopy(state)
    left_child = move_left(left_state)
    # Η move_left επιστρέφει None αν δεν μπορεί να γίνει η κίνηση
    if left_child != None:
        children.append(left_child)
    
    # Move right
    right_state = copy.deepcopy(state)
    right_child = move_right(right_state)
    # Η move_right επιστρέφει None αν δεν μπορεί να γίνει η κίνηση
    if right_child != None:
        children.append(right_child)
    
    # Άδειασμα
    robot_pos = state[0]
    base_pos = state[-2]
    capacity = state[-1]
    
    if robot_pos == base_pos and capacity > 0:
        empty_state = copy.deepcopy(state)
        empty_state[-1] = 0  # Αδειάζει τη σκούπα
        children.append(empty_state)
    
    return children

 
# Ευρετική Συνάρτηση

def heuristic(state):  

    robot_pos = state[0]  
    base_pos = state[-2]  
    vacuum_skou = state[-1]  

    total_skou= sum(state[1:9])  
    
    min_distance_to_skou= float('inf')  
    for i in range(1, 9):  
        if state[i] > 0:  
            distance = abs(robot_pos - i)  
            min_distance_to_skou = min(min_distance_to_skou, distance)  
    
    if min_distance_to_skou == float('inf'):  
        min_distance_to_skou = 0  
    
    distance_to_base = abs(robot_pos - base_pos)  
    
    if vacuum_skou >= 3:  
        return total_skou + distance_to_base * 2 + vacuum_skou  
    else:  
        return total_skou + min_distance_to_skou + vacuum_skou * 0.5  



# Διαχείριση Μετώπου


def make_front(state):
    return [state]
    
def expand_front(front, method):    

    if method == 'DFS':        
        if front:  
            print("Front:")  
            print(front)  
            node = front.pop(0)  
            for child in find_children(node):      
                front.insert(0, child)  
    elif method == 'BFS':  
        if front:  
            print("Front:")  
            print(front)  
            node = front.pop(0)  
            for child in find_children(node):      
                front.append(child)  
    elif method == 'BestFS':  
        if front:  
            print("Front:")  
            print(front)  
            node = front.pop(0)  
            children = find_children(node)  
            front.extend(children)  
            front.sort(key=lambda state: heuristic(state))  
    return front  


# Διαχείριση ουράς


def make_queue(state):
    # Αρχικοποίηση ουράς 
    return [[state]]

def extend_queue(queue, method):
    # Επέκταση ουράς,για καταγραφή διαδρομών 
    if not queue:
        return []
        
    # Αφαιρούμε τη διαδρομή του κόμβου που αφαιρείται από το front
    node = queue.pop(0) 
    queue_copy = copy.deepcopy(queue)
    children = find_children(node[-1])
    
    new_paths = []

    if method == 'DFS':
        # Εισάγουμε στην αρχή (DFS)
        for child in children:
            path = copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0, path)
            
    elif method == 'BFS':
        # Προσθέτουμε στο τέλος (BFS)
        for child in children:
            path = copy.deepcopy(node)
            path.append(child)
            queue_copy.append(path)
            
    elif method == 'BestFS':
        # Δημιουργούμε τις νέες διαδρομές
        for child in children:
            path = copy.deepcopy(node)
            path.append(child)
            new_paths.append(path)
            
        # Προσθέτουμε τις νέες διαδρομές στην ουρά
        queue_copy.extend(new_paths)
        
        # Ταξινομούμε όλη την ουρά με βάση την ευρετική τιμή της τελευταίας κατάστασης
        queue_copy.sort(key=lambda path: heuristic(path[-1]))
    
    return queue_copy

 
# Basic recursive function to create search tree (recursive tree expansion)
# Βασική αναδρομική συνάρτηση για δημιουργία δέντρου αναζήτησης (αναδρομική επέκταση δέντρου)


def find_solution(state, front, queue, closed, goal, method):
    
    if not front:
        print('_NO_SOLUTION_FOUND_')
    
    elif front[0] in closed:
        new_front = copy.deepcopy(front)
        new_front.pop(0)
        
        # Αφαίρεση της διαδρομής του κόμβου που ήδη υπάρχει στο closed
        new_queue=copy.deepcopy(queue)
        new_queue.pop(0) 
        
        find_solution(state, new_front, new_queue, closed, goal, method)
    
    elif front[0] == goal:
        print('_GOAL_FOUND_')
        # Εκτύπωση της διαδρομής
        print("Final Path:")
        print(queue[0])
        
        print(f"Εξερευνημένες Καταστάσεις ({method}): {len(closed)}")
        
    
    else:
        closed.append(front[0])
        
        # Επέκταση Μετώπου (Front)
        front_copy = copy.deepcopy(front)
        front_children = expand_front(front_copy, method)
        
        # Επέκταση Ουράς (Queue)
        queue_copy = copy.deepcopy(queue)
        queue_children = extend_queue(queue_copy, method)
        
        closed_copy = copy.deepcopy(closed)
        
        find_solution(state, front_children, queue_children, closed_copy, goal, method)
# Executing the code
# κλήση εκτέλεσης κώδικα

            
def main():
    
    initial_state = [3, 0,0, 0, 1, 1, 1, 3, 1, 3, 0]  
    """ 
    **** [Θέση σκούπας, σκουπίδια 1ου πλακιδίου, σκουπίδια 2ου, ..., σκουπίδια 8ου, θέση βάσης, σκουπίδια σκούπας]
    """
    goal = [3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0] # Όλα τα πλακίδια καθαρά, σκούπα στη βάση, άδεια.
    method = ""  
    
    print("Choose method: BFS, DFS, or BestFS")
    method = input().strip()
    print(f"Selected Method: {method}")
    
    while method not in ['BFS', 'DFS', 'BestFS']:
        print("Invalid choice. Choose method: BFS, DFS, or BestFS")
        method = input().strip()
    
    print('____BEGIN__SEARCHING____')
    
    # Έναρξη αναζήτησης, περνώντας το αρχικό state, το αρχικό front, την αρχική queue, το closed και τον στόχο
    find_solution(initial_state, make_front(initial_state), make_queue(initial_state), [], goal, method)

if __name__ == "__main__":
    main()