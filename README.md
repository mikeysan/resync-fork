# Resync repository

This project seeks to be an easy way to update an outdated forked project.

### Requirements:
- It takes two arguments:
    - 1. The remote user account,
    - 2. and the repository.
- USAGE: `python refresh.py [remote_user] [repository]`

TODO: I might change the arguments to user inputs that are requested when the script is run (hmm...).

TODO: Make the input an option for if no argument is provided or if missing.


### Known issues:
If you have your default set to 'main' and the repository you forked from is 'master', you may encounter some issues that seem confusing at first.

This is what that issue looks like
```py
fatal: The upstream branch of your current branch does not match
the name of your current branch.  To push to the upstream branch
on the remote, use

    git push origin HEAD:master

To push to the branch of the same name on the remote, use

    git push origin HEAD

To choose either option permanently, see push.default in 'git help config'.
```
To resolve it type: ```git push origin HEAD:master```

This issue highlights possible updates to the script
- A way to determine the head branch 'main' or 'master'.
- I am also assuming that the remote/upstream repository will be using 'upstream/master' and not 'main'. We should have a chack for that as well.
- Use one or the other when you change branches at the beginning

