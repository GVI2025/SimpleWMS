# Git Flow Instruction — Practical Assignment

## Context

This exercise is based on the **SimpleWMS** project. You must start from the branch:

```
course/git-flow/start-here
```

Each student will work under their own namespace using their **TRIGRAM** (replace `[TRIGRAM]` with yours).
This namespace will be used for all branches and tags created during the exercise (substituting the 'main' branch in the Git Flow model).
```
[TRIGRAM]/git-flow/start-here
```

## Objective

You will practice the Git Flow branching model in a realistic project scenario. The exercise will be completed in three main phases:

---

## Step 1 – Hotfix a Production Bug

A production issue related to missions must be addressed immediately.

- Start by creating a branch:
  ```
  [TRIGRAM]/git-flow/hotfix/fix-mission-status
  ```

- Investigate and fix the bug in `mission.py`. The issue is:
  > The function `list_missions(...)` returns terminated and failed missions, which should be filtered out by default.

- Once the fix is implemented and verified, follow the Git Flow process to merge and **tag the hotfix** using the following naming convention:
  ```
  v1.0.1.[TRIGRAM]
  ```

---

## Step 2 – Feature Development Round 1

You will now implement **two new micro-features**, grouped into a **first release**.

Create a `develop` branch to serve as the base for your feature work:

```
[TRIGRAM]/git-flow/develop
```

From there, create **feature branches** as needed:

```
[TRIGRAM]/git-flow/feature/...
```

### Features to implement in Release 1:

- **Feature A**: Add a new boolean field `urgent` to the `Mission` model and expose it through API CRUD operations.
- **Feature B**: Allow listing only active agents through the endpoint `GET /agents?actif=true`.

Once both features are complete and tested, create a **release branch**:

```
[TRIGRAM]/git-flow/release/v1.1.0
```

Finalize the release using Git Flow and **create a tag** with your trigram included:

```
v1.1.0.[TRIGRAM]
```

---

## Step 3 – Feature Development Round 2

Start a new round of developments for a second release. Reuse your `[TRIGRAM]/git-flow/develop` branch and continue as before.

### Features to implement in Release 2:

- **Feature C**: Add a search by SKU to the article listing endpoint: `GET /articles?sku=...`
- **Feature D**: Add a field `commentaire` (text, optional) to implantations and support it in creation/update/listing.

Create and merge your features under dedicated feature branches, then prepare a release:

```
[TRIGRAM]/git-flow/release/v1.2.0
```

As before, complete the release and create the tag:

```
v1.2.0.[TRIGRAM]
```

---

## Constraints

- You must follow Git Flow principles.
- Use tags to mark releases and hotfixes.
- All tags **must include your trigram**, following the format `vX.Y.Z.[TRIGRAM]`.
- Only merge to `main` from `release` or `hotfix` branches.
- Avoid fast-forward merges unless explicitly justified.

## Deliverable

At the end of the exercise, each student should have:
- A clean repository history reflecting the Git Flow process.
- Tags for each release and hotfix.
- Fully implemented and committed features.

## Annexe – Updating the Database from Models Using Alembic

To update the database schema based on changes in your SQLAlchemy models, follow these steps:

---

### Step 1 – Create a New Alembic Revision
1. Run the following command to generate a new migration script:
   ```bash
   alembic revision --autogenerate -m "Describe your changes here"
   ```
   - The `--autogenerate` flag inspects your models and compares them to the current database schema to generate the necessary changes.
   - Replace `"Describe your changes here"` with a meaningful message describing the migration.

---

### Step 2 – Review the Generated Migration Script
1. Open the generated migration file in the `migrations/versions` directory.
2. Verify that the `upgrade()` and `downgrade()` functions correctly reflect the changes you made to the models.

---

### Step 3 – Apply the Migration to the Database
1. Run the following command to apply the migration:
   ```bash
   alembic upgrade head
   ```
   - This updates the database schema to the latest revision.

---

### Step 4 – Verify the Changes
1. Check the database to ensure the schema matches the updated models.
2. Test the application to confirm everything works as expected.

---

### Notes
- Ensure that the `alembic.ini` file is correctly configured with the database connection URL.
- Always commit your migration scripts to version control to maintain a history of schema changes.