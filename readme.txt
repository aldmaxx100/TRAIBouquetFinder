Hello,
With advent of new TRAI rules for Indian DTH customer to select channels 
and bouquet of their own to create their own pack,
the freedom for Indian TV lover is all time high.
But it was observed that Indian Viewers are just selecting single 
channels to make their own pack, leading to increase in cost of
overall pack.
It was observed that selecting bouquet instead of single channel is more 
efficient and saves lot of money.
Thus this API is made.
Created it by finding all single channel cost and bouquet cost available 
in market.
Segregating them and feeding them to API.
The input to API is list of channels and the API returns Json object of 
bouquets and packs name,with its price.
Note:THe input feeded data is that of openly available in market and 
regulated by government.
Some DTH operator have their own custom pack which are not included in 
API.
The main program is API.py that creates a FLASK api listening on 
specified port.

start point in Project is in main_api.py
PEACE OUT!!!
