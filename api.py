from flask import Flask
from flask import jsonify
from full_file import load_data
from get_details import pack_details
api = Flask(__name__)

#data="aldrin"




@api.route("/pass_data/<data>")
def checkdata(data):
        try:
            my_channel=[]
            split_list=data.split("@")

            for n in split_list:
                my_channel.append(int(n))

            status_code,message,output_pack,output_cost,cost_ala=load_data(my_channel)
            if status_code==0:
                response=jsonify(status_code=status_code,message=message,alacarte_cost=cost_ala)
            else:



                response=jsonify(status_code=status_code,pack=pack_details(output_pack[4:]),cost=output_cost,alacarte_cost=cost_ala)



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