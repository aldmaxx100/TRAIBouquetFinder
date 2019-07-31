
from full_file import book

def pack_details(pack):
    return_list=[]
    list=pack.split('####')
    bouquet=book.sheet_by_index(0)
    single=book.sheet_by_index(1)


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
                    return_list.append([pack,bouquet.cell(r,2).value,"bouquet"])


    return (return_list)


