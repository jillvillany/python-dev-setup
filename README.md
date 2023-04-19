## View the documentation at: https://jillvillany.github.io/python-dev-setup/

### To create the documentation site

```
conda create -n python-dev-setup python=3.9
conda activate python-dev-setup
poetry install
python sync_or_create_all_mds.py
mkdocs gh-deploy
```

### To view a working version of the documentation site

```
mkdocs serve
```