"""
calc.py - A collection of mathematical utility functions.

Written for Python 3.9. Uses typing.Union/Optional/List/Tuple (the
pre-PEP604 style common in Python 3.9 codebases) rather than the
`X | Y` union syntax introduced in Python 3.10.
"""
import math
from typing import List, Optional, Tuple, Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return a minus b."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of two numbers."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return a divided by b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def integer_divide(a: int, b: int) -> int:
    """Return the integer (floor) division of a by b."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a // b


def modulo(a: Number, b: Number) -> Number:
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ZeroDivisionError("modulo by zero")
    return a % b


def power(base: Number, exponent: Number) -> Number:
    """Return base raised to the power of exponent."""
    return base ** exponent


def sqrt(value: Number) -> float:
    """Return the square root of a non-negative number."""
    if value < 0:
        raise ValueError("cannot take sqrt of a negative number")
    return math.sqrt(value)


def cube_root(value: Number) -> float:
    """Return the cube root of a number (handles negatives)."""
    if value < 0:
        return -((-value) ** (1.0 / 3.0))
    return value ** (1.0 / 3.0)


def absolute_value(value: Number) -> Number:
    """Return the absolute value of a number."""
    return abs(value)


def factorial(n: int) -> int:
    """Return n! for a non-negative integer n."""
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    return math.factorial(n)


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b."""
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of a and b."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)


def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, int(math.sqrt(n)) + 1, 2):
        if n % divisor == 0:
            return False
    return True


def prime_factors(n: int) -> List[int]:
    """Return the list of prime factors of n."""
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_sequence(count: int) -> List[int]:
    """Return a list of the first `count` Fibonacci numbers."""
    return [fibonacci(i) for i in range(count)]


def mean(values: List[Number]) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def median(values: List[Number]) -> float:
    """Return the median of a list of numbers."""
    if not values:
        raise ValueError("values must not be empty")
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2 == 0:
        return (ordered[mid - 1] + ordered[mid]) / 2
    return ordered[mid]


def mode(values: List[Number]) -> Number:
    """Return the most frequently occurring value in a list."""
    if not values:
        raise ValueError("values must not be empty")
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return max(counts, key=counts.get)


def variance(values: List[Number]) -> float:
    """Return the population variance of a list of numbers."""
    if not values:
        raise ValueError("values must not be empty")
    avg = mean(values)
    return sum((value - avg) ** 2 for value in values) / len(values)


def std_dev(values: List[Number]) -> float:
    """Return the population standard deviation of a list of numbers."""
    return math.sqrt(variance(values))


def percentage(part: Number, whole: Number) -> float:
    """Return what percentage `part` is of `whole`."""
    if whole == 0:
        raise ZeroDivisionError("whole must not be zero")
    return (part / whole) * 100


def percentage_change(old_value: Number, new_value: Number) -> float:
    """Return the percentage change from old_value to new_value."""
    if old_value == 0:
        raise ZeroDivisionError("old_value must not be zero")
    return ((new_value - old_value) / old_value) * 100


def area_circle(radius: Number) -> float:
    """Return the area of a circle given its radius."""
    return math.pi * radius ** 2


def circumference_circle(radius: Number) -> float:
    """Return the circumference of a circle given its radius."""
    return 2 * math.pi * radius


def area_rectangle(width: Number, height: Number) -> Number:
    """Return the area of a rectangle."""
    return width * height


def perimeter_rectangle(width: Number, height: Number) -> Number:
    """Return the perimeter of a rectangle."""
    return 2 * (width + height)


def area_triangle(base: Number, height: Number) -> float:
    """Return the area of a triangle given its base and height."""
    return 0.5 * base * height


def area_triangle_heron(a: Number, b: Number, c: Number) -> float:
    """Return the area of a triangle given three side lengths (Heron's formula)."""
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter_triangle(a: Number, b: Number, c: Number) -> Number:
    """Return the perimeter of a triangle given three side lengths."""
    return a + b + c


def volume_cube(side: Number) -> Number:
    """Return the volume of a cube given its side length."""
    return side ** 3


def volume_sphere(radius: Number) -> float:
    """Return the volume of a sphere given its radius."""
    return (4 / 3) * math.pi * radius ** 3


def volume_cylinder(radius: Number, height: Number) -> float:
    """Return the volume of a cylinder given its radius and height."""
    return math.pi * radius ** 2 * height


def surface_area_cube(side: Number) -> Number:
    """Return the surface area of a cube given its side length."""
    return 6 * side ** 2


def surface_area_sphere(radius: Number) -> float:
    """Return the surface area of a sphere given its radius."""
    return 4 * math.pi * radius ** 2


def celsius_to_fahrenheit(celsius: Number) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: Number) -> float:
    """Convert a temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius: Number) -> float:
    """Convert a temperature from Celsius to Kelvin."""
    return celsius + 273.15


def kelvin_to_celsius(kelvin: Number) -> float:
    """Convert a temperature from Kelvin to Celsius."""
    return kelvin - 273.15


def degrees_to_radians(degrees: Number) -> float:
    """Convert an angle from degrees to radians."""
    return math.radians(degrees)


def radians_to_degrees(radians: Number) -> float:
    """Convert an angle from radians to degrees."""
    return math.degrees(radians)


def log_base(value: Number, base: Number) -> float:
    """Return the logarithm of value in the given base."""
    if value <= 0:
        raise ValueError("value must be positive")
    return math.log(value, base)


def natural_log(value: Number) -> float:
    """Return the natural logarithm of a positive number."""
    if value <= 0:
        raise ValueError("value must be positive")
    return math.log(value)


def exponential(value: Number) -> float:
    """Return e raised to the power of value."""
    return math.exp(value)


def quadratic_roots(a: Number, b: Number, c: Number) -> Tuple[Optional[complex], Optional[complex]]:
    """Return the two roots of ax^2 + bx + c = 0 (may be complex)."""
    if a == 0:
        raise ValueError("a must not be zero for a quadratic equation")
    discriminant = b ** 2 - 4 * a * c
    sqrt_discriminant = math.sqrt(abs(discriminant))
    if discriminant >= 0:
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)
    else:
        root1 = complex(-b / (2 * a), sqrt_discriminant / (2 * a))
        root2 = complex(-b / (2 * a), -sqrt_discriminant / (2 * a))
    return root1, root2


def sum_of_digits(n: int) -> int:
    """Return the sum of the digits of a non-negative integer."""
    return sum(int(digit) for digit in str(abs(n)))


def is_perfect_square(n: int) -> bool:
    """Return True if n is a perfect square."""
    if n < 0:
        return False
    root = int(math.isqrt(n))
    return root * root == n


def is_perfect_number(n: int) -> bool:
    """Return True if n is a perfect number (sum of proper divisors equals n)."""
    if n < 2:
        return False
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n


def is_armstrong_number(n: int) -> bool:
    """Return True if n is an Armstrong (narcissistic) number."""
    digits = str(n)
    power_count = len(digits)
    return n == sum(int(digit) ** power_count for digit in digits)


def combinations_count(n: int, r: int) -> int:
    """Return the number of combinations of n items taken r at a time."""
    return math.comb(n, r)


def permutations_count(n: int, r: int) -> int:
    """Return the number of permutations of n items taken r at a time."""
    return math.perm(n, r)


def round_to_nearest(value: Number, multiple: Number) -> Number:
    """Round value to the nearest multiple of `multiple`."""
    if multiple == 0:
        raise ValueError("multiple must not be zero")
    return round(value / multiple) * multiple


def clamp(value: Number, minimum: Number, maximum: Number) -> Number:
    """Clamp value to the inclusive range [minimum, maximum]."""
    if minimum > maximum:
        raise ValueError("minimum must not be greater than maximum")
    return max(minimum, min(value, maximum))


def linear_interpolate(start: Number, end: Number, fraction: float) -> float:
    """Linearly interpolate between start and end at the given fraction (0-1)."""
    return start + (end - start) * fraction


def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 0


def is_odd(n: int) -> bool:
    """Return True if n is odd."""
    return n % 2 != 0


def average_of_two(a: Number, b: Number) -> float:
    """Return the average of two numbers."""
    return (a + b) / 2


def sum_range(start: int, end: int) -> int:
    """Return the sum of all integers from start to end, inclusive."""
    return sum(range(start, end + 1))


def product_range(start: int, end: int) -> int:
    """Return the product of all integers from start to end, inclusive."""
    result = 1
    for value in range(start, end + 1):
        result *= value
    return result
