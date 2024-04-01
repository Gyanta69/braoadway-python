#6811002655:AAFbQ81KRVqFl3hfREbLj8jBQg5B5X1ibAM
import requests
url =  "https://api.telegram.org/bot6811002655:AAFbQ81KRVqFl3hfREbLj8jBQg5B5X1ibAM/sendMessage"
params={
        "chat_id: self.-4148683331",
        "text: opening_data",
     }
# r = requests.post(url,params)
# print(r.json())



class Projectwork:
    def init(self):
        self.token = "6811002655:AAFbQ81KRVqFl3hfREbLj8jBQg5B5X1ibAM"
        self.chat_id = "-4148683331"
        self.url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        self.user = ["sudan", "broadway"]

    def upcoming_birthday(self):
        for i in self.user:
            params = {
                "chat_id": "-1002015317320",
                "text": f'hi i am {i}',
            }
            r = requests.post(url,json=params)


obj = Projectwork()
obj.upcoming_birthday()