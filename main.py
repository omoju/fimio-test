
def is_tree(tree):
    """Determine whether this is an instance of an acceptable tree. 
       Return boolean
    """
    
    # all trees must be of type tree and have atleast one element
    if type(tree) != list or len(tree) < 1:
        return False
    
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def tree(root, branches=[]):
    """
    Tree constructor
    Attributes
    ----------
    root: singleton list
    branches: list
    """
    
    for branch in branches:
        assert(is_tree(branch)), 'branches must be trees'
        
    return [root] + list(branches)


def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]
aTree = tree(5, [tree(1), tree(2)])
print(aTree)
