from output import Final_Output

class Attribute:
    table_list_new=[]   # output of table name from query
    attribute_list_new=[]  # output of columns names from query
    def __init__(self):
        
        self.table_list=["student","teacher"]   #given table names
        self.database_list=["university"]   #given database names
        self.attribute_dict={"student":["name","rollno","phone","section"]} # all tables attributes or columns names
           
    def parse_attribute(self,tagged):
        self.tagged=tagged
        #Sprint("this is \n",self.tagged)   
        for i in self.tagged:
            if(i[1] in ["NN","NNs","VB","VBs"]):
                if(i[0] in self.table_list):
                    Attribute.table_list_new.append(i[0])
                    if(i[0] in self.attribute_dict):
                        for j in self.tagged:
                            if(j[1] in ["NN","NNs","VB","VBs"]):
                                if(j[0] in self.attribute_dict[i[0]]):
                                    Attribute.attribute_list_new.append(j[0])
        #print(Attribute.attribute_list_new,"table-",Attribute.table_list_new)
        