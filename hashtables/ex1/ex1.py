#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    #iterate through weights in array
    #enumerate counts from 0 and loops through the array
    for index, weight in enumerate(weights):
        pair = hash_table_retrieve(ht, limit - weight)
        if pair is None:
            hash_table_insert(ht, weight, index)
        else:
            if index > weight:
                return (index, weight)
            return (weight, index)
        print(ht.storage)
        
    # add array to hashtable with index
    # for i in range(0, len(weights)):
    #     hash_table_insert(ht, weights[i], i)
    # # iterate through ht
    # for i in range(length):
    #     #subtract the weights from the limit
    #     j = hash_table_retrieve(ht, limit-weights[i])
    #     if j is not None:
    #         #return (larger_number, smaller_number)
    #         if i > j:
    #             return (i, j)
    #         else:
    #             return (j, i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


