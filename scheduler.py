from apscheduler.schedulers.blocking import BlockingScheduler
from fetch_vulnerabilities import get_recent_cves
from send_to_slack import send_message_to_admin

def check_for_vulnerabilities():
    vulnerabilities = get_recent_cves()
    if vulnerabilities:
        send_message_to_admin(vulnerabilities)
    else:
        print('No new vulnerabilties')


scheduler = BlockingScheduler()
scheduler.add_job(check_for_vulnerabilities, 'interval', minutes=1)
