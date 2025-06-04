# Git Practice Instructions: fetch, pull, merge, rebase

## 🛠️ Setup (5 min)
Start by creating your own branch ([TRIGRAM]/git) from the current one.
From here, you’ll use this branch to explore different Git commands.

---

## 🔍 Exercise 1: git fetch (10 min)

A remote branch named `course/git/git-fetch` contains updates.

1. Use `git fetch` to retrieve remote changes.
2. Without checking it out, figure out:
   - What commits are in `course/git/git-fetch` but not in your current branch?
   - What files changed?

> You are not expected to merge. Just observe.

Afterward, regroup and discuss:
- What `git fetch` does and doesn’t do.
- When it is useful in team collaboration.

---

## 🔄 Exercise 2: git pull (10 min)

You now want to sync with `course/git/git-pull`.

1. Pull the branch into your current branch.
2. Analyze the result:
   - Was it fast-forward or did Git create a merge commit?
   - Check your commit graph.

Discuss:
- The difference between `git pull` and `git fetch + merge`.
- Use cases and default behavior.

---

## 🔀 Exercise 3: git merge without conflict (10 min)

The branch `course/git/git-merge-without-conflict` is clean and can be merged directly.

1. Merge the branch.
2. Check your Git history:
   - Is the merge linear?
   - Was a merge commit created?

---

## ⚔️ Exercise 4: git merge with conflict (10 min)

Now try merging `course/git/git-merge-with-conflict` into your branch.

1. Attempt the merge.
2. Resolve the conflicts.
3. Commit the result.

Observation:
- What files conflicted?
- How did Git mark the conflict?

---

## 🧬 Exercise 5: git rebase without conflict (10 min)

Use the branch `course/git/git-rebase-without-conflict`.

1. Rebase its content onto your current branch.
   - `git checkout course/git/git-rebase-without-conflict`
   - `git rebase TTC/git-rebase`
2. Compare the result to a merge.

---

## 🔥 Exercise 6: git rebase with conflict (15 min)

Try rebasing `course/git/git-rebase-with-conflict` onto your branch.

1. Resolve conflicts.
2. Use `git rebase --continue`.
3. If necessary, abort with `git rebase --abort`.

Observe:
- How does the history differ from a merge?
- What are the pros/cons of rebasing in this context?

---

## 🧪 Bonus: Inspect the seed data

Each branch modifies some of the same entries in `seed_data.py`, especially:
- Articles’ names and SKUs
- Implantation or Mission quantities

You can inspect these differences manually or using:
```bash
git diff origin/course/git/git-merge-with-conflict
```
or
```bash
git log -p origin/course/git/git-rebase-with-conflict
```

This helps understand what causes merge or rebase conflicts.

---

## ✅ Wrap-up

- You should now know when to use `fetch`, `pull`, `merge`, and `rebase`.
- You should understand how Git tracks divergence and handles conflicts.