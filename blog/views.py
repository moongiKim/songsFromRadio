from django.shortcuts import render
from . import crawling

def post_list(request):
    address = "http://miniweb.imbc.com/"
    progCode = "FM4U000001140" # 푸른밤

    newAddress = address+"Music/?progCode="+progCode
    seqID = crawling.get_seqid(newAddress)

    #http://miniweb.imbc.com/Music/View?seqID=5036&progCode=FM4U000001140&page=1
    newAddress = address+"Music/View?progCode="+progCode+"&seqID="+seqID
    songlist = crawling.get_songlist(newAddress)

    return render(request, 'blog/post_list.html', {'songlist':songlist})
