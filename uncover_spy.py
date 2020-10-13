def uncover_spy(n, trust):
    # create an array of len n
    arr = [0] * n
    # iterate each 2-element array in trust
    for i, j in trust:
        # add 1 to the incoming node
        arr[j-1] += 1
        # subtract 1 to the outgoing element idx
        arr[i-1] -= 1
    # if max element in the array is n-1 there's one node that doesn't trust
    if max(arr) == n - 1:
        return arr.index(max(arr)) +1
    else:
        return -1
