rules = ["S-aSb", "S-a"]
E = ["a", "b"]
V = ["S"]


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
        print("Hola")
        if "e" in calculate_first(string[i]):
            flag = True
        else:
            flag = False
    return flag

def calculate_first(x):
    parts = parts_of(x)
    first = []
    if x in E:
        return x
    if x in V and len(parts) >= 1:
        for i in range(0, len(parts)):
            for j in range(0, len(parts[i])):
                print(parts[i][j])
                print(deriva_epsilon(parts[i], j))
                if calculate_first(parts[i][j]) in E and deriva_epsilon(parts[i], j) == True:
                    first.append(parts[i][j])
            if deriva_epsilon(parts[i], len(parts[i])) == True:
                first.append("e")
    if "e" in parts:
        first.append("e")
    return first

print(parts_of("S"))