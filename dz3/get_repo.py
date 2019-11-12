from subprocess import call


def clone_repo_in_github(git_url, directory):
    call('git clone {} {}'.format(git_url, directory))
    return directory










