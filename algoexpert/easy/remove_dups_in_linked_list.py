# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_duplicates_from_linked_list(linked_list):
    curr = linked_list
    while curr:
        next_uniq = curr.next
        while next_uniq and next_uniq.value == curr.value:
            next_uniq = next_uniq.next
        curr.next = next_uniq
        curr = next_uniq
    return linked_list   


def main():
    pass

if __name__ == "__main__":
    main()