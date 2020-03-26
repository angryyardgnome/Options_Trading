# wake up, check for changes to your branch

git fetch --all

# look at all branches

git branch -a

# realize you need to make a new branch to make a feature change

git checkout -b <<new_branch>>

# make some changes, and stage them

git add .

# leave a message with those changes

git commit -m '<<message>>'

# set up your local branch to track the remote branch, and push

git push -u origin <<new_branch>>

# after you make other changes, you can leave out the -u and origin

git add.
git commit -m '<<another message>>'
git push



