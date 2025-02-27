def str_length(s):
    return len(s)

def str_concat(s1, s2):
    return s1 + s2

def str_reverse(s):
    return s[::-1]

def str_search(s, sub):
    return s.find(sub)

def count_char(s, c):
    return s.count(c)

def to_upper(s):
    return s.upper()

def to_lower(s):
    return s.lower()

def is_palindrome(s):
    return s == s[::-1]

def remove_spaces(s):
    return s.replace(" ", "")

def replace_substring(s, sub, rep):
    return s.replace(sub, rep)

def main():
    str1 = input("Enter first string: ").strip()
    str2 = input("Enter second string: ").strip()
    sub = input("Enter substring to search: ").strip()
    rep = input("Enter substring to replace: ").strip()
    
    print("Length:", str_length(str1))
    print("Concatenation:", str_concat(str1, str2))
    print("Reversed:", str_reverse(str1))
    print("Substring found at:", str_search(str1, sub))
    print("Character count:", count_char(str1, 'l'))
    print("Uppercase:", to_upper(str1))
    print("Lowercase:", to_lower(str1))
    print("Palindrome:", "Yes" if is_palindrome(str1) else "No")
    print("Without spaces:", remove_spaces(str1))
    print("Replaced substring:", replace_substring(str1, sub, rep))
    
if __name__ == "__main__":
    main()
