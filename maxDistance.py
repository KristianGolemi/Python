# Variable with a given value greater than any element in the input array
max = 9999999999

# Function that prints out the two numbers in the input array whose sum is closer
# to the given x

def maxDistance(array, n, x):

    res_l, res_r = 0, 0
    # left and right indexes, difference x - pair sum
    l, r, diff = 0, n-1, max

    # While there are numbers in the array between indexes left and right
    while r > l:
        # Check if this pair is closer than the
        # closest pair so far
        if abs(array[l] + array[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(array[l] + array[r] - x)

        if array[l] + array[r] > x:
        # If this pair has a sum closer to the x, move to
        # smaller numbers or else move to larger numbers
            r -= 1
        else:
            l += 1

    print('The array numbers whose sum is closer to the given x are {} and {}'
         .format(array[res_l], array[res_r]))


# Testing code in which the user can give any input numbers to the array and the x
if __name__ == "__main__":
    # This is an example, the numbers can be changed
    array = [8, 16, 21, 36, 42, 50]
    n = len(array)
    x = 59
    maxDistance(array, n, x)
