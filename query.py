#!/usr/bin/python

from __future__ import print_function 
import arxiv
import sys


idString = sys.argv[1]
if idString[-4:] == '.pdf':
    idString = idString[:-4]

print(idString)

papers = arxiv.query(id_list = [idString])
if len(papers) > 1:
    exit('More than one paper found')
else:
    paper = papers[0]

print("Title: " + str(paper['title_detail']['value']))
print("Authors: " + str(paper['authors']))
print("Summary: " + str(paper['summary']))

