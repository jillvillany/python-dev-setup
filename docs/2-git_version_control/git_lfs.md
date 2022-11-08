## Git LFS

Git LFS is used to for large file storage.

- Download and install: [Git Large File Storage ](https://git-lfs.github.com/)

### Install Git LFS on Linux
1. Navigate to [https://github.com/git-lfs/git-lfs/releases](https://github.com/git-lfs/git-lfs/releases)
2. Download the package .rpm file for your Linux Distribution
3. Switch to root user `sudo su`
4. Install the package
    ```
    rpm -iv {absolute path to .rpm file}
    ```
5. Install git lfs
    ```
    git lfs install
    ```

### Fetch all git lfs files
**NOTE:** Use this command if you installed Git LFS after cloning the repo
```
git lfs fetch --all
```

### Track a file with git lfs
This will add the file paths to the .gitattributes file <br>
**NOTE:** The .gitattibutes file must be committed before it takes effect

```
git lfs track {path to file}
```

### See files currently tracked
```
git lfs ls-files
```

### See lfs files committed or staged for commit
```
git lfs status
```