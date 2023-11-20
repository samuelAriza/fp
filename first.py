rules = ["S-aSb", "A-a", "A-c"]
E = ["a", "b", "c"]
V = ["S", "A"]


#Lado derecho de una produccion
def parts_of(N):
    parts = []
    for i in range(0, len(rules)):
        if rules[i][0] == N:
            parts.append((rules[i].split("-"))[1])
    return parts

#Calcular el conjunto de terminales
def sigma():
    for i in range(0, len(V)):
        parts = parts_of(V[i])
        for j in range(0, len(parts)):
            for k in range(0, len(parts[j])):
                if parts[j][k] not in E and parts[j][k] not in V:
                    E.append(parts[j][k])

def deriva_epsilon(string, k):
    flag = True
    for i in range(0, k):
        if "e" in calculate_first(string[i]):
            flag = True
        else:
            flag = False
    return flag

def calculate_first(x):

    if x in E:
        return x
    if x in V and len(parts) >= 1:
        for i in range(0, len(parts)):
            for j in range(0, len(parts[i])):
                if calculate_first(parts[i][j]) in E and deriva_epsilon(parts[i], j) == True:
                    return parts[i][j]
        if "e" in parts:
            return "e"

    return first

def get_first(S):
    first = []
    parts = parts_of(S)

    for i in range(0, len(parts)):
        for j in range(0, len(parts[i])):
            f = calculate_first(parts[i][j])

    return first


print(get_first("S"))