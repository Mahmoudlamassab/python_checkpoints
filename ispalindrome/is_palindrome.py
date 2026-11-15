def is_palindrome(s):
    """
    Check if the given string is a palindrome.

    A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Normalize the string: remove spaces, punctuation, and convert to lowercase
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the normalized string is equal to its reverse
    return normalized_str == normalized_str[::-1]

assert is_palindrome("Never odd or even") is True
assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("hello") is False
assert is_palindrome("") is True
print("Checkpoint OK")