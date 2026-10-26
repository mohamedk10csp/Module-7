#Code Review 

##Initial Observations

1. Unclear Function and Variable Names

The names of functions and variables are not clear. The original code is named as 'do_math_stuff', 'do_string_stuff' , 'list1' and 'list2'. The names are not explicit of the use of functions and variables and are not descriptive enough. The code would be more readable if they could be renamed. 

2. Missing Documentation

There are no docstrings explaining the purpose, parameters, return value of the original functions. Other developers might want to read some code before understanding it because the code does not have docstrings.

3. Code Readability

Original code: The numbers and strings are processed using loops. There are certain parts that could be streamlined to make the code more readable and maintainable. Some variable names could be made more descriptive and the code could be better organized with the use of Python's features.

##Final Code Review 

1. Function and variable names
I renamed unclear actions such as do_math_stuff to process_numbers, and do_string_stuff to process_strings. I also changed the names of the variables such as list1 and list2 to numbers and strings. The names are given to make the purpose of the code easier to understand.

2. Documentation
I documented the function purpose in docstrings. The processing functions are also described with regard to the parameters and returns. My explanation of the calculations and string processing included comments. This results in the code being more readable and maintainable for other programmers.

3. Code Readability
I noted that I changed the original loops to list comprehensions and had more descriptive variable names. These changes reduced the code length and made it easier to understand without losing its functionality

**Testing & Verification
I ran the updated program in VS Code and checked that it was giving the same output as the original program, with no error. Processed Numbers: [3, 4, 9, 8, 15, 12, 21] 
Processed Strings: apple BANANA kiwi GRAPEFRUIT CHERRY 
The changes were overall, and solved the three original issues, as well as making the code more readable, documented and maintainable.
