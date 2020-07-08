import csv
import numpy as np

def transpose_2d_list(l_2d):

    print(l_2d)
    arr_t = np.array(l_2d).T

    print("arr_t", arr_t)
    print(type(arr_t))
    # [[0 3]
    #  [1 4]
    #  [2 5]]
    # <class "numpy.ndarray">

    l_2d_t = np.array(l_2d).T.tolist()

    print(l_2d_t)
    print(type(l_2d_t))
    # [[0, 3], [1, 4], [2, 5]]
    return l_2d_t
def transpose_2d_list_string(l_2d):
    print("l_2d", l_2d)
    max_length=max([len(item ) for item in l_2d])
    l_2d_T=[ [] for i in range(max_length)]
    print("l_2df_T", l_2d_T)
    for i_row, row in enumerate(l_2d):
        for i_column in range(max_length):
            try:
                l_2d_T[i_column].append(l_2d[i_row][i_column])
            except:
                pass
    print("l_2d_T", l_2d_T)
    return l_2d_T

def clean_row(l_2d):

    output=[[] for i in range(len(l_2d))]
    for i_row, row in enumerate(l_2d):
        for i_item, item in enumerate(row):
            print("pre-clean", item)


            item=item.replace("  ", "")
            item=item.replace("  ", "")
            print("post-clean", item)
            output[i_row].append(item)

    return output


with open("test.csv", newline='') as csvfile:
    # ---Reading the csv
    spamreader = csv.reader(csvfile)

    print(type(spamreader))
    # ---Reading the rows
    for i_row, row in enumerate(spamreader):
        # ---Getting the items in the rows
        if i_row==0:
            print(row)

            #l_2d=[[] for i in range(len(row))]
            l_2d=[]
            previous_pos=0
            # --- For items
            for i_item, item in enumerate(row):
                print("item:", item)
                pos=item.find("\n")+previous_pos+2
                list_item=item.split("\n")
                # TODO identify a header
                header=False

                if not header and not list_item==[""]:
                    #l_2d[i_row].append(list_item)
                    l_2d.append(list_item)
                    print("list_item: ", list_item)
                #print(item[previous_pos:pos])
                previous_pos=pos+1
            print("l_2d", l_2d)
            l_2d_cleaned=clean_row(l_2d)

            l_2d_trans=transpose_2d_list_string(l_2d_cleaned)
            print(l_2d_trans)

            with open('output.csv', 'w', newline='') as csvfile:
                #spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for row in l_2d_trans:
                    spamwriter = csv.writer(csvfile,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(row)


