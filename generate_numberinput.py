def generate(n : int) -> dict:
    """
    Generates all the number inputs for n seperate variables.
    n can NOT be > 26.
    @param an integer n that is the number of different variables.
    @returns a dictionary that contains all the possible combinations for
    each letter. (A->(A + n))
    """
    if n > 26:
        raise ValueError('Number is too large.')
    letters = generate_letters(n)
    keys = list(letters.keys())
    for index, letter in enumerate(reversed(keys)):
        for i in range(2 ** n):
           letters[letter].append(1 if (i % 2**(index+1) >= 2**index) else 0)
    return letters

def generate_letters(n: int) -> dict:
    """
    Generates all the letters for n variables (starts at A-> A+n in the alphabet).
    @param An integer n, number of different variables.
    @returns a dictionary that contains all the letters each initialised with
    an empty list.
    """
    start = 'A'
    dic = {}
    for i in range(n):
        dic[chr(ord(start) + i)] = []
    return dic

if __name__ == '__main__':
    n = input('Enter a number of variables: ')
    try:
        inputs = generate(int(n))
        print(list(zip(*inputs.keys())))
        for element in zip(*inputs.values()):
            print(element)
    except ValueError:
        print('ERROR: Please enter a valid int')