### Version Control with Git

#### Video Resource
Explore the comprehensive DevOps Bootcamp lecture on Version Control with Git [here](https://techworld-with-nana.teachable.com/courses/devops-bootcamp/lectures/29436454).

#### 1. Understanding Version Control

Version control is essential for collaborative coding projects. Here are the key aspects:

- Developers collaborate on the same codebase.
- Code is centrally hosted on a repository.
- Each developer maintains a local copy.
- Git automatically merges changes but may face conflicts.
- Regular pushes and pulls minimize merge conflicts.
- Continuous Integration ensures frequent code integration.

#### 2. Basic Git Concepts

Git, the most popular version control tool, consists of:

- Remote Git Repository (central code storage).
- UI for interaction.
- Local Git Repository (developer's local copy).
- Git History (tracking changes).
- Staging Area (preparing changes for commit).
- Git Clients (execution of commands).

#### 3. Setting Up Git Repository (Remote and Local)

Key platforms include GitHub, GitLab, and others. Local setup involves:

- Installing a Git client.
- Authenticating with a remote server using SSH.
- Cloning a repository using `git clone <repository-URL>`.

#### 4. Working with Git

Understanding the Git workflow:

- **Working Directory** ➜ `git add` ➜ **Staging Area** ➜ `git commit` ➜ **Local Repository**.
- Check status: `git status`.
- Stage changes: `git add FILENAME`.
- Commit changes: `git commit`.
- View history: `git log`.
- Push changes to remote: `git push`.

#### 5. Initializing a Git Project Locally

Initialize a local project as a Git repository:

```bash
cd existing_directory
git init
git remote add origin <git-repository-URL>
git add .
git commit -m 'Initial commit'
git push --set-upstream origin master
```

#### 6. Concept of Branches

Utilize branches for organized development:

- Master branch as the main branch.
- Create feature/bugfix branches for clean code separation.
- Commands like `git branch`, `git pull`, `git checkout`, and `git push` manage branches.

#### 7. Merge Requests

Adopt best practices for code review and collaboration:

- Review code changes before merging.
- Ideal for large features or junior developer work.
- Promotes learning and growth.

#### 8. Deleting Branches

Maintain a tidy repository by deleting inactive branches:

```bash
git branch -d <branchname>  # delete locally
git push <repo> --delete <branchname>  # delete remotely
```

#### 9. Rebase

Manage commit history efficiently to avoid pollution:

```bash
git pull -r  # Pull changes and rebase
```

#### 10. Resolving Merge Conflicts

Handle conflicts by resolving manually:

```bash
git pull -r  # Pull and rebase
# Resolve conflicts in editor
git rebase --continue
git push  # Push changes to remote
```

#### 11. .gitignore file

Exclude files or folders from Git tracking:

```bash
git rm -r --cached removed_directory/
```
[Gitignore.io](https://gitignore.io/) is a useful resource.

#### 12. git stash

Temporarily hide changes for testing:

```bash
git stash  # Hide changes
git stash pop  # Reapply changes
```

#### 13. Going back in History

Navigate through commit history:

```bash
git log  # View history
git checkout <commit-hash>  # Switch to a specific commit
git checkout -b <new-branch-name>  # Create a new branch from a commit
```

#### 14. Undoing Commits

Undo local commits or revert changes:

```bash
git reset --hard HEAD~1  # Revert commits
git commit --amend -m 'commit message'  # Amend commit
```

#### 15. Merging Branches

Merge changes from one branch to another:

```bash
git checkout master
git pull  # Pull latest changes
git checkout <branch-name>
git merge master  # Merge changes into your branch
```

#### 16. Git for DevOps

Git plays a crucial role in DevOps:

- Infrastructure as Code (IaC).
- CI/CD pipeline and Build Automation.
- Integration with automation tools and Git repositories is essential.