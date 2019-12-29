# -*- coding: utf-8 -*-

#from urllib.request import urlopen
#from urllib2 import urlopen
import urllib.request
from bs4 import BeautifulSoup
from parse import *
import json
import chardet

def get_seqid(address):
    html = urllib.request.urlopen(address)

    bsObject = BeautifulSoup(html, "html.parser")
    tbody = bsObject.find('tbody')

    for a in tbody.find_all('a'):
        href = a.attrs['href']
        #result = parse(href)
        parse1 = href.split("?")
        parse2 = parse1[1].split("&")
        parse3 = parse2[0].split("=")
        seqID = parse3[1]
        break

    return seqID

def get_songlist(address):
    html = urllib.request.urlopen(address)
    bsObject = BeautifulSoup(html, "html.parser")

    #print(bsObject)
    tbody = bsObject.find('tbody')
    #title_all = tbody.find_all('p', class_='title')

    songlist = []
    i = 0
    for p in tbody.find_all('p'):
        if i%2 == 0:
            title = p.get_text()
        else:
            singer = p.get_text()
            dict = {'title' : title, 'singer' : singer} #dictionary
            songlist.append(dict)

        i = i+1

    return songlist


'''
address = "http://miniweb.imbc.com/"
progCode = "FM4U000001140" # 푸른밤

newAddress = address+"Music/?progCode="+progCode
seqID = get_seqid(newAddress)

#http://miniweb.imbc.com/Music/View?seqID=5036&progCode=FM4U000001140&page=1
newAddress = address+"Music/View?progCode="+progCode+"&seqID="+seqID
songlist = get_songlist(newAddress)


for song in songlist:
    print (chardet.detect (song['title']))
    print (song['title'])
    print (song['singer'])
    print ("")
'''
