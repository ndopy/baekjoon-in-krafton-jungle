from typing import Any

class FixedQueue:

    class Empty(Exception):
        """비어 있는 FixedQueue 에서 디큐 또는 피크할 때 내보내는 예외 처리"""
        pass

    class Full(Exception):
        """가득 차 있는 FixedQueue 에서 인큐할 때 내보내는 예외 처리"""
        pass

    def __init__(self, capacity: int) -> None:
        """큐 초기화"""
        self.no = 0                     # 현재 데이터 개수.
                                        # front 와 rear 의 값이 같을 경우, 큐가 비어 있는지 혹은 가득 차 있는지를 구별하기 위해 필요하다.
        self.front = 0                  # 맨 앞 원소 커서 = 맨 앞 원소의 인덱스
        self.rear = 0                   # 가장 마지막에 넣은 맨 끝 원소의 바로 다음 인덱스
                                        # = 다음 인큐 때 데이터를 저장할 원소의 인덱스
        self.capacity = capacity        # 큐의 크기
        self.que = [None] * capacity    # 큐의 본체

    def __len__(self) -> int:
        """큐에 있는 모든 데이터 개수를 반환"""
        return self.no

    def is_empty(self) -> bool:
        """큐가 비어있는지 판단"""
        return self.no == 0

    def is_full(self) -> bool:
        """큐가 가득 차 있는지 판단"""
        return self.no == self.capacity

    def enqueue_item(self, x: Any) -> None:
        """데이터 x를 인큐"""
        if self.is_full():                  # 큐가 가득 차 있는 경우 예외 처리 발생
            raise FixedQueue.Full

        self.que[self.rear] = x             # rear = 마지막 데이터가 들어가야 할 위치
        self.rear += 1                      # 마지막 데이터를 넣었으므로, 그 다음 위치로 업데이트
        self.no += 1                        # 데이터를 넣었으므로 개수 +1 증가

        # rear += 1 의 결과가 capacity 와 같다면 배열 인덱스의 한계를 벗어나게 된다.
        # 따라서 이 때는 rear 를 배열의 맨 앞 인덱스인 0으로 되돌린다.
        if self.rear == self.capacity:
            self.rear = 0

    def dequeue_item(self) -> Any:
        """데이터를 디큐"""
        if self.is_empty():
            raise FixedQueue.Empty

        # 디큐 = 가장 먼저 들어간 데이터를 꺼내는 작업
        x = self.que[self.front]

        self.front += 1         # 맨 앞 요소가 나갔으므로, 그 다음 요소를 맨 앞 요소로 지정한다.
        self.no -= 1            # 데이터를 하나 꺼냈으므로 개수 -1 처리

        # front += 1 전에 front 가 배열의 맨 끝인 경우, +1 하게 되면
        # 그 값이 capacity 와 같아지고, 배열의 인덱스 한계를 벗어나게 된다.
        # 따라서 front 를 맨 앞 인덱스인 0으로 되돌린다.
        if self.front == self.capacity:
            self.front = 0

        return x

    def peek(self) -> Any:
        """큐에서 데이터를 피크(맨 앞 데이터를 들여다 봄)"""
        if self.is_empty():
            raise FixedQueue.Empty

        return self.que[self.front]

cards_count = int(input())

queue = FixedQueue(cards_count)

# 숫자를 1부터 cards_count 까지 추가하기
for idx in range(1, cards_count + 1):
    queue.enqueue_item(idx)

while queue.no > 1:
    queue.dequeue_item()
    x = queue.dequeue_item()
    queue.enqueue_item(x)

print(queue.peek())