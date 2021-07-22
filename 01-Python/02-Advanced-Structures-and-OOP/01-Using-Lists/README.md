# Using lists: Mathematics results

[List](https://docs.python.org/3/tutorial/introduction.html#lists) is a fundamental compound data type that you will find in almost every programming language (in other languages, we call it _Array_). A Python list holds elements (of any type) in memory. We can perform CRUD operations on it meaning that we can read a stored element, add an element, update an element and delete an element.

Lists are **indexed** by integers, with the first element being indexed at `0`. You can think of how it's stored in memory with the following diagram:

```python
words = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
```

![](https://res.cloudinary.com/wagon/image/upload/v1562058697/list_ttgeba.png)

Lists have some great properties:

- They are **ordered** thanks to their indexes
- They can contain any number of arbitrary objects (integer, float, string or even list and dictionaries as well!)
- List elements can be accessed by their index
- Lists are mutable & dynamic (you can change them and add any number of elements you want without worrying about memory management)

## Exercises
In this exercise, you are going to work with results (ranging from 0 to 10) of a mathematics exam passed by a few student.
Therefore, you'll use two lists parameters (`students` & `results`) in most of your functions:
- the first one contains all students
- the second one contains lists composed with the students who _passed_ the course and their result

The later one is called a **nested** array, you can access the sub lists contained in a list the same way you do for a simple list and mixing in a bit of substitution.

E.g.: To access the second element of the first list in `ids` (the age of our first character)
```python
ids = [['Jane Doe', 24], ['John Doe', 36]]
print(ids[0][1])  # Would print 24
```

Note that we first reach the first list and then reach the desired element within. Also the index always start at 0 which means that the second element will have the index *1*.

Now that you're set, you'll have to answer to a few questions to manage this data!

## Hints
Here are some hints to help you if you are stuck 👇

<details><summary markdown='span'>Exercise 1
</summary>
You have first to loop through the list, to do so use the `for` loop.
Then you'll have to check if the first letter is matching the parameter or not, to do so use indexes.
</details>


<details><summary markdown='span'>Exercise 2
</summary>
If you know the position of each element, you have access to them with their index! Read the reminder above ;-)
If you don't, as in the first exercise, you'll have to loop through the list to find what you are looking for!
</details>

<details><summary markdown='span'>Exercise 4
</summary>
You have to check which student has >= 5 points. After that, how can you add an element to a list?
</details>

<details><summary markdown='span'>Exercise 5
</summary>
The easiest way to perform that is to first create another list containing all student who _passed_ the exam, and then compare them to the `students` list.
</details>
