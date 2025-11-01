#!/usr/bin/python3
def weight_average(my_list=[]):
    """Return the weighted average of all integers in tuples (score, weight)"""
    if not my_list:
        return 0
    total_weighted = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)
    return total_weighted / total_weight
