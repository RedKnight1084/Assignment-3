# Implement your Node class here
class Node:
    
    #Defines node class
    def __init__(self, value):
        self.value = value
        self.next = None
        
#A stack is the right choice for an undo redo system because it allows us to keep track of actions from what was done most recently to what was done least recently. Essentially, it works in reverse cronilogical order for what the user had inputted while taking and changes into account, making it way easier to undo or redo actions that were previously undone.
#A queue is the right choice for a help desk system because it allows us to keep track of customers in the order they arrive, ensuring that the first customer to arrive is the first to be helped. This ensures fairness and proper order of service. It basically clears out the oldest value first, maintaining the order of service.
#My implementations differ from Python's built in lists by first requiring the creation of a Node class to represent each value, then the selection process for picking which values are selected is far more structured and explicit, rather than relying on manually selecting each element. Stacks allow me to easily manage the order of actions for undo and redo operations, while queues help maintain the order of customers in something like a help desk system as done here.