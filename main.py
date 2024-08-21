import parse_formula as parse_formula
import brute_force as brute_force_sat
import DPLL 


# Función para procesar el archivo y convertir cada línea de infix a postfix
def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    for line in lines:
        formula = line.strip()
        # Ejemplo de fórmula booleana
        clauses = parse_formula.parse_formula(formula)
        print("Cláusulas parseadas:", clauses)

        # Ejecución del algoritmo de fuerza bruta
        brute_force_result = brute_force_sat.brute_force_sat(clauses)
        print("Fuerza Bruta:", brute_force_result)

        # Ejecución del algoritmo DPLL
        dpll_result = DPLL.DPLL(clauses)
        print("DPLL:", dpll_result)
        print('-' * 50)

if __name__ == "__main__":
    filename = 'a.txt'
    process_file(filename)
