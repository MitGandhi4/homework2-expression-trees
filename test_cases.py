from expression_tree import build_expression_tree, preorder, postorder, inorder
from evaluator import evaluate_postfix


# Test 1: Simple postfix expression
postfix_list = ["3", "4", "+", "2", "*"]

root = build_expression_tree(postfix_list)

print("Preorder:", preorder(root))
print("Postorder:", postorder(root))
print("Inorder:", inorder(root))


# Test 2: Postfix evaluation
expression = "5 1 2 + 4 * + 3 -"
print("Evaluation:", evaluate_postfix(expression))

# Edge Case Tests

print("\n--- Edge Case Tests ---")

# Empty expression
try:
    evaluate_postfix("")
except ValueError as e:
    print("Empty expression test passed:", e)

# Division by zero
try:
    evaluate_postfix("5 0 /")
except ZeroDivisionError as e:
    print("Division by zero test passed:", e)

# Malformed expression
try:
    evaluate_postfix("3 4")
except ValueError as e:
    print("Malformed expression test passed:", e)

# Invalid token
try:
    evaluate_postfix("5 2 &")
except ValueError as e:
    print("Invalid token test passed:", e)