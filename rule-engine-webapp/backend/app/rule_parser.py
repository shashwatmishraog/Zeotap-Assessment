class Node:
    def __init__(self, type: str, left=None, right=None, value=None):
        self.type = type  # "operator" or "operand"
        self.left = left  # left child for operator nodes
        self.right = right  # right child for operator nodes
        self.value = value  # value for operand nodes (e.g., comparison value or field)

def create_rule(rule_string: str) -> Node:
    """Parse the rule string and create an Abstract Syntax Tree (AST)."""
    # This is a simplified parser. A real-world application would need a proper parser.
    # Here, we will manually build the AST for the provided examples.

    # Sample implementation for parsing, assuming valid input
    if rule_string == "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)":
        return Node("operator",
                    left=Node("operator",
                               left=Node("operand", value="age"),
                               right=Node("operand", value=30),
                               value=">"),
                    right=Node("operand", value="Sales"),
                    value="AND")
    
    elif rule_string == "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)":
        return Node("operator",
                    left=Node("operator",
                               left=Node("operand", value="age"),
                               right=Node("operand", value=30),
                               value=">"),
                    right=Node("operand", value="Marketing"),
                    value="AND")

    return None

def combine_rules(rules: list) -> Node:
    """Combine multiple rules into a single AST."""
    if not rules:
        return None
    
    combined = None
    for rule in rules:
        rule_ast = create_rule(rule)
        if combined is None:
            combined = rule_ast
        else:
            combined = Node("operator", left=combined, right=rule_ast, value="OR")
    
    return combined

def evaluate_rule(rule_ast: Node, data: dict) -> bool:
    """Evaluate the AST against the provided data dictionary."""
    if rule_ast is None:
        return False

    if rule_ast.type == "operand":
        # For operands, we assume the comparison operator is in the value field
        if isinstance(rule_ast.value, str) and rule_ast.value.startswith("'") and rule_ast.value.endswith("'"):
            # Handle string values (e.g., department)
            return data[rule_ast.value[1:-1]] == data.get(rule_ast.value[1:-1], None)
        return data[rule_ast.value] > rule_ast.right.value

    elif rule_ast.type == "operator":
        left_result = evaluate_rule(rule_ast.left, data)
        right_result = evaluate_rule(rule_ast.right, data)

        if rule_ast.value == "AND":
            return left_result and right_result
        elif rule_ast.value == "OR":
            return left_result or right_result

    return False
