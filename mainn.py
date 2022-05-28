# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. it is a big cake!")
# -->{"cake":2,"big":1,"is":2,"the":1,"a":1,"it":1}

def read_file_content(filename):
    #[assingnment] Add your code here
    with open(filename,"r") as file:
        data = file.read()
    # return "Hello world"
    return data


def count_word():
    #openfile=open("./story.txt","r")
    with open("./story.txt","r") as openfile:
        read_file =openfile.read()
        print(read_file)
    
    print ("This file is true")
    
    
    
    