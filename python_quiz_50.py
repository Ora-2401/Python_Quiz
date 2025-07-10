def ask_question(question, options, correct_option):
    print("\n" + question)
    for idx, option in enumerate(options):
        print(f"{chr(65 + idx)}. {option}")
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == chr(65 + correct_option):
        print("✅ Correct!\n")
        return 1
    else:
        print(f"❌ Incorrect. Correct answer: {chr(65 + correct_option)} - {options[correct_option]}\n")
        return 0

def main():
    score = 0
    total = 0

    print("🧠 Welcome to the Ultimate Python Quiz! (50 Questions)")
    input("Press Enter to begin...")

    # Section 1: Python Basics
    print("\n📘 SECTION 1: Python Basics")
    basics = [
        ("1. How do you print text in Python?", ["echo()", "print()", "printf()", "write()"], 1),
        ("2. Which symbol is used to write comments?", ["//", "#", "/* */", "--"], 1),
        ("3. Which of the following is a valid variable name?", ["1var", "var_1", "my-var", "def"], 1),
        ("4. What is the output of: print(5 + 3)?", ["8", "53", "Error", "None"], 0),
        ("5. How do you create a string?", ['str = "Hello"', "str = Hello", "str = 'Hello", "str = Hello'"], 0),
        ("6. What is the correct file extension for Python files?", [".pyth", ".pt", ".py", ".p"], 2),
        ("7. What does the input() function do?", ["Outputs text", "Receives user input", "Creates variables", "Ends program"], 1),
        ("8. What is the correct way to convert a string to an integer?", ["int(str)", "str(int)", "toInt()", "convert()"], 0),
        ("9. Which of these is not a Python keyword?", ["while", "if", "do", "def"], 2),
        ("10. What is indentation used for in Python?", ["Code style", "Separating lines", "Code structure", "Looping"], 2),
        ("11. What will `type(5.0)` return?", ["int", "float", "str", "double"], 1),
        ("12. How do you make a multi-line comment?", ["///", "'''", "/* */", "//"], 1),
        ("13. Which operator is used for exponentiation?", ["^", "**", "//", "exp()"], 1),
    ]
    for q in basics:
        score += ask_question(*q)
    total += len(basics)

    # Section 2: Data Structures
    print("\n📗 SECTION 2: Python Data Structures")
    structures = [
        ("14. Which one is a list?", ["{1, 2, 3}", "[1, 2, 3]", "(1, 2, 3)", "None"], 1),
        ("15. Which structure uses key-value pairs?", ["List", "Tuple", "Set", "Dictionary"], 3),
        ("16. What is the index of 'b' in ['a', 'b', 'c']?", ["1", "2", "0", "3"], 0),
        ("17. What will `len({'a':1, 'b':2})` return?", ["1", "2", "3", "Error"], 1),
        ("18. How do you access the first element in a list `mylist`?", ["mylist[1]", "mylist(0)", "mylist[0]", "mylist.first()"], 2),
        ("19. What does the `pop()` method do?", ["Adds to end", "Removes from start", "Removes last", "Sorts list"], 2),
        ("20. Which data structure is ordered and immutable?", ["List", "Set", "Tuple", "Dict"], 2),
        ("21. What does `set([1,2,2,3])` return?", ["[1,2,2,3]", "{1,2,3}", "(1,2,3)", "{1,2,2,3}"], 1),
        ("22. Which one allows duplicates?", ["Set", "List", "Dict", "None"], 1),
        ("23. What’s the output of `len([[], [1], [2,3]])`?", ["3", "2", "1", "4"], 0),
        ("24. How do you create an empty dictionary?", ["{}", "[]", "()", "set()"], 0),
        ("25. What’s the output of `(1, 2) + (3,)`?", ["(1, 2, 3)", "[1, 2, 3]", "Error", "None"], 0),
        ("26. How do you access a value in a dictionary?", ["dict.value()", "dict.key", "dict['key']", "dict[0]"], 2),
    ]
    for q in structures:
        score += ask_question(*q)
    total += len(structures)

    # Section 3: Programming Fundamentals
    print("\n📙 SECTION 3: Programming Fundamentals")
    programming = [
        ("27. What does `if` do?", ["Loop", "Branch", "Import", "Function"], 1),
        ("28. What is the result of `5 == 5`?", ["True", "False", "None", "Error"], 0),
        ("29. How do you define a function?", ["func myFunc():", "def myFunc():", "function myFunc():", "define myFunc()"], 1),
        ("30. What does `return` do in a function?", ["Prints result", "Exits loop", "Returns value", "Starts loop"], 2),
        ("31. What’s the output of `3 > 2 and 2 > 1`?", ["True", "False", "Error", "None"], 0),
        ("32. What’s the output of `not True`?", ["True", "False", "None", "Error"], 1),
        ("33. Which of these is a loop?", ["if", "for", "def", "import"], 1),
        ("34. What keyword exits a loop?", ["end", "exit", "break", "close"], 2),
        ("35. How do you skip to the next loop iteration?", ["stop", "pass", "skip", "continue"], 3),
        ("36. What is a parameter?", ["Function return", "Function name", "Input to function", "Output"], 2),
        ("37. What will `range(0, 3)` produce?", ["[0,1,2]", "[1,2,3]", "[0,1,2,3]", "[1,2]"], 0),
        ("38. Which one is not a comparison operator?", ["==", "!=", "=>", "<="], 2),
    ]
    for q in programming:
        score += ask_question(*q)
    total += len(programming)

    # Section 4: Working with Data Collections
    print("\n📕 SECTION 4: Working with Data Collections")
    data_collections = [
        ("39. Which function gives number of list items?", ["length()", "count()", "len()", "size()"], 2),
        ("40. What does `append()` do?", ["Removes element", "Adds to end", "Clears list", "Sorts list"], 1),
        ("41. What’s the result of `[1,2] + [3]`?", ["[1,2,3]", "[1,5]", "[1,2,3,3]", "Error"], 0),
        ("42. What method removes an item by value?", ["remove()", "pop()", "delete()", "discard()"], 0),
        ("43. What’s the result of `' '.join(['Hi','there'])`?", ["Hi there", "Hithere", "['Hi', 'there']", "Hi,there"], 0),
        ("44. What’s the output of `'abc'.upper()`?", ["abc", "ABC", "Abc", "error"], 1),
        ("45. Which method checks if list contains an item?", ["has()", "in", "contains()", "exist()"], 1),
        ("46. What’s the output of `sorted([3,1,2])`?", ["[3,1,2]", "[1,2,3]", "[2,1,3]", "None"], 1),
        ("47. Which method removes the last list element?", ["del()", "remove()", "pop()", "cut()"], 2),
        ("48. Which method can be used to copy a list?", ["copy()", "clone()", "duplicate()", "slice()"], 0),
        ("49. What does `list.clear()` do?", ["Deletes list", "Clears items", "Sorts list", "Adds items"], 1),
        ("50. Which of these can store different data types?", ["Set", "Tuple", "List", "All"], 3),
    ]
    for q in data_collections:
        score += ask_question(*q)
    total += len(data_collections)

    print(f"\n🎉 Quiz Completed! Your Score: {score}/{total}")
    if score == total:
        print("🏆 Perfect! Python Master!")
    elif score >= total * 0.8:
        print("✅ Great job! You're getting it.")
    elif score >= total * 0.6:
        print("👍 Not bad, but review the basics.")
    else:
        print("📚 Keep practicing and you'll improve!")

if __name__ == "__main__":
    main()
