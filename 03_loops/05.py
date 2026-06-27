text = "aabbcc"
for i in text:
    if text.lower().count(i.lower()) == 1:
        print(i)
        break