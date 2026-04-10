text = input("Enter text: ")
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

for key in sorted(freq):
    print(key, ":", freq[key])
