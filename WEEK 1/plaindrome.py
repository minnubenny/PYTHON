def is_palindrome(s):

    cleaned = ''.join(c.lower() for c in s if c.isalnum())# Remove non-alphanumeric characters and convert to lowercase
    return cleaned == cleaned[::-1]# Check if cleaned string is equal to its reverse

# Example usage:
print(is_palindrome("malayalam")) 
print(is_palindrome("hello"))                 
