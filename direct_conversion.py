import csv
import numpy as np
import re

# TODO remove header/footer
# TODO figure out table head
# TODO ignore words (item etc )
# TODO


def transpose_2d_list(l_2d):

    arr_t = np.array(l_2d).T
    l_2d_t = np.array(l_2d).T.tolist()

    return l_2d_t

def transpose_2d_list_string(l_2d):
    max_length=max([len(item ) for item in l_2d])
    l_2d_T=[ [] for i in range(max_length)]
    for i_row, row in enumerate(l_2d):
        for i_column in range(max_length):
            try:
                l_2d_T[i_column].append(l_2d[i_row][i_column])
            except:
                pass
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

    return output


cap_is_newline=False

with open("test.csv", newline='') as csvfile:
    # ---Reading the csv
    spamreader = csv.reader(csvfile)

    # ---Reading the rows

    output_csv=open('output.csv', 'w', newline='')

    spamwriter = csv.writer(output_csv,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i_row, row in enumerate(spamreader):
        # ---Getting the items in the rows

        l_2d=[]
        previous_pos=0
        # --- For items
        for i_item, item in enumerate(row):
            list_item=item.split("\n")
            # if it's not column 1
            if not i_item==0 and cap_is_newline:
                list_item=further_split_at_cap(list_item)

            # TODO identify a header
            header=False

            if not header and not list_item==[""] and not list_item==[]:
                l_2d.append(list_item)
        l_2d_cleaned=clean_2dlist(l_2d)

        if l_2d_cleaned==[]:
            continue
        else:
            l_2d_trans=transpose_2d_list_string(l_2d_cleaned)


        for output_row in l_2d_trans:
            spamwriter.writerow(output_row)
