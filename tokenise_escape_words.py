from List_map import Attribute
import nltk
from nltk.corpus import stopwords 

from nltk.tokenize import word_tokenize 
import csv
from output import Final_Output
from query import Calc_Query

  
class TokeniseAndStopWords:
    def __init__(self,string):
        self.text=string
    def token_and_stop_words(self):
        stop_words = set(stopwords.words('english'))
        #print(type(stopwords))
        #stopwords.remove("what")

        word_tokens = word_tokenize(self.text)        
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = [] 
        for w in word_tokens: 
            if w not in stop_words: 
                filtered_sentence.append(w) 
        #print(word_tokens) 
        #print(filtered_sentence) 
        tagged = nltk.pos_tag(word_tokens)  #filtered_sentence)

        att=Attribute()
        att.parse_attribute(tagged)

        qy=Calc_Query()
        qy.read(tagged) 

        
        #print("this is print whole\n",tagged)
        '''fop=Final_Output()
        f=open("dataset.csv","r")
        reader=csv.reader(f)'''
        '''for row in reader:
            if('SELECT' in row):
                query_type=row[1:]
                for word in query_type:
                    if(word in tagged):
                        fop.write_query('SELECT yeh')'''
                        

        #tagged=tagged


        

        #print(type(tagged[1]))


 

  

 

  

 

  

