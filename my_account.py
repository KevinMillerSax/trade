from tda.auth import easy_client
from tda.client import Client
import json
import config

c = easy_client(
        api_key=config.api_key,
        redirect_uri=config.redirect_uri,
        token_path=config.token_path)

resp = c.get_account(config.account_id, fields=c.Account.Fields.POSITIONS)
assert resp.ok
history = resp.json()

print(json.dumps(history, indent=4))