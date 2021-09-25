# pylint: disable=missing-docstring

# Warning:
# - One line of code for each method
# - Just look in the doc for the right method of the String class!

def add_comma(a_string):
    """
    returns a copy of the string with every word separated by a comma
    example: add_comma("John Peter Jude") => "John, Peter, Jude"
    """
<<<<<<< HEAD
    return ", ".join(a_string.split())
=======
    pass  # YOUR CODE HERE
>>>>>>> 0782c767536f39d257c82e4fa630528b55d96c35

def belongs_to(a_string, a_word):
    """
    returns True if a_string contains a_word
    example: belongs_to("hey jude", "jude") => True
    """
<<<<<<< HEAD
    return a_word in a_string
=======
    pass  # YOUR CODE HERE
>>>>>>> 0782c767536f39d257c82e4fa630528b55d96c35

def count_repetition(a_string, a_substring):
    """
    returns how many times a_substring occurs in a_string
    example: count_repetition("000123000123", "0") => 6
    """
<<<<<<< HEAD
    return list(a_string).count(a_substring)
=======
    pass  # YOUR CODE HERE
>>>>>>> 0782c767536f39d257c82e4fa630528b55d96c35

def is_a_question(a_string):
    """
    returns True if a_string ends with a "?"
    example: is_a_question("How are you?") => True
    """
<<<<<<< HEAD
    return a_string.endswith("?")
=======
    pass  # YOUR CODE HERE
>>>>>>> 0782c767536f39d257c82e4fa630528b55d96c35

def remove_surrounding_whitespaces(a_string):
    """
    returns a copy of the string with leading and trailing whitespaces removed
    example: delete_surrounding_whitespaces("  hey yo  ") => "hey yo"
    """
<<<<<<< HEAD
    return a_string.strip()
=======
    pass  # YOUR CODE HERE
>>>>>>> 0782c767536f39d257c82e4fa630528b55d96c35

def replace(initial_string, old_letter, new_letter):
    """
    returns a copy of the string with the new letter replacing the old one
    example: replace("casanova", "a", "o") => "cosonovo"
    """
<<<<<<< HEAD
    return initial_string.replace(old_letter, new_letter)
=======
    pass  # YOUR CODE HERE
>>>>>>> 0782c767536f39d257c82e4fa630528b55d96c35

def full_description_concatenation(first_name, last_name, age):
    """
    returns a sentence with the first_name and the last_name capitalized and
     the age using concatenation
    example: full_description_concatenation("john", "doe", 33) => "John Doe is 33"
    """
<<<<<<< HEAD
    return first_name.capitalize() + " " + last_name.capitalize() + " is " + str(age)
=======
    pass  # YOUR CODE HERE
>>>>>>> 0782c767536f39d257c82e4fa630528b55d96c35

def full_description_formatting(first_name, last_name, age):
    """
    returns a sentence with the first_name and the last_name capitalized and
     the age using formatting
    example: full_description_formatting("john", "doe", 33) => "John Doe is 33"
    """
<<<<<<< HEAD
    return f"{first_name.capitalize()} {last_name.capitalize()} is {age}"
=======
    pass  # YOUR CODE HERE

>>>>>>> 0782c767536f39d257c82e4fa630528b55d96c35
