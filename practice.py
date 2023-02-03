def greet():
    username=input("ENTER YOUR NAME: ")
    print("HELLO "+username+". HOW ARE YOU?")

#greet()

def countwordsfile():
    filename=input("ENTER YOUR FILE NAME: ")
    no_of_words=0
    file=open(filename,'r')    
    for line in file:
        words=line.split()
        print("len")
        print(len(words))
        no_of_words=no_of_words+len(words)
    print("no of words")
    print(no_of_words)


countwordsfile()