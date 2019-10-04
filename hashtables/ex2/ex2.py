#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length
    # build hashtable
    for ticket in tickets:
        s = ticket.source
        d = ticket.destination
        hash_table_insert(ht, s, d)
    # take_off = if source = None
    take_off = hash_table_retrieve(ht, "NONE")
    # print(take_off)
    # find first ticket, add to route
    route[0] = take_off

    # iterate through ht
    for i in range(1, length):
        #hashtable shuffle
        final_approach = hash_table_retrieve(ht, take_off)
        route[i] = final_approach
        take_off = final_approach 

    return route

ticket_1 = Ticket("PDX", "DCA")
ticket_2 = Ticket("NONE", "PDX")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

expected = ["PDX", "DCA", "NONE"]
print(reconstruct_trip(tickets, 3))