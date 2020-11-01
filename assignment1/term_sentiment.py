import sys
import os
import string 
import json
import re

def construct_dict(sentiment_score_file):
    senti_file = open(sentiment_score_file)
    scores = {}
    for line in senti_file:
      term, score  = line.split("\t") 
      scores[term] = int(score)  
    return scores

def normalise_word(word):
	exclude = set(string.punctuation)
	word = ''.join(ch  for ch in word.lower() if ch not in exclude)
	word = re.sub("\s+", " ", word)
	return word

def get_sentiments(senti_dict,line):
	senti_score = 0
	non_senti_words = []
	for word in line.split(' '):
		if word in senti_dict:
			senti_score += senti_dict[word]
		else:
			non_senti_words.append(word)
	return senti_score,non_senti_words
    

def lines(fp):
    print(len(fp.readlines()))

def main():
	senti_dict = construct_dict(sys.argv[1])
	tweet_file = open(sys.argv[2], "r")
	for line in tweet_file:
		d = json.loads(line)
		if 'text' in d.keys():
			norm_tweet = normalise_word(d['text'])
			senti_score,non_senti_words = get_sentiments(senti_dict,norm_tweet)
			for w in non_senti_words:
				print(w,senti_score/float(len(norm_tweet)-len(non_senti_words)))

    
if __name__ == '__main__':
    main()
