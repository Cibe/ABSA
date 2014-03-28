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
    word_count={}

    for line in sent_lines:            	   # create a dictionary containing word count for every word
    	word,count=line.split("\t")
     	word_count[word]=count

    for line in tweet_lines:
    	json_object=json.loads(line) 	   		   # parse the json object and extract the tweets from them
     	tweet_text=json_object["text"].encode("utf-8")

     for sentence in nltk.sent_tokenize(tweet_text):
     	for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)), binary=True):
        	if hasattr(chunk,'node'):
                	str=chunk.node, ' '.join(c[0] for c in chunk.leaves())     

     words=tweet_text.split(" ")
     sum=0
     for word1 in words:
      sum+=word_count[word1] if word1 in word_count else 0
     print tweet_text,":",sum

if __name__ == '__main__':
    main()
