def addBinary( a, b):
    a1 = int(a, 2)  # Convert the first binary string to an integer
    b1 = int(b, 2)  # Convert the second binary string to an integer
    sums = a1 + b1  # Add the two integers
    result = bin(sums)[2:]  # Convert the sum back to a binary string, and strip the '0b' prefix
    res=print(result)  #printing the result
    return res # Return the binary sum as a string
addBinary("11","1")#  calling the function