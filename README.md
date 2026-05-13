# Branching-Out Demo(Python)

A simple Python project for learning and practice purposes.  
This application demonstrates the usage of branches.

## Features

- Filters user data from a JSON structure
- Main branch implemented a simple name filter
- Feature branch _feature-filter-by-age_ added an age filter 
- Feature branch _feature-filter-by-email_ added an email filter 
- The email filter was merged with main by a pull request

---

## Run the application

Start the project with:
```text
python|python3 filter_users.py
```

## Git History with Fast-Forward and Merge Commit

This document explains the following Git history step by step:

```text
git log --oneline --graph
```

```text
* d7ed803 (HEAD -> main, origin/main) code comments added
*   f05a05b Merge pull request #1 from user0815/feature-filter-by-email
|\  
| * 2b3cf4e (origin/feature-filter-by-email, feature-filter-by-email) filter by email added
|/  
* 435faed (origin/feature-filter-by-age, feature-filter-by-age) filter by age added
* 35d4671 basic user filter by name added
* d987b26 first commit
```

---

### 1. Initial Commit

```text
* d987b26 first commit
```

The repository is created.  
This is the starting point of the entire history.

```text
main
 |
 v
d987b26
first commit
```

---

### 2. Development on `main`

```text
* 35d4671 basic user filter by name added
* d987b26 first commit
```

A second commit is added directly to the `main` branch.

```text
d987b26
first commit
   |
   v
35d4671
basic user filter by name added
```

At this point, the history is completely linear.

---

### 3. Feature Branch `feature-filter-by-age`

A new feature branch is created from `main`:

```bash
git checkout -b feature-filter-by-age
```

A new commit is added on this branch:

```text
435faed filter by age added
```

The history now looks like this:

```text
d987b26
first commit
   |
   v
35d4671
basic user filter by name added
   |
   v
435faed
filter by age added
```

Since no new commits were added to `main` in the meantime, this branch can later be integrated using a fast-forward merge.

---

### 4. Fast-Forward Merge of `feature-filter-by-age`

The branch is merged into `main`:

```bash
git checkout main
git merge feature-filter-by-age
```

Git recognizes:

```text
main is a direct ancestor of feature-filter-by-age
```

Therefore, no additional merge commit is required.

Instead, Git simply moves the `main` branch pointer forward.

Before fast-forward:

```text
d987b26 --- 35d4671        main
              \
               435faed    feature-filter-by-age
```

After fast-forward:

```text
d987b26 --- 35d4671 --- 435faed
                         main
                         feature-filter-by-age
```

Important:

- No new commit is created.
- The history remains linear.
- `main` now points to the same commit as `feature-filter-by-age`.

---

### 5. New Feature Branch `feature-filter-by-email`

Another feature branch is created from the current state:

```bash
git checkout -b feature-filter-by-email
```

A new commit is added on this branch:

```text
2b3cf4e filter by email added
```

The history now looks like this:

```text
d987b26 --- 35d4671 --- 435faed
                              \
                               2b3cf4e
                               feature-filter-by-email
```

The commit `2b3cf4e` initially exists only on the feature branch.

---

### 6. Merge via Pull Request

The branch `feature-filter-by-email` is later merged into `main` using a pull request.

This creates a dedicated merge commit:

```text
f05a05b Merge pull request #1 from user0815/feature-filter-by-email
```

The history now looks like this:

```text
d987b26 --- 35d4671 --- 435faed -------- f05a05b
                              \         /
                               2b3cf4e
```

The merge commit `f05a05b` combines two development lines:

1. the existing `main` history
2. the feature branch `feature-filter-by-email`

Therefore, this commit has two parent commits.

---

### 7. Merge Visualization in Git Log

The merge is displayed in `git log --oneline --graph` like this:

```text
*   f05a05b Merge pull request #1 from user0815/feature-filter-by-email
|\  
| * 2b3cf4e filter by email added
|/  
* 435faed filter by age added
```

Meaning of the symbols:

```text
*    Commit
|    Connection line
\    Branch split
/    Merge back into main line
|\   Merge commit with two parents
```

---

### 8. Additional Commit on `main`

After the merge, development continues directly on `main`.

```text
d7ed803 code comments added
```

The final history becomes:

```text
d987b26 --- 35d4671 --- 435faed -------- f05a05b --- d7ed803
                              \         /
                               2b3cf4e
```

`HEAD`, `main`, and `origin/main` now point to the latest commit:

```text
d7ed803 (HEAD -> main, origin/main)
```

This means:

- The current local branch is `main`
- `HEAD` points to `main`
- The local `main` branch is synchronized with `origin/main`

---

### 9. Complete Git Graph

```text
* d7ed803 (HEAD -> main, origin/main) code comments added
*   f05a05b Merge pull request #1 from user0815/feature-filter-by-email
|\  
| * 2b3cf4e (origin/feature-filter-by-email, feature-filter-by-email) filter by email added
|/  
* 435faed (origin/feature-filter-by-age, feature-filter-by-age) filter by age added
* 35d4671 basic user filter by name added
* d987b26 first commit
```

---

### 10. Summary

This history contains two different integration strategies.

#### Fast-Forward Merge

Used for `feature-filter-by-age`:

```text
main was simply moved forward.
```

Characteristics:

- no merge commit
- linear history
- clean and simple
- possible only if `main` has not changed since the branch was created

---

#### Real Merge Commit

Used for `feature-filter-by-email`:

```text
A dedicated merge commit was created.
```

Characteristics:

- visible branch structure
- dedicated merge commit
- two parent commits
- common for GitHub pull requests

---

### 11. Key Takeaway

A fast-forward merge is simply moving the branch pointer forward.

A merge commit is a real combination of two separate development histories.