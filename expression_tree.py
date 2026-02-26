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

        for token in postfix_tokens:

            # If token is a number (operand)
            if token.isdigit():
                node = TreeNode(token)
                stack.push(node)

                # If token is an operator
            elif token in ["+", "-", "*", "/"]:

                # Pop right and left operands
                right = stack.pop()
                left = stack.pop()

                # Create new operator node
                node = TreeNode(token)
                node.left = left
                node.right = right

                # Push the new subtree back to stack
                stack.push(node)

        # After processing all tokens,
        # there should be exactly one node in the stack
        if stack.size() != 1:
            raise ValueError("Malformed postfix expression")

        return stack.pop()

def preorder(root):
        """
        Return the preorder (prefix) traversal of the tree as a list.
        """

        if root is None:
            return []

        return [root.value] + preorder(root.left) + preorder(root.right)

def postorder(root):
        """
        Return the postorder (postfix) traversal of the tree as a list.
        """

        if root is None:
            return []

        return postorder(root.left) + postorder(root.right) + [root.value]
