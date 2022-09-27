# twitter-analysis-script
Building a twitter-analysis script through the power of friendship! 

## GOAL
Build a python tool for analyzing networks of transphobia on Twitter

## TOOLS
- Twitter library
    - [Tweepy - Twitter library for Python](https://www.tweepy.org/)
- NLP Library for Python
    - NLTK?
- Database
    - non-relational?
    - MongoDB?
- Visualization

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

## Program Flow  -- Future
### VARIABLES
Account *a* of set of accounts *A*
Tweet *t* of set of tweets *T*
Like *l* of set of likes *L*
Retweet *r* of set of retweets *R*
Subtweet *s* of set of subtweets *S*
Follower *f* of set of followers *F*
Follow *g* of set of follows *G* (follow, followed, following, this is exhausting)
Period *p* of set of periods *P*

*x'* for derivative of *x*
*x_specifier* as needed

### INGEST TWEETS
- Select tweet *t* from account *a*
- Fetch likes *L*, retweets *R*, subtweets *S* (comments) for tweet *t*
- Select accounts *A'* from *L*, *R*, and *S* of *t* (as desired)
- For period *p*, ingest tweets from *a'* as selected from *A'*

### INGEST ACCOUNTS
- Fetch followers *F* and following *G* for account *a*


## RESOURCES
- [Bellingcat Social Network Analysis Tool](https://www.bellingcat.com/app/uploads/2022/08/Bellingcat-Hackathon-Social-Network-Analysis-Tool-Aug22.pdf)
- [Natural Language Toolkit (for Python)](https://www.nltk.org/)
- [Python AI Projects - Twitter Sentiment Analysis in Python - Youtube](https://www.youtube.com/watch?v=pgZcP852dMg)
