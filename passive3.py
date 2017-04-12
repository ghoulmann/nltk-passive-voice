 #!/usr/bin/env python2

import nltk
import sys
from itertools import dropwhile
import postagger
import os
from mimetypes import MimeTypes
import codecs

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
    if mime_type[0] == "\'text/plain\'":
        fh = codec.open(file, encoding='utf-8')
        raw_text = fh.read()
        raw_text = raw_text.replace("\n", " ").replace("\r", " ")
        
        return raw_text 

def sentence_tokens(string):
    return nltk.sent_tokenize(string)

def main():
    raw_text = process_file("data/example.txt")
    sentence_list = nltk.tokenize.punkt.PunktSentenceTokenizer(raw_text)

    

if __name__ == "__main__":
    main()
