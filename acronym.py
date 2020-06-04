def abbreviate(words):
    return ''.join([word[0] for word in words.replace('_', '').replace('-', ' ').split()]).upper()

print(abbreviate("Portable Network Graphics"))
print(abbreviate("The Road _Not_ Taken"))
