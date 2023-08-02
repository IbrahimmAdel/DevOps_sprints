# Task 3 python
```
def balance_check(input_brackets):
    # Set opening brackets
    open_brackets = ['[', '{', '(']

    # set Matching Pairs
    matches = [('(', ')'), ('[', ']'), ('{', '}')]

    # set an empty stack
    stack = []

    # Check input brackets are even number of brackets or odd, if odd --> not balance
    if len(input_brackets) % 2 != 0:
        return False

    for bracket in input_brackets:

        # If it is an open bracket, append it to the stack
        if bracket in open_brackets:
            stack.append(bracket)

        else:
            # Check if there are open brackets in Stack or not
            if len(stack) == 0:
                return False

            # Check the last open bracket
            last_open = stack.pop()

            # Check if it has a closing match
            if (last_open, bracket) not in matches:
                return False

    return len(stack) == 0


while True:
    reply = input(print("do you want to enter an input or exit? [yes/no] "))
    if reply == 'no':
        break
    else:
        user_input = input(print("enter your characters: "))
        print(balance_check(user_input))
```

