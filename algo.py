import json
alacarte=0

def formatter_channel_name(list,mapping,output,alacarte_cost,output_cost,single_cost):
    global alacarte
    res=[]

    for o in output:
        res.append([o['name'],float(o['cost']),"bouquet",o['channelname']])

    for l in list:
        res.append([mapping[str(l)],alacarte[str(l)],"single"])








    return {
        "alacarte_cost":alacarte_cost,
        "cost":output_cost+single_cost,
        "message":"success",
        "pack":res,
        "status_code":1
    }






def get_single_cost(list):
    #print(list)
    global alacarte
    alacost=alacarte
    cost=0
    for l in list:
        #print(l)
        cost=cost+alacost[str(l)]
    return cost


def filter_bouquet(masterb,channel):
    full=set()
    selection=[]
    for k in masterb:
        inte=channel.intersection(k['channel'])
        if len(inte)>0 and k['cost']<get_single_cost(inte):
            selection.append(k)
            full=full.union(k['channel'])
    return selection,full

def update_pcp(selection,channel):
    result=[]
    for s in selection:
        s['pcp']=s['cost']/len(channel.intersection(s['channel']))
        result.append(s)
    return sorted(result,key=lambda i:i['pcp'])
def main_func(channel,masterselection,alcarinput,mapping):
    global alacarte
    alacarte=alcarinput
    output=[]
    mincost=get_single_cost(channel)
    print('alacartecost='+str(get_single_cost(channel)))
    #print('channel='+str(len(channel)))
    #print(single_channel_name(channel,mapping))

    #print('bouquet='+str(len(masterselection)))
    #print('filtering')
    selection,full=filter_bouquet(masterselection,channel)
    common=full.intersection(channel)
    single=channel.difference(full)
    #print(common)
    #print(single)
    cost=0

    while len(selection)!=0:
        selection=update_pcp(selection,common)
        first=selection[0]
        output.append(first)
        cost=cost+first['cost']
        common=common.difference(first['channel'])
        selection,f=filter_bouquet(selection,common)
    single=single.union(common)

    return formatter_channel_name(single,mapping,output,mincost,cost,get_single_cost(single))





