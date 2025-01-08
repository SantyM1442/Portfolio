def things_in_list(list):
    separator1=', '
    separator2=' and '
    final_string=''
    i=0
    for i in range(0,int(len(list))):
        if i < int(len(list))-2:
            final_string+=list[i]+separator1
        elif i == int(len(list))-2:
            final_string+=list[i]+separator2
        else:
            final_string+=list[i]
    return print(final_string)

spam=['apples','bananas','tofu','cats']
things_in_list(spam)
