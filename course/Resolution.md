# Git Practice – Solutions and Explanations

This document provides detailed solutions for each of the exercises listed in the `Instruction.md` file.

---

## 🔍 Exercise 1: git fetch

```bash
git fetch origin
git branch -r                  # See remote branches
git log origin/course/git/git-fetch --oneline --graph
git diff origin/course/git/git-fetch..HEAD
```

💡 You fetched changes, but didn’t integrate them. `git fetch` only updates your local references to the remote.

---

## 🔄 Exercise 2: git pull

```bash
git pull origin course/git/git-pull
```

🎯 If your branch had no local changes, this is a fast-forward.
Check with:
```bash
git log --oneline --graph
```

---

## 🔀 Exercise 3: git merge without conflict

```bash
git fetch origin
git merge origin/course/git/git-merge-without-conflict
```

✅ The merge should succeed automatically.
Check:
```bash
git log --oneline --graph --all
```

---

## ⚔️ Exercise 4: git merge with conflict

```bash
git fetch origin
git merge origin/course/git/git-merge-with-conflict
```

💥 Conflict appears. Fix the file(s) manually.

```bash
git status                  # Shows conflicting files
# Open file, resolve >>> <<< conflict markers
git add seed_data.py
git commit
```

---

## 🧬 Exercise 5: git rebase without conflict

```bash
git fetch origin
git rebase origin/course/git/git-rebase-without-conflict
```

✅ Changes replayed on top. Linear history preserved.

---

## 🔥 Exercise 6: git rebase with conflict

```bash
git fetch origin
git rebase origin/course/git/git-rebase-with-conflict
```

💥 Conflict arises. Fix it:

```bash
git status
# Edit file(s)
git add seed_data.py
git rebase --continue
```

If it becomes unmanageable:
```bash
git rebase --abort
```

---

## 🧪 Bonus: Inspect the seed_data.py

Example diff:
```bash
git diff origin/course/git/git-merge-with-conflict
```

Example patch history:
```bash
git log -p origin/course/git/git-rebase-with-conflict
```

---

## ✅ Summary

Each command:
- `git fetch`: updates remote refs
- `git pull`: fetch + merge
- `git merge`: combines branches, may create merge commits
- `git rebase`: replays commits for a linear history, can be cleaner but riskier