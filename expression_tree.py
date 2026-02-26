from stack import Stack
class TreeNode:
    def __init__(self, value):
        """
        Create a node in the expression tree.
        Each node stores:
        - value (operator or operand)
        - left child
        - right child
        """
        self.value = value
        self.left = None
        self.right = None

    def build_expression_tree(postfix_tokens):
        """
        Build and return the root of an expression tree
        from a postfix expression (list of tokens).
        """

        # If the input is empty, return None
        if not postfix_tokens:
            return None

        stack = Stack()

        # We will add logic here step by step

        return None