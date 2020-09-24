# linkedList에 저장할 데이터를 기억하는 클래스
class Node:
    def __init__(self, data = None):
        self.data = data # 실제 데이터
        self.next = None # 다음 데이터의 위치

# linkedList 자체를 의미하는 클래스
class LinkedList:
    def __init__(self):
        self.head = None # 리스트의 시작 위치
        self.count = 0 # 리스트에 저장된 데이터의 개수

    # 리스트의 맨 앞에 데이터를 추가하는 메소드
    def appendFirst(self, data):
        self.count += 1
        newData = Node(data)
        # LinkedList의 맨 앞에 데이터를 추가한다. 순서를 반드시 지켜야 한다.
        # 맨 앞에 삽입할 데이터의 다음 데이터를 기억하는 next에 head에 저장된
        # 값을 넣어준다.
        newData.next = self.head
        # head에 새로 삽입되는 데이터의 위치를 넣어준다.
        self.head = newData

    # 리스트의 맨 뒤에 데이터를 추가하는 메소드
    def appendLast(self, data):
        self.count += 1 # 리스트에 저장된 데이터의 개수를 증가시킨다.
        # 리스트의 맨 뒤에 추가할 데이터를 넘겨받아 Node 클래스의 객체로 만든다.
        newData = Node(data) # 리스트에 추가할 데이터의 객체를 생성한다.
        # 리스트가 비어있을 경우와 비어있지 않을 경우에 따라서 리스트에 데이터를
        # 추가하는 방법이 다르다.
        if self.head is None: # 리스트에 저장된 데이터가 없는가?
            # 리스트가 비어있으면 head 다음에 데이터를 추가시킨다.
            self.head = newData
            return # 데이터를 head 다음에 추가했으므로 함수를 종료한다.
        last = self.head # 리스트의 시작 위치를 저장한다.
        # head 부터 시작해서 리스트의 마지막 데이터로 이동한다.
        # last.next가 None이 아니면 True, None이면 False
        # 리스트의 마지막 데이터로 이동한다.
        while last.next: # 리스트에 저장된 다음 데이터가 있는가?
            last = last.next
        # 마지막 위치에 데이터를 추가한다.
        last.next = newData

    # 리스트의 특정 위치(position)에 데이터를 삽입하는 메소드
    def appendInsert(self, position, data):
        # 데이터가 삽입될 위치가 올바른가 검사한다.
        if position < 1 or position > self.count - 1:
            print("데이터를 삽입할 위치가 올바르지 않습니다.")
            return
        # 데이터가 삽입될 위치가 올바르므로 position 번째 위치에 데이터를 삽입한다.
        self.count += 1
        newData = Node(data)
        # 데이터가 삽입될 전 위치로 이동한다.
        node = self.head
        for i in range(position - 1):
            node = node.next
        # 데이터를 삽입할 위치를 찾았으므로 데이터를 삽입한다.
        #print(node.data)
        newData.next = node.next
        node.next = newData

    # 리스트에서 지정된 데이터를 제거하는 메소드
    def remove(self, data):
        node = self.head
        if node:
            # 제거할 데이터가 LinkedList 0번째 데이터일 경우
            if node.data == data:
                # 0번째 데이터의 다음 데이터의 위치를 head에 넣어준다.
                self.head = node.next
                # LinkedList에 저장된 데이터의 개수를 감소시킨다.
                self.count -= 1
                return
            # 제거할 데이터가 LinkedList 1번째 데이터 이후일 경우
            # 제거할 데이터를 찾아서 제거한다.
            while node is not None:
                if node.data == data: # 제거할 데이터를 찾았는가?
                    break
                # 삭제할 데이터의 이전 데이터를 저장한다.
                prev = node
                # 다음 데이터로 이동한다.
                node = node.next
            # 제거할 데이터가 LinkedList에 없을 경우 처리
            if node == None:
                print("{}은(는) LinkedList에 존재하지 않습니다.".format(data))
                return
            # LinkedList에서 데이터를 제거한다.
            prev.next = node.next
            self.count -= 1
        else:
            print("LinkedList가 비어 있습니다.")

    # 리스트에서 특정 위치의 데이터를 제거하는 메소드
    def removeIndex(self, index):
        # 데이터를 삭제할 위치가 올바른가 검사한다.
        if index < 0 or index > self.count - 1:
            print("{}번째 데이터가 없어서 삭제 할 수 없습니다.".format(index))
            return
        node = self.head
        # 0번째 데이터를 삭제한다.
        if index == 0:
            self.head = node.next
            self.count -= 1
            return
        # 삭제할 데이터의 위치로 이동한다.
        for i in range(index):
            prev = node
            node = node.next
        print("삭제할 위치의 데이터는 {} 입니다.".format(node.data))
        prev.next = node.next
        self.count -= 1

    # 리스트에서 특정 위치의 데이터를 검색하는 메소드
    def searchIndex(self, index):
        # 검색할 데이터의 위치가 올바른가 검사한다.
        if index < 0 or index > self.count - 1:
            print("{}번째 데이터가 없어서 검색 할 수 없습니다.".format(index))
            return
        node = self.head
        # 삭제할 데이터의 위치로 이동한다.
        for i in range(index):
            node = node.next
        print("검색한 위치의 데이터는 {} 입니다.".format(node.data))

    # 리스트에서 특정 데이터를 검색해서 출현하는 위치를 출력하는 메소드
    def search(self, data):
        node = self.head
        count = 0
        while node is not None:
            if node.data == data:
                break
            prev = node
            node = node.next
            count += 1
        if node == None:
            print("{}은(는) LinkedList에 존재하지 않습니다.".format(data))
            return
        print("{}은(는) LinkedList의 {}번째 위치에 있습니다.".format(data, count))

    # 리스트에 저장된 모든 데이터를 출력하는 메소드
    def listPrint(self):
        node = self.head
        # node가 None이 아니면 True, None이면 False
        if node:
            print("{}개의 데이터가 LinkedList에 저장되어 있습니다.".format(self.count))
            # LinkedList에 저장된 데이터의 개수 만큼 반복한다
            for i in range(self.count):
                print(node.data, end = " ") # 데이터를 출력한다.
                node = node.next # 다음에 출력할 데이터로 이동한다.
            print() # LinkedList에 저장된 데이터를 한 줄로 출력한 후 줄을 바꾼다.
        else:
            print("LinkedList에 저장된 데이터가 없습니다.")
            
if __name__ == "__main__":
    # LinkedList를 만든다.
    list = LinkedList()
    list.listPrint()
    list.remove("사요일")
    print("=======================================================")
    # LinkedList의 맨 뒤에 데이터를 추가한다.
    list.appendLast("일요일")
    list.listPrint()
    list.appendLast("이요일")
    list.listPrint()
    list.appendLast("삼요일")
    list.listPrint()
    print("=======================================================")
    # LinkedList의 맨 앞에 데이터를 삽입한다.
    list.appendFirst("사요일")
    list.listPrint()
    list.appendFirst("오요일")
    list.listPrint()
    print("=======================================================")
    # LinkedList의 특정 위치에 데이터를 삽입한다.
    list.appendInsert(0, "육요일")
    list.appendInsert(5, "육요일")
    list.appendInsert(1, "육요일")
    list.listPrint()
    print("=======================================================")
    # LinkedList의 특정 데이터를 삭제한다.
    list.remove("오요일")
    list.listPrint()
    list.remove("칠요일")
    list.remove("일요일")
    list.listPrint()
    print("=======================================================")
    # LinkedList의 특정 위치의 데이터를 삭제한다.
    list.removeIndex(4)
    list.removeIndex(0)
    list.listPrint()
    list.removeIndex(1)
    list.listPrint()
    print("=======================================================")
    list.searchIndex(0)
    list.search("토요일")
    list.search("삼요일")
    list.search("사요일")
    

