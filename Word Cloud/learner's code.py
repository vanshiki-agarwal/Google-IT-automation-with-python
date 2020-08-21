# LEARNER CODE START HERE
    dic={}
    x=file_contents.split(" ")
    for word in x:
        char=""
        for c in word:
            if c not in punctuations:
                char=char+c
        if char not in uninteresting_words:
            if char not in dic.keys():
                dic[char]=1
            else:
                dic[char]+=1
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dic)
    return cloud.to_array()