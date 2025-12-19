const express = require('express');
const path = require('path');
const fs = require('fs/promises');
const { exec } = require('child_process');

const router = express.Router();

/**
 * Workspace directory
 */
const WORKSPACE_DIR = path.join(
  __dirname,
  '../../workspace'
);

/**
 * Execute user code
 * POST /api/execute
 * body: { language, code }
 */
router.post('/', async (req, res) => {
  const { language, code } = req.body;

  if (!language || !code) {
    return res.status(400).json({
      error: 'language and code are required'
    });
  }

  try {
    const filename = getTempFilename(language);
    const filePath = path.join(WORKSPACE_DIR, filename);

    await fs.writeFile(filePath, code, 'utf-8');

    const command = buildCommand(language, filePath);

    exec(
      command,
      {
        cwd: WORKSPACE_DIR,
        timeout: 10000,
        maxBuffer: 1024 * 1024
      },
      (error, stdout, stderr) => {
        if (error) {
          return res.json({
            output: stdout || '',
            error: stderr || error.message
          });
        }

        res.json({
          output: stdout,
          error: stderr
        });
      }
    );
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

/**
 * Helpers
 */
function getTempFilename(language) {
  switch (language) {
    case 'javascript':
      return 'temp.js';
    case 'python':
      return 'temp.py';
    case 'java':
      return 'Solution.java';
    case 'cpp':
      return 'temp.cpp';
    case 'typescript':
      return 'temp.ts';
    default:
      throw new Error(`Unsupported language: ${language}`);
  }
}

function buildCommand(language, filePath) {
  const baseName = path.basename(filePath, path.extname(filePath));
  const dir = path.dirname(filePath);
  
  switch (language) {
    case 'javascript':
      return `node "${filePath}"`;
    case 'python':
      return `python "${filePath}"`;
    case 'java':
      // Compile then run
      return `cd "${dir}" && javac "${filePath}" && java ${baseName}`;
    case 'cpp':
      // Compile then run
      const exePath = path.join(dir, baseName + '.exe');
      return `cd "${dir}" && g++ "${filePath}" -o "${exePath}" && "${exePath}"`;
    case 'typescript':
      // Compile TypeScript to JS then run
      const jsPath = filePath.replace('.ts', '.js');
      return `cd "${dir}" && npx tsc "${filePath}" --target es2020 --module commonjs && node "${jsPath}"`;
    default:
      throw new Error(`Unsupported language: ${language}`);
  }
}

module.exports = router;
