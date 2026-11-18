def is_palindrome(s):
    """
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]


assert is_palindrome("Never odd or even") is True
assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("hello") is False
assert is_palindrome("") is True
print("Checkpoint OK")
