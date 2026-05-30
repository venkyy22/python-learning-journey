
comments  = [
    "Buy now and get rich!" ,
    "Nice video",
    "Click here to win money",
    "Thank you for the tutorial",
    "Free crypto giveaway"
]

spam_words = [
    "rich",
    "buy",
    "money",
    "crypto",
]

for comment in comments:
    is_spam = False

    for word in spam_words:
        if word in comment:
            is_spam = True
            break

    if is_spam:
        print("spam")
    else:
        print("not spam")
