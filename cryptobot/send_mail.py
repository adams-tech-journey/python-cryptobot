import os

SLACK_TOKEN= str(os.environ.get('SLACK_TOKEN'))
class SendMail():

    # Posting to a Slack channel
    def send_slack(self,text):
        from urllib import request
        import json

        post = {"text": "{0}".format(text)}
        try:
            json_data = json.dumps(post)
            req = request.Request("https://hooks.slack.com/services/TU4MJSYUE/BU4UJ281L/"+SLACK_TOKEN,
                                  data=json_data.encode('ascii'),
                                  headers={'Content-Type': 'application/json'})
            resp = request.urlopen(req)
        except Exception as em:
            print("EXCEPTION: " + str(em))

