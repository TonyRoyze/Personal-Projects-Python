tweet = "I am tired! I like fruit...and milk"
print(tweet)
pnct = '!#$%&()*+,-./:;<=>?@[]^_`{|}~'
lst = list(pnct)
print(lst)
for p in lst:
    tweet = tweet.replace(p, ' ')
    print(tweet)
