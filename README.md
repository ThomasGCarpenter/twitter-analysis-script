# twitter-analysis-script
Building a twitter-analysis script through the power of friendship! 

## GOAL
Build a python tool for analyzing networks of transphobia on Twitter

## TOOLS
Tweepy - Twitter library for Python

~NLP Library for Python
NLTK 

Database
~non-relational?
~MongoDB?

Visualization

## High Level 
1. Python/Tweepy Script
2. Database 
3. NLP 
4. Collect Nodes
5. Check for edges 

## Version 0.01
- Select and fetch Tweet via Tweet-URL
- Store Tweet in database
- Do basic NLP on Tweet (sentiment, correlation to transphobia(?)

## Flow  -- Future
*INGEST TWEETS*
- Select tweet T from account A
- Fetch likes l, retweets r, subtweets s (comments) for tweet T
- Select accounts A' for l, r, and/or s of T (as desired)
- For period p, ingest tweets from A'

*INGEST ACCOUNTS*
- Fetch followers F and following f for account A


## RESOURCES
- [Bellingcat Social Network Analysis Tool](https://www.bellingcat.com/app/uploads/2022/08/Bellingcat-Hackathon-Social-Network-Analysis-Tool-Aug22.pdf)
- [Natural Language Toolkit (for Python)](https://www.nltk.org/)
- [https://www.youtube.com/watch?v=pgZcP852dMg]
