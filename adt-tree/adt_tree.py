
""" This class represents a TreeNode of a Tree Data Structure TAD. """
class TreeNode:

    """ The TreeNode is initiated with a Single Value to represents it as a Key. """
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.parent = None

    """ Calling string on a python list calls the __repr__ method on each element
        inside. For some items, __str__ and __repr__ are the same. """
    def __repr__(self):
        return self.__str__()

    """ The main description of a TreeNode is it's value. """
    def __str__(self):
        return self.value

    """ It returns the TreeNode value, if this TreeNode is Root, it's level and others
        information related to this current TreeNode. """
    def info(self):
        return ''.join(["TreeNode Value: ", self.value, "\n",
                        "Is Root: ", str(self.is_root()), "\n",
                        "Level: ", str(self.level())])

    """ Self-destruction of this TreeNode. The Root TreeNode can not be removed. """
    def remove(self):
        if not self.is_root():
            self.parent.children.remove(self)

    def replace_for(self, treenode):
        swap_treenode = treenode
        treenode = self
        self = swap_treenode
        return self

    """ It returns the list of lings TreeNodes related to this calling TreeNode.
        The parent TreeNode related to this TreeNode must be valid. In this case,
        there will be no lings list related with the Root TreeNode. """
    def siblings(self, only_values=False):
        if self.is_root():
            return []
        siblings = []
        if self.parent is not None:
            for treenode in self.parent.children:
                if not treenode.value == self.value:
                    if only_values:
                        siblings.extend([treenode])
                    else:
                        siblings.extend([treenode.value])
        return siblings

    """ It adds a new child in to this TreeNode children list and points the new
        child parent as this TreeNode. """
    def add_child(self, child):
        if isinstance(child, TreeNode) == False:
            child = TreeNode(child)
        self.children.extend([child])
        child.parent = self
        # Fluent interface to keep adding children.
        return self

    """ It returns child added in to the children list with a specific name.
        The return is necessary due to reuse of the same method. """
    def child(self, value):
        if self.has_children():
            for child in self.children:
                if child.value == value:
                    return child
    """

    It returns the last child added in to the children list. The return is
    necessary due to reuse of the same method.
    """
    def add_children(self, children):
        this_TreeNode = None
        for child in children:
            this_TreeNode = self.add_child(child)
        return this_TreeNode

    """ This routine verifies if this present TreeNode has children. """
    def has_children(self):
        return self.how_many_children() > 0

    """ It returns how many children the TreeNode that calls this routine has."""
    def how_many_children(self):
        return len(self.children)

    """ It verifies if this TreeNode is leaf of not. If it doesn't have any
        children it will be considered leaf TreeNode. """
    def is_leaf(self):
        return len(self.children) == 0

    """ It informs if this TreeNode is Root TreeNode in the structure. Basically
        it checks if it's parent is None. """
    def is_root(self):
        return self.parent is None

    """ It verifies if the TreeNode is the last one set as child in a children
        list of it's parents children list. It's parent TreeNode must be valid.
        In this case, the root TreeNode will be considered the youngest by
        default. """
    def is_youngest(self):
        if self.is_root():
            return True
        youngest = self.parent.children[-1]
        if self == youngest:
            return True
        else:
            return False

    """ It informs if the TreeNode is the first born in a children list of a
        parent TreeNode. """
    def is_first_born(self):
        if self.is_root():
            return True
        first = self.parent.children[0]
        if self == first:
            return True
        else:
            return False

    """ It informs if the TreeNode is the last born in a children list of a parent
        TreeNode. """
    def is_last_born(self):
        if self.is_root():
            return True
        last = self.parent.children[-1]
        if self == last:
            return True
        else:
            return False

    """ It returns the level of the TreeNode. Self.call level will return the
        current level recursively till it hits the root TreeNode of the Tree. """
    def level(self):
        return self.above_level(self, 0)

    """ It recursively calculates the level of a TreeNode. This routine is called
        by routine/method level. """
    def above_level(self, TreeNode, level):
        if TreeNode.parent is None:
            return level
        else:
            return self.above_level(TreeNode.parent, level+1)

    """ It sets the TreeNode entered as parameter to be the new parent of self
        TreeNode, which is the current TreeNode. There is another method to do
        the same thing which is the method: as_parent_of. The second method do
        the same action but the difference is that the parameter will be the
        child TreeNode and not the parent. """
    def set_parent_as(self, TreeNode):
        TreeNode.add_child(self)

    """ Sets the current TreeNode as parent TreeNode of the TreeNode entered as
        parameter. """
    def as_parent_of(self, TreeNode):
        self.add_child(TreeNode)

    """ It can't be in a descendent place. """
    def put_below(self, TreeNode):
        moving_TreeNode = self
        if not self.parent is None:
            TreeNode.parent.children.remove(self)
            TreeNode.add_child(moving_TreeNode)

    def put_above(self, TreeNode):
        if TreeNode.is_root():
            self.add_child(TreeNode)
            # Only in this case.
            TreeNode.parent = None

    """ This is going to be lings element.same_level(element) """
    def put_at_same_level_as(self, TreeNode):
        if not self.is_root():
            if not self in TreeNode.parent.children:
                if not self in self.children:
                    TreeNode.parent.add_child(self)
                    child_to_remove = self
                    TreeNode.children.remove(child_to_remove)

    """ Return true If this TreeNode is descendent of the TreeNode entered by
        parameter. """
    def is_descendent_of(self, treenode):
        if self.is_root() and not self.value == treenode.value:
            return False
        if self.parent.value == treenode.value:
            return True
        else:
            self_parent_treenode = self.parent
            return self_parent_treenode.is_descendent_of(treenode)

    """ Return if the treenode is descendent of self TreeNode. This method calls
        the method is_descendent_of to check for descendent recursively til it
        finds a parent with the same value of treenode entered as paremeter. """
    def has_descendent(self, treenode):
        return treenode.is_descendent_of(self)

    """ It verifies if this treenode has youngest siblings. """
    def has_yonger_siblings(self):
        if self.parent is not None:
            return self.parent.children.index(self)<len(self.parent.children)-1
        return False

""" The class Tree is responsible to hold a tree structure and it keeps methods
    that can not be in the TreeNode structure. """
class Tree:

    """ It receives the root TreeNode. The purpose of the root TreeNode is to keep
        the reference of the first TreeNode of the tree. """
    def __init__(self, root=None):
        self.root(root)
        self.identation = 1
        self.dash_space = 1

    """ It sets or resets the root TreeNode with a new value. """
    def root(self, value):
        if isinstance(value, TreeNode):
            self.root = value
        else:
            if value is None:
                self.root = TreeNode(None)
            else:
                self.root = TreeNode(value)
        return self.root

    """ This method isn't working yet. """
    def swap_treenodes(self, origin, destiny):
        if not isinstance(origin, TreeNode):
            origin = self.find(origin)
        if not isinstance(destiny, TreeNode):
            destiny = self.find(destiny)
        origin.swap_for(destiny)

    """ It performs a search among the TreeNodes in order to find a TreeNode with
        the value entered as a parameter. The search is made recursively throw the
        TreeNodes."""
    def find(self, value):
        return self.find_recursively(value, self.root)

    """ This method is used by the method "find" to perform a search among the
        TreeNodes recursively. The difference is that this method has two parameters,
        the first is the value to find and the second one is the "root" TreeNode to
        start the recursive search. This method is also effective when a subject
        tries to find a specific TreeNode in a sub-tree. """
    def find_recursively(self, value, treenode):
        if treenode.value == value:
            return treenode
        else:
            if treenode.has_children():
                for subject in treenode.children:
                    retrieve = self.find_recursively(value, subject)
                    if retrieve is not None:
                        return retrieve

    """ It creates a new child into the children list of a parent TreeNode entered
        by parameter. If the parent is None, the new TreeNode will be set as root
        TreeNode."""
    def add(self, child, parent=None):
        if parent is None:
            self.root = TreeNode(child)
        else:
            treenode_parent = self.find(parent)
            treenode_child = TreeNode(child)
            treenode_parent.add_child(treenode_chield)

    """ It adds children into a TreeNode parent entered by parameter. """
    def add_children(self, parent=None, *children):
        treenode_parent = self.find(parent)
        for child in children:
            treenode_parent = TreeNode(child)
            treenode_parent.add_child(treenode_child)

    """ It returns a list of children of a TreeNode parent entered by parameter if
        exists. The parent TreeNode must be valid. """
    def children(self, parent):
        treenode_parent = self.find(parent)
        return treenode_parent.children()

    """ It returns a TreeNode parent of a child entered by parameter. The method
        works for both TreeNode and Value of a TreeNode child to return it's parent."""
    def parent(self, child):
        if not isinstance(child, TreeNode):
            treenode_child = self.find(child)
        return treenode_child.parent

    """ It returns the number of children of a entered TreeNode. The parent TreeNode must
        be valid. """
    def how_many_children(self, parent):
        treenode_parent = self.find(parent)
        return treenode_parent.how_many_children()

    """ It informs if a individual is root of the tree, which means that if the
        TreeNode entered by parameter has a valid parent of not. """
    def is_root(self, individual):
        treenode_individual = self.find(individual)
        return (treenode_individual == self.root)

    """ It verifies if this TreeNode has leaves, which means children without
        descendents. """
    def has_leaves(self, individual):
        if self.has_children():
            result = False
            for child in self.children:
                if child.has_children():
                    return True
        return False

    """ It shows the tree graphicaly by using arrows, levels and identation.
        This is the best way to see the tree graphicaly. """
    def display(self, root=None):
        if root is None:
            self.display_recursively(self.root, 0)
        else:
            self.display_recursively(root, root.level())

    """ Find a TreeNode recursively among it's descendents TreeNodes. """
    def display_recursively(self, treenode, level):
        if treenode.is_root():
            print treenode.value
        else:
            print " "*treenode.parent.level()*(self.identation + 1) + "|" +("-"*self.dash_space) + treenode.value
        if treenode.has_children():
            for subject in treenode.children:
                self.display_recursively(subject,level)

    """ It returns the tree as a list of nodes. """
    def as_list(self):
        return self.as_list_from(self.root)

    """ It returns a list with the tree elements """
    def as_list_from(self, treenode, treenodes=[]):
        if treenode is not None:
            treenodes.extend([treenode])
        if treenode.has_children():
            for subject in treenode.children:
                treenodes = self.as_list_from(subject,treenodes)
        return treenodes

    """ Serial of this tree with parenteses """
    def as_serial(self):
        return self.as_serial_from(self.root)

    """ This routine generates a serial from the specified treenode. """
    def as_serial_from(self, treenode, serial=""):
        if treenode is not None:
            serial += str(treenode)
            # If not last child or if it hasn't children.
            if not treenode.is_youngest() and treenode.is_leaf() and treenode.has_yonger_siblings():
                serial += ", "
        if treenode.has_children():
            serial += "("
            for subject in treenode.children:
                serial = self.as_serial_from(subject,serial)
            serial += ")"
            if treenode.has_yonger_siblings():
                serial += ", "
        return serial

    """ Adds a new child in the parent entered by parameter. The child will be
        included in the parent's children list. """
    def add_child_into_parent(self, child, parent):
        parent.add_child(child)
        return self
