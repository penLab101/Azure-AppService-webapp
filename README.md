# webapp

## deployment

```sh
# Create an webapp with --deployment-local-git first
# az webapp create --resource-group <rg> --plan <appServicePlansName> --name <appName> --runtime "PYTHON:3.11" --deployment-local-git
az webapp deployment list-publishing-credentials --resource-group chanel --name w0w0
#> "scmUri": "<scmUri>"; but the url can be wrong
# Find the "local git" url from the portal;
# append cred to it, then
git remote add azure '<scmUri>'
git push azure <localBranchName>:<remoteBranchName>
```
