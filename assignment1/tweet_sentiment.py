import sys


def hw():
    afinnfile = None
    outputfile = None
    with open("AFINN-111.txt") as f:
        afinnfile = f.readlines()

    scores = {}  # initialize an empty dictionary
    for line in afinnfile:
        # The file is tab-delimited. "\t" means "tab character"
        term, score = line.split("\t")
        scores[term] = int(score)  # Convert the score to an integer.

    with open("output.txt") as f:
        outputfile = f.readlines()

    for line in outputfile:
        if line.strip():
            words = line.strip().split()
            sentiment = 0
            for word in words:
                if word.lower() in scores.keys():
                    sentiment += scores[word.lower()]
            print(sentiment)

def lines(fp):
    print(str(len(fp.readlines())))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)


if __name__ == '__main__':
    main()
