# Module 1 — Git & GitHub

## Student: Russell Nunag
## Date: Sept. 26, 2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

[Git is a tool that tracks the changes on a project and let you go back to your previous version. GitHub is a website where the Git Projects can be store, shard, and worked on.]1
## Key vocabulary (in your own words)

- repository: This is where a projects are stored .  
- commit: Where you saved the changes on your project.
- branch: A another version of your project is making changes.  
- push / pull: Push is when you upload you changes, pull is when you get the changes.   
- pull request: request to add changes from the other branch.   
- merge conflict: This is a problem when a git cant combine the changes.

---

## Walking through what I did

I started by creating or using a Git repository and checking the current branch. I then created a separate branch so I could work on my changes without directly changing the main branch. After making changes to the files, I added the changes, committed them, and pushed the branch to GitHub. From GitHub, I created a pull request so the branch could be reviewed and eventually merged.
```
git checkout -b feature-branch
git add . 
git commit -m "Add Changes"
git push -u origin feature-branch
```

---

## A mistake I made (or one I want to avoid)

[What tripped you up? A confusing error message, committing to the wrong branch, a merge conflict — explain it so a classmate reading this avoids the same mistake.]

I was kinda confused about the git checkout and how to merge the branch to the main branch, i forgot the branch name and the branch also i made. That is why i should alwats use the git status and git branch before merging.

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]

this connects that in programming organization is important when working with the different files or version of codes. just like me that of forgot my branch name and chech the branch before merging. 