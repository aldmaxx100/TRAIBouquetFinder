import xlrd
from flask import jsonify
#from main_sort import main_sort_function
channel_req=[]
filteredList=[]
alacarte_list=[]
cost_ala=0
#import xlwt
#workbook = xlwt.Workbook()
#name='$$$'
#sheet = workbook.add_sheet('output_sheet_for_'+name)
#excel_row=0
all_pack=[]
book = xlrd.open_workbook('Listpay.xlsx')


def interim_cost(string_calling):
    interim_cost=0
    a=0
    b=0
    for i, c in enumerate(string_calling):

        if "@" == c:
            if a==0:
                a=i

        if "#"==c:
            if b==0:
                b=i

        if a!=0 and b!=0:
            interim_cost=interim_cost+float(string_calling[a+1:b])
            a=0
            b=0

    return interim_cost


def find_hit(channel_list,bouquet_list):

    for n in channel_list:
        for b in bouquet_list:
            if b==n:
                return 1

    return 0

def find_ala_cost(n):
    for a in alacarte_list:
        if n in a:
            return interim_cost(str(a))




def is_cost_effective(channel_list,bouquet_list):
    price=interim_cost(str(bouquet_list))
    channel_cost=0
    chan=""
    for n in channel_list:
        for b in bouquet_list:
            if b==n:
                chan=chan+","+str(n)
                channel_cost=channel_cost+find_ala_cost(n)
    #print(str(channel_list))
    #print(str(bouquet_list))
    #print ("b="+str(price))
    #print("c="+str(channel_cost))
    if(price<=channel_cost):
        #print(str(bouquet_list))
        #print("channel_cost="+str(channel_cost))
        #print("bou_cost="+str(price))
        #print (chan)
        return 1
    else:
        return 0


def load_data(channels):
    #print("loading_data")
    #book = xlrd.open_workbook('/home/aldrinmachado/mysite/Listpay.xlsx')

    #print(channels)
    #channel_req=channels
    global cost_ala
    cost_ala=0
    global numbersList
    numbersList = []



    count=0

    first_sheet = book.sheet_by_index(0)
    max=first_sheet.nrows
    mylist=[]

    #load bouquet list
    for r in range(max):

        if(first_sheet.cell(r,0).value)!="":

            if r==0:
                name=(first_sheet.cell(r,0).value)
                price=(first_sheet.cell(r,2).value)
            else:
                mylist.append("@"+str(float(price))+"#")
                mylist.append("$" + name + "%")
                mylist.append(name.replace(" ",""))
                numbersList.append(mylist)
                mylist=[]
                name=(first_sheet.cell(r,0).value)
                price=(first_sheet.cell(r,2).value)




        mylist.append(int(first_sheet.cell(r,3).value))


    #load channel_required list
    second_sheet=book.sheet_by_index(1)
    max=second_sheet.nrows

    mylist=[]
    #channel_req=[]
    cost_ala=0
    global alacarte_list
    alacarte_list=[]
    for n in channels:

        for r in range(max):
                mylist=[]
                if (int(n)==second_sheet.cell(r,1).value):
                    #channel_req.append(int(second_sheet.cell(r,1).value))
                    cost_ala=cost_ala+float(second_sheet.cell(r,2).value)
                    mylist.append(int(second_sheet.cell(r,1).value))
                    mylist.append("@"+str(second_sheet.cell(r,2).value)+"#")
                    name="alacarte_"+second_sheet.cell(r,0).value
                    mylist.append("$"+name+"%")
                    mylist.append(name.replace(" ",""))
                    alacarte_list.append(mylist)
                    #numbersList.append(mylist)



    #print("ala_cost="+str(cost_ala))
    #print("totallist="+str(len(numbersList)))
    #print("channel_list="+str(channel_req))
    global filteredList
    filteredList=[]
    #print(cost_ala)
    #print("channels="+str(channels))
    for num in numbersList:
        if(interim_cost(str(num))<cost_ala and is_cost_effective(channels,num)==1):
            filteredList.append(num)

    #print("filtered_list="+str(len(filteredList)))
    #print("alacarte_list="+str(len(alacarte_list)))
    #print("loading complete")
    #print("calling_main_function")
    return (main_sort_function(channels))


def find_hit(channel_list,bouquet_list):

    for n in channel_list:
        for b in bouquet_list:
            if b==n:
                return 1

    return 0

def find_rem(channel_list,bouquet_list):
     rem=[]
     for n in channel_list:
         if n not in bouquet_list:
             rem.append(n)

     return rem


def display_pack_cost(cost_string):
    cost=0.0
    final_pack=""
    k=0
    l=0

    print(cost_string)

    for i, c in enumerate(cost_string):

        if "$" == c:
            if k==0:
                k=i

        if "%"==c:
            if l==0:
                l=i

        if k!=0 and l!=0:
            final_pack=final_pack+"####"+cost_string[k+1:l]
            k=0
            l=0

    k=0
    l=0
    for i, c in enumerate(cost_string):

        if "@" == c:
            if k==0:
                k=i

        if "#"==c:
            if l==0:
                l=i

        if k!=0 and l!=0:
            cost=cost+float((cost_string[k+1:l]))
            k=0
            l=0


    #print(final_pack)
    #rint(str(cost))
    global excel_row
    global all_pack
    interim_detail=[]
    interim_detail.append(final_pack)
    interim_detail.append(cost)
    all_pack.append(interim_detail)
   # sheet.write(excel_row,0,final_pack)
    #sheet.write(excel_row,1,cost)
    #sheet.write(excel_row,2,(cost+float(130))*1.18)
    #excel_row=excel_row+1




def interim_cost(string_calling):
    interim_cost=0
    a=0
    b=0
    for i, c in enumerate(string_calling):

        if "@" == c:
            if a==0:
                a=i

        if "#"==c:
            if b==0:
                b=i

        if a!=0 and b!=0:
            interim_cost=interim_cost+float(string_calling[a+1:b])
            a=0
            b=0

    return interim_cost

def find_channel(mylist,calling,cost_ala):
        #print("in find channel")

        if (interim_cost(calling)>=cost_ala):
        #print(interim_cost(current))
                    return


        for n in filteredList:

            current=calling
            i=0
                #print(calling)
                #print(str(n))

                #print("calling "+calling)
            #print("pack "+str(n))

            #print("list"+str(mylist))
            i = find_hit(mylist,n)
                #print("pack"+str(n))
            if i==1:
                    #print("hit")
                    #print("hit"+str(n))
            #if(interim_cost(str(current)+str(n))<cost_ala):
                r=find_rem(mylist,n)
                #print("hit"+str(r))
                current=str(current)+str(n)
                                        #print("len"+str(len(r)))
                                        #current=current+"###"
                #print(current)
                if len(r)!=0:
                    find_channel(r,current,cost_ala)
                else:
                    if(interim_cost(current)<cost_ala):
                        display_pack_cost(current)
                        return

        for m in mylist:
            for a in alacarte_list:
                if m in a:
                    current=current+str(a)

        display_pack_cost(current)


def main_sort_function(channel_req):
    global  all_pack
    all_pack=[]
    #print("in main function")

    global filteredList
    #print(str(len(filteredList)))
    if(len(filteredList)==0):
        status_code=0
        return (status_code,"select all alacarte channels","","",cost_ala)
        exit(0)
    #print("channel_req="+str(channel_req))
    #print(cost_ala)
    find_channel(channel_req,"",cost_ala)
    #workbook.save('output.xls')
    #print("check output file")
    output_pack=""
    output_cost=10000
    for n in all_pack:
        if(int(n[1])<output_cost):
            output_pack=str(n[0])
            output_cost=int(n[1])


    return (1,"Success",output_pack,output_cost,cost_ala)
