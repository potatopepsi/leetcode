

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


def cloneGraph(node) -> Node:
    
    counter = 1
    output = Node(counter, [])
    trav = output

    head = node

    

    #Edge Case 1 - No node (empty graph)
    if(node==None):
        return None
    #Edge Case 2 - 1 Node w/ no neighbors
    elif(node.neighbors==None or node.neighbors==[]):
        return output
    #A connected undirected graph
    else:
        #nodeTracker - Keeps track of all nodes created in copy
        nodeTracker = {counter: output}
        #originalTracker - Keeps track of all nodes seen in original node
        originalTracker = {node.val: node}

        x = True
        while(x):
            
            #Create neighbor node if it doesn't exist in the copy
            #Add it to both dictionaries
            try:
                for i in range(len(head.neighbors)):
                    curVar = head.neighbors[i].val
                    originalTracker.update({curVar: head.neighbors[i]})
                    if(nodeTracker.get(curVar)==None):
                        tempNode = Node(curVar, [])
                        nodeTracker.update({curVar:tempNode})
                        trav.neighbors.append(tempNode)
                    else:
                        trav.neighbors.append(nodeTracker.get(curVar))
                
                counter += 1
                trav = nodeTracker.get(counter)
                head = originalTracker.get(counter)
            except:
                return output



def main():
    print()

if __name__ == "__main__":
    main()



#OUTLINING STEP BY STEP

# prev = trav
# FIRST = trav
# temp_node = Node(2, [])
# trav.neighbors.append(temp_node)
# temp_node = Node(4, [])
# UGH = temp_node
# trav.neighbors.append(temp_node)

# trav = trav.neighbors[0]

# trav.neighbors.append(prev)
# prev = trav
# temp_node = Node(3, [])
# trav.neighbors.append(temp_node)

# trav = trav.neighbors[1]
# trav.neighbors.append(prev)
# prev = trav
# trav.neighbors.append(UGH)

# trav = trav.neighbors[1]

# trav.neighbors.append(FIRST)
# trav.neighbors.append(prev)

# return output