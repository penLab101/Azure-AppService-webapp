import os
from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# Set the Key Vault URL
KEY_VAULT_URL = os.environ["KEY_VAULT_URL"]

    
@app.route('/')
def get_secret():
    # Authenticate to Azure
    try:
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)
        secret = client.get_secret("topsecret")
        return f"The secret value is: {secret.value}"
    except Exception as E: 
        return str(E)

    return "dummy test"

if __name__ == '__main__':
    app.run(debug=True)

