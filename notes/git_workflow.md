# Git Workflow Notes

## Basic Git Flow

1. Check repository status
git status

2. Add files to staging
git add .

3. Commit changes
git commit -m "message"

4. Push changes to GitHub
git push origin main

## Removing unnecessary files

Some IDEs create folders like `.idea` which should not be stored in Git.

Steps:
1. Add `.idea/` to `.gitignore`
2. Remove folder locally
rm -rf .idea

## Git Areas

Git has three main areas:

1. Working Directory
2. Staging Area
3. Repository

Flow:

Working Directory → git add → Staging Area → git commit → Repository