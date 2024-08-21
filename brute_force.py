from itertools import product

def brute_force_sat(clauses):
    # Extraer literales únicos (sin considerar la negación)
    literals = set(lit.lstrip("~") for clause in clauses for lit in clause)

    # Probar todas las combinaciones de valores de verdad
    for assignment in product([True, False], repeat=len(literals)):
        truth_map = dict(zip(literals, assignment))
        
        # Evaluar cada cláusula con la asignación actual
        satisfied = True
        for clause in clauses:
            clause_satisfied = False
            for lit in clause:
                if lit.startswith("~"):
                    if not truth_map[lit[1:]]:
                        clause_satisfied = True
                        break
                else:
                    if truth_map[lit]:
                        clause_satisfied = True
                        break
            if not clause_satisfied:
                satisfied = False
                break

        if satisfied:
            # Convertir la asignación a representación con literales originales
            return True, {literal: truth_map[literal] for literal in literals}
    
    return False, {}
