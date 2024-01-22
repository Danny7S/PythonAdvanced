import math
from collections import deque
from math import floor

operators=["*", "+", "-", "/"]
numbers=deque()
expression=deque(input().split())

while len(expression)>1 or numbers:
    current_part=expression.popleft()

    if current_part not in operators:
        numbers.append(int(current_part))

    else:
        if current_part=='+':
            while len(numbers)>1:
                first_num=numbers.popleft()
                second_num=numbers.popleft()
                new_num=first_num+second_num
                numbers.appendleft(new_num)

            expression.appendleft(numbers.popleft())

        elif current_part=='-':
            while len(numbers)>1:
                first_num=numbers.popleft()
                second_num=numbers.popleft()
                new_num = (first_num - second_num)
                numbers.appendleft(new_num)

            expression.appendleft(numbers.popleft())

        elif current_part == '*':
            while len(numbers) > 1:
                first_num = numbers.popleft()
                second_num = numbers.popleft()
                new_num = first_num * second_num
                numbers.appendleft(new_num)

            expression.appendleft(numbers.popleft())
        elif current_part == '/':
            while len(numbers) > 1:
                first_num = numbers.popleft()
                second_num = numbers.popleft()
                new_num=math.floor(first_num/second_num)
                numbers.appendleft(new_num)

            expression.appendleft(numbers.popleft())

print(*expression)

