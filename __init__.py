from tokenise_escape_words import TokeniseAndStopWords
from speechtotext import speechtotext

def menuDriven(choice):
    if(choice==1):
        ch="y"
        while(ch=="y"or ch=="Y"):
            string = speechtotext()
            string.lower()
            tk_sw=TokeniseAndStopWords(string)
            tk_sw.token_and_stop_words()
            print("\nContinue using Speech option(y/n): ")
            ch=input()
    elif(choice==2):
        ch="y"
        while(ch=="y"or ch=="Y"):
            string=input()  #to enter the query asked by user
            string.lower()
            tk_sw=TokeniseAndStopWords(string)
            tk_sw.token_and_stop_words()
            print("\nContinue using text option(y/n): ")
            ch=input()
    elif (choice==3):
        print("\nThanks!!!")
        exit()


if(__name__=='__main__'):
    choice =2
    print("Welcome to NLP to SQL. Generate your SQL query from natural language\n")
    while(choice==1 or choice == 2 or choice ==3):
        print("Enter your choice\n1. Speech\n2. text\n3. Exit")
        choice=int(input())
        menuDriven(choice)

