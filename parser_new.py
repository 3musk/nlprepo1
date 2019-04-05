
import re
import string
import sys
import unicodedata
import functools
from threading import Thread

from output import Final_Output

class Parser_new:
    count_keywords = []
    sum_keywords = []
    average_keywords = []
    max_keywords = []
    min_keywords = []
    junction_keywords = []
    disjunction_keywords = []
    greater_keywords = []
    less_keywords = []
    between_keywords = []
    order_by_keywords = []
    asc_keywords = []
    desc_keywords = []
    group_by_keywords = []
    negation_keywords = []
    equal_keywords = []
    like_keywords = []

    def __init__(self):
        self.database_dico =["student"]

    def remove_accents(self, string):
        nkfd_form = unicodedata.normalize('NFKD', str(string))
        return "".join([c for c in nkfd_form if not unicodedata.combining(c)])

    def parse_sentence(self,input_word_list):

        number_of_table = 0
        number_of_select_column = 0
        number_of_where_column = 0
        last_table_position = 0
        columns_of_select = []
        columns_of_where = []


        self.input_word_list=input_word_list
        number_of_where_column_temp = 0
        number_of_table_temp = 0
        last_table_position_temp = 0
        start_phrase = ''
        med_phrase = ''

        # TODO: merge this part of the algorithm (detection of values of where)
        #  in the rest of the parsing algorithm (about line 725) '''
        print(self.input_word_list)
        for i in range(0, len(self.input_word_list)):
            for table_name in self.database_dico:
                #print(self.database_dico)
                if (self.input_word_list[i] == table_name): #or (input_word_list[i] in self.database_object.get_table_by_name(table_name).equivalences):
                    if number_of_table_temp == 0:
                        start_phrase = self.input_word_list[:i]
                    number_of_table_temp += 1
                    last_table_position_temp = i

                columns =["name","rollno","phone","section"] 
                #self.database_object.get_table_by_name(table_name).get_columns()
                for column in columns:
                    if (self.input_word_list[i] == column): #or (input_word_list[i] in column.equivalences):
                        if number_of_where_column_temp == 0:
                            med_phrase = self.input_word_list[len(start_phrase):last_table_position_temp + 1]
                        number_of_where_column_temp += 1
                        break
                    else:
                        if (number_of_table_temp != 0) and (number_of_where_column_temp == 0) and (
                                    i == (len(self.input_word_list) - 1)):
                            med_phrase = self.input_word_list[len(start_phrase):]
                else:
                    continue
                break

        end_phrase = self.input_word_list[len(start_phrase) + len(med_phrase):]
        print("start phrase",start_phrase)

        tables_of_from = []
        select_phrase = ''
        from_phrase = ''
        where_phrase = ''

        #words = re.findall(r"[\w]+", self.remove_accents(sentence))

        for i in range(0, len(self.input_word_list)):
            for table_name in self.database_dico:
                if (self.input_word_list[i] == table_name):# or (words[i] in self.database_object.get_table_by_name(table_name).equivalences):
                    if number_of_table == 0:
                        select_phrase = self.input_word_list[:i]
                    tables_of_from.append(table_name)
                    number_of_table += 1
                    last_table_position = i

                #columns = self.database_object.get_table_by_name(table_name).get_columns()
                for column in columns:
                    if (self.input_word_list[i] == column):# or (words[i] in column.equivalences):
                        if number_of_table == 0:
                            columns_of_select.append(column)
                            number_of_select_column += 1
                        else:
                            if number_of_where_column == 0:
                                from_phrase = self.input_word_list[len(select_phrase):last_table_position + 1]
                            columns_of_where.append(column)
                            number_of_where_column += 1
                        break
                    else:
                        if (number_of_table != 0) and (number_of_where_column == 0) and (i == (len(self.input_word_list) - 1)):
                            from_phrase = self.input_word_list[len(select_phrase):]

        where_phrase = self.input_word_list[len(select_phrase) + len(from_phrase):]
        print("from phrase",from_phrase)
        print("where phrase",where_phrase)
        print("columns of slect",columns_of_select)
        print("column of where",columns_of_where)

        if(len(columns_of_select)==0):
            columns_of_select=None

        if (number_of_select_column + number_of_table + number_of_where_column) == 0:
            print("No keyword found in sentence!")

        if(len(where_phrase)>0):
            value_of_where=where_phrase[len(where_phrase)-1]
        else:
            value_of_where=None

        f_op=Final_Output()
        f_op.output_query(columns_of_select,from_phrase,columns_of_where,value_of_where)
        
