from tokenise_escape_words import TokeniseAndStopWords


def menuDriven(choice):
    if(choice==1):
        print("sorry")
    elif(choice==2):
        string=input()  #to enter the query asked by user
        string.lower()
        tk_sw=TokeniseAndStopWords(string)
        tk_sw.token_and_stop_words()

    





if(__name__=='__main__'):
    print("Enter your choice\n1. Speech\n2. text\n")
    choice=int(input())
    menuDriven(choice)

