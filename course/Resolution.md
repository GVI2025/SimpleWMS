# Git Practice – Solutions and Explanations

This document provides detailed solutions and answers for each of the exercises listed in the `Instruction.md` file.

---

## 🔍 Exercise 1: git fetch

```bash
git fetch origin
git branch -r                  # See remote branches
git log origin/course/git/git-fetch --oneline --graph
git diff origin/course/git/git-fetch..HEAD
```

💡 `git fetch` updates your local references to the remote branches but **does not modify your current working branch or files**.

**Answers**:
- `git fetch` retrieves new commits from remote but doesn't merge them.
- It’s useful to stay up-to-date without modifying your current branch.
- It's ideal before running comparisons, manual merges, or before using rebase.

---

## 🔄 Exercise 2: git pull

```bash
git pull origin course/git/git-pull
```

🎯 If your branch had no local changes, Git performs a **fast-forward**.

Check with:
```bash
git log --oneline --graph
```

**Answers**:
- `git pull` = `git fetch` + `git merge`
- A fast-forward happens if no divergence exists between branches.
- Use `git pull --rebase` if you want to maintain linear history.

---

## 🔀 Exercise 3: git merge without conflict

```bash
git fetch origin
git merge origin/course/git/git-merge-without-conflict
```

✅ Merge completes without conflict.

Check:
```bash
git log --oneline --graph --all
```

**Answers**:
- A merge commit may or may not be created depending on Git config (`--no-ff` forces a merge commit).
- The history will contain both parent branches merged together.
- Used to preserve branch history in a collaborative context.

---

## ⚔️ Exercise 4: git merge with conflict

```bash
git fetch origin
git merge origin/course/git/git-merge-with-conflict
```

💥 A conflict appears. Fix manually:
```bash
git status
# Edit files to resolve
git add seed_data.py
git commit
```

**Answers**:
- Git marks the conflict with `<<<<<<<`, `=======`, `>>>>>>>`.
- You must manually decide which part to keep.
- Merge commits preserve both branch histories and are preferred for team history clarity.

---

## 🧬 Exercise 5: git rebase without conflict

```bash
git fetch origin
git rebase origin/course/git/git-rebase-without-conflict
```

✅ Rebasing applies the new commits cleanly on top of your branch.

**Answers**:
- Rebase rewrites history to be linear.
- No merge commits are created.
- Preferred for a clean and readable history when working solo or in short-lived branches.

---

## 🔥 Exercise 6: git rebase with conflict

```bash
git fetch origin
git rebase origin/course/git/git-rebase-with-conflict
```

💥 Conflict arises.

```bash
git status
# Fix manually
git add seed_data.py
git rebase --continue
```

Abort if needed:
```bash
git rebase --abort
```

**Answers**:
- Rebase rewrites each commit one by one, stopping at conflicts.
- It produces a linear history but requires caution to avoid confusion.
- Useful for preparing clean history before merging feature branches.

---

## 🧪 Bonus: Inspect the seed_data.py

To explore what causes conflicts:

```bash
git diff origin/course/git/git-merge-with-conflict
git log -p origin/course/git/git-rebase-with-conflict
```

**Observation**:
- Conflicts arise when two branches modify the **same lines** differently.
- Git cannot auto-merge these changes and requires manual intervention.

---

## ✅ Summary

- `git fetch`: download changes, no integration
- `git pull`: fetch + merge
- `git merge`: preserves both histories, may create merge commits
- `git rebase`: creates a linear history by replaying commits
- Choose merge when you want to preserve context, rebase for clarity