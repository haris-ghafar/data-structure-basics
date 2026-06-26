
## Time Complexity

Time complexity describes how the running time of an algorithm changes as the input size (`n`) increases. It helps us compare the efficiency of different operations and choose the most suitable data structure or algorithm.

### What is Big O Notation?

**Big O (`O`) notation** measures the **worst-case performance** of an operation. It doesn't represent the exact execution time in seconds; instead, it shows how the running time grows as the amount of data increases.

---

## O(1) — Constant Time

An operation takes the **same amount of time** regardless of the number of elements.

**Example:**

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[2])
```

Whether the list contains **5**, **5,000**, or **5 million** elements, accessing `numbers[2]` takes approximately the same time.

**Common O(1) Operations**

* Access a list element by index
* Dictionary lookup (`dict[key]`) *(average case)*
* Set lookup (`value in set`) *(average case)*
* Stack `push` and `pop`
* Queue `enqueue` and `dequeue` (using `deque`)

---

## O(n) — Linear Time

The running time increases **linearly** with the number of elements.

**Example:**

```python
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 40:
        print("Found")
```

If the list grows, the number of comparisons also grows.

**Common O(n) Operations**

* Searching in a list
* Iterating through a list
* Inserting into the middle of a list
* Removing an element from the middle of a list

---

## O(log n) — Logarithmic Time

The running time grows **very slowly** because the search space is reduced by half in each step.

**Example:**

**Binary Search** on a sorted list.

Instead of checking every element, Binary Search repeatedly divides the search space into two halves.

Examples:

* 16 elements → ~4 steps
* 32 elements → ~5 steps
* 1,024 elements → ~10 steps

---

## O(n²) — Quadratic Time

The running time grows rapidly because each element is compared with many other elements.

**Example:**

```python
numbers = [1, 2, 3]

for i in numbers:
    for j in numbers:
        print(i, j)
```

As the number of elements increases, the total number of operations increases significantly.

This complexity is commonly seen in algorithms like **Bubble Sort**.

---

## Quick Summary

| Time Complexity | Meaning          | Example                          |
| --------------- | ---------------- | -------------------------------- |
| **O(1)**        | Constant time    | Access a list element by index   |
| **O(log n)**    | Logarithmic time | Binary Search                    |
| **O(n)**        | Linear time      | Search or iterate through a list |
| **O(n²)**       | Quadratic time   | Nested loops, Bubble Sort        |




## DATA STRUCTURE


## Lists

It stores multiple items in a single variable . Lists are **mutable**, meaning their contents can be modified after creation by adding, removing, or updating elements.

Lists can store different data types, including integers, strings, floating-point numbers, and even other lists.

### Creating a List

```python
fruits = ["Apple", "Banana", "Orange"]
```

### Common Operations

### Common List Operations

### Common List Operations

**Create a List**

```python
fruits = ["Apple", "Banana", "Orange"]
```

**Access an Element**

```python
print(fruits[0])      # Apple
print(fruits[-1])     # Orange
```

**Add an Element**

```python
fruits.append("Mango")
```

**Insert an Element**

```python
fruits.insert(1, "Grapes")
```

**Update an Element**

```python
fruits[0] = "Pineapple"
```

**Remove an Element**

```python
fruits.remove("Banana")
```

**Remove the Last Element**

```python
fruits.pop()
```

**Find the Length**

```python
len(fruits)
```

**Check if an Element Exists**

```python
"Orange" in fruits
```

**Iterate Through the List**

```python
for fruit in fruits:
    print(fruit)
```

**Sort a List**

```python
fruits.sort()
```

**Reverse a List**

```python
fruits.reverse()
```
### Time Complexity

* **Access an element by index:** `O(1)`
* **Search for an element:** `O(n)`
* **Append an element:** `O(1)` *(average)*
* **Insert at a specific position:** `O(n)`
* **Remove an element:** `O(n)`
* **Iterate through the list:** `O(n)`


## Dictionary (Hash Map)

A **dictionary** stores data as **key-value pairs**. Each key must be unique and is used to access its corresponding value. Dictionaries are mutable, which means you can add, update, or remove key-value pairs.

### Common Dictionary Operations

**Create a Dictionary**

```python
student = {
    "name": "Haris",
    "age": 20
}
```

**Access a Value**

```python
print(student["name"])
print(student.get("age"))
```

**Add a Key-Value Pair**

```python
student["city"] = "Rahim Yar Khan"
```

**Update a Value**

```python
student["age"] = 21
```

**Remove a Key-Value Pair**

```python
student.pop("age")
```

**Get All Keys**

```python
student.keys()
```

**Get All Values**

```python
student.values()
```

**Iterate Through a Dictionary**

```python
for key, value in student.items():
    print(key, value)
```

### Time Complexity

* **Lookup by key:** `O(1)` *(average)*
* **Insert a key-value pair:** `O(1)` *(average)*
* **Update a value:** `O(1)` *(average)*
* **Delete a key-value pair:** `O(1)` *(average)*
* **Iterate through the dictionary:** `O(n)`




## Stack

A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle. The last element added to the stack is the first one to be removed. In Python, a stack is commonly implemented using a list.

### Common Stack Operations

**Create a Stack**

```python
stack = []
```

**Push (Add an Element)**

```python
stack.append(10)
```

**Pop (Remove the Top Element)**

```python
stack.pop()
```

**Peek (View the Top Element)**

```python
print(stack[-1])
```

**Check if the Stack is Empty**

```python
len(stack) == 0
```

**Get the Stack Size**

```python
len(stack)
```

**Iterate Through the Stack**

```python
for item in stack:
    print(item)
```

### Time Complexity

* **Push:** `O(1)`
* **Pop:** `O(1)`
* **Peek:** `O(1)`
* **Check if Empty:** `O(1)`
* **Get Size:** `O(1)`
* **Iterate through the stack:** `O(n)`




## Queue

A **queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle. The first element added to the queue is the first one to be removed. In Python, a queue is commonly implemented using `collections.deque`.

### Common Queue Operations

**Create a Queue**

```python
from collections import deque

queue = deque()
```

**Enqueue (Add an Element)**

```python
queue.append(10)
```

**Dequeue (Remove the Front Element)**

```python
queue.popleft()
```

**Peek (View the Front Element)**

```python
print(queue[0])
```

**Check if the Queue is Empty**

```python
len(queue) == 0
```

**Get the Queue Size**

```python
len(queue)
```

**Iterate Through the Queue**

```python
for item in queue:
    print(item)
```

### Time Complexity

* **Enqueue:** `O(1)`
* **Dequeue:** `O(1)`
* **Peek:** `O(1)`
* **Check if Empty:** `O(1)`
* **Get Size:** `O(1)`
* **Iterate through the queue:** `O(n)`
