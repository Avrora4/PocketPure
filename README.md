# PocketPure

## 1. Git and Issue Usage Rules

Emphasizing "small, frequent commits" and "clear history management," we adopt a **simple Trunk-Based Development** approach.

### 1.1. Issue Management Rules
In this project, to eliminate hesitation and ensure you can immediately start your 1.5 hours of daily work, always create an Issue for a task before starting development.

### 1.2. Issue Title Naming Conventions
Add the same "prefix (type tag)" used for branches and commits to the beginning of the title so that the nature of the task is clear at a glance in the list.

**Format:** `[Type] Brief description of the task`

| Type Tag | Overview (Purpose) | Title Example | Corresponding Branch Name |
| :--- | :--- | :--- | :--- |
| **`[feat]`** | Development of new features | `[feat] Add CSV upload feature` | `feat/add-csv-upload` |
| **`[fix]`** | Bug or defect fixes | `[fix] Fix issue with negative amounts` | `fix/amount-validation` |
| **`[refactor]`**| Code organization and improvement | `[refactor] Centralize API communication logic`| `refactor/api-client` |
| **`[chore]`** | Chores like tool setup or research | `[chore] Initial setup of Linter/Formatter`| `chore/setup-linter` |

---

### 1.3. Issue Content (Template)
An Issue is a "work instruction for your future self." At a minimum, describe "What (Overview)", "Why (Context)", and "Definition of Done (Acceptance Criteria)".

Please copy the template to create an Issue. (*If using GitHub, saving this as `.github/ISSUE_TEMPLATE/task.md` will automatically populate the input field.)

### 1.4. Branching Strategy
- The `main` branch must always be kept in a **working (deployable) state**.
- Always create a feature branch from `main` when working.
- **Branch Naming Convention:** `prefix/short-description`
  - `feat/add-transaction-api` (New feature)
  - `fix/date-format-bug` (Bug fix)
  - `refactor/ui-components` (Refactoring)

### 1.5. Commit Message Rules (Conventional Commits)
Write messages so that someone looking back can understand in one second **"why the change was made and what exactly changed,"** rather than just "what was done."

**Naming Format**
- **Branch Name:** `type/short-english-description` (e.g., `feat/add-csv-upload`)
- **Commit Message:** `type: summary of changes[#issue-number]` (e.g., `feat: Add CSV file upload feature`)

**Prefix (Type) List**

| Type | Overview | Specific Example (Commit Message) |
| :--- | :--- | :--- |
| **`feat`** | New feature addition | `feat: Add a form for manual transaction entry from the screen` |
| **`fix`** | Bug fix | `fix: Fix a bug where negative amounts could be registered` |
| **`docs`** | Documentation changes only | `docs: Add API endpoint list to README` |
| **`style`** | Formatting changes that do not affect code execution | `style: Auto-format code using Prettier/Ruff` |
| **`refactor`**| Refactoring (excluding feature additions or bug fixes) | `refactor: Extract API communication processing using fetch into a common function` |
| **`perf`** | Changes to improve performance | `perf: Optimize the query for fetching the transaction list from the DB` |
| **`test`** | Adding test code or modifying existing tests | `test: Add unit tests for the total amount calculation logic` |
| **`build`** | Changes to the build system or external dependencies | `build: Change Vite configuration, remove unused npm packages` |
| **`ci`** | Changes to CI/CD configuration files or scripts | `ci: Add automatic deployment setup using GitHub Actions` |
| **`chore`** | Other chores that do not affect the source code or tests | `chore: Update .gitignore, add editor configurations` |

### 1.6. Merge Rules
- At the end of your 1.5-hour work session, always commit and push (WIP: Work In Progress is acceptable).
- Once a single feature (vertical slice) is complete, create a Pull Request (PR) to `main`.
- When merging, **"Squash and Merge"** is recommended. Combine small WIP commits into one to keep the `main` history clean.

### 1.7. Pull Request (PR) Rules
#### 1.7.1. PR Title Naming Convention
Since we use "Squash and Merge", the PR title will become the final commit message on the `main` branch. Therefore, the PR title **must follow the exact same Conventional Commits format** as your commit messages. Adding the Issue number at the end is highly recommended.

**Format:** `type: Brief summary of changes (#IssueNumber)`

**Examples:**
- `feat: Add manual transaction entry form (#12)`
- `fix: Prevent negative values in amount field (#15)`
- `refactor: Centralize API fetch logic (#18)`

**Why this matters:**
When you look back at the Git history months later, you will see a clean, readable list of exactly what was introduced and which Issue triggered it, without the noise of temporary WIP commits.
As a solo developer with limited time, PRs serve as a final checkpoint before merging code into `main` and as documentation for your future self.

- **Keep it Small:** A PR should ideally cover one specific Issue (one vertical slice). Avoid bundling unrelated features.
- **Self-Review:** Before merging, review your own code on GitHub's "Files changed" tab. Check for leftover `console.log`s, typos, and ensure it meets the Acceptance Criteria of the original Issue.
- **Draft PRs:** If your 1.5-hour session ends before a feature is complete, push your branch and open a "Draft PR". This is a great way to save your progress and leave notes on where to resume tomorrow.

### 1.8. PR Description (Template)
Use the following template to ensure the "Why" and "How" of your changes are clearly documented. You can automate this by saving the text below as `.github/PULL_REQUEST_TEMPLATE.md` in your repository.

---

## 2. Directory Structure

We will use a monorepo structure with a clear separation between the backend (FastAPI) and frontend (React+Vite). Prioritizing learning cost and development speed (1.5h/day), this is a flat, practical design that avoids excessive nesting (such as Atomic Design).

```text
credit-card-tracker/  (Project Root)
│
├── backend/                  # FastAPI (Python)
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py           # Application entry point
│       ├── database.py       # DB connection settings (SQLAlchemy, etc.)
│       ├── models/           # DB table definitions (SQL models)
│       │   └── transaction.py
│       ├── schemas/          # API input/output type definitions (Pydantic models)
│       │   └── transaction.py
│       └── api/              # API endpoints (Routers)
│           └── transactions.py
│
├── frontend/                 # React + Vite (JavaScript/TypeScript)
│   ├── package.json
│   ├── vite.config.js
│   └── src/
│       ├── main.jsx          # React mount point
│       ├── App.jsx           # Routing and main layout
│       ├── api/              # Common fetch communication logic (axios alternative)
│       │   └── client.js
│       ├── components/       # UI components (No Atomic Design, flat placement)
│       │   ├── Button.jsx
│       │   ├── Button.module.scss
│       │   ├── TransactionForm.jsx
│       │   └── TransactionTable.jsx
│       └── styles/           # Global CSS/SCSS
│           └── global.scss
│
├── docker-compose.yml        # For launching DB (PostgreSQL) and backend together
├── .gitignore
└── README.md                 # This file
