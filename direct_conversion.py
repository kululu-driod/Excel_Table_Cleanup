import csv
import re

import argparse
from config import *

""" The following code splits the lines, clean up headers/footers and remove keywords from an csv input file"""
""" Author: Y,  2020"""

# TODO table head rip
# TODO splitting table
# TODO if something is in column 1, and they are all just alphabets of more than 3 words, move them up 1 row to the last non-empty cell
#TODO remove cells that contains nothing but special characters

parser = argparse.ArgumentParser(description='Auto clean up OCR output csv file for tendering uses')
parser.add_argument('input_file', nargs='?',
                    help='input csv file, follows right after program name, default to test.csv if not specfied', default="test.csv")
parser.add_argument('--keep_header', dest='keep_header',default=False, action="store_true",help='Remove lines containing headers/footers as is specified in the script')
parser.add_argument('--caps_newline', dest='caps_is_newline',default=False, action="store_true",help='Split line in cells by capitalization')
parser.add_argument('--ignore_keywords', dest='ignore_keywords',default=False,
action="store_true", help="ignore and drop certain keywords as is specified in the script")
parser.add_argument('--remove_table_head', dest='remove_table_head',default=False,action="store_true", help="Remove recurring table head as is specified in the script")
parser.add_argument('--extra_format', dest='extra_format',default=False,action="store_true", help="Extra Formatting to put numbers in one row and words in another")
#parser.add_argument('--table_split', dest='table_split',default=False,
#                    help="Auto figure out and splitting tables")
parser.add_argument('--unmerge_cells', dest='unmerge_cells',default=False,
                    help="Auto figure out and splitting tables")
args = parser.parse_args()


def transpose_2d_list_string(l_2d):
    max_length=max([len(item) for item in l_2d])
    l_2d_T=[ [] for i in range(max_length)]
    for i_row, row in enumerate(l_2d):
        for i_column in range(max_length):
            try:
                l_2d_T[i_column].append(l_2d[i_row][i_column])
            except:
                l_2d_T[i_column].append('')

    #if (not args.unmerge_cells):
    #    l_2d_T=merge_cells(l_2d_T)

    return l_2d_T



def further_split_at_cap(input_list, cap=True):
    #TODO need too ignore number characters
    if cap:
        split_on='[A-Z][^A-Z]*'
    final_list=list()
    for item in input_list:
        final_list=final_list+re.findall(split_on, item)

    return final_list


def clean_2dlist(l_2d, ugly_chars=["  "]):
    # removing all ugly characters in a 2d list
    output=[[] for i in range(len(l_2d))]
    for i_row, row in enumerate(l_2d):
        for i_item, item in enumerate(row):

            for ugly_char in ugly_chars:
                item=item.replace(ugly_char, "")
                item=item.replace(ugly_char, "")
            output[i_row].append(item)
    # if the item in the ignore list, ignore them

    if args.ignore_keywords:

        precleaned_output=output
        for i_row, row in enumerate(precleaned_output):
            for i_item, item in enumerate(row):

                for keyword in remove_items:
                    if item==keyword:
                        output[i_row][i_item]=''
    return output

def remove_header(l_2d, header_keyword=header_keyword, header_contain=header_contain):
    output=[]
    for i_row, row in enumerate(l_2d):
        skip_row=False
        for item in row:

            for keyword in header_keyword:
                if keyword==item:
                    skip_row=True
            for contain_keyword in header_contain:
                if contain_keyword in item:
                    skip_row=True
        if skip_row==False:
            output.append(row)
    return output

def further_format(l_2d):

    #--- Using column list from config.py
    #--- If special keyword in first digits, collect second row digits into first row
    l_2d_output=l_2d

    for i_row, row in enumerate(l_2d):
        #for i_item, item in enumerate(row):
        append_string=""
        #--- Appended string
        contains_alpha=False

        if any(keyword in row[0] for keyword in column_list):
            try:
                # -- if there are any characters at all in the row
                contains_alpha=any([ char.isalpha() for char in row[1] ])
                for i_index, char in enumerate(row[1]):
                    if (row[1][i_index].isdigit() or row[1][i_index]==".") and not "mm" in row[1]:
                        append_string=append_string+row[1][i_index]
                    else:
                        break
            except:
                pass
        if not append_string=="":# and not contains_alpha:
            l_2d_output[i_row][0]=l_2d_output[i_row][0]+" "+append_string
            if (l_2d_output[i_row][1]==append_string):
                l_2d_output[i_row].pop(1)
            else:
                l_2d_output[i_row][1]=l_2d_output[i_row][1]=l_2d_output[i_row][1][len(append_string):]

    #--- If alphabets in the first column following numbers and ., move them
    #--- to the beginning of the second column
    l_2d=l_2d_output
    for i_row, row in enumerate(l_2d):

        there_is_numbers=False
        number=""
        string_appended=""
        char_starts=False
        for i_index, char in enumerate(row[0]):
            if char.isdigit():
                there_is_numbers=True

            if there_is_numbers and char.isalpha():
                char_starts=True
            if there_is_numbers and char_starts:
                string_appended=string_appended+char
            elif there_is_numbers and not char_starts:
                number=number+char


        if not string_appended=="":
            l_2d_output[i_row][0]=number
            if len(l_2d_output[i_row])==1:
                l_2d_output[i_row].append(string_appended)
            else:
                l_2d_output[i_row][1]=string_appended+l_2d_output[i_row][1]



    l_2d=l_2d_output

    for i_row, row in enumerate(l_2d):

        if len(row)==1:

            there_is_alpha=any([char.isalpha for char in row[0]])
            if there_is_alpha:
                l_2d_output[i_row].append(l_2d_output[i_row][0])
                l_2d_output[i_row][0]=""

    # --- If the column 1 does not contain numbers, move it to column 2, if column 2 does not contain characters, move it to column 1, move everything else up 1


    l_2d=l_2d_output
    for i_row, row in enumerate(l_2d):
        # if column 1 does not contain numbers
        if not any([char.isdigit() for char in row[0]]):
            if len(row)==1:
                l_2d_output[i_row].append(row[0])
                l_2d_output[i_row][0]=""
            else:
                l_2d_output[i_row][1]=l_2d[i_row][0]+" "+l_2d[i_row][1]
                l_2d_output[i_row][0]=""


    # popping all the first cells if they are empty
    l_2d=l_2d_output
    for i_row, row in enumerate(l_2d):
        for i_item, item in enumerate(row):
            if item=="":
                l_2d_output[i_row].pop(i_item)

    # if there are more than 3 characters in the first row, move them right
    l_2d=l_2d_output
    for i_row, row in enumerate(l_2d):
        l_char=[char for char in row[0] if char.isalpha()]
        if len(l_char)>=3:
            if len(row)>1:
                l_2d_output[i_row][1]=l_2d[i_row][0]+l_2d[i_row][1]
                l_2d_output[i_row][0]=""
            else:
                l_2d_output[i_row].append(l_2d[i_row][0])
                l_2d_output[i_row][0]=""

    return l_2d_output




print("input_file:", args.input_file)

with open(args.input_file, newline='') as csvfile:
    # ---Reading the csv
    spamreader = csv.reader(csvfile)
    # ---Reading the rows
    output_csv=open('output.csv', 'w', newline='')

    spamwriter = csv.writer(output_csv,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #--- smart split line
    for i_row, row in enumerate(spamreader):
        # ---Getting the items in the rows

        l_2d=[]
        # --- For items
        for i_item, item in enumerate(row):
            list_item=item.split("\n")
            # if it's not column 1
            if not i_item==0 and args.caps_is_newline:
                list_item=further_split_at_cap(list_item)

            # If line contain header keyword, remove it
            if not args.keep_header:
                for keyword in header_keyword:
                    if keyword in list_item:
                        continue
            if not list_item==[""] and not list_item==[]:
                l_2d.append(list_item)


        l_2d_cleaned=clean_2dlist(l_2d)


        if l_2d_cleaned==[]:
            continue
        else:
            l_2d_trans=transpose_2d_list_string(l_2d_cleaned)


        #--- remove header
        if not args.keep_header:
            l_2d_trans=remove_header(l_2d_trans)

        #---Futher formatting (keeps number in one column and alphabets in another)
        if args.extra_format:
            l_2d_trans=further_format(l_2d_trans)

        for output_row in l_2d_trans:
            spamwriter.writerow(output_row)
