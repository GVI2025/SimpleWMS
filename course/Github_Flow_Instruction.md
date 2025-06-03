# GitHub Flow Instruction — Practical Assignment

## Context

This practical exercise is based on the **SimpleWMS** project. Students must start from the following branch:

```
course/github-flow/start-here
```

Each student will work under their own namespace using their **TRIGRAM** (replace `[TRIGRAM]` with yours).
This namespace will be used for all branches and tags created during the exercise (substituting the 'main' branch in the Git Flow model).
```
[TRIGRAM]/github-flow/start-here
```

Throughout this assignment, students must follow the **GitHub Flow** process and apply the **Conventional Commits** specification in all commit messages:  
➡ https://www.conventionalcommits.org/en/v1.0.0/

## Objective

You will apply GitHub Flow principles through two tasks:
1. Writing missing unit tests
2. Adding a new functional feature

Each contribution must go through a **feature branch**, a **pull request**, a **code review**, and be merged after successful CI tests and review approval.

---

## Step 1 — Add Missing Unit Tests

The goal of this step is to complete the test coverage for an existing router.

- **Focus area**: The router layer for `emplacements` lacks sufficient unit tests.
- You must identify missing tests and write additional unit tests accordingly.

Expected behavior:
- Ensure key scenarios of the router are covered (listing, creating, updating, error handling).
- Use mocking for the service layer.
- Respect naming and structure consistency with existing test files.

---

## Step 2 — Add a New Feature

You will now implement a new feature in the system.

### Add Search by Designation (Commande)

Allow filtering `commandes` by partial designation of articles included in the order.

Example:
```
GET /commandes?designation=perceuse
```

Expected behavior:
- Only orders that include at least one article with `"perceuse"` in the designation are returned.
- Ensure query performance and write appropriate tests.

---

## Deliverables

Each student must:
- Work from a **feature branch**
- Open a **pull request**
- Apply **Conventional Commits**
- Get their pull request reviewed and approved
- Merge using a **squash merge**
- Ensure the main branch remains stable and CI passes

The goal is to replicate the GitHub Flow lifecycle for collaborative development.

---

## Step 3 — Breaking Change Feature

You will now implement a change that introduces a **non-backward compatible behavior** in the system. This must be clearly marked using a `feat!:` commit and documented.

### Feature — Rename Field `etat` in `Commande` to `statut`

Update the following:
- Rename the field `etat` to `statut` in the `Commande` model and everywhere it is used:
  - SQLAlchemy model
  - Pydantic schemas
  - CRUD functions
  - Test cases
  - Any related business logic
- Migrate the database schema accordingly with Alembic.
- Update seed data if needed.

Expected behavior:
- The system should now consistently use `statut` instead of `etat` for commands.
- Existing API clients **will break** if not updated — this is intentional.

This step is designed to practice managing breaking changes in API design under GitHub Flow.

---