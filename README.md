# Notify Timeslot
Send you a SMS using Twilio API when a timeslot becomes available on a given day for a signup genius template survey

## Setup
```
$ pip install requests beautifulsoup4 os twilio dotenv
```

Add your Twilio credentials, destination url, sender twilio provided phone number and target phone numer to a `.env`

```
$ python signup.py &
```

This starts a background process that will poll the given URL every 5 minutes to search for certain words under a certain element on the page and sends you a text if found