# In a city-state of n people, there is a rumor going around that one
# of the n people is a spy for the neighboring city-state.
#
# The spy, if it exists:
#
# Does not trust anyone else.
# Is trusted by everyone else (he's good at his job).
# Works alone; there are no other spies in the city-state.
# You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.
#
# If the spy exists and can be found, return their identifier. Otherwise, return -1.

# in a city we have n people - n being the number of people in that city
# One of these people is a spy
# if the spy exists, spy doesn't trust anyone.
# Everyone except the spy trusts the spy.
# the spy works alone so there are no other spies

# with each pair we the first one is trusted and the second one isn't
# so the second one will need to be stored in a separate array so it can be counted.
# We'll do this with each pair, adding to the one that isn't trusted and subtracting 1 from the one that is trusted
# the one with the highest count is the spy
# unless... if the spy can't be identified because there's a tie, then we'll return a -1 automatically.

# I am given trust in an array of pairs. If the spy exists then return that number. otherwise, return -1

# this person is just walking around spying on everyone, gotta find the spy

# every time someone trusts someone else, we'll increment that person by 1,
# The person trusting's number will go down
# [1, 2]  so 1 trusts 2,
# 1 will be -1 and 2 will get  +1
# person with the highest number will be the spy
# so we'll fill up the new array and find the one that is n and they are the spy

def uncover_spy(n, trust):
    # create an array of len n
    arr = [0] * n
    # iterate each 2-element array in trust
    for i, j in trust:  # O(i + j) = O(n) linear time - it preforms constant time operation once for each element.
        # add 1 to the incoming node
        arr[j - 1] += 1
        # subtract 1 to the outgoing element idx
        arr[i - 1] -= 1
    #  If maximum element in the array is N-1 it means there's one node which does not trust any other person)
    if max(arr) == n - 1:  # o(1) time complexity
        return arr.index(max(arr)) + 1
    else:
        return -1

# The max() function returns the item with the highest value, or the item with the highest value in an iterable.

# There, you’re looping over an array of arrays.
# In that case, i and j decompose the inner arrays to make referencing them more convenient.
# You could have written:
#
# for x in trust:
#  i = x[0]
#  j = x[1]

# for loop is O(i +j) it preforms constant time operation once for each element = O(n)
# max comparison is # O(1) time
# O(N) + O(1) = O(n) as worse case

# storing a new array is O(n), so the space complexity is O(n)