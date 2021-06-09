def road_less_travelled():
    words = ['diverged','in','I']
    word_dict = {}
    with open('poem.txt', mode='r') as txt_file:
        for line in txt_file:
            temp = line.split(" ")
            for word in temp:
                if word in words:
                    if word in word_dict:
                        word_dict[word] +=1
                    else:
                        word_dict[word] = 1
    for k,v in word_dict.items():
        print(k,v)

road_less_travelled()

