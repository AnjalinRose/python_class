word=input("enter the word: ")
counter={}
for letter in word:
    if not letter in counter:
        counter[letter]=1
    else:
        counter[letter]=counter[letter]+1
print(counter)
maxsofar=0
mostoccurring=""
for letter in counter:
    if counter[letter]>=maxsofar: 
        maxsofar=counter[letter]
        mostoccurring=letter
print(mostoccurring)

    