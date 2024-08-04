# Slack Vulnerability Notification App

## Description

This application fetches new vulnerabilities from the National Vulnerability Database (NVD) and notifies system administrators through Slack. It allows administrators to forward vulnerability details to other team members for remediation.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [File Structure and Description](#file-structure-and-description)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Installation

### Prerequisites

- Python 3.7+
- Django

### Steps

1. Clone the repository:

   ```sh
   git clone https://github.com/your-repo/slack-vulnerability-app.git
   cd slack-vulnerability-app
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Run the Django server:
   ```sh
   python manage.py runserver
   ```

## Usage

1. Start the Django server.
2. Configure your Slack app to send interactive message payloads to your server’s endpoint.
3. Configure Scope under OAuth & Permission to allow the app to send messages.
   chat:write
   chat:write.public
   incoming-webhook
   users:read
   users:read.email
4. Add the end point in allowed hosts in settings.py file of the project.
5. The application will fetch new vulnerabilities at the configured interval (you can configure this in scheduler.py file) and notify the admin on Slack.
6. Remove break statement at end of send_to_slack.py file

## Configuration

- **SLACK_TOKEN:** Your Slack API token.
- **ADMIN_ID:** The Slack user ID of the administrator.

## API Endpoints

- **api/slack/interactive:** Endpoint for handling interactive responses from Slack. Sample -> https://2b88-117-245-201-60.ngrok-free.app/api/slack/interactive/

## File Structure and Description

Here is an overview of the project's structure and a brief description of each file and directory:

1. fetch_vulnerabilties.py -> This file is reponsible for fetching the new vulnerabilties added to the NVD database, using the API end point provided by them, in the last 24 hours. You can change the time duration to suit your needs.

2. main.py file -> run this file using "python main.py" and the scheduler will start, hence the whole application

3. message_payloads.py -> used for creating message payloads to be sent to the slack API to send messages to admin or user.

4. scheduler.py -> starts the scheduler which fetches data from NVD at regular intervals and send message to admin

5. send_to_slack.py -> sends vulnerability details to the admin.

6. api folder -> this is the app created using django. Helpful if you want to scale and have more endpoints

7. api/views.py -> this will contain the api endpoint to which slack will send the POST data when a button is clicked.

8. api/urls.py -> add the urls here if you have more end points. And handle the same in views.py file
