import re

def parse_formula(formula):
    formula = formula.replace(" ", "")
    formula = formula.replace("∧", " & ").replace("∨", " | ").replace("¬", "~")
    formula = re.sub(r'(~?[a-zA-Z])', r'"\1"', formula)
    formula = formula.replace("&", ",").replace("|", "],[").replace("(", "[").replace(")", "]")
    clauses = eval(f"[{formula}]")
    
    parsed_clauses = []
    for clause in clauses:
        parsed_clause = set()
        for literal in clause:
            parsed_clause.add(literal)
        parsed_clauses.append(parsed_clause)
    
    return parsed_clauses
