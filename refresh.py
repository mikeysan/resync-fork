import sys
import os

'''
    This script is designed to help keep your forked repositories up to date
    It takes two arguments:
    1. The remote user account,
    2. and the repository.
    USAGE: python refresh.py [remote_user] [repository]
    TODO FOR SELF/CONTRIBUTORS:
    TODO: I might change the arguments to user inputs that are requested when the script is run (hmm...)
    TODO: Make the input an option if no argument is provided or if missing

'''

# Set variables
'''
    TODO: Change values of yourUser to GitHub username
'''
yourUser = "mikeysan"
remoteUser = str(sys.argv[1])
repository = str(sys.argv[2])


# os.path.isdir(path)
'''
    TODO: Change values of chgDir to path of the working directory
'''
working_path = "/home/sspade/Documents"
os.chdir(working_path)
path = os.getcwd()

print('*' * 80)

print(path)

_dir = path + '\\' + repository

print('*' * 80)

print(_dir)

print('=' * 80)


def createGit():
    try:
        os.system('git init')
        os.system('git commit -m "first commit"')
        os.system('git branch -M main')
        print(f'Git for {repository} initialized')
    except (FileNotFoundError, IOError, AttributeError):
        print(f'Unable to initialize {repository}')


# Let's create our local repository
def createFolder():
    """
    1. Create a new project folder
    2. Initialize git on the new folder
    3. Create a README.md file
    4. Change default branch to main
    """
    try:
        os.mkdir(_dir)
        os.chdir(_dir)
        os.system('git init')
        os.system(f'echo "# {repository}" > README.md')
        os.system('git add README.md')
        os.system('git commit -m "first commit"')
        os.system('git branch -M main')

        print(f'{repository} created locally')
        
    except (FileNotFoundError, IOError, AttributeError):
        print("create <project_name> l")


# createFolder()
# os.path

if os.path.isdir(_dir):
    try:

        print(f'Pulling down {repository} from {remoteUser}')
        # Let's change working directory to repository path
        # os.chdir(_dir)
        # print(f'Changed directory to local {repository} folder\n')
        # Clone repository from your account first
        # os.system(f'git clone https://github.com/{yourUser}/{repository}.git')
        # print('Cloned our repository\n')
        # pull down the upstream from original repository
        os.system(f'git remote add upstream https://github.com/{remoteUser}/{repository}.git')
        print('Add remote connection to original as upstream\n')
        os.system('git fetch upstream')
        print('Pulled down upstream\n')
        os.system('git checkout main')
        print('Make sure we are on our main branch before merging\n')
        os.system('git merge upstream/master')
        print('Merged upstream/master\n')
        os.system('git push origin main')
        print('All changes pushed to our repository\n')
    except (FileNotFoundError, IOError, AttributeError):
        print(f"{_dir} Missing!")
else:
    try:
        # Couldn't find local copy of repository so we must clone it
        print(f'We could not find {repository} folder so we are cloning it')
        # Clone repository
        os.system(f'git clone https://github.com/{yourUser}/{repository}.git')
        # Let's try and change working path
        new_path = f'/home/sspade/Documents/{repository}'
        os.chdir(new_path)
        # Gittify folder
        createGit()
        # Change/confirm current branch
        os.system('git checkout main')
        os.system(f'git remote add upstream https://github.com/{remoteUser}/{repository}.git')
        # fetch origin (from your repo)
        os.system(' git fetch origin')
        os.system('git fetch upstream')
        os.system('git merge upstream/master')
        os.system('git push origin main')

    except (FileNotFoundError, IOError, AttributeError):
        print(f"{_dir} Missing!")
