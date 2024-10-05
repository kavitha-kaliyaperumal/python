text = "abracadabraaabbccrr"
counts = {}
ct = 0
lst = []
for word in text :
    if word not in lst :
        lst . append(word)
        counts[word] = 0
    ct = ct + 1
    counts [word] = counts [word] + 1
print (counts)
print (lst)
