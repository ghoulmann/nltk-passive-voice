#!/usr/bin/env python

import nltk
import sys
import os
from itertools import dropwhile
import postagger

def tag_sentence(sentence):
    """
    Take a sentence as string and return a list of word:tag tuples.
    """

    assert isinstance(sentence, basestring)
    tokens = nltk.word_tokenize(sentence)
    return TAGGER.tag(tokens)

def passive_test(tags):
    """
    Return True if test for passive is positive
    """

    # Check for forms of to be (the first indicator)
    postToBe = list(dropwhile(lambda(tag): not tag.startswith("BE"), tags))
    # check for nongerund
    nonGerund = lambda(tag): tag.startswith("V") and not tag.startswith("VBG")

    filtered = filter(nonGerund, postToBe)
    out = any(filtered)
    return out

def clean_sentence(sentence):
    return sentence.replace("\n", " ").replace("\r", " ")
def filter_active(sentence):
    """
    Identify passive voice.

    Tags a given sentence; returns true if it seems passive.
    """

    tagged = tag_sentence(sentence)
    tags = map( lambda(tup): tup[1], tagged )
    passive_count = 0
    if passive_test(tags):
        passive_count = passive_count + 1
        print("Passive: " + clean_sentence(sentence))
    #print passive_count
def sentence_tokenizer(fn):
    with open(fn) as f:
        text = f.read()
        sentences = PUNKT.tokenize(text)
        sentence_count = len(sentences)
        for sentence in sentences:
            filter_active(sentence)
    return sentence_count





def main():
    """
    This is the main function.

    Set the TAGGER constant; check for a filename from argument or other source.
    If no filename is found by command line or file.open(), then look for variable.
    """
    global TAGGER
    global PUNKT
    TAGGER = postagger.get_tagger()
    PUNKT = nltk.tokenize.punkt.PunktSentenceTokenizer()

    if len(sys.argv) >= 2:
        for fn in sys.argv[1:]:
            try:
                 sentence_tokenizer(fn)
            except:
                print "No useable txt file found."
    elif fn:
            try:
                sentence_tokenizer(fn)
            except:
                print("No useable txt file found.")
    else:
        fn = "data/example.txt"
        sentence_tokenizer(fn)



if __name__ == "__main__":
    main()
