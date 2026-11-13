
def encode(text):
    result = ""
    i = 0
    while i < len(text):
        count = 1
        while i + count < len(text) and text[i + count] == text[i]:
            count = count + 1
        result = result + text[i] + str(count)
        i = i + count
    return result


samples = ["aaabbbccccd", "abcd", "zzzzzzzz", "aabcccdddd"]

for s in samples:
    e = encode(s)
    print("Original:", s, "(", len(s), ")  Encoded:", e, "(", len(e), ")", end="  ")
    if len(e) < len(s):
        print("-> Compression is beneficial")
    else:
        print("-> Not beneficial, keep original")
