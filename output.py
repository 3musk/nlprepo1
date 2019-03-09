
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
    