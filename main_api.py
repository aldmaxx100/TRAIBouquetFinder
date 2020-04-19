from flask import Flask
from flask import jsonify
api = Flask(__name__)
from data_loader import main_function
selection,alacarte,mappingname=main_function()
from algo import main_func



@api.route("/pass_data/<data>")
def checkdata(data):
    global selection
    global alacarte
    global mappingname
    try:
        my_channel=set()
        split_list=data.split("@")

        for n in split_list:
            my_channel.add(int(n))
        data=main_func(my_channel,selection,alacarte,mappingname)
        response=jsonify(alacarte_cost=data['alacarte_cost'],cost=data['cost'],pack=data['pack'],message='success',status_code=1)


    except Exception as e:
        response=jsonify(status_code=-1,message=str(e))

    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")

    return response


@api.route("/test")
def check():

    response=jsonify({"message":"test Successfull2"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response




if __name__ == '__main__':
    api.run()