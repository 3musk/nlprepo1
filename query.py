import csv
from output import Final_Output
from List_map import Attribute

class Calc_Query:
    def __init__(self):
        self.sample=[]
        self.dataset=[]
    def read(self,tagged):
        self.sample=tagged
        print(self.sample)
        fop=Final_Output()
        f=open("dataset.csv","r")
        reader=csv.reader(f)
        for row in reader:
            self.dataset.append(row)
        x=[]
        flag=0
        #print("dataset\n\n",self.dataset,"\n\n")
        for tup in self.sample:
            if((tup[0] in Attribute.attribute_list_new) or (tup[0] in Attribute.table_list_new) or (not Attribute.attribute_list_new)):
                if(tup[0] in Attribute.table_list_new):
                        fop.write_query("FROM")
                        fop.write_query(tup[0])
                        
                elif(tup[0] in Attribute.attribute_list_new):
                        fop.write_query(tup[0])
                elif(not Attribute.attribute_list_new):
                        fop.write_query("*")
                        
            for x in self.dataset:
                #print(x,"\n")
                if((tup[0] in x)):
                    fop.write_query(x[0])
                    flag=1
                    break
    
        fop.read_query()
        
