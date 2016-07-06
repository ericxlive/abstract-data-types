class GraphNode:

    def __init__(self, value):
        self.value = value
        self.targets = []

    """ Calling string on a python list calls the __repr__ method on each element
        inside. For some items, __str__ and __repr__ are the same. """
    def __repr__(self):
        return self.__str__()

    """ The main description of a TreeNode is it's value. """
    def __str__(self):
        return self.value

    """ It defines a new target for this GraphNode. The new target is included in
        the targets list. """
    def target(self, value):
        if not isinstance(value, GraphNode):
            value = GraphNode(value)
        self.targets.extend([value])

    def has_targets(self):
        return len(self.targets) > 0

class Graph:

    def __init__(self, value=None):
        self.origin = GraphNode(value)

    def display(self):
        self.display_recursively(self.origin)

    def display_recursively(self, graphnode):
        if not graphnode is None:
            if len(graphnode.targets) > 0:
                print graphnode.value + ":" + str(graphnode.targets)
                for target in graphnode.targets:
                    self.display_recursively(target)

    def find(self, value):
        return self.find_recursively(value, self.origin)

    def find_recursively(self, value, graphnode):
        if graphnode.value == value:
            return graphnode
        else:
            if len(graphnode.targets) > 0:
                for target in graphnode.targets:
                    retrieve = self.find_recursively(value, target)
                    if retrieve is not None:
                        return retrieve

    def as_list(self):
        return self.as_list_from(self.origin)

    def as_list_from(self, graphnode, graphnodes=[]):
        if graphnode is not None:
            #if self.find(graphnode.value) not in graphnodes:
            if graphnode.value not in str(graphnodes):
                graphnodes.extend([graphnode])
        if len(graphnode.targets) > 0:
            for subject in graphnode.targets:
                graphnodes = self.as_list_from(subject,graphnodes)
        return graphnodes

    def display_matrix(self):
        matrix_head = "-"
        for subject in self.as_list():
            matrix_head += str(subject)
        print matrix_head
        for subject_y in self.as_list():
            line = str(subject_y)
            for subject_x in self.as_list():
                if subject_y.value == subject_x.value:
                    line += "0"
                #elif subject_x.value in str(subject_y.targets):
                if subject_x in subject_y.targets:
                    line += "1"
            print line
