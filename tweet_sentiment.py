#    Aspect based sentiment analysis on tweets data
#     it takes tweets as input and returns the scores associated with the aspects!

import sys
import json                  # for parsing the tweets in the json format
import nltk                  # NLTK Toolkit!

def lines(fp):
    print str(len(fp.readlines()))


def main():
    sent_file = open(sys.argv[1])          # file containing sentiment scores
    tweet_file = open(sys.argv[2])         # file containing tweets
    sent_lines=sent_file.readlines()
    tweet_lines=tweet_file.readlines()
    sentiment_score={}

    for line in sent_lines:            	   # create a dictionary containing word count for every word
    	word,count=line.split("\t")
     	sentiment_score[word]=count

    for line in tweet_lines:
    	json_object=json.loads(line) 	   		   # parse the json object and extract the tweets from them
     	tweet_text=json_object["statuses"][0]["text"].encode("utf-8")

    # tweet_text  = ["Nexus is realy awesome"]
    print tweet_text

    for sentence in tweet_text:
        postags = nltk.pos_tag(sentence.split(" "))                   # tags associated with the sentence is taken out
	print postags
	nounflag = 0
	adj_flag = 0
	score = 0
	noun = "No Subject"
	for postag in postags:    
		if postag[1] == 'NNP' or postag[1] == 'NN':		# store the noun words 
			nounflag = 1
		        noun = postag[1]		
		if postag[1] == 'JJ' or postag[1] == 'VBN':
			adjflag = 1
			adj = postag[0]
			score += int(sentiment_score[postag[0]]) if postag[0] in sentiment_score else 0			
	
	print "Tweet is about"+str(sentence)
 	print str(score)+'\n'

if __name__ == '__main__':
    main()
