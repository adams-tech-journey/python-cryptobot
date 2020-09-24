class SendMail():

    # Posting to a Slack channel
    def send_slack(self,text):
        from urllib import request
        import json

        post = {"text": "{0}".format(text)}
        try:
            json_data = json.dumps(post)
            req = request.Request(SLACK_HOOK,
                                  data=json_data.encode('ascii'),
                                  headers={'Content-Type': 'application/json'})
            resp = request.urlopen(req)
        except Exception as em:
            print("EXCEPTION: " + str(em))

