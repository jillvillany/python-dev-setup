# python-dev-setup

## Table of Contents

1. [Version Control Your Code - Git](#1-version-control-your-code---git)
    - Install Git
        - [Mac](#Mac-Git-Install) 
        - [Red Hat Linux](#Red-Hat-Linux-Git-Install)
        - [Windows](#Windows-Git-Install)
    - [Configure SSH Auth](#Configure-SSH-Auth)
        - [Mac/Linux](#Mac/Linux-Configure-SSH-Auth)
        - [Windows](#Windows-Configure-SSH-Auth)
    - [Useful Git Commands](#Useful-Git-Commands) 
2. [Run Scripts from Command Line - Mac Terminal/ Git Bash](#2-run-scripts-from-command-line---mac-terminal-git-bash)
    - [Git Bash Differences](#Git-Bash-Differences)
    - [Format Your Terminal](#Format-Your-Terminal)
3. [Edit and Debug Your Code - VS Code](#3-edit-and-debug-your-code---vscode)
    - [Install VS Code and Key Extensions](#Install-VS-Code-and-Key-Extensions)
4. [Manage Your Python Version - Pyenv](#4-manage-your-python-version---pyenv)
    - Install Pyenv
        - [Mac](#Mac-Pyenv-Install)
        - [Linux](#Linux-Pyenv-Install)
        - [Windows](#Windows-Pyenv-Install)
    - [Useful Pyenv Commands](#Useful-Pyenv-Commands)
5. [Manage Your Python Package Versions - Poetry](#5-manage-your-python-package-versions---poetry)
    - [Install Poetry](#Install-Poetry)
    - [Use Poetry to Create a Venv](#Use-Poetry-to-Create-a-Venv)
    - [Useful Poetry Commands](#Useful-Poetry-Commands)

<hr>

## 1. Version Control Your Code - Git

### Mac Git Install
[Back to Table of Contents](#Table-of-Contents)

1. 	Install Apple Xcode developer tools
    - ``` code-select --install```
2. Download Homebrew: https://brew.sh/
    - Homebrew helps you easily manage installs on a Mac from command-line
3. Install git using homebrew <br>
    - ```brew install git```

### Red Hat Linux Git Install
[Back to Table of Contents](#Table-of-Contents)

1. Switch to the super user (a.k.a root user)
    - ```sudo su```
2. Enter your password
3. Install git
    - ```yum install git```
4. Switch back to a normal user
    - ```exit```

### Windows Git Install
[Back to Table of Contents](#Table-of-Contents)

1. Install git https://git-scm.com/download/win
    - This includes Git Bash which provides a terminal similar to the native Mac terminal app
    - See [Git Bash Differences](#Git-Bash-Differences) for details for more information
    

### Configure SSH Auth
[Back to Table of Contents](#Table-of-Contents)

To easily authenticate with Github/ Bitbucket (i.e. not need to enter your username/ password every time you pull/push to the repo) you can set up SSH authentication


#### Mac/Linux Configure SSH Auth
[Back to Table of Contents](#Table-of-Contents)

1. Create an SSH key pair
    - ```ssh-keygen```
    - **NOTE:** In order to make the setup flexible to multiple different user accounts on the same machine (helpful when working on a team's Linux server in a shared account) add your git profile to the end of the id_rsa file name
        - For example: `Users/jillvillany/.ssh/id_rsa_jillvillany`
    - <img src="img/ssh-keygen.png" width=500>
2. Navigate to where the ssh key pair was created 
    - Mac: use shortcut `shift + cmd + .` to view hidden directories/files
    - Linux WinSCP: Options > Preferences > Panels > Show hidden files
3. Create the config file (in finder or in terminal using below commands)
    ```
    cd ~/.ssh
    touch config
    open config
    ```
    - If using Github, add the below to your config file:
        ```
        Host github-{git username}
         HostName github.com
         IdentityFile ~/.ssh/id_rsa_{git username}
         IdentitiesOnly yes
        ```
    - If Bitbucket:
        ```
        Host bitbucket.org-{git username}
         HostName bitbucket.org
         User git
         IdentityFile ~/.ssh/id_rsa_{git username}
         IdentitiesOnly yes
        ```
    - **NOTE:** If you have other users to add, create similar entries below in the file
4. Open the `id_rsa_{git username}.pub` file with a text editor and copy the contents
5. Add SSH key in Github or Bitbucket  
    - In Github:
        - Navigate to Settings > SSH and GPG keys
        - <img src="img/git-settings.png" width=500>
        - Click New SSH key and add the contents of your `id_rsa_{git username}.pub` file in the key field
    - In Bitbucket:
        - Navigate to personal settings
        - <img src="img/bitbucket-settings.png" width=300>
        - Select SSH Key > Add Key add the contents of your `id_rsa_{git username}.pub` file in the key field
6. Add the SSH key to the SSH agent
    ```
    ssh-add ~/.ssh/id_rsa_{git username}
    ```
7. Test your SSH connection
    - Github: ```ssh -T git@github-{your username}```
    - Bitbucket: ```ssh -T git@bitbucket.org-{your username}```


#### Windows Configure SSH Auth
[Back to Table of Contents](#Table-of-Contents)

1. Create an SSH key pair
    - ```ssh-keygen -t ed25519 -C "your_email@example.com```
    - **NOTE:** If you will need to connect to different accounts (i.e. Github for personal use and Bitbucket for work), you can add a differentiator at the end of the id_ed25519 file. For example, below I added "_ibm" for the key I use with my IBM Bitbucket account.
    - <img src="img/ibm key.png" width=700>
2. Navigate to where the ssh key pair was created 
4. Open the `id_ed25519` PUB file with a text editor and copy the contents
5. Add SSH key to Github or Bitbucket  
    - In Github:
        - Navigate to Settings > SSH and GPG keys
        - <img src="img/git-settings.png" width=500>
        - Click New SSH key and add the contents of your `id_ed25519.pub` file in the key field
    - In Bitbucket:
        - Navigate to personal settings
        - <img src="img/bitbucket-settings.png" width=300>
        - Select SSH Key > Add Key add the contents of your `id_ed25519.pub` file in the key field
6. Add the SSH key to the SSH agent:
    - Start up the SSH agent in the background
        ```
        eval $(ssh-agent -s)
        ```
    - Add the identity
        ```
        ssh-add ~/.ssh/id_ed25519
        ```
7. Test your SSH connection to github
    - Github: `ssh -T git@github.com`
    - Bitbucket: `ssh -T git@bitbucket.org`


### Useful Git Commands
[Back to Table of Contents](#Table-of-Contents)

- Clone repo with SSH auth
    - On a new repo:
        - Select SSH when you clone the code and copy the URL
            - <img src="img/ssh-clone.png" width=500>
        - Enter the command ```git clone {SSH URL}```
            - For example: `git clone git@github.com:jillvillany/python-dev-setup.git`
            - <img src="img/ssh-clone-success.png" width=500>
    - On an existing git repo (i.e. if had cloned this repo using username and password auth)
        - Set the remote URL to the URL used with ssh
        - ```git remote set-url origin {SSH URL}```
        - Now try ```git push```
        - Answer yes to the prompt and you will see git connects/ shows everything up to date without prompting for username/ password
            - <img src="img/ssh-success.png" width=500>

- Add new/ modified files, commit and push changes
    ```
    git pull 
    git add {relative file path}
    git commit -m "commit message"
    git push
    ```
    - **IMPORTANT:** If multiple users are working in the directory, be sure to set the git config user.email before pushing so that commits belong to the user that made the change
    ```
    git config user.email {your email}
    ```
- Undo all local changes to the checked out branch
    ```
    git stash
    ```
- Undo local changes to a particular file
    ```
    git checkout --{file name}
    ```
- Create a New Branch
    ```
    git checkout -b {branch name} {branch making new branch from}
    git push -u origin {branch name}
    ```
- Abort a merge
    ```
    git merge --abort
    ```
- Revert to a previous commit
    ```
    git revert {commit hash}
    ```
    - **NOTE:** See [this stack overflow post](https://stackoverflow.com/questions/4114095/how-do-i-revert-a-git-repository-to-a-previous-commit) for more details
- Archive & Delete a Branch
    ```
    git tag archive/{branchname} {branchname}
    git push origin --tags
    git branch -d {branchname}
    git push -d origin {branch_name}
    ```
    - **NOTE:** If need to delete a created tag
    ```
    git tag -d
    ```
    - **NOTE:** The process of archiving numerous branches can get tedious. See the [archive_branch.sh](https://github.com/jillvillany/python-dev-setup/blob/main/archive_branch.sh) script in this repo for an automated way to archive branches.
- Restore an archived branch
    ```
    git checkout -b {branch name} archive/{archived branch name}
    ```
-  Maintain a Forked Repo
    - Sync your forked version of the repo with the most updated version of the main repo
        - ```git checkout master```
        - If not already done: ```git remote add upstream https://github.ibm.com/ML-Pipelines/ml-pipelines.git``` 
        - ```git fetch upstream```
        - ```git rebase upstream/master```
        - ```git push -u origin```

For other useful commands delivered in an entertaining way see: https://ohshitgit.com/


## 2. Run Scripts from Command Line - Mac Terminal/ Git Bash
[Back to Table of Contents](#Table-of-Contents)

Mac's Terminal app is ideal for running scripts from command line because it is Linux based and most apps are deployed to Linux machines in Production due to their cost effectiveness.

On a Windows, you can get very close to Mac terminal functionality by using the Git Bash terminal that comes with [Git for Windows](#https://gitforwindows.org/).


### Git Bash Differences
[Back to Table of Contents](#Table-of-Contents)

Although the Git Bash terminal is similar to the Mac Terminal, some key differences include:
    
    - `notepad` instead of `open` for opening a file
    - `shift + ins` to copy/ paste into/ from the terminal
    - `python -i` instead of just `python` to use an interactive python shell in the terminal

### Format Your Terminal
[Back to Table of Contents](#Table-of-Contents)

No matter the command line interface (CLI) used, it helps to format your CLI to work well with Git so that you know what branch you are working on and don't accidentally commit code to the wrong branch.

**NOTE:** Code below found in [this Medium article](#https://medium.com/@charlesdobson/how-to-customize-your-macos-terminal-7cce5823006e)

1. Open your terminal of choice (i.e. Mac users default terminal/ Windows users Git Bash)
2. Cd to your home directory
    ```cd ~```
3. Create .bash_profile file if it doesn't already exist (this was part of the Mac set up but not Windows)
    ```touch .bash_profile```
4. Open .bash_profile
    - Mac: ```open .bash_profile```
    - Windows: ```notepad .bash_profile```
5. Add this line to the bottom of the file
    ```source ~/.bash_prompt```
6. Create .bash_prompt file
    ```touch .bash_prompt```
7. Open .bash_prompt file
    - Mac: ```open .bash_prompt``` 
    - Windows: ```notepad .bash_prompt``` 
8. Add these lines to your file
    ```
    #!/usr/bin/env bash
    
    # GIT FUNCTIONS
    git_branch() {
    git branch 2>/dev/null | sed -e '/^[^*]/d' -e 's/* \\(.*$ \\(.*\\)/  (\\1)/'
    }

    # TERMINAL PROMPT
    PS1="\[\e[0;93m\]\u\[\e[m\]"    # username
    PS1+=" "    # space
    PS1+="\[\e[0;95m\]\W\[\e[m\]"    # current directory
    PS1+=" "      # space
    PS1+="\[\e[0;92m\]\$(git_branch)\[\e[m\]"  # current branch
    PS1+=" "      # space
    PS1+=">> "    # end prompt
    export PS1;

    export CLICOLOR=1
    export LSCOLORS=ExFxBxDxCxegedabagacad
    ```
9. Relaunch you terminal and navigate to a git repo (i.e. this python-dev-setup repo). You will now see your terminal prompt formatted with your username, current folder and repo branch 
![](img/terminal_formatting.png)


## 3. Edit and Debug Your Code - Vscode
[Back to Table of Contents](#Table-of-Contents)

### Install VS Code and Key Extensions

1. Download Vscode: https://code.visualstudio.com/download
2. Install the extensions below:

    - Python
        - Extension ID: ms-python.python
        - <img src="img/python extension.png">
    - Jupyter
        - Extension ID: ms-toolsai.jupyter
        - <img src="img/jupyter extension.png">
     - Prettify JSON
        - Extension ID: mohsen1.prettify-json
        - <img src="img/prettify json extension.png">
    - JSON Viewer
        - Extension ID: ccimage.jsonviewer
        - <img src="img/json viewer extension.png">
    - Markdown Preview Enhanced
        - Extension ID: shd101wyy.markdown-preview-enhanced
        - <img src="img/markdown extension.png">
    - Rainbow CSV
        - Extension ID: mechatroner.rainbow-csv
        - <img src="img/rainbow csv extension.png">
    - vscode-pdf
        - Extension ID: tomoki1207.pdf
        - <img src="img/pdf extension.png">


## 4. Manage Your Python Version - Pyenv

### Mac Pyenv Install
[Back to Table of Contents](#Table-of-Contents)

See [this article](#https://chamikakasun.medium.com/how-to-manage-multiple-python-versions-in-macos-2021-guide-f86ef81095a6) for reference.

- Install pyenv:
    ```
    brew install openssl readline sqlite3 xz zlib
    curl https://pyenv.run | bash
    ```
- Install pyenv-virtualenv plugin
    ```
    git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
    ```
- Open .bash_profile (create it if needed) 
    ```
    touch ~/.bash_profile # create if needed
    open ~/.bash_profile
    ```
- Add pyenv to bash profile
    ```
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    ```
- Add pyenv virtualenv-init to the .bash_profile file so that the local Python version of a directory will activate automatically when you cd to that directory
- Add pyenv and pyenv virtualenv path to bash profile
    ```
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    if command -v pyenv 1>/dev/null 2>&1; then
        eval "$(pyenv init --path)"
        eval "$(pyenv virtualenv-init -)"
    fi
    ```
- Restart terminal
- Type `pyenv` and you should see a list of commands returned
- Test can install a python version with pyenv
    `pyenv install 3.8.3`
    - **NOTE1:** If you get an error, try running this patch command (make sure the version after patch matches the version you are installing)
    ```
    CFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix bzip2)/include -I$(brew --prefix readline)/include -I$(xcrun --show-sdk-path)/usr/include" LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix readline)/lib -L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" pyenv install --patch 3.8.3 < <(curl -sSL https://github.com/python/cpython/commit/8ea6353.patch\?full_index\=1)
    ```
    - **NOTE2:** If your error looks like the error below, try this fix instead:
        - Error:
            ```
            /Library/Developer/CommandLineTools/SDKs/MacOSX12.1.sdk/usr/include/mach-o/dyld.h:98:54: note: passing argument to parameter 'bufsize' here
            extern int _NSGetExecutablePath(char* buf, uint32_t* bufsize)                 __OSX_AVAILABLE_STARTING(__MAC_10_2, __IPHONE_2_0);
                                                                ^
            ./Modules/posixmodule.c:9221:15: error: implicit declaration of function 'sendfile' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
                    ret = sendfile(in, out, offset, &sbytes, &sf, flags);
            ```
        - Fix:
            - Add explicit dev tools path to ~/.bash_profile
            ```
            ####### adding paths needed for working with different python versions using pyenv #########
            #pyenv
            export PATH="/Users/jillvillany/.pyenv/bin:$PATH"
            eval "$(pyenv init --path)"
            eval "$(pyenv virtualenv-init -)"

            #openssl
            export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"
            export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"

            #readline
            export LDFLAGS="-L/usr/local/opt/readline/lib"
            export CPPFLAGS="-I/usr/local/opt/readline/include"

            #sqlite
            export LDFLAGS="-L/usr/local/opt/sqlite/lib"
            export CPPFLAGS="-I/usr/local/opt/sqlite/include"

            #zlib
            export LDFLAGS="-L/usr/local/opt/zlib/lib"
            export CPPFLAGS="-I/usr/local/opt/zlib/include"
            ```
            - Run the following command - See [this article](#https://github.com/pyenv/pyenv/issues/1643#issuecomment-655710632) for reference
            ```
            CFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix bzip2)/include -I$(brew --prefix readline)/include -I$(xcrun --show-sdk-path)/usr/include" LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix readline)/lib -L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" \
            pyenv install --patch 3.8.3 < <(curl -sSL https://github.com/python/cpython/commit/8ea6353.patch\?full_index\=1)
            ```
- Check it's in your Python versions
    `pyenv versions`
- Use pyenv to set your local python version
    `pyenv local 3.8.3`
- Check that your python version is now set to 3.8.3
    `python -V`


### Windows Pyenv Install
[Back to Table of Contents](#Table-of-Contents)

- You can follow the first half of the instructions in [this article](#http://evaholmes.com/how-to-set-up-pyenv-and-poetry-on-windows-10-for-python-project-management/)
- Basic steps include:
    - Open Git Bash
    - cd to home `cd ~`
    - Enter the following command
        - ```git clone https://github.com/pyenv-win/pyenv-win.git $HOME/.pyenv```
    - Edit your system path variables
        - Search "edit the system environment variables" in windows home menu
            - <img src="img/edit-env-vars.PNG" width=300>
        - Select environment variables
            - <img src="img/env-var-select.PNG" width=300>
        - Select Path under System Variables and click Edit
            - <img src="img/path-edit.PNG" width=300>
        - Click New and add the following two paths:
            - c:\users\{your username}\.pyenv\pyenv-win\bin
                - For example: c:\users\jillv\.pyenv\pyenv-win\bin
            - c:\users\{your username}\.pyenv\pyenv-win\shims
                - For example: c:\users\jillv\.pyenv\pyenv-win\shims
        - The environment variables should now look like below:
            - <img src="img/path-added.png" width=500>
        - Click OK to close the windows

    - Relaunch git bash and type ```pyenv``` you should see a list of commands retrun
    - Test can install a python version with pyenv
        `pyenv install 3.8.3`
    - Check it's in your Python versions
        `pyenv versions`
    - Use pyenv to set your local python version
        `pyenv local 3.8.3`
    - Check that your python version is now set to 3.8.3
        `python -V`

- **NOTE:** You cannot use the pyenv virtualenv plugin with the windows version of pyenv. To make a virtual environment off of a pyenv python version see [Useful Pyenv Commands](#Useful-Pyenv-Commands)


### Linux Pyenv Install
[Back to Table of Contents](#Table-of-Contents)

- Install pyenv prereqs from root
    ```
    cd ~
    Sudo su – 
    ```
- Install prerequisites based on your Linux distribution
    - On Debian/Ubuntu/Linux Mint 
        ```
        sudo apt install curl git-core gcc make zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libssl-dev
        ```
    - On CentOS/RHEL 
        ```
        yum -y install epel-release
        yum install git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel libffi-devel
        ```
	- On Fedora 22+ 
        ```
        yum install git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel libffi-devel
        ```
- Install pyenv from git
    ```git clone https://github.com/pyenv/pyenv.git ~/.pyenv```
- Install pyenv virtualenv plugin
    ```git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv```
- Add pyenc and pyenv-virtuaslenv to the .bash_profile
    ```
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    if command -v pyenv 1>/dev/null 2>&1; then
        eval "$(pyenv init --path)"
        eval "$(pyenv virtualenv-init -)"
    fi
    ```
- Repeat the .bash_profile steps with .bashrc
- Restart terminal
- Test that you can install a python version with pyenv 
    - ```pyenv install 3.8.3 ```
- Check the installed Python version is in your pyenv versions 
    - ```pyenv versions```
- Use pyenv to set your local Python version 
    - ```pyenv local 3.8.3```
- Check that your Python version is now set to 3.8.3 
    - ```python -V```


### Useful Pyenv Commands
[Back to Table of Contents](#Table-of-Contents)

- pyenv install 
    - Install the version of Python needed. For example:
    ```
    pyenv install 3.9.6
    ```
    - NOTE: One Mac, if you get an error, try running this patch command (make sure the version after patch matches the version you are installing)
    ```
    CFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix bzip2)/include -I$(brew --prefix readline)/include -I$(xcrun --show-sdk-path)/usr/include" LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix readline)/lib -L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" pyenv install --patch 3.9.6 < <(curl -sSL https://github.com/python/cpython/commit/8ea6353.patch\?full_index\=1)
    ```
- `pyenv versions`
    - See Python versions and virtual environments aviable to be set as your Python version
- `pyenv local`
    - Set Python version in cwd
- `pyenv global`
    - Set Python version to use system-wide (overwritten by local pyenv is specified)
- Create a virtual env with pyenv (Mac & Linux only)
    - `pyenv virtualenv {python version} {venv name}`
    - Set venv as the local python for the project
        - `pyenv local {venv name}`
    - Now when you cd into the project's directory, the venv set as the local python version will automatically be activated
- Create a virtual env with pyenv (Windows)
    - You cannot use the pyenv-virtualenv plugin with the windows version of pyenv. To make a virtual environment from a pyenv Python version:
        ```
        pyenv local {Python version to use with the venv}
        python -m venv venv
        pip install --upgrade pip
        pip install -r requirements.txt
        ```
    - To activate the venv 
        - ```source venv/Scripts/activate```

## 5. Manage Your Python Package Versions - Poetry
[Back to Table of Contents](#Table-of-Contents)

### Install Poetry

- Install `poetry` with the following command:
    ```curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -```
- Restart your terminal
- Enter `poetry` and you should see a list of commands returned

### Use Poetry To Create a Venv
[Back to Table of Contents](#Table-of-Contents)

**NOTE:** For demo purposes, let's pretend this project is dependent on Python version 3.9.6 and pandas

1. Create a `poetry.toml` file with the following contents so that the venv is created within your project
    ```
    [virtualenvs]
    in-project = true
    ```
2. Create a `pyproject.toml` file using the following template:
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
3. Set your local Python version to one compatible with the Python version specified
    ```
    pyenv local {Python version}
    ```
4. Add `.venv` and `.python-version` to your `.gitignore`
5. Run command `poetry install`

    - ![](img/poetry_install_output.png)

6. You will see the following created in your repo:

    -  .venv folder 
    - poetry.lock file
    - ![](img/post_poetry_install.png)

7. Add the needed packages (i.e. for this example pandas)

    A. Using `poetry add` (the easiest way)
        ```
        poetry add pandas
        ```
        - ![](img/poetry_add.png)
        - **NOTE1:** This will install the latest package version. The pyproject.toml will show a version greater than or equal to the version is required and the poetry.lock file will update to specify the specific version installed.
        - **NOTE2:** If you need to install a version other than the latest version, you can specify `poetry add {package name}=={version}`
    B. Directly updating the pyproject.toml file
        - Explicitly specify package version
            - `{package name}= "{version}"`
        - Any version greater than that version also compatible with the other dependencies
            -  `{package name}= "^{version}" `

8. You will see the package(s) added to the `pyproject.toml` file and the `poetry.lock` file updated

    - ![](img/poetry_add_file_updates.png)

9. Push the poetry.loc file to you git repo so other team members can install matching requirements using `poetry install`

### Useful Poetry Commands
[Back to Table of Contents](#Table-of-Contents)

- Install the requirements in the poetry.lock file
    ```
    poetry install
    ```
- Add a package to the pyproject.toml file and update lock file
    ```
    poetry add {package name}
    ```
- Remove a package from the pyproject.toml file and update lock file
    ```
    poetry remove {package name}
    ```
