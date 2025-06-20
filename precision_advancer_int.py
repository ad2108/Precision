# --------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Precision advancer with integer vales
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --------------------------------------------------

# --------------------------------------------------
# Author: ad2108
# Version: 1.0
# Date: 2025-06-15
# License: MIT
# 
# Description:
#   Functions to work with floats as integers and boost precision
# --------------------------------------------------

# --------------------------------------------------
# Convert float to integer through string manipulations
# Return a tuple with 2 integers that represent the float
# Example: 1.23 -> (123, -2)
def to_int(x: float or str):

    # Extract values after the dot for the factor
    # If string use direct string manipulations
    # without conversion
    if type(x) == str:
      spl = x.split('.') if '.' in x else None
    elif type(x) == float:
      spl = str(x).split('.') if '.' in str(x) else None
    else:
      raise TypeError('Only float or string supported')
      

    # The factor * -1 equals the length of the values after the .
    length = int(len(spl[1])) if spl[1]!=None else 0

    # return a tuple with the float times 10^{-factor} and the factor
    return (int(str(spl[0]) + str(spl[1])), -length) #return (int, int)

# --------------------------------------------------
# Convert the number back from the tuple
# Returns a float
# Example: (1234, -2) -> 12.34
def from_int(tup):

    # Split the tuple to number and factor
    numb, fac = tup

    # The first result is the number \cdot 10^{factor}
    res1 = float(numb*10**fac)

    # If the number is negative a boolean value is set to True
    # And get rid of the negative number
    is_negative = False
    if numb <= 0:
      is_negative = True
      numb = abs(numb)

    # If the factor is smaller than the number res2 can be
    # created directly ((12, -1) -> 1.2)
    if abs(fac) <= len(str(numb)):
        res2 = float(str(numb)[0:fac] + '.' + str(numb)[fac:])

    # If the factor is bigger than the number, 0 need to be added to
    # the string before evaluating ((12, -3) -> 0.012)
    else:
        diff = abs(fac)-len(str(numb))
        str_numb = diff*'0' + str(numb)
        res2 = float(str_numb[0:fac] + '.' + str_numb[fac:])

    # To get rid of any calculation errors the difference
    # between res1 and res2 is added to to res1
    res = res1+(res2-res1) if  res2-res1 != 0 else res1

    # If number was negative return negative number
    if is_negative == True:
      return -res
    else:
      return res

# --------------------------------------------------
# Decorator to return the result of a function in (numb, fac) notation
def dec_to_int(func):

    # Wrapper function
    def wrapper(*args):

        # Calculation of the result
        result = func(*args)

        # If the result is a number the function to_int can be applied
        if type(result) == float or type(result) == int:
            return to_int(result)

        # Otherwise the function to_int can not be applied and a TypeError is raised
        else:
            raise TypeError('Result of the function is neither float nor int')
    return wrapper


# --------------------------------------------------
# Decorator to return the result of a function as a float if (numb, fac) notation was used
def dec_from_int(func):

    # Wrapper function
    def wrapper(*args):

        # Calculation of the result
        result = func(*args)

        # If the result has the (numb, fac) notation from_int is applied
        if type(result) == tuple and len(result) == 2:
            return from_int(result)

        # Otherwise the function from_int can not be applied and a TypeError is raised
        else:
            raise TypeError('Result of function is not a tuple with (numb, fac): int')
    return wrapper

# --------------------------------------------------
# Find the smallest factor in a list of values with the (numb, fac) notation
# The factor is in most cases negative therefore the smallest is the important
def __sm_factor__(lst: list):

    # small is initialised with factor 0
    small = 0

    # Enumeration through the list of values
    # If fac is smaller that the previous small
    # it gets stored in small
    for tup in lst:
        numb, fac = tup
        small = fac if fac<=small else small

    # Return of the smallest factor
    return small

# --------------------------------------------------
# Adjust a list of values to the smallest factor
# This is important for Addition and subtraction of values in
# (numb, fac) notation
def __refactor__(lst):

    # Find the smallest factor and create the resultlist
    sm_fac = __sm_factor__(lst)
    new_lst = []

    # Enumerate through the list and adjust numb and fac
    # to the smallest fac
    for tup in lst:
        numb, fac = tup
        numb *= 10**(abs(sm_fac)-abs(fac))
        new_lst.append((int(numb), int(sm_fac)))

    # Return the resulting list
    return new_lst

# --------------------------------------------------
# Add numbers in (numb, fac) notation
def add(*args):

  # Append args to a lst
  lst = []
  for arg in args:
    lst.append(arg)

  # Refactor all the list to the smallest factor
  lst = __refactor__(lst)

  # Sum all numbs through a loop
  result = 0
  for tup in lst:
    numb, fac = tup
    result += numb

  # Return the sum of the numbs and the fac
  return (result, fac)
    
# --------------------------------------------------
# Subtract numbers in (numb, fac) notation
def sub(*args):

  # Append args to a lst
  lst = []
  for arg in args:
    lst.append(arg)

  # Refactor all the list to the smallest factor
  lst = __refactor__(lst)

  # Subtract all numbs from the first through a loop
  result = 0
  is_first = True
  for tup in lst:
    numb, fac = tup
    if is_first == True:
      result += numb
      is_first = False
    else:
      result -= numb

  # Return the sum of the numbs and the fac
  return (result, fac)

# --------------------------------------------------
# Multiply numbers in (numb, fac) notation
def mul(*args):

  # Extract the numbers and the factors to two lists
  numb = []
  fac = []
  for arg in args:
    numb.append(arg[0])
    fac.append(arg[1])

  # Loop through the numbers
  # Result stores the values of the multiplication
  # Factor stores the sum of the factors
  # Example: 1*10^{-1}*2*10^2 = 2*10^{2-1}
  result = 1
  factor = 0
  for i in range(len(numb)):
    result *= numb[i]
    factor += fac[i]

  # Return the result of the numbs and sum of the factors
  return (result, factor)

# --------------------------------------------------
# Divide numbers in (numb, fac) notation
def div(*args):

  # Extract the numbers and the factors to two lists
  numb = []
  fac = []
  for arg in args:
    numb.append(arg[0])
    fac.append(arg[1])

  # Loop through the numbers
  # Result stores the values of the division
  # Factor stores the sum of the factors
  # Example: 1*10^{-1}/2*10^2 = 1/2*10^{-2-1}
  # The factor of the divider changes from fac to -fac !!!
  result = 1
  factor = 0
  is_first = True
  for i in range(len(numb)):
    if is_first:
      result *= numb[i]
      factor += fac[i]
      is_first = False
    else:
      result /= numb[i]
      factor -= fac[i]

  # Return the result of the numbs and sum of the factors
  return (result, factor)

# --------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# End of file
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --------------------------------------------------

