import sys
import json


def hw(sent_file, tweet_file):
    afinnfile = None
    outputfile = None
    with open(sent_file) as f:
        afinnfile = f.readlines()

    scores = {}  # initialize an empty dictionary
    for line in afinnfile:
        # The file is tab-delimited. "\t" means "tab character"
        term, score = line.split("\t")
        scores[term] = int(score)  # Convert the score to an integer.

    with open(tweet_file) as f:
        outputfile = f.readlines()

    for line in outputfile:
        if line.strip():
            tweet_dict = json.loads(line.strip())
            words = tweet_dict['text'].strip().split()
            sentiment = 0
            for word in words:
                if word.lower() in scores.keys():
                    sentiment += scores[word.lower()]
            print(sentiment)

def lines(fp):
    print(str(len(fp.readlines())))

def main():
    hw(sys.argv[1], sys.argv[2])
    # lines(sent_file)
    # lines(tweet_file)


if __name__ == '__main__':
    main()
