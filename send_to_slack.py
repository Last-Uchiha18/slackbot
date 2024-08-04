import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from message_payloads import create_to_send_to_admin

def send_message_to_admin(vulnerabilities):
    
    try:
        with open('config.json') as config_file:
            config = json.load(config_file)
            slack_token = config['slack_token']
            admin_user_id = config['admin_id']
    except FileNotFoundError:
        print("Error: config.json file not found.")
        exit(1)
    except KeyError as e:
        print(f"Error: Missing key {e} in config.json.")
        exit(1)

    client = WebClient(token=slack_token)
    
    # using client to send message to admin after fetching the list of users he can forward the message to

    #getting user list
    try:
        response = client.users_list()
        users = response['members']
        
        member_options = [
            {
                "text": {
                    "type": "plain_text",
                    "text": user['profile']['real_name']
                },
                "value": user['id']
            }
            for user in users
            if not user['is_bot'] and user['deleted'] is False
        ]

    except SlackApiError as e:
        print(f"Error fetching users: {e.response['error']}")
        exit(1)
    

    # sending messages to admin
    
    for vulnerability in vulnerabilities:

            vulnerability_description = vulnerability['cve']['descriptions'][0]['value']


            message = create_to_send_to_admin(vulnerability_description, member_options)
            try:
                response = client.chat_postMessage(
                    channel=admin_user_id,
                    blocks=message["blocks"]
                )
                assert response["ok"]
                print("Message sent successfully to admin.")
            except SlackApiError as e:
                print(f"Error sending message: {e.response['error']}")
            break # remove this break statement to show all the vulnerabilities fetched, added this so that it does not get flooded with messages
    

