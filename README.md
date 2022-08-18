## View the documentation at: https://jillvillany.github.io/python-dev-setup/

### To create the documentation site

```
conda create -n python-dev-setup python=3.9
poetry install
python sync_or_create_all_mds.py
mkdocs gh-deploy
```