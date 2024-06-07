def reverse_string(s):
    reversed = ""
    for i in range(len(s)):
        reversed += s[len(s) - i - 1]

    return reversed

print(reverse_string("Hemanth"))