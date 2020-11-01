# -*- coding: utf-8 -*-
import sys
import json
import string
from collections import defaultdict

def construct_dict(sentiment_score_file):
	scores = {} 
	with open(sentiment_score_file) as senti_file:
		for line in senti_file:
			term, score  = line.split("\t")  
			scores[term] = int(score)  
	return scores

def norm_tweet(sentence):
    exclude = set(string.punctuation)
    sentence = ''.join(ch for ch in sentence.lower() if ch not in exclude)
    return sentence

def get_sentiments(sentiments_dict,line):
	senti_score = 0
	for word in line.split(' '):
		if word in sentiments_dict:
			senti_score += sentiments_dict[word]
	return senti_score

def geo_info(tweet):
	try:
		if tweet['place']['country_code'] == 'US':
			state = tweet['place']['full_name'][-2:]
			return True,state
		else:
			return False,''
	except:
		pass
	return False,''


def main():
	senti_dict = construct_dict(sys.argv[1])
	tweet_file = open(sys.argv[2])
	
	state_happy_index = defaultdict()
	total_tweet_count = 0

	for line in tweet_file:
		d = json.loads(line)
		try:
			if d['lang'] == 'en': 
				if 'text' in d.keys(): 
					norm_tweet = norm_tweet(d['text'].encode('utf8'))
					is_US, state = geo_info(d)
					if is_US: 
						total_tweet_count += 1
						senti_score = get_sentiments(senti_dict,norm_tweet)
						if state in state_happy_index:
							state_happy_index[state] += senti_score
						else:
							state_happy_index[state] = senti_score
		except:
			pass

	happiest_state = 'XX'
	happy_score = -1
	saddest_state = 'YY'
	sad_score = 99999
	
	if state_happy_index and total_tweet_count	:
		for state,score in state_happy_index.items():
			if score > happy_score:
				happy_score = score
				happiest_state = state
			if score < sad_score:
				saddest_state = state
				sad_score = score

		print(happiest_state,happy_score/float(total_tweet_count))

if __name__ == '__main__':
    main()