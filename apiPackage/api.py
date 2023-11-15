#api.py


import requests

class TimeZoneInfo:
    def __init__(self):
        self.url = "https://api-basketball.p.rapidapi.com/timezone"

        self.headers = {
            "X-RapidAPI-Key": "18c1b9c702msh842f6c060f6794cp148669jsn2c8a0053d687",
            "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
        
    #this is a get that retrieves the time zones for cities 
    def get_timezone(self):
        response = requests.get(self.url, headers=self.headers)
        return response.json()

    def print_timezone(self):
        data = self.get_timezone()
        addis_ababa = data['response'][2]
        argentina = data['response'][57]
        chicago = data['response'][87]
        new_york = data['response'][152]
        hong_kong = data['response'][239]        
        berlin = data['response'][321]        
        london = data['response'][341]
        print(f'{addis_ababa}, {argentina}, {chicago}, {new_york}, {hong_kong}, {berlin}, {london}')
        
