import os 
import json
import re
import string 
import sys


count_dict = {}
total_words = 0
puncts = set(string.punctuation)

def normalise_word(tweet):
    tweet = "".join([x.lower() for x in tweet if x not in puncts])
    tweet = re.sub("\s+", " ", tweet)
    return tweet

if __name__ == "__main__":
    tweet_file = open(sys.argv[1], "r")
    for line in tweet_file:
        d = json.loads(line)
        if 'text' in d.keys():
            norm_tweet = normalise_word(d['text'])
            for word in norm_tweet.split():
                if word in count_dict:
                    count_dict[word] += 1
                else:
                    count_dict[word] = 1
                total_words += 1
    for k, v in count_dict.items():
        print("{} {:.4f}".format(k, round(v/float(total_words),4)))

    