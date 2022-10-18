import requests
from bs4 import BeautifulSoup
import time
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

# returns a list of spans
def parse_page():
    url = os.environ.get('URL')
    page = requests.get(url)
    # print(page.text)
    soup = BeautifulSoup(page.content, 'html.parser')
    # find div in question
    spans = soup.find_all('span', {'class': 'SUGbigbold'})
    spans = [span.get_text() for span in spans]
    return spans

# returns boolean if thursday available --> 1 for availablility
def search_for_avail(spans):
    friday = "10/21/2022"
    one_of_two = "1 of 2 slots filled"
    for s in spans:
        if one_of_two in s:
            return 1
        if friday in s:
            return 0

# send message from twillio api
def send_message():
    account_sid = os.environ.get('AUTH_SID')
    auth_token = os.environ.get('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="A timeslot has opened for Thursday",
                        from_=os.environ.get('SENDER'),
                        to=os.environ.get('TARGET')
                    )
        
if __name__ == '__main__':
    while not search_for_avail(parse_page()):
        # wait 5 min before next poll
        time.sleep(300)
    send_message()
        
    
