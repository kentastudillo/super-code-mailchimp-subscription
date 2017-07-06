""" Import required libraries """
import json
import requests

URL = "https://us16.api.mailchimp.com/3.0/lists/{list_id}/members"


def main(api_key, list_id, email_address, fields):
    """ Add new user to mailchimp subscription. """

    response = {}
    response["type"] = "error"

    headers = {"Content-Type": "application/json"}

    data = {
        "email_address": email_address,
        "status": "subscribed",
        "merge_fields": fields
    }

    try:
        result = requests.post(
            URL.format(list_id=list_id),
            auth=('username', api_key),
            data=json.dumps(data),
            headers=headers)

        result_json = json.loads(result.text)

        if result.status_code == 200:
            response["type"] = "success"
            response["data"] = result_json
        elif result.status_code == 403:
            response["error"] = {}
            response["error"]["message"] = "Authentication failed. "
        elif result.status_code in [400, 404]:
            response["error"] = {}
            response["error"]["message"] = result_json["detail"]
    except requests.exceptions.HTTPError as err:
        response["error"] = {}
        response["error"]["message"] = "Failed to connect."
    except Exception as err:
        response["error"] = {}
        response["error"]["message"] = str(err)

    return response