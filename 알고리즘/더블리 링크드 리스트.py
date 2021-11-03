class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_with_data(self, data):
        return

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정한다"""

        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        # index 번째 있는 노드로 간다
        for _ in range(index):
            iterator = iterator.next

        return iterator

    def __str__(self):
        res_str = "|"
        iterator = self.head

        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next
        return res_str

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, previous_node, data):
        new_node = Node(data)
        if previous_node.next is None:
            self.tail = new_node

        new_node.prev = previous_node
        new_node.next = previous_node.next
        previous_node.next = new_node
        previous_node.next.prev = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""
        data = self.head.data
        if self.head is not None:
            if node_to_delete is self.head:
                # self.head.next.prev = None
                self.head = self.head.next
                return data

            elif node_to_delete is self.tail:
                self.tail.prev.next = None
                self.tail = node_to_delete.prev
            else:
                node_to_delete.next.prev = node_to_delete.next.prev.prev
                node_to_delete.prev.next = node_to_delete.prev.next.next
        
