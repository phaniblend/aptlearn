# APT Learn – Complete Architecture & Merge Guide

This document gives the **full architecture** of this app and a **merge strategy** plus a **ready-to-use prompt** for integrating this repo with another similar app in a different Cursor instance.

---

## 1. Complete Architecture

### 1.1 What This App Is

- **Name:** APT Learn (aptlearn-mentor-backend)
- **Role:** Backend + minimal in-repo frontend for a **lesson engine**: step-by-step, mentor-led lessons (algorithms, React, Angular, Vue, etc.).
- **Stack:** Node.js ≥18, Express, no DB (JSON files + optional file-based user storage). Frontend: static HTML/CSS/JS; can be replaced by external `ide-frontend`.

### 1.2 Repository Layout

```
aptlearn-main/
├── package.json                 # name: aptlearn-mentor-backend, main: src/server.js
├── src/
│   ├── server.js                # Express app, session, routes, static serving
│   ├── user/
│   │   ├── user-model.js        # User entity, canAccessLesson(), toJSON()
│   │   ├── user-storage.js      # getOrCreateUser, getUserById, file-based (data/users/)
│   │   └── user-router.js       # /api/user/* endpoints
│   ├── mentor/
│   │   ├── lesson-engine.js      # loadLessons(), findLessonById, findStepById, getNextStep()
│   │   ├── lesson-loader.js     # (if present) lesson utilities
│   │   └── mentor-router.js      # /api/mentor/* endpoints
│   └── ide/
│       ├── file-api.js          # /api/files – workspace file tree, read/write/delete
│       └── execute-api.js        # /api/execute – run code (language + code)
├── public/                      # In-repo frontend (used if present)
│   ├── index.html
│   ├── lessons.html
│   ├── learn.html
│   └── assets/
│       ├── styles.css
│       ├── lessons.js           # Fetches /api/mentor/lessons, renders list
│       └── learn.js             # POST start/next, renders steps (mentorSays, example, choices)
├── mentor/
│   ├── lessons/                 # Algorithm lessons (*.json, e.g. two-sum.json)
│   └── lessonGen/
│       ├── react/               # React JS lessons
│       ├── react-typescript/     # React TS lessons
│       ├── angular/             # Angular lessons
│       └── vue/                 # Vue lessons
├── workspace/                   # Created at runtime – IDE file workspace
└── data/users/                  # Optional – user storage (users.json)
```

- **Frontend source:** Server uses `public/` if it exists, else `../ide-frontend`. Static assets at `/assets`, HTML routes below.

### 1.3 API Surface (Complete)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/health` | Health check |
| POST | `/api/session` | Optional session (e.g. body `{ email }`), sets cookie `apt_sid` |
| **User** | | |
| GET | `/api/user/me` | Current user (creates guest if none); session has `userId` |
| POST | `/api/user/register` | Register (email, authProvider); merge guest progress |
| GET | `/api/user/access/:lessonId` | Access check (canAccess, reason, price, etc.) |
| POST | `/api/user/visit/:lessonId` | Record visit |
| POST | `/api/user/complete/:lessonId` | Mark complete |
| POST | `/api/user/purchase/:lessonId` | Purchase (placeholder) |
| GET | `/api/user/dashboard` | Dashboard data |
| POST | `/api/user/logout` | Logout |
| **Mentor (lesson engine)** | | |
| GET | `/api/mentor/lessons` | List all lessons (id, title, technology, difficulty, language, status, pattern, metadata) |
| POST | `/api/mentor/start` | Start lesson; body `{ lessonId }` → `{ lessonId, step }` |
| POST | `/api/mentor/next` | Advance; body `{ lessonId, currentStepId, choiceLabel? }` → `{ lessonId, step }` or `{ done: true }` |
| **IDE** | | |
| GET | `/api/files` | File tree of workspace |
| GET | `/api/files/*` | Read file |
| POST | `/api/files/*` | Write file |
| DELETE | `/api/files/*` | Delete file |
| POST | `/api/execute` | Execute code; body `{ language, code }` |

All mentor and user routes that need it get session via middleware (`getOrCreateSession`), which sets `req.session` (in-memory store keyed by cookie `apt_sid`).

### 1.4 Frontend Routes (HTML)

- `/` → index.html  
- `/landing` → index.html  
- `/auth` → auth.html  
- `/lessons` → lessons.html (list + links to `/learn/:id`)  
- `/algos` → algos.html  
- `/interview-prep` → interview-prep.html  
- `/dashboard` → dashboard.html  
- `/learn/:lessonId` → learn.html (SPA-like: reads lessonId from path, calls mentor API)  
- `/done` → done.html  

Assets: `/assets/*` → `FRONTEND_DIR/assets/`.

### 1.5 Lesson JSON Format (Universal)

Same shape for algorithms, React, Angular, Vue:

```json
{
  "id": "two-sum",
  "title": "Two Sum",
  "pattern": "hash-map",
  "difficulty": "easy",
  "language": "javascript",
  "status": "draft",
  "technology": "Angular",
  "metadata": { "time_estimate": "5 minutes", "challenge_number": "1" },
  "flow": [
    {
      "stepId": "title",
      "mentorSays": "Text with \\n newlines...",
      "action": "continue",
      "next": "problem-illustration"
    },
    {
      "stepId": "thinking-challenge",
      "mentorSays": "How would you solve this?",
      "choices": [
        { "label": "Option A", "next": "step-a" },
        { "label": "Option B", "next": "step-b" }
      ]
    },
    {
      "stepId": "step-a",
      "mentorSays": "Explanation...",
      "example": "code or text block",
      "action": "continue",
      "next": "next-step"
    }
  ]
}
```

- **Navigation:** `next` for linear; `choices[].next` for branches. Engine uses `findStepById` and `getNextStep(lesson, currentStep, choiceLabel)`.

### 1.6 Session & Config

- **Session:** Cookie `apt_sid`, in-memory `Map` (sessionId → `{ email?, userId?, lessonId?, currentStepId? }`). No Redis in repo.
- **Port:** `process.env.PORT || 5000`.
- **Paths:** `ROOT_DIR = path.resolve(__dirname, '..')`, then `public/`, `mentor/`, `workspace/`, `data/users/` under ROOT_DIR.

### 1.7 Dependencies

- express, cors, cookie-parser, dotenv, uuid. Dev: nodemon. No database driver.

---

## 2. How to Merge This App With Another Similar App

### 2.1 Options (high level)

1. **Backend as a mountable module**  
   - In the other app, mount this app’s Express router(s) under a prefix (e.g. `/aptlearn/api`) and serve this app’s `public/` (or a built frontend) from that app.
2. **Shared lesson engine only**  
   - Copy `mentor/` (lesson-engine, mentor-router, lesson JSON format) and `public/learn.html` + `learn.js` into the other app; keep one backend, one lesson list, one “learn” experience.
3. **Full merge**  
   - One codebase: merge routes, user model, session, and lesson data; single domain, single deployment; optional namespace (e.g. `/learn`, `/api/mentor`) to avoid clashes.

### 2.2 Recommended approach for “merge alongside”

- **Other app** = primary (its auth, its DB, its frontend framework).
- **This app** = “lesson engine + content”: keep mentor API + lesson JSON + learn UI (or reimplement learn UI in the other app’s stack).
- **Concrete steps:**
  - Add this repo as a dependency or submodule, or copy in only: `src/mentor/`, `src/ide/` (if you want IDE), `mentor/lessons/`, `mentor/lessonGen/`, and optionally `public/learn.html` + `public/assets/learn.js` + `public/assets/styles.css` (or their equivalents).
  - In the other app’s server: mount mentor router at e.g. `app.use('/api/mentor', mentorRouter)` and, if needed, `app.use('/api/files', fileApi)`, `app.use('/api/execute', executeApi)`. Ensure session middleware runs before these (and that `req.session` exists).
  - If the other app has its own session: either adapt this app’s `getOrCreateSession` to use that session store or pass through a `req.session` that has at least `userId` (and optionally `lessonId`, `currentStepId` for progress).
  - Serve the “learn” page at e.g. `/learn/:lessonId` and point it at the other app’s origin so `fetch('/api/mentor/lessons')`, `fetch('/api/mentor/start')`, `fetch('/api/mentor/next')` hit the merged backend.
  - Keep lesson format unchanged so all existing JSON (algorithms, Angular, Vue, React) keeps working.

### 2.3 What to give to the other codebase

- **This repo URL** (so the other Cursor instance can read it).
- **This prompt** (below), which describes the merge goal and points to this architecture.

---

## 3. Prompt for the Other Cursor Instance (Merge/Integrate)

Copy the block below and paste it into the Cursor instance that has the **other** (similar) app. Replace `REPO_URL` with this repo’s actual URL (e.g. `https://github.com/your-org/aptlearn-main` or the local path you’ll give it).

---

**Start of prompt (give to the other app’s Cursor):**

```
We want to merge or integrate the "APT Learn" lesson engine app with this codebase.

**Source repo to read:** [REPO_URL]

Use the file `ARCHITECTURE_AND_MERGE_GUIDE.md` in that repo. It contains:
- Full architecture (directory layout, all API endpoints, session, lesson JSON format).
- Merge strategy: recommend mounting this app’s mentor + optional IDE APIs and serving the learn UI (or reimplementing it in our stack), while keeping our app as the primary (auth, domain, deployment).

**Concrete tasks:**
1. Read ARCHITECTURE_AND_MERGE_GUIDE.md from the source repo (and optionally key files: src/server.js, src/mentor/lesson-engine.js, src/mentor/mentor-router.js, public/learn.html, public/assets/learn.js).
2. Propose where in our app to mount the mentor API (/api/mentor) and, if we need it, the IDE APIs (/api/files, /api/execute). Ensure our session or auth middleware provides a session object compatible with the mentor routes (they expect req.session for progress).
3. Either (a) copy the lesson engine code (mentor router + lesson-engine + lesson loaders) and the mentor/lessons + mentor/lessonGen content into our repo and wire routes, or (b) run the other app as a separate service and proxy/forward to it from our app—recommend (a) for a single deployment.
4. Expose a "learn" experience: either serve the source repo’s public/learn.html (and assets) under a path like /learn/:lessonId and fix API base URLs, or reimplement the same flow (list lessons → start lesson → step through with mentorSays/choices/example) in our frontend using GET /api/mentor/lessons, POST /api/mentor/start, POST /api/mentor/next.
5. Keep the lesson JSON format unchanged so all existing lessons (algorithms, Angular, Vue, React) work without modification.

Output a short integration plan (steps and file changes) and then implement the minimal changes needed to list lessons and run one lesson end-to-end in our app.
```

**End of prompt**

---

## 4. One-Line Summary

- **Architecture:** Single Node/Express backend with session, user + mentor + IDE APIs; lesson data in JSON under `mentor/lessons` and `mentor/lessonGen/{react,react-typescript,angular,vue}`; optional in-repo frontend in `public/` or external `ide-frontend`.
- **Merge:** Add mentor (and optionally IDE) routes and lesson content to the other app; keep one learn UI (imported or reimplemented) and the same lesson JSON format so Angular, Vue, and the rest keep working.

Use the prompt in Section 3 in the Cursor instance that has the similar app, and point it at this repo (and this file) for the full architecture and merge steps.
