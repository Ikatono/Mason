class System:
    def __init__(self):
        self.nodes = []
    
    def create(*args):
        if len(args) == 0:
            self.nodes.append(Node(self, self.nextname()))
    
    def findtransfer(self, source, sink):
        def findpaths():
            
        virtual = False
        if not source.issource():
            raise ValueError('first node must be a source')
        if not sink.issink():
            virtual = True
            self.nodes.append(Node(self, 'virtual'))
            sink = self.nodes[-1]
        paths = []
        loops = []
        
    
    def nextname(self):
        pass
    
    #returns True if there are no connections pointing to the node#returns True if there are no connections pointing to the node
    def issource(self, node):
        if not isinstance(node, Node):
            raise TypeError('argument must be a Node')
        for i in self.nodes:
            for j in i.connections:
                if node is j[1]:
                    return False
        return True
        
    #returns True if there are no connections starting from the node
    def issink(self, node):
        if not isinstance(node, Node):
            raise TypeError('argument must be a Node')
        return node.issink()

class Node:
    def __init__(self, system, name):
        self.system = system
        self.name = name
        self.connections = []
    
    def connect(target, transfer):
        self.connections.append((taget, transfer))
    
    #returns True if there are no connections pointing to the node
    def issource(self):
        return self.system.issource(self)
    
    #returns True if there are no connections starting from the node
    def issink(self):
        return self.connections == []

class Connection:
    def __init__(self, target, gain):
        

class Loop:
    def __init__(self):
        pass
