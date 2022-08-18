# return the output of the most recent command that was captured by cap
ret () { cat /tmp/capture.out; }

# checkout source branch -> named master or main based on bitbucket/ github use
# Use &> to capture both stdout and stderr
git checkout master &> /tmp/capture.out
switch_master_out=$(ret)
if [[ $switch_master_out == *"error: pathspec 'master' did not match any file(s) known to git"* ]]; then
    source_branch="main"
else
    source_branch="master"
fi
echo "Using $source_branch for source branch name"
echo

# error: pathspec 'master' did not match any file(s) known to git
git pull

# After fetching, remove any remote-tracking branches which no longer exist on the remote
echo
echo "Removing any remote-tracking branches which no longer exist on the remote..."
git fetch --prune

#### checkout and pull all the remote branches  ####
echo
echo "CHECKING LOCAL AND REMOTE BRANCHES SYNCED..."

git branch -r &> /tmp/capture.out
# echo "$(ret)"

remote_branches_string=$(ret)
IFS=$'\n' read -rd '' -a remote_branches_array <<<"$remote_branches_string"

# potential source branch names: head, main, master
source_branch_regex="(\s*(head|main|master)\s*|.*(origin/head|origin/main|origin/master).*)"

echo
for branch in "${remote_branches_array[@]}"
do
    # NOTE: important to put the longer string on the left
    if ! [[ $branch =~ $source_branch_regex ]]; then
        # replace origin with empty str 
        branch_name=$(echo $branch | sed 's/origin\///')
        # split on space and take first element - for origin/head -> origin/master
        branch_name_array=($branch_name)
        branch_name=$(echo ${branch_name_array[0]})
        echo "BRANCH NAME: $branch_name"
        git checkout $branch_name
        git pull
    fi
done

#### Clean up local branches that no longer have an upstream ref ####
echo
echo "CHECKING IF LOCAL BRANCHES NEED CLEAN-UP..."
git checkout $source_branch
git branch &> /tmp/capture.out
# echo "$(ret)"

local_branches_string=$(ret)
IFS=$'\n' read -rd '' -a local_branches_array <<<"$local_branches_string"

echo
for branch in "${local_branches_array[@]}"
do
    if ! [[ $branch =~ $source_branch_regex ]]; then
        echo "BRANCH NAME: $branch"
        git checkout $branch &> /tmp/capture.out
        branch_checkout_msg=$(ret)
        echo $branch_checkout_msg
        if [[ $branch_checkout_msg == *"the upstream is gone"* ]]; then
            git checkout $source_branch
            git branch -D $branch
            echo "Deleted $branch"
        fi
        git pull &> /tmp/capture.out
        branch_pull_msg=$(ret)
        echo $branch_pull_msg
        if [[ $branch_pull_msg == *"no such ref was fetched"* ]]; then
            git checkout $source_branch
            git branch -D $branch
            echo "Deleted $branch"
        elif [[ $branch_pull_msg == *"There is no tracking information for the current branch"* ]]; then
            git checkout $source_branch
            git branch -D $branch
            echo "Deleted $branch"
        fi
    fi
done
