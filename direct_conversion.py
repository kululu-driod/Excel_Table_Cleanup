import csv
import re

import argparse
from config import *

""" The following code splits the lines, clean up headers/footers and remove keywords from an csv input file"""
""" Author: Y,  2020"""

# TODO table head rip
# TODO splitting table
# TODO if something is in column 1, and they are all just alphabets of more than 3 words, move them up 1 row to the last non-empty cell

parser = argparse.ArgumentParser(description='Auto clean up OCR output csv file for tendering uses')
parser.add_argument('input_file', nargs='?',
                    help='input csv file, follows right after program name, default to test.csv if not specfied', default="test.csv")
parser.add_argument('--keep_header', dest='keep_header',default=False,
                    help='Remove lines containing headers/footers as is specified in the script')
parser.add_argument('--ignore_keywords', dest='ignore_keywords',default=False,
                    help="ignore and drop certain keywords as is specified in the script")
parser.add_argument('--remove_table_head', dest='remove_table_head',default=False,
                    help="Remove recurring table head as is specified in the script")
parser.add_argument('--table_split', dest='table_split',default=False,
                    help="Auto figure out and splitting tables")
#parser.add_argument('--unmerge_cells', dest='unmerge_cells',default=False,
#                    help="Auto figure out and splitting tables")
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

#def merge_cells(l_2d):
#    # If there is nothing else in the first transposed column, merge the cells in same row the following columns
#    output_l_2d=l_2d
#    line_merged=1
#    for i_row, row in enumerate(l_2d):
#        # if first item ==""
#        if row[0] == "" and (not i_row ==0):
#            for i_item, item in enumerate(l_2d[i_row-1][1:]):
#                # if
#                if not item=="":
#                    output_l_2d[i_row-line_merged][i_item]=item+"\n"+l_2d[i_row][i_item]
#
#                print("row:")
#                print(output_l_2d[i_row-line_merged][i_item])
#                output_l_2d[i_row][i_item]=""
#    return output_l_2d


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
    #if args.ignore_keywords:
    #    for i_row, row in enumerate(l_2d):
    #        for i_item, item in enumerate(row):
    #            if item==




    return output

def remove_header(l_2d, header_keyword=header_keyword, header_contain=header_contain):
    output=[]
    for i_row, row in enumerate(l_2d):
        skip_row=False
        for item in row:

            #print("item: ", item)
            for keyword in header_keyword:
                #print("keyword", keyword)
                if keyword==item:
                    #print("keyword matched: ", keyword)
                    skip_row=True
            for contain_keyword in header_contain:
                #print(contain_keyword)
                if contain_keyword in item:
                    #print("keyword contained: ", contain_keyword)
                    skip_row=True
        if skip_row==False:
            #print("row appending :", row)
            output.append(row)
        #print("output", output)
    return output


print("input_file:", args.input_file)
with open(args.input_file, newline='') as csvfile:
    # ---Reading the csv
    spamreader = csv.reader(csvfile)

    # ---Reading the rows

    output_csv=open('output.csv', 'w', newline='')


    spamwriter = csv.writer(output_csv,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    #TODO call the following smart split line
    for i_row, row in enumerate(spamreader):
        # ---Getting the items in the rows

        l_2d=[]
        # --- For items
        for i_item, item in enumerate(row):
            list_item=item.split("\n")
            # if it's not column 1
            if not i_item==0 and cap_is_newline:
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

        for output_row in l_2d_trans:

            spamwriter.writerow(output_row)
