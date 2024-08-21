def DPLL(B, I={}):
    # Caso base: si no hay cláusulas, la fórmula es satisfacible
    if not B:
        return True, I

    # Caso base: si alguna cláusula es vacía, la fórmula no es satisfacible
    if any(not clause for clause in B):
        return False, {}

    # Seleccionar un literal arbitrario L (string, con o sin ~)
    L = next(iter(next(iter(B))))

    # Propagación de la asignación L = True
    B1 = [clause - {L} for clause in B if L not in clause]
    I1 = I.copy()
    I1[L] = True
    res1, I1 = DPLL(B1, I1)
    if res1:
        return True, I1

    # Propagación de la asignación L = False
    neg_L = L[1:] if L.startswith("~") else f"~{L}"
    B2 = [clause - {neg_L} for clause in B if neg_L not in clause]
    I2 = I.copy()
    I2[L] = False
    return DPLL(B2, I2)
