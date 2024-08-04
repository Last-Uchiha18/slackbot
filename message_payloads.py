# message payload to send to team
def create_to_send_to_team(vulnerability_description):

    return {
        "blocks": [
            {
                "type": "section",
                "block_id": "vulnerability_description",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Description of Vulnerability:*\n{vulnerability_description}"
                }
            },
            {
                "type": "input",
                "block_id": "remediation_description",
                "label": {
                    "type": "plain_text",
                    "text": "Remediation Description"
                },
                "element": {
                    "type": "plain_text_input",
                    "action_id": "remediation_input",
                    "multiline": True
                }
            },
            {
                "type": "actions",
                "block_id": "actions_block",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Confirm"
                        },
                        "action_id": "confirm_vulnerability",
                        "value": "confirm"
                    }
                ]
            }
        ]
    }

# message payload to send confirmation message to admin
def create_to_reply(description, sent_by, reply_by_member):

    return {
        "blocks": [
                    {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": description
                    }
                    },
                    {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Reply by:*\n{sent_by}"
                    }
                    },
                    {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": reply_by_member
                    }
                    }
                ]
    }

# message payload to send message to admin after fetching from NVD database
def create_to_send_to_admin(description, member_options):

    return {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*New Vulnerability Added to NVD*\n\n*Description:*\n{description}"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Select team members to forward the details:"
                    },
                    "accessory": {
                        "type": "multi_static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select members"
                        },
                        "options": member_options
                    }
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Forward"
                            },
                            "value": "forward",
                            "action_id": "forward_vulnerability"
                        }
                    ]
                }
            ]
        }
