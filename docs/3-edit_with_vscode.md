## Install

1. [Download Vscode](https://code.visualstudio.com/download)
2. Install the extensions below (optional):

    - Python
        - Extension ID: ms-python.python
        - <img src="./img/python-extension.png" alt="img" width=500>
    - Python Environment Manager
        - Extension ID: donjayamanne.python-environment-manager
        - <img src="./img/python-env-manager-extension.png" alt="img" width=500>
    - Jupyter
        - Extension ID: ms-toolsai.jupyter
        - <img src="./img/jupyter-extension.png" alt="img" width=500>
     - Prettify JSON
        - Extension ID: mohsen1.prettify-json
        - <img src="./img/prettify-json-extension.png" alt="img" width=500>
    - JSON Viewer
        - Extension ID: ccimage.jsonviewer
        - <img src="./img/json-viewer-extension.png" alt="img" width=500>
    - Markdown Preview Enhanced
        - Extension ID: shd101wyy.markdown-preview-enhanced
        - <img src="./img/markdown-extension.png" alt="img" width=500>
    - Rainbow CSV
        - Extension ID: mechatroner.rainbow-csv
        - <img src="./img/rainbow-csv-extension.png" alt="img" width=500>
    - vscode-pdf
        - Extension ID: tomoki1207.pdf
        - <img src="./img/pdf-extension.png" alt="img" width=500>
    - Remote-SSH
        - Extension ID: ms-vscode-remote.remote-ssh
        - <img src="./img/remote-ssh-pkg.png" alt="img" width=500>
    - WSL (only if using Windows WSL)
        - Extension ID: ms-vscode-remote.remote-wsl
        - <img src="./img/vscode_wsl.png" alt="img" width=500>

**NOTE:** If you are using a remote WSL or SSH server, you will also need to install these packages there.


## Use VSCode with WSL

1. Once you install the WSL extension, navigate to the Remote Explorer tab and connect to your WSL distribution
    - <img src="./img/wsl-targets.png" alt="img" width=350>
2. Navigate to open a folder as you normally would
    - <img src="./img/open_wsl_folder.png" alt="img" width=500>
3. Install VSCode extensions that are installed locally by navigating to the marketplace and clicking the `Install in WSL:Ubuntu` button
    - <img src="./img/install_vscode_ext_in_wsl.png" alt="img" width=400>

## Configure Remote-SSH Editing

When project files are hosted on a Linux Machine, you can easily edit/ debug them as you would local files by taking advantage of VS Code's Remote-SSH extension.

To use SSH to connect to a remote Linux machine:

1. Open the Command Palette 
    - Mac: `shift + cmd + P`
    - Windows: `shift + ctrl + P`
2. Search for/ Select Remote-SSH: Add New SSH Host..
    - <img src="./img/add-ssh-host.png" alt="img" width=500>
3. Enter the ssh connection command 
    - `ssh {username}@{ip}`
    - <img src="./img/ssh-connect-command.png" alt="img" width=500>
4. Select the ssh file to update 
    - <img src="./img/update-ssh-file.png" alt="img" width=500>
5. You will see a pop-up in the bottom right corner that the host has been added
    - <img src="./img/host-added.png" alt="img" width=500>
6. In the Remote Explorer tab, you will now see your new SSH Target. Click the plus folder icon to "Connect to Host in New Window"
    - <img src="./img/remote-edit-tab.png" alt="img" width=500>
7. A new window will open and you will be prompted to enter your password
    - <img src="./img/enter-ssh-pw.png" alt="img" width=500>
8. Choose the folder in the remote machine you want to open and select "OK"    
    - <img src="./img/open-ssh-folder.png" alt="img" width=500>
9. You will be prompted for your password one more time
    - <img src="./img/enter-ssh-pw2.png" alt="img" width=500>
10. Upon successful connection, you will see the remote machine's ip as well as the git branch you are currently on (if opened to a git repo) in the bottom left corner
    - <img src="./img/ssh connected.png" alt="img" width=500>

You can now easily edit and debug your code as you would locally. 

### Note on High Security Remote Machines
If you are connecting to the remote machine with a normal user (i.e. non-root user) you will may get access errors when trying to run a ipynb file depending on the user's permissions.

<img src="./img/notebook-access-error.png" alt="img" width=500>

This happens because, in a Unix/Linux system, you can’t bind to external facing ports without super user/root access. 

If you do not have an environment controlled with Puppet, you can try editing the user's permissions to not need password authentication when entering root user mode. However, it is easiest to just test small code snippets in a noteboook file locally.

For more information, see [https://code.visualstudio.com/docs/remote/ssh](https://code.visualstudio.com/docs/remote/ssh)

