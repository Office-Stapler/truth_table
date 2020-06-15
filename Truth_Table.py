from generate_numberinput import generate
class Truth_Table:
    """
    A class used to represent a Truth Table.

    Attributes:
    ----------
    function : str
        The boolean function as in its string form.

    inputs : dict
        All the possible input combination for each variable.
        E.g if n was 2 it would generate:
        { 
            'A': [0, 0, 1, 1],
            'B': [0, 1, 0, 1]
        }

    postfix : list
        The postfix queue to calculate the expression for each input.

    operators : list
        The list of possible operators in precident order
    
    variables : list
        List of all the possible variables from A -> A + n
    Methods
    --------
    generate_postfix(self)

    """
    def __init__(self, function : str, n : int):
        """ 
        Parameters
        ----------
        function : str
            The boolean function in its string form, the only valid operators
            are &,|,^ and ~ each representing and, or, xor and not respectively.
            Note:
            The function MUST have variables starting at A and going to A + n
            in the alphabet.
            If you have function = "A & D" but n is only 2 it will not work,
            since D is > A + n in the alphabet.

        n : int
            The number of different variables in the function from A -> A + n.
            Hence, n MUST be <= 26. 
        
        """
        self.operators = ['~', '^', '&', '|']
        self.function = function.upper().replace(' ', '')
        self.inputs = generate(n)
        self.variables = list(self.inputs.keys())
        if not self._check_valid_expr():
            raise ValueError('Expression is not valid')
        self.postfix = self._generate_postfix()
        self.output = self.process_all_inputs()

    def _check_valid_expr(self):
        """ 
        Uses a stack method to check whether the expression is valid

        Returns
        -------
        valid : bool
            Whether the expr is a valid expr
        """
        i = 0
        prevOperator = True
        prevVariable = False
        for char in self.function:
            if char == '(':
                i += 1
            elif char == ')':
                i -= 1
            elif char in self.variables: 
                if prevVariable:
                    return False
                prevVariable = True
                prevOperator = False
            elif char in self.operators:
                if prevOperator and char != '~':
                    return False
                prevVariable = False
                prevOperator = True
            else:
                return False
            if i < 0:
                return False
        self.function = self.function.replace('~~', '')
        return True
    def process_postfix(self, values):
        """
        Processes the instance's generated postfix queue.
        Parems:
        -------
        values: list(int)
            Values you'd liked to pass into the truth_table's function
            where each value maps to each variable respectively.
            E.g.
            if you have the variables [A, B, C]
            and gave values as [0,0,1]
            it'll sub:
            A -> 0
            B -> 0
            C -> 1
        
        Returns:
        --------
        output : int
            The evaluated function given the values mapped to each variable
            accordingly. 
            E.g. If the function is:
            A & B, and you passed in [0,1] into values,
            it'll sub A with 0 and B with 1
        """
        q = self.postfix[::]
        stack = []
        while len(q):
            obj = q.pop(0)
            if obj not in self.operators:
                obj = values[ord(obj) - ord('A')]
                stack.append(obj)
            else:
                num1 = stack.pop()
                num2 = stack.pop() if obj != '~' else None
                if obj == '|':
                    stack.append(num2 or num1)
                elif obj == '&':
                    stack.append(num2 and num1)
                elif obj == '^':
                    stack.append(num2 ^ num1)
        return stack.pop(0)
    def process_all_inputs(self)->list:
        """
        Processes all possible values for the function
        """
        output = []
        for values in list(zip(*self.inputs.values())):
            output.append(self.process_postfix(values))
        return output
    
    def print_truth_table(self):
        """
        Prints out the truth table
        """
        variables = self.variables[::]
        variables.append('output')
        print(' '.join(variables))
        for elements in list(zip(*self.inputs.values(), self.output)):
            print(elements)
    
    def _generate_postfix(self) -> list:
        """ 
        Uses Shunting Yard algorithm to generate a postfix queue that will
        later be used to evaluate all inputs of each variable.

        Returns
        -------
        postfix : list
            The generated queue to be used in calculating the truth_table
        """
        q = []
        stack = []
        for char in self.function:
            if char == '(':
                stack.append(char)
                continue
            elif char == ')':
                op = stack.pop()
                while op != '(':
                    q.append(op)
                    op = stack.pop()
            elif char in self.variables:
                q.append(char)
            else:
                if len(stack) == 0:
                    stack.append(char)
                    continue
                if stack[-1] == '(':
                    stack.append(char)
                    continue
                op1 = self.operators.index(stack[-1])
                op2 = self.operators.index(char)
                if op2 > op1:
                    q.append(stack.pop())
                stack.append(char)

        while len(stack) != 0:
            q.append(stack.pop())
        return q