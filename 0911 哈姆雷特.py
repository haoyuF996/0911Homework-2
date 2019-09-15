def main():
    pre_text = open('hamlet.txt','r')
    text = [pre_text.read()]
    pre_text.close()
    words,fre_dict,fre_list = texts_to_words(text),{},[]
    for i in words:
        if i in fre_dict:
            fre_dict[i]+=1
        else:
            fre_dict[i]=1
    for i in fre_dict:
        fre_list.append((fre_dict[i],i))
    fre_list.sort(reverse=True)
    save = open('WordFrequency.txt','w')
    for i in fre_list:
        save.write(f'{i[1]:<10}{i[0]}\n')
    save.write
    save.close()
def texts_to_words(text_list):
    '''Transfer all text into words(lowercased) and return a list with all the words'''
    words = []
    for i in text_list:
        my_substitutions = i.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      "abcdefghijklmnopqrstuvwxyz                                          ")
        cleaned_text = i.translate(my_substitutions)
        wds = cleaned_text.split()
        words += wds
    return words
if __name__ == "__main__":
    main()