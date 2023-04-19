## Install
### Mac

1. Install `wget`
    ```bash
    brew install wget
    ```
2. Install Mambaforge (Type "yes" wherever asked)
    ```bash
    wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
    bash Mambaforge-$(uname)-$(uname -m).sh
    ```

### Windows WSL/ Linux

1. Install `wget` 
    ```bash
    sudo apt install wget
    ```
2. Install Mambaforge (Type "yes" wherever asked)
    ```bash
    wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
    bash Mambaforge-$(uname)-$(uname -m).sh
    source ~/.bashrc
    ```
3. If not done already, add sourcing `.bashrc` to your `.bash_profile`
    ```
    source ~/.bashrc
    ```
## Useful Mambaforge Commands

- Create new conda python virtual environment
    * Note: If it asks you to select y/n, enter "y"
        ```bash
        conda create -n {name} python={version}
        ```
- Activate conda environment
    ```bash
    conda activate {name}
    ```
- Deactivate conda environment
    ```bash
    source deactivate
    ```
