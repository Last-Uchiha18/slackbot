import requests
from datetime import datetime, timedelta

NVD_URL = 'https://services.nvd.nist.gov/rest/json/cves/2.0/'

# this function fetches CVE data using the above endpoint and the given time interval
def get_recent_cves():

    now = datetime.now()
    twenty_four_hours_ago = now - timedelta(days=1)

    publish_start_date = twenty_four_hours_ago.strftime('%Y-%m-%dT%H:%M:%S.000')
    publish_end_date = now.strftime('%Y-%m-%dT%H:%M:%S.000')

    params = {
        'pubStartDate': publish_start_date,
        'pubEndDate': publish_end_date
    }

    try:
        response = requests.get(NVD_URL, params=params)
        response.raise_for_status() 

        data = response.json()

        return data['vulnerabilities']

    except requests.RequestException as e:

        print(f"An error occurred: {e}")
        return None

