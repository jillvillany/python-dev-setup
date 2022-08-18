# This script takes one input:
    # branch name
# To archive a branch in this repo run: ./archive_branch.sh branch_name

# capture the standard output of a command so it can be retrieved with ret
cap () { tee /tmp/capture.out; }

# return the output of the most recent command that was captured by cap
ret () { cat /tmp/capture.out; }

# checkout master to make sure not on the branch archiving
git checkout main
git pull
# redirect error message to stdout so can be captured
git tag archive/$1 $1 2>/tmp/capture.out | cap
echo $(ret)

if [[ $(ret) == *"Failed to resolve"* ]]; then
    # try checking out the branch first
    git checkout $1 2>/tmp/capture.out | cap
    echo $(ret)
        if [[ $(ret) == *"did not match any file"* ]];
        then
        echo "ERROR REASON: $1 branch doesn't exist"
        exit 0 
        fi
    git checkout master
    git tag archive/$1 $1 2>/tmp/capture.out | cap
    echo $(ret)
    if [[ $(ret) == *"already exists"* ]]; then
        echo Tag already exists, specify new name:
        read newTag
        git tag archive/$newTag $1 2>/tmp/capture.out | cap
        echo $(ret)
        if [[ $(ret) == *"already exists"* ]]; then
            echo ERROR REASON: New tag name already exists
            exit 0
        fi
    fi
elif [[ $(ret) == *"already exists"* ]]; then
    echo Tag already exists, specify new name:
    read newTag
    git tag archive/$newTag $1 2>/tmp/capture.out | cap
    echo $(ret)
    if [[ $(ret) == *"already exists"* ]]; then
        echo ERROR REASON: New tag name already exists
        exit 0
    fi
else 
    echo tag archive/$1 created successfully
fi

git push origin --tags
git branch -d $1
git push -d origin $1