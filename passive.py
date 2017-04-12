#!/usr/bin/env python

"""passive.py: First pass at finding passive voice sentences, and more
importantly, getting familiar with NLTK.

Tags a sentence with a way-overkill four-level tagger trained from the Brown
Corpus, and then looks at its verbs. If somewhere in the sentence, there's a
to-be verb and then later on a non-gerund, we'll flag the sentence as probably
passive voice.

Developed against NLTK 2.0b5.
Copied from http://narorumo.googlecode.com in late April 2013"""

import nltk
import sys
import os
from itertools import dropwhile
import postagger
from itertools import *

TAGGER = None

def tag_sentence(sent):
    """Take a sentence as a string and return a list of (word, tag) tuples."""
    assert isinstance(sent, basestring)

    tokens = nltk.word_tokenize(sent)
    return TAGGER.tag(tokens)

def passivep(tags):
    """Takes a list of tags, returns true if we think this is a passive
    sentence."""
    # Particularly, if we see a "BE" verb followed by some other, non-BE
    # verb, except for a gerund, we deem the sentence to be passive.

    postToBe = list(dropwhile(lambda(tag): not tag.startswith("BE"), tags))
    nongerund = lambda(tag): tag.startswith("V") and not tag.startswith("VBG")

    filtered = filter(nongerund, postToBe)
    out = any(filtered)

    return out

def oneline(sent):
    """Replace CRs and LFs with spaces."""
    return sent.replace("\n", " ").replace("\r", " ")

"""
def print_if_passive(sent):
    #Given a sentence, tag it and print if we think it's a passive-voice
    #formation.
    tagged = tag_sentence(sent)
    tags = map( lambda(tup): tup[1], tagged)

    if passivep(tags):
        print "passive:", oneline(sent)
"""
def report_if_passive(sent):
    """
    Given a sentences, tag it and save to list if it looks like passive voice
    formation
    """
    tagged = tag_sentence(sent)
    tags = map ( lambda(tup): tup[1], tagged)
    counter = 0
    report = []
    if passivep(tags):
        for tag in tags:
            raw_report = "Passive: " + str(oneline(sent))
        #sent_report = nltk.sent_tokenize(raw_report)
        #report = list(chain.from_iterable(sent_report))
        list_report = raw_report.split("\n")
        for x in list_report:
            if hasattr(x, '__iter__'):
                for y in flatten(x):
                    yield y
            else:
                yield x
















punkt = nltk.tokenize.punkt.PunktSentenceTokenizer()
def findpassives(fn):
    with open(fn) as f:
        text = f.read()
        sentences = punkt.tokenize(text)

        for sent in sentences:
            report_if_passive(sent)

def repl():
    """Read eval (for passivity) print loop."""
    try:
        while True:
            line = raw_input()
            report_if_passive(line)
    except EOFError,e:
        pass

def main():
    global TAGGER
    TAGGER = postagger.get_tagger()

    if len(sys.argv) > 2:
        for fn in sys.argv[2:]:
            findpassives(fn)
    else:
        fn = "swartz.txt"
        findpassives(fn)



if __name__ == "__main__":
    main()
