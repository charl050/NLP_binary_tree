# Python binary tree implementation for NLP projects


class tree:

    def __init__(self, weight = None, score = None, data = '', ascend = None, descend_left = None, descend_right = None):
        self.weight = weight
        self.score = score
        self.ascend = ascend
        self.data = data
        self.descend_left = descend_left
        self.descend_right = descend_right


    def show_tree(self):
        # Recursively show all tree
        if self.descend_left is None and self.descend_right is None:
            print(self.weight, self.score ,self.data)
        if self.descend_left is not None:
            print(self.weight, self.score ,self.data)
            self.descend_left.show_tree()
        if self.descend_right is not None:
            print(self.weight, self.score ,self.data)
            self.descend_right.show_tree()

    def calculate_weight(self):
        # Recursively calculate the weight of the tree
        if self.descend_left is not None:
            self.descend_left.calculate_weight()
        if self.descend_right is not None:
            self.descend_right.calculate_weight()
        if self.descend_left is None and self.descend_right is None:
            self.weight = 1
        if self.descend_left is not None and self.descend_right is not None:
            if self.descend_left.weight is not None and self.descend_right.weight is not None:
                self.weight = self.descend_left.weight + self.descend_right.weight
                return self.weight

    def calculate_score(self):
        # Recursively calculate the score of the tree
        if self.descend_left is not None:
            self.descend_left.calculate_score()
        if self.descend_right is not None:
            self.descend_right.calculate_score()
        if self.descend_left is None and self.descend_right is None:
            self.score = int(self.data[0])
        if self.descend_left is not None and self.descend_right is not None:
            if self.descend_left.score is not None and self.descend_right.score is not None:
                self.score =  ((self.descend_left.weight*self.descend_left.score)+(self.descend_right.weight*self.descend_right.score))/(self.descend_left.weight+self.descend_right.weight)
                return self.score

    def score(self):
        return self.score

    def weight(self):
        return self.weight



def create_tree(text):
    # Initialize a tree with 'text' syntax
    try:
        self = tree()
        text = text.replace(' ', '') + '|'
        config_tree(self, text, i=1)
        self.calculate_weight()
        self.calculate_score()
        return self
    except:
        return None


def config_tree(ascend, text, i):
    # Config the tree with the 'text' syntax

    item = text[i]

    if item == '(':
        temp = tree(ascend=ascend)
        if ascend.descend_left is None:
            ascend.descend_left = temp
        else:
            ascend.descend_right = temp

    elif item == ')':

        temp = ascend.ascend

    elif item == '|':

        return None

    else:

        ascend.data += item
        temp = ascend

    config_tree(temp, text, i+1)


