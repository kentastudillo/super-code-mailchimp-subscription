# Mailchimp Subscription

A [Supercode](http://gosupercode.com) function that adds a new subscriber to list members.

## Usage

```
import json
import pprint
import supercode

data = {
  "apikey": "mailchimp-api-key",
  "list_id": "mailchimp-list-id",
  "data": {
    "email_address": "john.doe@example.com",
    "status": 'subscribed',
    "merge_fields": {
        "FNAME": "John",
        "LNAME": "Doe",
        "ADDRESS": "Cebu City"
    }
  }
}

response = supercode.call(
    "super-code-function",
    "your-supercode-api-key",
    data=json.dumps(data)

pprint(response)
```

**Note:** Supercode has not been launched yet. This is for internal testing only.
