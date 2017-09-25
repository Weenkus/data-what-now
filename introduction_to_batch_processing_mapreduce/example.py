#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import mincemeat

partitions = [
'Data is the core of predictive modeling, visualization, and analytics.',
'Unfortunately, the needed data is not always readily available to the user,',
'it is most often unstructured. The biggest source of data is the Internet, and',
'with programming, we can extract and process the data found on the Internet for',
'our use – this is called web scraping.',
'Web scraping allows us to extract data from websites and to do what we please with it.',
'In this post, I will show you how to scrape a website with only a few of lines of code in Python.',
'All the code used in this post can be found in my GitHub notebook.'
]


# The data source can be any dictionary-like object
datasource = dict(enumerate(partitions))

def mapper(key, value):
    for word in value.split():
	normalized_word = word.lower()
        yield normalized_word, 1

def reducer(key, values):
    result = sum(values)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapper
s.reducefn = reducer

results = s.run_server(password="datawhatnow")
print(results)
