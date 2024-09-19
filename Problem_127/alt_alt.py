# Efficient Python3 program to print
# Farey Sequence of order n
import math


# Optimized function to print Farey
# sequence of order n
def farey(n):
    # We know first two terms are
    # 0/1 and 1/n
    x1 = 0;
    y1 = 1;
    x2 = 1;
    y2 = n;

    print(x1, end="")
    print("/", end="")
    print(y1, x2, end="")
    print("/", end="")
    print(y2, end=" ");

    # For next terms to be evaluated
    x = 0;
    y = 0;
    while (y != 1.0):
        # Using recurrence relation to
        # find the next term
        x = math.floor((y1 + n) / y2) * x2 - x1;
        y = math.floor((y1 + n) / y2) * y2 - y1;

        # Print next term
        print(x, end="")
        print("/", end="")
        print(y, end=" ");

        # Update x1, y1, x2 and y2 for
        # next iteration
        x1 = x2;
        x2 = x;
        y1 = y2;
        y2 = y;

    # Driver Code


n = 120000;

farey(n);

# This code is contributed by mits
