def gridChallenge(grid):
    # Write your code here
    ans = "YES"
    row_length = 0
    grid_sorted = []

    for row in grid:
        row_length = len(row)
        row_sorted = sorted(row)  # Sort each row first

        grid_sorted.append(row_sorted)  # Append sorted rows into grid
    print(grid_sorted)
    for index in range(row_length):
        column = [row[index] for row in grid_sorted]
        # column = []
        # for row in grid_sorted
        #   column.append(row[index])
        col_sorted = sorted(column)  # sort columns
        print(col_sorted)
        if (column != col_sorted):
            ans = "NO"
            break

    return ans

# Calculate super digit (my version : 4 testcases wrong)


def superDigit(n, k):
    # Write your code here
    n = list(n)*k
    Calc = 0
    for i in n:
        Calc += int(i)
    j = []
    
    while len(j) != 1:
        j = list(str(Calc))
        turnCalc = 0
        for i in j:
            turnCalc += int(i)
            Calc = turnCalc
        print(len(j), Calc)
    return Calc

# ChatGPT Ver:


def superDigit(n, k):
    # Sum the digits of n
    digit_sum = sum(int(digit) for digit in n)

    # Multiply by k and convert it back to string
    digit_sum *= k
    digit_sum_str = str(digit_sum)

    # Calculate the super digit without creating large strings
    while len(digit_sum_str) > 1:
        digit_sum = sum(int(digit) for digit in digit_sum_str)
        digit_sum_str = str(digit_sum)

    return int(digit_sum_str)


# New Year Chaos: counting how many bribes a person needs to reach an updated queue.
def minimumBribes(q):
    bribes = 0
    # Length of the queue
    n = len(q)

    # Iterate from the last position to the first
    for i in range(n-1, -1, -1):
        # The original position of the current person is q[i]
        # Calculate how far the person has moved
        """
        q[i] is the sticker number (original position) of the person currently standing at position i. 
        Since we are using zero-based indexing, the actual queue position for comparison is i + 1.
        For example, if q[i] (original position) is 5 and i (current position) is 1, 
        then the person has moved forward 5 - (1 + 1) = 3 positions from their original place. That is more than 2, and per the rules, it's not allowed, hence "Too chaotic."
        """
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        # Count the number of bribes by checking how many people with a number
        # greater than q[i] are in front of them starting from q[i] - 2 to i
        # This is because they could not have moved farther than q[i] - 2
        """
        Iterate through the position where the person could have received bribe.
        max(0,q[i]-2),i) because a person can at most bribe 2 people, use max to not go below 0
        """
        for j in range(max(0, q[i] - 2), i):
            #if true, j is originally behind the queue, and is now infront of i
            #Only if bribed 
            if q[j] > q[i]:
                bribes += 1

    print(bribes)


