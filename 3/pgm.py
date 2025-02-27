def str_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def str_concat(s1, s2):
    return s1 + s2

def str_reverse(s):
    return s[::-1]

def str_search(s, sub):
    for i in range(str_length(s) - str_length(sub) + 1):
        if s[i:i + str_length(sub)] == sub:
            return i
    return -1

def count_char(s, c):
    count = 0
    for ch in s:
        if ch == c:
            count += 1
    return count

def to_upper(s):
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    return result

def to_lower(s):
    result = ""
    for c in s:
        if 'A' <= c <= 'Z':
            result += chr(ord(c) + 32)
        else:
            result += c
    return result

def is_palindrome(s):
    return s == str_reverse(s)

def remove_spaces(s):
    result = ""
    for c in s:
        if c != ' ':
            result += c
    return result

def replace_substring(s, sub, rep):
    result = ""
    i = 0
    while i < str_length(s):
        if s[i:i + str_length(sub)] == sub:
            result += rep
            i += str_length(sub)
        else:
            result += s[i]
            i += 1
    return result

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
