# truth_table
A simple truth table generator that can generate values for boolean function.

# How it works
The truth table uses the "Shunting Yard" algorithm to evaluate the boolean function.
So far the precident order of operators follows (~, ^, &, |) which are
(not, xor, and, or) respectively.

# How to use
The Truth_Table class takes in two arguments, the boolean function as a string and
the number of distinct variables. Once you have the truth_table instance, you can pass
in a list of values into the ``process_postfix`` to evaluate the function.
# Issues
- So far the truth_table might not always generate the correct output for each function.
- <s>It isn't able to parse the ~ (not) symbol yet</s>
- <s>The valid expression checker does not raise an error when the unary operator ~ (not) is used as an operator between two variables</s>