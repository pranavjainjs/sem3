# importing the string module
import string

# string of 26 capital english letters
alphas = string.ascii_uppercase

# reading input from command line
n = int(input("Number of people sitting around table : "))
k = int(input("Skip number is : "))

number = n  # a temporary variable number is made

alive = list(alphas)[0:n]  # a list of n letters is initialized

if n > 26:  # edge case when initial number of people is > 26
    print("enter a number strictly less than 27")
elif n <= 0:
    print("number of people should be positive ")
elif k == 0:  # edge case when skip number is 0
    for i in range(0, n):
        print(alive[i], " kills ", alive[i])
elif k < 0:
    print("enter a non negative number as skip count")
else:
    target = 0
    while len(alive) != 0:  # run the loop till array is non-empty
        killer = target % n  # updating killer to the position of target
        target = (killer + k) % n  # updating target to the kth position left of killer

        print(alive[killer], " kills ", alive[target])  # printing the event
        for i in range(
            target, n - 1
        ):  # all alive people to the right to target are shifted one position to the left
            alive[i] = alive[i + 1]

        n = n - 1  # updating the number of alive people
        alive = alive[0:n]  # array is reinitialized to remove the killed person

    print()
    print(number, " steps until no one remains")
