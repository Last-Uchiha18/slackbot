from rest_framework.decorators import api_view
from rest_framework.response import Response
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from message_payloads import create_to_reply, create_to_send_to_team

# this handles the post request sent by slack after button click

@api_view(['POST'])
def button_clicked(request):

    payload = json.loads(request.data.get('payload', ''))
    
    # parsing of payload to extract the information required
    reply_by_member = ''
    information = payload['state']['values']
    
    for i in information:
        for j in information[i]:
            if 'selected_options' in information[i][j]:
                selected_users = information[i][j]['selected_options']
            else:
                reply_by_member = information[i][j]['value']

    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../config.json'))

    try:
        with open(config_path) as config_file:
            config = json.load(config_file)
            slack_token = config['slack_token']
            admin_id = config['admin_id']
    except FileNotFoundError:
        print("Error: config.json file not found.")
        exit(1)
    except KeyError as e:
        print(f"Error: Missing key {e} in config.json.")
        exit(1) 

    client = WebClient(token=slack_token)


    description = payload['message']['text']
    sent_by = payload['user']['username']
    
    # if a team member replies
    if reply_by_member:

        message = create_to_reply(description, sent_by, reply_by_member)

        try:
            response = client.chat_postMessage(
                channel= admin_id,
                blocks = message["blocks"]
            )
            
            # Check response and handle errors if needed
            if response["ok"]:
                print(f"Confirmation message sent successfully to {admin_id}")
            else:
                print(f"Failed to send confirmation message to {admin_id}: {response}")
        
        except SlackApiError as e:
            print(f"Error sending confirmation message to {admin_id}: {e.response['error']}")

    # if a confirm/foward button is clicked
    else:

        # need not do anything if confirm button is clicked and hence early return
        if payload['actions'][0]['type'] == 'multi_static_select':
            return Response({"Succesful": "!!!"})

        user_ids = []
        for i in range(len(selected_users)):
            user_ids.append(selected_users[i]['value'])
        
        message = create_to_send_to_team(description)
        for user_id in user_ids:

            try:
                response = client.chat_postMessage(
                    channel=user_id,
                    blocks=message["blocks"]
                    )
                assert response["ok"]
                print("Message sent successfully to admin.")
            except SlackApiError as e:
                print(f"Error sending message: {e.response['error']}")

        
    return Response({"Succesful": "!!!"})

