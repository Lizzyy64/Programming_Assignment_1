"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data
import math
from math import sqrt 


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # TODO: Purpose: counts the vowels in a string
    # TODO: Input(s): it is the string we use to count the vowels in
    # TODO: Output: It will return an int of the amount of vowels in text
    vowel = "aeiou"
    count = 0
    for char in text:
        if char.lower() in vowel:
            count += 1
    return count



# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: it checks to see if a nested list has a length 
    # of 2 and puts it in a new list
    # TODO: Input(s): they are items, a list of lists of integers
    # TODO: Output: A new list that contains only the nested lists
    # with a length of 2, in their original order
    new_list = []
    for item in items:
        if len(item) == 2:
            new_list.append(item)
    return new_list

    
# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: creates a new list where it appends the nested lists in the 
    # argument and if it has a length of 2, it will arrange into non-descending
    # order and append to the new list
    # TODO: Input(s): items, lists inside of a list of integers
    # TODO: Output: A new list of nested lists in our argument, but
    # if they have a length of 2, it will append into our
    # new list into non-descending order
    new_list = []
    for item in items:
        if len(item) == 2:
            if item[0] <= item[1]:
                non_descending = [item[0], item[1]]
                new_list.append(non_descending)
            else:
                non_descending = [item[1], item[0]]
                new_list.append(non_descending)
        else:
            new_list.append(item[:])
    return new_list

# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: finds the total of two prices, carrying any extra cents
    # over into dollars
    # TODO: Input(s): first is the first price to add and second is the second
    # price to add
    # TODO: Output: A new price whose value is the sum of the first and 
    # second price with cents always between 0-99.
    total_cents = first.cents + second.cents
    total_dollars = first.dollars + second.dollars + total_cents // 100
    return data.Price(total_dollars, total_cents % 100)


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: fidns the area of the rectangle from its corner points
    # TODO: Input(s): rectangle defined by its top-left and bottom-right
    # corner points
    # TODO: Output: The area of the rectangle
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.bottom_right.y - rectangle.top_left.y
    return width * height


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: Finds all books in a collection that were written by 
    # a given author
    # TODO: Input(s): author is the name of the author to search for
    # bookd is the list of books to search through 
    # TODO: Output: A list of the books that include the given author
    result: list[Book] = []
    for book in books:
        if author in book.authors:
            result.append(book)
    return result


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: computes the smallest cirle that completely contains
    # a rectangle
    # TODO: Input(s): rectangle is a rectangle defined by its top-left
    # and bottom-right corners
    # TODO: Output: A cricle that bounds the rectangle, so all four
    # corners lie on or inside the circle
    x1, y1 = rectangle.top_left.x, rectangle.top_left.y
    x2, y2 = rectangle.bottom_right.x, rectangle.bottom_right.y
    center = data.Point((x1 + x2) / 2, (y1 + y2) / 2)
    radius = math.sqrt((x2-x1) ** 2 + (y2 - y1)**2) / 2
    return data.Circle(center, radius)


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: Finds the employees who earn less than the average
    # rate of the whole group
    # TODO: Input(s): employees is the list of employees to compare
    # TODO: Output: A list of the names of employees whose pay_rate is 
    # below the average. Returns empty list if the input is empty or no one
    # is below average
    if not employees:
        return []

    average = sum(e.pay_rate for e in employees) / len(employees)
    return [e.name for e in employees if e.pay_rate < average]