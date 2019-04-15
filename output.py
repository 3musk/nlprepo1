
query_op=[]
class Final_Output:
    '''@staticmethod
    def __init__(self):
        self.query_op=[]'''
    def write_query(self,query_word):
        query_op.append(query_word)
        #print("query    ",query_op)
    def read_query(self):
        print(*query_op)
        #print(" ".join(query_op))
    def output_query(self,col_of_select,table_name,col_of_where,value_of_where):
    
        self.col_of_select=col_of_select
        self.table_name=table_name
        self.col_of_where=col_of_where
        self.value_of_where=value_of_where

        print("SELECT",end=" ")
        if(self.col_of_select is None):
            print("*",end=" ")
        else:
            i=0
            for i in range(len(self.col_of_select)-1):
                print(self.col_of_select[i],end=",")
            if(len(self.col_of_select)==1):
                print(self.col_of_select[i],end=" ")
            else:
                print(self.col_of_select[i+1],end=" ")
        print("FROM",end=" ")
        print(*self.table_name,end=" ")
        if(self.value_of_where is not None):
            print("WHERE",end= " ")
            print(*self.col_of_where,end=" = ")
            print("\"",self.value_of_where,"\"")




    