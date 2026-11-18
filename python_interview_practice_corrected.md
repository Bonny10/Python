# Python Interview Practice -- Corrected Solutions

This document contains the nine Python interview questions, corrected
code, and brief explanations.

## 1. Reverse a string

``` python
text = "hello"
print(text[::-1])
```

**Output:**

``` text
olleh
```

**Explanation:** `[::-1]` uses slicing with a step of `-1`, which reads
the string from right to left.

## 2. Find duplicate elements in a list

``` python
numbers = [1, 2, 3, 2, 4, 5, 3, 6]
duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)
```

**Output:**

``` text
[2, 3]
```

**Explanation:** `numbers.count(num)` returns how many times `num`
appears. The condition `num not in duplicates` ensures each duplicate is
added only once.

**Note:** This approach is easy to understand, but can be slow for large
lists because `count()` scans the list each time.

## 3. Find the second-largest number in a list

``` python
numbers = [10, 25, 5, 40, 30]

greatest = float("-inf")
second = float("-inf")

for num in numbers:
    if num > greatest:
        second = greatest
        greatest = num
    elif num > second and num != greatest:
        second = num

if second == float("-inf"):
    print("There is no second-largest distinct number")
else:
    print(second)
```

**Output:**

``` text
30
```

**Explanation:** - `greatest` stores the largest number found so far. -
`second` stores the second-largest distinct number found so far. -
`float("-inf")` allows the code to work correctly even when all numbers
are negative. - The `elif` updates the second-largest number when the
current number is smaller than the largest but greater than the current
second-largest.

**Note:** This solution finds the second-largest **distinct** value. For
example, in `[10, 10, 8]`, the answer is `8`.

## 4. Check whether a string is a palindrome

``` python
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

**Output:**

``` text
Palindrome
```

**Explanation:** A palindrome reads the same forward and backward.
Comparing the original string with its reversed version checks this.

## 5. Count the occurrence of each character in a string

``` python
text = "Welcome to python"
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)
```

**Output:**

``` text
{'W': 1, 'e': 2, 'l': 1, 'c': 1, 'o': 3, 'm': 1, ' ': 2, 't': 1, 'p': 1, 'y': 1, 'h': 1, 'n': 1}
```

**Explanation:** - The dictionary stores each character as a key and its
count as the value. - If the character is already present, increase its
count by one. - Otherwise, add it to the dictionary with a count of one.

**Note:** This counts spaces and treats uppercase and lowercase letters
as different characters.

## 6. Remove duplicates from a list

``` python
numbers = [1, 2, 3, 2, 4, 5, 3, 6]
nonduplicate = []

for num in numbers:
    if num not in nonduplicate:
        nonduplicate.append(num)

print(nonduplicate)
```

**Output:**

``` text
[1, 2, 3, 4, 5, 6]
```

**Explanation:** Add an element only if it is not already in the result
list. This preserves the original order.

**Alternative:** `list(set(numbers))` is shorter, but a set does not
guarantee preserving the original order.

## 7. Find the factorial of a number

``` python
number = 10
factorial = 1

if number < 0:
    print("Factorial is not defined for negative integers")
else:
    for i in range(1, number + 1):
        factorial *= i

    print(factorial)
```

**Output:**

``` text
3628800
```

**Explanation:** Factorial means multiplying all positive integers from
`1` to the given number. Use `*=` to multiply and update the variable.

**Note:** `0!` is `1`. The initial value of `factorial` must therefore
be `1`, not `0`.

## 8. Print the Fibonacci series

``` python
number = 10
a = 0
b = 1

for i in range(number):
    print(a, end=" ")
    a, b = b, a + b
```

**Output:**

``` text
0 1 1 2 3 5 8 13 21 34
```

**Explanation:** - The first two Fibonacci numbers are `0` and `1`. -
Each next number is the sum of the previous two. - `a, b = b, a + b`
updates both variables at the same time. - `range(number)` prints the
first `number` terms.

## 9. Check whether a number is prime

``` python
number = 7

if number <= 1:
    print("Not Prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
```

**Output:**

``` text
Prime
```

**Explanation:** - A prime number is greater than `1` and divisible only
by `1` and itself. - The loop checks whether any number from `2` to
`number - 1` divides it exactly. - If `number % i == 0`, a divisor is
found, so print `"Not Prime"` and exit the loop with `break`. - The
`else` belongs to the `for` loop. It runs only if the loop finishes
without `break`.

**More efficient version:** Only check divisors up to the square root of
the number.

``` python
number = 7

if number <= 1:
    print("Not Prime")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
```

------------------------------------------------------------------------

## Quick revision

    No. Problem                 Key concept
  ----- ----------------------- ------------------------------------
      1 Reverse a string        Slicing: `[::-1]`
      2 Find duplicates         `count()` and membership check
      3 Second-largest number   Comparison and tracking two values
      4 Palindrome              Reverse and compare
      5 Character frequency     Dictionary
      6 Remove duplicates       List membership
      7 Factorial               Multiplication and loop
      8 Fibonacci series        Multiple assignment
      9 Prime number            Modulo, loop, and `for-else`

**Practice tip:** Try writing each program without looking at the
solution. Focus on understanding the logic, not memorizing the code.
