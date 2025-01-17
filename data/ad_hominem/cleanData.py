def notThread(string):
    return string[0] != ">";

def containsText(string):
    return not all(char in "=+-_0)9(8*7&6^5%4$3#2@1!?/.>,<:;][\{}|" for char in string);

def isStr(body):
    return isinstance(body, str);

def notSubReddit(word):
    return word[0:2] != "r/";

def notURL(word):
    return "http" not in word;

def removeWords(text):                              # Remove URLs and subreddits 
    words = text.split(" ");
    words = list(filter(notSubReddit, words));
    words = list(filter(notURL, words));
    newText = ' '.join(words);
    return newText;          
        

def clean(text):
    subtext = text.split("\n");
    subtext = list(filter(None, subtext));          # Remove empty lines
    subtext = list(filter(notThread, subtext));     # Remove sentences starting with ">" (it references what the reply is about)
    subtext = list(filter(containsText, subtext));  # Remove lines of special characters only
    newText = ''.join(subtext);
    return newText;