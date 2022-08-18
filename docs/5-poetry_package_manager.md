
## Install

- Install `poetry` with the following command:
    ```curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -```
- Restart your terminal
- Enter `poetry` and you should see a list of commands returned

## Use Poetry To Install Project Dependencies

**NOTE:** For demo purposes, let's pretend this project is dependent on Python version 3.9.6 and pandas

1. Create a `pyproject.toml` file using the following template (See this repo's [pyproject.toml](https://github.com/jillvillany/python-dev-setup/blob/main/pyproject.toml)):
    - NOTE: We are assuming this repo represents a project dependent on Python version 3.9.6 and a pandas version greater than or equal to 1.4.1

        ```
        [tool.poetry]
        name = "{repo/project name}"
        version = "1.0.0"
        description = "{free text description}"
        readme = "README.md"
        repository = "{git repo link}"
        documentation = "{site url if applicable}"
        authors = [
            "{full name} <{email}>"
        ]

        [tool.poetry.dependencies]
        python = "=={Python version}"

        [tool.poetry.dev-dependencies]

        [build-system]
        requires = ["poetry-core>=1.0.0"]
        build-backend = "poetry.core.masonry.api"
        ```
        
2. Create a conda environment that uses the Python version specified in the `pyproject.toml` file and active the environment

    - `conda create -n python-dev-setup python=3.9.6`
    - <img src="../img/conda_env_created.png" alt="img" width=500>


3. Run command `poetry install`

    - <img src="../img/conda_deps_installed.png" alt="img" width=500>
    - NOTE: You will see a `poetry.lock` file created. This is important to be committed to your repo so that other team members can install the dependencies from the lock file by running `poetry install`


## Useful Poetry Commands

- Install the requirements in the poetry.lock file
    ```
    poetry install
    ```
- Add a package to the pyproject.toml file and update lock file
    ```
    poetry add {package name}
    ```
    - **NOTE1:** This will install the latest package version. The pyproject.toml will show a version greater than or equal to the version is required and the poetry.lock file will update to specify the specific version installed.
     - **NOTE2:** If you need to install a version other than the latest version, you can specify `poetry add {package name}=={version}`
- Remove a package from the pyproject.toml file and update lock file
    ```
    poetry remove {package name}
    ```
