 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
import nltk
import sys
from itertools import dropwhile
import postagger
import os
from mimetypes import MimeTypes
import codecs
import proselint

def process_file(file):
    """
    open and prepare a (txt) file for passive voice report.

    Open file, read each sentence into a list of strings,
    remove (clean) new line and line feed characters.

    :param: string, filename

    :returns: raw_text
    """

    mime = MimeTypes()
    mime_type = mime.guess_type(file)
    if mime_type[0] == "text/plain":
        fh = open(file, "r")
        raw_text = fh.read()
        fh.close()
        raw_text = raw_text.replace("\n", "").replace("\r", "")

    return raw_text

def sentence_tokens(string):
    #return nltk.tokenize.punkt.PunktSentenceTokenizer(string)
    return nltk.sent_tokenize(string)

def suggestions(sentence):
    return proselint.tools.lint(sentence)

def tagged_text(sentence):
    tagger = postagger.get_tagger()
    #tokens_list = []
    #for sentence in sentence_list:
    #    assert isinstance(sentence, basestring)
    tokens = nltk.word_tokenize(sentence)
    return tagger.tag(tokens)
    #return tokens_list

def aux_verb_test(sentence):
    verbs = ["am", "is", "are", "was", "were", "be", "being", "been", "may", "might", "must", "can", "could", "shall", "should", "will", "would", "do", "does", "did", "has", "have", "had"]

    for verb in verbs:
        if verb in sentence:
            return True
        else:
            return False

def main():
    raw_text = process_file("data/example.txt")
    sentence_list = sentence_tokens(raw_text)
    print len(sentence_list)
    tags_list = []
    for sentence in sentence_list:
        tags_list.append(tagged_text(sentence))
    aux_verb_count = 0
    for sentence in sentence_list:
        if aux_verb_test(sentence):
            aux_verb_count = aux_verb_count + 1
    print("Sentences with auxilary verbs: " + str(100 * float(aux_verb_count)/float(len(sentence_list))) + "%")
    suggestions(raw_text)

if __name__ == "__main__":
    main()
