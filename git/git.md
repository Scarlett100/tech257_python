#  Git


* Centralised version control system
* repo on server
* working copy of file - local machine
* distributed VCS (like git)
* repository on server - usually online

## centralised vs distributed VCS :

## Centralised Version Control System
* Centralised VCS (CVCS): Single central repository, developers commit directly to the central server (cloud).
* Centralised VCS (CVCS): Relies on constant network access for collaboration and version control with the central server (cloud).
* Centralised VCS (CVCS): Branching and merging often more centralised and heavyweight, managed on the central server (cloud).

## Distributed VCS

* Distributed VCS (DVCS): Each developer has a local copy with full history (local), commits locally, and synchronizes with remote repositories (cloud).
* Distributed VCS (DVCS): Allows offline work with local repository copies (local), synchronization with remote repositories (cloud) when the network is available.
* Distributed VCS (DVCS): branching and merging,  developers can work independently and efficiently with local repositories (local)

## 3 stages of git.
stage → check →  commit

* Untracked: the file exists, but is not part of git's version control
* Staged: the file has been added to git's version control but changes have not been committed
* Committed: change committed to git

normal folder → git init (to initialise turning folder into repository) →untracked/unstaged,  gitadd. = (change of file) tracked/staged ||| git commit - m “label” = committed.
```
git add -> git status -> git commit -m <message>
```
Normal folder → git init (to initialise turning folder into repository) → untracked/unstaged,  gitadd. = (change of file) tracked/staged ||| git commit - m “label” = committed.

## Making a repo locally
```
git init
```


## Staging
Stage all files (only if you are at the root of your project)
Staging is the step that you must take before commiting a change.
Make sure to stage the file, before committing it.
```
git add .
```
or 
```
git add <fileName>
```

##  Check the status
know whats going on!
```
git status
```

##  Commiting your changes
saving the changes that you have staged to the repository.
Snapshot of a file is a commit
```
git commit -m "[COMMIT_MESSAGE]"
```

## .gitignore

If you don't want files tracked put them in the  .gitignore folder

specify a list of things I don't want included


## Pushing 
Pushing: local to server
```
# git push -u [REMOTE] [REMOTE_BRANCH]
git push -u origin main
```

## Pulling
Pull changes: server to local
```
# git pull [REMOTE] [REMOTE_BRANCH]
git pull origin main
```
If entire team is working on same branch and you would like the  updated version you have to pull.

## Git log
will give you a git history amd git id's

## Git diff
see the differences between two commits, can only show you two newest commits
git diff <old-commit-id> <new-commit-id>
eg.
git diff c0e9768c6ed1d1cc7e61e989c39bc3537cfea0a6 5e098b74e3f651f83511b018ab547f0afe637688

## Git checkout - SAFE view previous versions of commits
git checkout <any commit id>
git checkout master/main -> will bring you to most recent commit even if you don't know the id

## DANGEROUS - revert to a previous commit (lose changes made after it) - DANGEROUS
git reset --hard <commit_id>


            _____Feature x------(complete replica of main branch)--------------|
            |                                                a merge happens   |
-main branch|------------------------------------------------------------------|

## GitHub
GitHub is a cloud-based code hosting platform to help developers store, manage, track and control changes to their code. 
It is a platform used for collaboration and version control.

## GitBash
Git Bash is the command prompt used between GitHub and a local copy code.
Git Bash allows you to interact with the Windows environment using Linux commands and comes preloaded with Git for source control

GitHub vs Git 
once cloned remote and local repo are synched.

if all working on same branch and want updated version you have to pull.

## Check your branch
```
#  git branch
```

## How to push
```
git branch -M master
git remote add origin https://github.com/Scarlett100/hellofeb.git
git push -u origin master

don't always need to put branch if on correct branch
```

## To switch to https from ssh
```
 git remote -v
 git remote set-url origin 
 git remote set-url --push origin
```

## How to remove files
git rm  --cached .idea
git rm  --cached -r .idea

Remove from public
delete .git folder to remove all commit history
remove hidden folder, commit history deleted if you need to do this delete .git

Never put credentials in a git repo....ever!!!

## Good to know
any file that starts with a dot eg .gitignore linux considers a hidden file.









