"""
Use only the first headline from your headlines list.

Check how many positive words are present in that headline.

"""


positive_words=["strong","growth","raise","expands","demand","positive","gain","profit"]
negative_words=["concerns","worry","loss","decline","weak","risk","fall","negative"]


headline1="NVDA reports strong AI chip demand"

count=0
for word in headline1.split():
    if word.lower() in positive_words:
        print(f"Positive word found: {word}")
        count+=1

print(f"Positive count: {count}")
