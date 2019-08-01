
from full_file import book

bouquet = book.sheet_by_index(0)
single = book.sheet_by_index(1)


def pack_details(pack):
    return_list=[]
    list=pack.split('####')


    for pack in list:
        #print(pack)
        #print(pack[8:])
        if 'alacarte' in pack:
            #search in single sheet:
            for r in range(single.nrows):
                #print(single.cell(r,0).value)
                if pack[9:]==single.cell(r,0).value:
                    return_list.append([pack[9:],single.cell(r,2).value,"single"])
        else:
            for r in range(bouquet.nrows):
                if pack==bouquet.cell(r,0).value:

                    return_list.append([pack,bouquet.cell(r,2).value,"bouquet",get_pack_channels(pack)])

    return (return_list)

def get_pack_channels(pack):
    included_channels=[]
    flag=0
    i=0
    #print(pack)
    #print("in get pack")
    while(1):
        if bouquet.cell(i,0).value==pack or flag==1:
            if bouquet.cell(i,0).value!="" and bouquet.cell(i,0).value!=pack:
                return included_channels
            else:
                flag=1
                included_channels.append(bouquet.cell(i,1).value)

        i=i+1



