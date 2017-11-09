 ### Bitcoin Price Tracker
#### Requirements

- Use latest version of Python3
- Once you've cloned the repo, create a dummy gmail account to send emails from - don't use an email address you care about - The best option is 
to learn to use keyring or securely store your email and password.
- This is meant to be run in conjunction with Cron Tabs to check Bitcoin price at some interval (recommended: every two hours)


#### Instructions

1) `git clone https://github.com/rodcoelho/BTC.git`
2) In `sendmessages.py`, change the username and password to a dummy gmail account (non-personal). In the gmail account settings, disable security features that keep you from sending emails via the terminal.
3) Use Cron Tabs to re-run `btc_api.py` at some interval - recommended: every 2-4 hours. Any shorter interval may not result in a significant change in price.

####PSA: This README is ahead of the application's intended capabilities.
`btc_api.py` is not ready for Cron Tab functionality - a placeholder time.sleep() function is in place for what should be a method for saving data outside of the file so Cron Tabs can re-run the script at the next interval with the prior relevant data points. 