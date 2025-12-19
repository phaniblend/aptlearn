const express = require('express');
const path = require('path');
const fs = require('fs/promises');

const router = express.Router();

/**
 * Root workspace directory
 */
const WORKSPACE_DIR = path.join(
  __dirname,
  '../../workspace'
);

/**
 * Safety: ensure workspace exists
 */
async function ensureWorkspace() {
  try {
    await fs.mkdir(WORKSPACE_DIR, { recursive: true });
  } catch (_) {}
}

ensureWorkspace();

/**
 * Resolve and validate a path inside workspace
 */
function resolveSafePath(relativePath = '') {
  const fullPath = path.join(WORKSPACE_DIR, relativePath);
  if (!fullPath.startsWith(WORKSPACE_DIR)) {
    throw new Error('Access denied');
  }
  return fullPath;
}

/**
 * ------------------------
 * GET /api/files
 * Returns file tree
 * ------------------------
 */
router.get('/', async (_req, res) => {
  try {
    const tree = await buildTree(WORKSPACE_DIR);
    res.json(tree);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

/**
 * ------------------------
 * GET /api/files/:path
 * Read file content
 * ------------------------
 */
router.get('/*', async (req, res) => {
  try {
    const filePath = resolveSafePath(req.params[0]);
    const content = await fs.readFile(filePath, 'utf-8');
    res.json({ content });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

/**
 * ------------------------
 * POST /api/files/:path
 * Create / update file
 * ------------------------
 */
router.post('/*', async (req, res) => {
  try {
    const filePath = resolveSafePath(req.params[0]);
    const dir = path.dirname(filePath);

    await fs.mkdir(dir, { recursive: true });
    await fs.writeFile(filePath, req.body.content || '', 'utf-8');

    res.json({ success: true });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

/**
 * ------------------------
 * DELETE /api/files/:path
 * Delete file
 * ------------------------
 */
router.delete('/*', async (req, res) => {
  try {
    const filePath = resolveSafePath(req.params[0]);
    await fs.unlink(filePath);
    res.json({ success: true });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

/**
 * ------------------------
 * Helpers
 * ------------------------
 */
async function buildTree(dir, base = '') {
  const entries = await fs.readdir(dir, { withFileTypes: true });

  return Promise.all(
    entries.map(async entry => {
      const relPath = path.join(base, entry.name);
      const fullPath = path.join(dir, entry.name);

      if (entry.isDirectory()) {
        return {
          name: entry.name,
          path: relPath,
          type: 'directory',
          children: await buildTree(fullPath, relPath)
        };
      }

      return {
        name: entry.name,
        path: relPath,
        type: 'file'
      };
    })
  );
}

module.exports = router;
