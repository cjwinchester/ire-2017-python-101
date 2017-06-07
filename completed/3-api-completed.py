"""
~ post to an API ~

*** NOTE: If you are trying out this script at any point after the 2017 IRE conference in Phoenix, it will not work. You can adapt it to work with your _own_ slack team, tho. LMK if you get stuck. ***

Let's post some data to an API. To make it interesting, let's post a message on Slack. To make it ~even more~ interesting, let's post a message to an IRE employee slack channel.

And we'll do it in three! easy! steps!

1. Grab a string -- a secret "webhook" URL token that allows you to post data to our slack channel -- that your computer is helping keep track of for us.

2. Format your message data in a way that the Slack API will understand.

3. Send the message data to the webhook URL you grabbed in step 1.

"""

import os
import requests
import json

# grab the webhook URL from your computer's environment
# if it's not there, return None
slack_webhook = os.environ.get('IRE_SLACK_WEBHOOK', None)

# check to see if you have the URL
if slack_webhook:

    # if you do, build a dictionary of payload data
    payload = {
        'channel': '#ire-python-101-alerts',
        'username': 'IRE Python Bot',
        'icon_emoji': ':ire:',
        'text': 'sup'
    }

    # turn it into a string of JSON
    payload_as_json = json.dumps(payload)

    # send it to slack!
    r = requests.post(slack_webhook, data=payload_as_json)

else:

    # if you don't have it, print a message to the terminal
    print('You don\'t have the IRE_SLACK_WEBHOOK'
          ' environmental variable')



"""
EXERCISES:
Read through the Slack documentation -- https://api.slack.com/incoming-webhooks -- and post a message to our Slack channel ...
- with a different emoji
- with an image URL instead of an emoji
- with a link in it
- with other kinds of fancy formatting
"""
