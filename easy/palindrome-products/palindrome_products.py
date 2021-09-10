"""
Solution to Palindrome Products task on Exercism

https://exercism.org/tracks/python/exercises/palindrome-products

Note: this is a very greedy algorithm, works REALLY slow for big numbers
"""

def is_palindrome(string: str) -> bool:
    """Check if string is a palindrome"""
    return string == string[::-1]


def get_palindrome_products(min_factor: int, max_factor: int) -> tuple:
    """
    Get list of palindrome products and list of their factors on the given range.
    factors[i] is a list of pairs(factors) for products[i]

    Ex.: products[i] = 9; factors[i] = [[1, 9], [3, 3]]
    """

    if max_factor < min_factor:
        raise ValueError("Max factor can not be less than min factor")

    products, factors = [], []
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if is_palindrome(str(product)):
                try:
                    product_index = products.index(product)
                    factors[product_index].append([i, j])
                except ValueError:
                    products.append(product)
                    factors.append([[i, j], ])
    return products, factors


def largest(min_factor: int, max_factor: int) -> int:
    """Get the largest palindrome product on given range"""

    products, factors = get_palindrome_products(min_factor, max_factor)
    if not products:
        return None, []
    index = products.index(max(products))
    return products[index], factors[index]


def smallest(min_factor: int, max_factor: int) -> int:
    """Get the smallest palindrome product on given range"""

    products, factors = get_palindrome_products(min_factor, max_factor)
    if not products:
        return None, []
    index = products.index(min(products))
    return products[index], factors[index]
