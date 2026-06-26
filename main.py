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

for key in student:  # iterating through dictionary
    print(key, ":", student[key])
