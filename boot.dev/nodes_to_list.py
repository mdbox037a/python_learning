class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def nodes_to_list(head):
    nodes_list = []
    while head is not None:
        nodes_list.append(head.value)
        head = head.next
    return nodes_list
