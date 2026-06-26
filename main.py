# LIST EXAMPLE

marks=[90, 80, 70, 60, 50]

for mark in marks:   #iteration
    print(mark)

print(marks[2])  #accessing element at index 2

marks.append(40)   #add 40 in list
marks.remove(70)  #remove 70 from list
marks.sort()      #sort the list in ascending order
marks.insert(2, 75)  #insert 75 at index 2
marks.pop()      #remove last element from list
marks.pop(1)   #remove element at index 1


print("length of list is:", len(marks))  #length of list




# DICTIONARY EXAMPLE

student = {
    "name": "Haris",
    "age": 20,
    "grade": "A"
}


print(student["name"])  # accessing value for key "name"

student["age"] = 21  # updating value for key "age"

student["city"] = "Rahim Yar Khan"  # adding new key-value pair

for key in student.keys():  # iterating through dictionary to get keys
    print(key)


for value in student.values():  # iterating through dictionary to get values
    print(value)


for key, value in student.items():  # iterating through dictionary to get key-value pairs
    print(key, ":", value)


student.pop("grade")  # removing key-value pair with key "grade"


# TIME COMPLEXITY
"""
Dictionary
Lookup      O(1)
Insert      O(1)
Delete      O(1)

"""


#STACK EXAMPLE (LIFO)

stack = []

#push operation
stack.append(10)
stack.append(20)
stack.append(30)


peek = stack[-1]  # accessing the top element of the stack
print("Top element of stack is:", peek)



popped_element = stack.pop()  # removing the top/last element of the stack
print("Popped element from stack is:", popped_element)


"""
Time Complexity
Stack
Push        O(1)
Pop         O(1)
Peek        O(1)
"""




# QUEUE EXAMPLE (FIFO)

from collections import deque

# Creating an empty queue
queue = deque()

# Enqueue (Add elements)
queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")

print("Queue after Enqueue Operations:")
print(queue)

# Peek (View the front element)
print("\nFront Element:", queue[0])

# Dequeue (Remove the front element)
removed_item = queue.popleft()
print("\nRemoved Item:", removed_item)





"""
Time Complexity
Queue
Enqueue     O(1)
Dequeue     O(1)
Peek        O(1)
"""
