import json
class Match:
    def __init__(self,match_data):
        self.match_data=match_data
        self.data_match=json.dumps(self.match_data, indent=4, sort_keys=True)
        print(self.data_match)
    
    def get_list(self,obj1):
        # list1=[]
        # for i in obj1.keys():
        #     list1.append(i)
        # return list1
        return obj1

    def retrive_match(self,sport,country,data_match):
        data_a=data_match['sport'].append(sport) #data_match['sport'] is a list of sport
        data_b=data_match['country'].append(country)
        # for i in data_a:
        #     if data_a[::]==sport:
        #         return sport
        # for j in data_b:
        #     if data_b[::]==country:
        #         return country
        # return sport+" - "+country
        # data_b=data_match[country][country]
        # return data_a,data_b
        # print(data_a['sport'])
        # print(data_match['sport'])
        return data_match
    