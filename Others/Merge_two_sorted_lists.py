"""
 We can do better. With this algorithm, we're not really taking advantage of the fact that the input lists are themselves already sorted. How can we save time by using this fact?

A good general strategy for thinking about an algorithm is to try writing out a sample input and performing the operation by hand. If you're stuck, try that!

Since our lists are sorted, we know they each have their smallest item in the 0th index. So the smallest item overall is in the 0th index of one of our input lists!

Which 0th element is it? Whichever is smaller!
"""
def merge_lists(my_list,alice_list):
    merged_size=len(my_list)+len(alice_list)
    merge_list=[None]*merged_size
