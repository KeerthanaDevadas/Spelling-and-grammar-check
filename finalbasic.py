import nltk
import re
import language_check
from Tkinter import *
from filename import *
from correct import *
from output import *

tool = language_check.LanguageTool('en-US')
tokenise = nltk.data.load('tokenizers/punkt/english.pickle')


def autocorrect(s,match):
    return language_check.correct(s,match)


def detection():
    global sentence
    matches = tool.check(sentence)
    k=nltk.word_tokenize(sentence)
    tag = nltk.pos_tag(k)
    #print tag
    match = []
    for i in range(len(matches)):
        ignore = 'n'
        for j in match1:
            if (sentence[matches[i].fromx:matches[i].tox] == j):
                ignore = 'y'
        for j in match2:
            if (sentence[matches[i].fromx:matches[i].tox] == j):
                ignore = 'n'
                break
        for j in tag:
            if ((sentence[matches[i].fromx:matches[i].tox] == j[0]) and (j[1] == 'NNP')):
                ignore = 'y'
        if (ignore == 'n' or ignore == 'N'):
            match.append(matches[i])
            match2.append(sentence[matches[i].fromx:matches[i].tox])
        if (ignore == 'y' or ignore == 'Y'):
            if (sentence[matches[i].fromx:matches[i].tox] not in match1):
                match1.append(sentence[matches[i].fromx:matches[i].tox])
    if match:
        correction(match)
    else:
        outp.write(sentence)
    
def correction(match):
    global sentence
    s = sentence
    rep = fun1(s,match)
    #rep = raw_input('Your correction? ')
    if rep:
        sentence = s[0:match[0].fromx] + rep + s[match[0].tox:]
    else:
        sentence = autocorrect(s,match)
    print sentence
    #root.destroy()
    detection()

def main():        
    global sentence
    file_pointer = open(fname).read()
    s = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', file_pointer)
    #print s[0]
    #s = nltk.sent_tokenize(file_pointer)
    for i in s:
        sentence = i
        detection()
    outp.close()
    f()
            
match1 = []
match2 = []
sentence = ''
outp = open("out1.txt","w+")
main()
