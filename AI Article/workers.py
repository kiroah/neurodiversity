import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import pandas as pd


def count_words(args):
    """
    Count number of word occurance, but also filters out words that are not included in the filter list

    Parameters:
    args: which is a tuple of:
        row : pd dataframe row that includes the article metadata + content (for tagging)
        pos_filter (list) : List of POS tags to retain for the word count

    Returns:
    Counter: Counter object from collections, that has (word,pos) as the key and the value as the occurence of the word in the article
    df: metadata of the article, which include url, # of sentences, and # of words in the article
    """
    row,pos_filter = args
    # Perform processing on the row here
    content = row['content']
    df = pd.DataFrame(columns=['url','year','month','sentence count','word count'])
    filtered_content = []
    sentence_count = 0
    word_count = 0
    tokenenized_content = word_tokenize(content)
    # Perform POS tagging
    pos_content = nltk.pos_tag(tokenenized_content)
    # Check if the query string is in the set
    for word, pos in pos_content:
        word_count += 1
        if (word == '.'):
            sentence_count += 1
        elif pos in pos_filter:
            filtered_content.append((word,pos))

    df.loc[row['index']] = [row['url'],row['date'][0:4],row['date'][5:7],sentence_count,word_count] 
    return (Counter(filtered_content),df)
       