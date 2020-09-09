import git

repo = git.Repo("./data")
remote = repo.remote()
remote.pull()
