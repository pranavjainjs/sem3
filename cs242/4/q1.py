# reading input
amount = int(input("Enter the amount: "))

# to handle arbitrarily large inputs, we divide amount into two parts
# the number of 50 unit coins in minimum composition equals amount//50
# and we can calculate required number of coins of other denominations by the function totalCoins

# MinCoins array maps index to minimum number of coins required to amount index
MinCoins = [None] * 50
MinCoins[0] = 0        

# noOfCoins dictionary matches denomination to the number of coins in minimium composition
noOfCoins = {}
noOfCoins[1] = 0
noOfCoins[5] = 0
noOfCoins[10] = 0
noOfCoins[20] = 0
noOfCoins[25] = 0
noOfCoins[50] = amount // 50

# amount remaining after counting 50 unit coins
rem = amount % 50

def totalCoins(a):
    # don't look in the MinCoins array if MinCoins[a] equals None
    if MinCoins[a] != None:
        return MinCoins[a]  # return only if MinCoins[a] has been previously calculated
    else:
        if a < 1:
            return 0  # base case, to prevent errors

        elif a == 1 or a == 5 or a == 10 or a == 20 or a == 25:  # another base case
            MinCoins[a] = 1  # only 1 coin is needed to make these amounts
            return MinCoins[a]

        # in each of the subsequent cases, we find the minimum of
        # positive values among a-1, a-5, a-10, a-20, a-25 recursively
        # increment it by 1, and store in MinCoins[a]
        # this operation gives the minimum number of coins required to amount 'a', which the function returns

        elif a > 25:
            MinCoins[a] = (
                min(
                    {
                        totalCoins(a - 1),
                        totalCoins(a - 5),
                        totalCoins(a - 10),
                        totalCoins(a - 20),
                        totalCoins(a - 25),
                    }
                )
                + 1
            )
            return MinCoins[a]
        elif a > 20:
            MinCoins[a] = (
                min(
                    {
                        totalCoins(a - 1),
                        totalCoins(a - 5),
                        totalCoins(a - 10),
                        totalCoins(a - 20),
                    }
                )
                + 1
            )
            return MinCoins[a]
        elif a > 10:
            MinCoins[a] = (
                min({totalCoins(a - 1), totalCoins(a - 5), totalCoins(a - 10)}) + 1
            )
            return MinCoins[a]
        elif a > 5:
            MinCoins[a] = min({totalCoins(a - 1), totalCoins(a - 5)}) + 1
            return MinCoins[a]
        elif a > 1:
            # number of coins needed to amount x (where x<5) equals x
            for x in range(1, a + 1):
                MinCoins[x] = x
            return MinCoins[a]
        else:
            return -1  # base case, to be safe


# total number of coins = number of 50 unit coins + other coins
ans = noOfCoins[50] + totalCoins(rem)

# iterating over following loop till rem exceeds 0
# if rem is greater than x and difference between minimum number of coins
# which amount (rem) and (rem-x) equals 1
# then increment noOfCoins[x] by 1 and decrease rem by x
while rem > 0:
    if rem >= 25 and MinCoins[rem] - MinCoins[rem - 25] == 1:
        noOfCoins[25] += 1
        rem -= 25
    else:
        if rem >= 20 and MinCoins[rem] - MinCoins[rem - 20] == 1:
            noOfCoins[20] += 1
            rem -= 20
        else:
            if rem >= 10 and MinCoins[rem] - MinCoins[rem - 10] == 1:
                noOfCoins[10] += 1
                rem -= 10
            else:
                if rem >= 5 and MinCoins[rem] - MinCoins[rem - 5] == 1:
                    noOfCoins[5] += 1
                    rem -= 5
                else:
                    if rem >= 1 and MinCoins[rem] - MinCoins[rem - 1] == 1:
                        noOfCoins[1] += 1
                        rem -= 1

# print the required number of coins of each unit if it is non zero
print("minimum number of coins needed - ", ans)
for x in [50, 25, 20, 10, 5, 1]:
    if noOfCoins[x] != 0:
        print(x, "unit coins -", noOfCoins[x])
