from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    numOfWords=len(wordlist)
    wordDict={}
    for word in wordlist:
        if word in wordDict:
            #increment
            wordDict[word]=wordDict[word]+1
        else:
            wordDict[word]=1
    dict=wordDict.items()
    sortedWords=sorted(dict,key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'yourText':fulltext,'wordNum':numOfWords,'countedWords':sortedWords})
def about(request):
    return render(request,'about.html')