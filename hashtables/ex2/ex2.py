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
    hashtable = HashTable(length)
    route = [None] * length

    for i in range(length):
        ticket = tickets[i]
        if ticket.source == "NONE":
            route[0] = ticket.destination
            continue
        hash_table_insert(hashtable, tickets[i].source, ticket.destination)

    for i in range(1, length-1):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route[:-1]

