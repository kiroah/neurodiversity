import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import pandas as pd


def pos_tag(content,pos_filter):
    """
    Count number of word occurance for two sources/columns, but also filters out words that are not included in the filter list

    Parameters:
    args: which is a tuple of:
        row : pd dataframe row that includes the article metadata + original content + modified content
        pos_filter (list) : List of POS tags to retain for the word count

    Returns:
    Counter: Counter object from collections, that has (word,pos) as the key and the value as the occurence of the word in the article
    df: metadata of the article, which include url, # of sentences, and # of words in the article
    """
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

    return sentence_count,word_count,filtered_content



def count_words_2(args):
    """
    Count number of word occurance for two sources/columns, but also filters out words that are not included in the filter list

    Parameters:
    args: which is a tuple of:
        row : pd dataframe row that includes the article metadata + original content + modified content
        pos_filter (list) : List of POS tags to retain for the word count

    Returns:
    Counter: Counter object from collections, that has (word,pos) as the key and the value as the occurence of the word in the article
    df: metadata of the article, which include url, # of sentences, and # of words in the article
    """
    row,pos_filter = args
    # Perform processing on the row here
    content = row['content orig']
    sentence_count_orig, word_count_orig, filtered_content_orig = pos_tag(row['content orig'],pos_filter)
    sentence_count_mod, word_count_mod, filtered_content_mod = pos_tag(row['content mod'],pos_filter)

    df = pd.DataFrame(columns=['url','sentence count orig','word count orig','sentence count mod','word count mod'])
    df.loc[row['index']] = [row['url'],sentence_count_orig,word_count_orig,sentence_count_mod,word_count_mod ] 
    return (Counter(filtered_content_orig),Counter(filtered_content_mod),df)
       