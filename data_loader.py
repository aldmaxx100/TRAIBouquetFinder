import xlrd
selection=[]
alacarte={}
mappingname={}
wb = xlrd.open_workbook('/home/aldrinmachado/mysite/Listpay.xlsx')
bouquetsheet = wb.sheet_by_index(0)
singlesheet=wb.sheet_by_index(1)

def load_bouquet():
    global selection
    last=''
    blist=[]
    bnamelist=[]
    for i in range(bouquetsheet.nrows):

        bname=bouquetsheet.cell_value(i,0)
        bvalue=bouquetsheet.cell_value(i,2)
        bchannelnames=bouquetsheet.cell_value(i,1)
        bchannel=int(bouquetsheet.cell_value(i,3))
        #print(bname)
        if i==0:
            blist=[]
            bnamelist=[]
            last=bname
            lastcost=bvalue
            blist.append(bchannel)
            bnamelist.append(bchannelnames)
        elif bname=='':
            blist.append(bchannel)
            bnamelist.append(bchannelnames)
        elif bname!=last and bname!='':
            data={
                'name':last,
                'channelname':bnamelist,
                'channel':set(blist),
                'cost':lastcost

            }
            #print(data)
            selection.append(data)
            last=bname
            lastcost=bvalue
            blist=[]
            bnamelist=[]
            blist.append(bchannel)
            bnamelist.append(bchannelnames)






def load_single():
    global selection
    global alacarte
    for i in range(singlesheet.nrows):
        data={
            'name':'single_'+singlesheet.cell_value(i,0),
            'channel':set([int(singlesheet.cell_value(i,1))]),
            'cost':singlesheet.cell_value(i,2)

        }
        #selection.append(data)
        alacarte[str(int(singlesheet.cell_value(i,1)))]=singlesheet.cell_value(i,2)
        mappingname[str(int(singlesheet.cell_value(i,1)))]=singlesheet.cell_value(i,0)
    return






def main_function():

    load_bouquet()
    load_single()
    #print(mappingname)
    return selection,alacarte,mappingname



