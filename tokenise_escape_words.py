from List_map import Attribute
import nltk
from nltk.corpus import stopwords 

from nltk.tokenize import word_tokenize 

  
class TokeniseAndStopWords:
    def __init__(self,string):
        self.text=string
    def token_and_stop_words(self):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(self.text)        
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = [] 
        for w in word_tokens: 
            if w not in stop_words: 
                filtered_sentence.append(w) 
        print(word_tokens) 
        print(filtered_sentence) 
        tagged = nltk.pos_tag(filtered_sentence) 
        print(tagged)
        #tagged=tagged
        att=Attribute(tagged)
        att.parse_attribute()
        #print(type(tagged[1]))


 

  

 

  

 

  

