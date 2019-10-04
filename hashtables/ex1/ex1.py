#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    #iterate through weights in array
    #enumerate counts from 0 and loops through the array
    for index, weight in enumerate(weights):
        #add all weights to hashtable
        hash_table_insert(ht, weight, index)
    #loop through again, find the pairs that equal the limit
    for index, weight in enumerate(weights):
        #subtract the weights from the limit
        pair = limit - weight
        #if we find the pair for limit-weight in hashtable
        key_index = hash_table_retrieve(ht,pair)
        if key_index is not None:
            #return (larger_number_index, smaller_number_index)
            if key_index > index:
                return (key_index, index)
            else:
                return (index, key_index)
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# print(get_indices_of_item_weights(weights_4, 9, 40))


