const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const path = require('path');
const fs = require('fs');
const { v4: uuidv4 } = require('uuid');
const cookieParser = require('cookie-parser');

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

/**
 * ------------------------
 * Core Middleware
 * ------------------------
 */
app.use(cors());
app.use(express.json());
app.use(cookieParser());

/**
 * ------------------------
 * Paths
 * ------------------------
 */
const ROOT_DIR = path.resolve(__dirname, '..');
const MENTOR_DIR = path.join(ROOT_DIR, 'mentor');
const WORKSPACE_DIR = path.join(ROOT_DIR, 'workspace');
const FRONTEND_DIR = path.join(ROOT_DIR, '..', 'ide-frontend');

/**
 * Ensure required directories exist
 */
if (!fs.existsSync(WORKSPACE_DIR)) {
  fs.mkdirSync(WORKSPACE_DIR, { recursive: true });
}

/**
 * ------------------------
 * In-Memory Session Store
 * ------------------------
 */
const sessions = new Map(); // sessionId -> { email?, lessonId?, currentStepId? }

function getOrCreateSession(req, res) {
  let sessionId = req.cookies.apt_sid;
  
  if (!sessionId || !sessions.has(sessionId)) {
    sessionId = uuidv4();
    sessions.set(sessionId, {});
    res.cookie('apt_sid', sessionId, {
      httpOnly: true,
      maxAge: 7 * 24 * 60 * 60 * 1000, // 7 days
      sameSite: 'lax'
    });
  }
  
  return { sessionId, session: sessions.get(sessionId) };
}

/**
 * ------------------------
 * Session API (optional)
 * ------------------------
 */
app.post('/api/session', (req, res) => {
  const { email } = req.body;
  const { session } = getOrCreateSession(req, res);
  
  if (email) {
    session.email = email;
  }
  
  res.json({ ok: true });
});

/**
 * ------------------------
 * Health Check
 * ------------------------
 */
app.get('/health', (_req, res) => {
  res.json({
    status: 'ok',
    service: 'aptlearn-mentor-backend',
    time: new Date().toISOString()
  });
});

/**
 * ------------------------
 * Mentor APIs (with session context)
 * ------------------------
 */
const mentorRouter = require('./mentor/mentor-router');
app.use('/api/mentor', (req, res, next) => {
  const { session } = getOrCreateSession(req, res);
  req.session = session;
  next();
}, mentorRouter);

/**
 * ------------------------
 * IDE APIs
 * ------------------------
 */
const fileApi = require('./ide/file-api');
const executeApi = require('./ide/execute-api');

app.use('/api/files', fileApi);
app.use('/api/execute', executeApi);

/**
 * ------------------------
 * Frontend Routes
 * ------------------------
 */
// Serve static assets (CSS, JS)
app.use('/assets', express.static(path.join(FRONTEND_DIR, 'assets')));

// Frontend page routes
app.get('/', (req, res) => {
  res.sendFile(path.join(FRONTEND_DIR, 'landing.html'));
});

app.get('/auth', (req, res) => {
  res.sendFile(path.join(FRONTEND_DIR, 'auth.html'));
});

app.get('/algos', (req, res) => {
  res.sendFile(path.join(FRONTEND_DIR, 'algos.html'));
});

app.get('/learn/:lessonId', (req, res) => {
  res.sendFile(path.join(FRONTEND_DIR, 'learn.html'));
});

app.get('/done', (req, res) => {
  res.sendFile(path.join(FRONTEND_DIR, 'done.html'));
});

/**
 * ------------------------
 * Start Server
 * ------------------------
 */
app.listen(PORT, () => {
  console.log(`APT Learn backend running on http://localhost:${PORT}`);
  console.log(`Frontend served from: ${FRONTEND_DIR}`);
});
