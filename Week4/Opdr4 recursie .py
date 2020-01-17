# Maak een functie F(n) met
# n: het bedrag uitgedrukt in eurocenten
# return-waarde: het aantal manieren waarmee het geldbedrag betaald kan worden.

# Je kunt de volgende strategie gebruiken.
# m = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
# In de matrix A is A[i,j] = het aantal manieren waarmee bedrag j betaald kan worden met de
# munten m[0] t/m m[i].

# Er geldt: A[i,0] = 1 voor alle i
#           A[0,j] = 1 voor alle j
#           Als j >= m[i] : A[i,j] = A[i-1,j] + A[i,j-m[i]]
#           j < m[i] : A[i,j] = A[i-1,j]

# m   0 1 2 3 4 5 6 7
# 1 0 1 1 1 1 1 1 1 1
# 2 1 1 1 2 2 3 3 4 4
# 5 2 1 1 2 2 3 4 5 6

#coinList = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
#get_one_single_possible_variable_of_the_total_possible_combinations_of_coins_by_using_dynamic_programming_recusively
#table[row][col] = table[row-1][col]+table[row][col-coins[row-1]]

# Maak een functie F(n) met
# n: het bedrag uitgedrukt in eurocenten
# return-waarde: het aantal manieren waarmee het geldbedrag betaald kan worden.
matrix = {}
def F(n):
    if n <= 1:
        return 1
    coinList = [0, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    coinsCanBeUsed = list(filter(lambda x: x <= n, coinList))
    startValue = 0
    if coinList[0] not in matrix and coinList[1] not in matrix:
        matrix[coinList[0]], matrix[coinList[1]] = [], []
        matrix[coinList[0]] = [0] * ((n - len(matrix[0])) + 1)
        matrix[coinList[0]][0] = 1
        matrix[coinList[1]] = [1] * ((n - len(matrix[1])) + 1)
    else:
        startValue =len(matrix[coinsCanBeUsed[0]])
        if n + 1 < len(matrix[coinList[0]]):
            return matrix[coinsCanBeUsed[-1]][n]
        else:
            matrix[coinList[0]] = matrix[coinList[0]] + [0] * ((n - len(matrix[coinList[0]])) + 1)
            matrix[coinList[1]] = matrix[coinList[1]] + [1] * ((n - len(matrix[coinList[1]])) + 1)

    def Inner(coin, value):
        if coin < len(coinsCanBeUsed):
            if coinsCanBeUsed[coin] not in matrix:
                matrix[coinsCanBeUsed[coin]] = []
                return Inner(coin, 0)
            else:
                if value > n:
                    return Inner(coin +1, startValue)
                else:
                    if coinsCanBeUsed[-1] == coinsCanBeUsed[coin] and value == n:
                        matrix[coinsCanBeUsed[coin]].append(matrix[coinsCanBeUsed[coin - 1]][value] + matrix[coinsCanBeUsed[coin]][value - coinsCanBeUsed[coin]])
                        return matrix[coinsCanBeUsed[coin]][-1]
                    if value >= coinsCanBeUsed[coin]:
                        matrix[coinsCanBeUsed[coin]].append(matrix[coinsCanBeUsed[coin - 1]][value] + matrix[coinsCanBeUsed[coin]][value - coinsCanBeUsed[coin]])
                        return Inner(coin, value + 1)
                    else:
                        matrix[coinsCanBeUsed[coin]].append(matrix[coinsCanBeUsed[coin - 1]][value])
                        return Inner(coin, value + 1)
    return Inner(2, startValue)

def PrintMatrix(n):
   for nb in n:
       print(nb, n[nb])
   print()

print(F(7))
PrintMatrix(matrix)

print(F(3))
PrintMatrix(matrix)

print(F(9))
PrintMatrix(matrix)

print(F(2))
PrintMatrix(matrix)

print(F(150))
PrintMatrix(matrix)




