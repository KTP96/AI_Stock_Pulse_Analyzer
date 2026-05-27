"""
Print Final Sentiment as
- Sentiment: Positive
- Sentiment: Negative
- Sentiment: Neutral
"""


positive_words=["strong","growth","raise","expands","demand","positive","gain","profit"]
negative_words=["concerns","worry","loss","decline","weak","risk","fall","negative"]


headline1="NVDA faces supply chain concerns"

pos_count=0
neg_count=0

for word in headline1.split():
    if word.lower() in positive_words:
        print(f"Positive word found: {word}")
        pos_count+=1
    elif word.lower() in negative_words:
        print(f"Negative word found: {word}")
        neg_count+=1
    else:
        print(f"Neutral word found: {word}")

print(f"Positive count: {pos_count}")
print(f"Negative count: {neg_count}")

if pos_count>neg_count:
    print("Positive")
elif neg_count>pos_count:
    print("Negative")
else:
    print("Neutral")
