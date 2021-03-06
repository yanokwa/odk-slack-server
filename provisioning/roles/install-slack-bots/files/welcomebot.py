#!/usr/bin/env python

import sys
import time
import datetime
from slackclient import SlackClient

BOT_TOKEN=sys.argv[1]
WELCOME_MESSAGE="Welcome to the ODK Slack, @{}! There are just three things you need to be aware of.\n\n1. We've automatically added you to some of the more active channels (e.g., #collect-code, #build-code), but make sure to browse and join other channels that interest you (e.g., #meta, #random).\n\n2. Everything that happens on the public Slack channels is archived and searchable at http://opendatakit.slackarchive.io. Private channels and private messages are never publicly archived.\n\n3. To ensure the chat remains a valuable resource, please use the appropriate channels for discussions and refrain from asking non-developer support questions about form design or tool configuration.\n\nSo yeah, that's it. Please introduce yourself to the community in the #general channel and welcome again to the ODK Slack!"

def main():

    sc = SlackClient(BOT_TOKEN)
    if not sc.rtm_connect():
      raise Exception("Couldn't connect to Slack.")

    while True:
     for slack_event in sc.rtm_read():
      if slack_event.get('type') == 'team_join':
        user = slack_event.get('user')
        print sc.api_call('chat.postMessage',channel=user['id'],text=WELCOME_MESSAGE.format(user['name']),parse='full',as_user='true')

     print str(datetime.datetime.utcnow()) + " Sleeping..."
     time.sleep(5)

if __name__ == '__main__':
    main()