class System:
    def __init__(self):
        self.nodes = []
    
    def create(*args):
        if len(args) == 0:
            self.nodes.append(Node(self, self.nextname()))
    
    def findtransfer(self, source, sink):
        def concat(*args):
            res = []
            map(res.extend, args)
            
        
        def findpaths(crnt, path, target):
            if crnt is target:
                return Path(path + [crnt])
            nxt = [i.target for i in crnt.connections if i.target not in deadnodes]
            newpath = path + [crnt]
            return [findpaths(i, newpath, sink) for i in nxt]
            
            
        virtual = False
        if not source.issource():
            raise ValueError('first node must be a source')
        if not sink.issink():
            virtual = True
            self.nodes.append(Node(self, 'virtual'))
            sink = self.nodes[-1]
        paths = []
        loops = []
        
    #create automatic node names
    def nextname(self):
        pass
    
    #returns True if there are no connections pointing to the node#returns True if there are no connections pointing to the node
    def issource(self, node):
        if not isinstance(node, (Node, Connection)):
        elif for i in self.nodes:
            for j in i.connections:
                if node is j[1]:
                    return False
        return True
            raise TypeError('argument must be a Node or Connection')
        
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
        self.connections.append((target, transfer))
    
    #returns True if there are no connections pointing to the node
    def issource(self):
        return self.system.issource(self)
    
    #returns True if there are no connections starting from the node
    def issink(self):
        return self.connections == []

#I'm still not sure whether I want to use this or just tuples
class Connection:
    def __init__(self, origin, target, gain):
        self.origin = origin
        self.target = target
        self.gain = gain

class NodeLink:
    def __init__(self, nodes):
        self.nodes = nodes
    
    def contains(self, node):
        return node in self.nodes

class Path(NodeLink):
    pass

class Loop(NodeLink):
    pass
