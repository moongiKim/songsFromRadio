from django.shortcuts import render
from . import crawling

def post_list(request):
    address = "http://miniweb.imbc.com/"
    progCode = "FM4U000001140" # 푸른밤
    hdr = {'User-Agent':'Mozilla/5.0','referer': address}

    newAddress = address+"Music/?progCode="+progCode
    seqID = crawling.get_seqid(newAddress, hdr)

    #http://miniweb.imbc.com/Music/View?seqID=5036&progCode=FM4U000001140&page=1
    newAddress = address+"Music/View?progCode="+progCode+"&seqID="+seqID
    songlist = crawling.get_songlist(newAddress, hdr)

    return render(request, 'blog/post_list.html', {'songlist':songlist})
