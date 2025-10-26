""" 
 * Given an 6x6 array, arr, an hourglass subset of values with indices falling int
 * the following pattern:
 *      a b c
 *        d
 *      e f g
 * There are 16 hourglasses in a 6x6 array. The hourglass sum is the sum of the values
 * in an hourglass. Calculare the hourglass sum for every hourglass in arr, then print 
 * the maximum hourglass sum.
 * 
 * Do:
 *  - A method called hourglassSum which receives an 2d array (int array[6][6]) of 
 *    integers.
 *  - The method must return the maximum sum.
"""
def hourglass_sum(arr):
    # variables
    sum_hg = []

    # [i][j],   [i][j+1],   [i][j+2]
    # [i+1][j], [i+1][j+1], [i+1][j+2]
    # [i+2][j], [i+2][j+1], [i+2][j+2]

    # processing arr
    for i in range(4): # we through every list [],[],[] (we focus on 3 (since is 6x6))
        # print(f"{arr[i]}")
        for j in range(4): # we go through the elements IN the lists [1,2,...]
            # print(f"Elemento: {arr[i][j]}") # ok, si se puede hacer esto!

            # sum of elements and adding result to sum_hg
            sum_hg.append(
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                arr[i+1][j+1] +
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )
    return max(sum_hg) # returning max value

## llamando a funcion
arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

print(hourglass_sum(arr))