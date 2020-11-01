# -*- coding: utf-8 -*-
import sys
import json
import string
from collections import defaultdict
import operator


def norm_tweet(sentence):
    exclude = set(string.punctuation)
    sentence = ''.join(ch for ch in sentence.lower() if ch not in exclude)
    return sentence


def upd_dict(h_tags, h_dict):
    for hashtag in h_tags:
        if hashtag in h_dict:
            h_dict[hashtag] += 1
        else:
            h_dict[hashtag] = 1


def main():
    tweet_file = open(sys.argv[1])
    h_dict = {}
    for line in tweet_file:
        d = json.loads(line)
        hashtags = d['entities']['hashtags']
        h_tags = []
        for tags in hashtags:
            h_tags.append(norm_tweet(tags['text']))

        upd_dict(h_tags, h_dict)

    h_dict = {k: v for k, v in sorted(h_dict.items(), key=lambda item: item[1])}
    i = 0
    for key in h_dict.keys():
        if i < 10:
            print("{} {}".format(key, float(h_dict[key])))
            i += 1

if __name__ == '__main__':
    main()
