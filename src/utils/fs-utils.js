const fs = require('fs/promises');
const path = require('path');

/**
 * Ensure directory exists
 */
async function ensureDir(dirPath) {
  await fs.mkdir(dirPath, { recursive: true });
}

/**
 * Check if path exists
 */
async function pathExists(targetPath) {
  try {
    await fs.access(targetPath);
    return true;
  } catch {
    return false;
  }
}

/**
 * Safely resolve a path inside a base directory
 */
function resolveSafePath(baseDir, relativePath = '') {
  const fullPath = path.join(baseDir, relativePath);
  if (!fullPath.startsWith(baseDir)) {
    throw new Error('Access denied');
  }
  return fullPath;
}

/**
 * Read JSON file safely
 */
async function readJson(filePath) {
  const raw = await fs.readFile(filePath, 'utf-8');
  return JSON.parse(raw);
}

/**
 * Write JSON file safely
 */
async function writeJson(filePath, data) {
  const content = JSON.stringify(data, null, 2);
  await fs.writeFile(filePath, content, 'utf-8');
}

module.exports = {
  ensureDir,
  pathExists,
  resolveSafePath,
  readJson,
  writeJson
};
