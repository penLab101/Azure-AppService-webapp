# webapp

## deployment

```sh
az webapp deployment list-publishing-credentials --resource-group chanel --name w0w0
#> "scmUri": "<scmUri>",
git remote add azure '<scmUri>'
git push azure
```
