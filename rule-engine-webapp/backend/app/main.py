from fastapi import FastAPI
from app.rule_parser import create_rule, combine_rules, evaluate_rule

app = FastAPI()

@app.post("/create_rule/")
def create_rule_endpoint(rule_string: str):
    rule_ast = create_rule(rule_string)
    return {"rule_ast": rule_ast}

@app.post("/combine_rules/")
def combine_rules_endpoint(rules: list):
    combined_ast = combine_rules(rules)
    return {"combined_ast": combined_ast}

@app.post("/evaluate_rule/")
def evaluate_rule_endpoint(rule_ast: dict, data: dict):
    result = evaluate_rule(rule_ast, data)
    return {"result": result}
