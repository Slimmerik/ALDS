def possible_coin_combs_dynamic_matrix_rec(cent):
    coinList = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    combinedEntrys = []
    insertArrayStart = [0] * int(cent + 1)
    insertArrayStart[0] = 1
    combinedEntrys.append(insertArrayStart[:])

    def F(combinedEntrys, insertArray, coin):
        if coin < cent:
            for amount in range(0, int(cent + 1)):
                if amount >= coin:
                    insertArray[amount] += insertArray[amount - coin]
            combinedEntrys.append(insertArray[:])
            return F(combinedEntrys, insertArray, coinList.pop(0))
        return combinedEntrys
    return F(combinedEntrys,insertArrayStart,coinList.pop(0))

a = possible_coin_combs_dynamic_matrix_rec(7)


for temp in a:
    print(temp)