import os
from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# Set the Key Vault URL
KEY_VAULT_URL = os.environ["KEY_VAULT_URL"]

# Authenticate to Azure
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)

@app.route('/')
def get_secret():
    secret = client.get_secret("topsecret")
    return f"The secret value is: {secret.value}"

if __name__ == '__main__':
    app.run(debug=True)

