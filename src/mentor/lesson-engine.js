const fs = require('fs');
const path = require('path');

const LESSONS_FILE = path.join(__dirname, '..', '..', 'mentor', 'lessons.json');
const LESSONS_DIR = path.join(__dirname, '..', '..', 'mentor', 'lessons');
const LESSON_GEN_DIR = path.join(__dirname, '..', '..', 'mentor', 'lessonGen');
const REACT_LESSONS_DIR = path.join(LESSON_GEN_DIR, 'react');
const REACT_TS_LESSONS_DIR = path.join(LESSON_GEN_DIR, 'react-typescript');

/**
 * Load lessons from individual JSON files or fallback to lessons.json
 * Also loads Interview Prep lessons from lessonGen directories
 */
async function loadLessons() {
  const allLessons = [];
  
  // Load algorithm lessons from mentor/lessons
  if (fs.existsSync(LESSONS_DIR)) {
    const files = fs.readdirSync(LESSONS_DIR).filter(f => f.endsWith('.json') && f !== 'algorithm-list.json');
    for (const file of files) {
      try {
        const filePath = path.join(LESSONS_DIR, file);
        const raw = fs.readFileSync(filePath, 'utf-8');
        const lesson = JSON.parse(raw);
        allLessons.push(lesson);
      } catch (err) {
        console.warn(`Failed to load lesson from ${file}:`, err.message);
      }
    }
  }
  
  // Load React JavaScript Interview Prep lessons from mentor/lessonGen/react
  if (fs.existsSync(REACT_LESSONS_DIR)) {
    const files = fs.readdirSync(REACT_LESSONS_DIR).filter(f => f.endsWith('.json'));
    for (const file of files) {
      try {
        const filePath = path.join(REACT_LESSONS_DIR, file);
        const raw = fs.readFileSync(filePath, 'utf-8');
        const lesson = JSON.parse(raw);
        allLessons.push(lesson);
      } catch (err) {
        console.warn(`Failed to load React lesson from ${file}:`, err.message);
      }
    }
  }
  
  // Load React TypeScript Interview Prep lessons from mentor/lessonGen/react-typescript
  if (fs.existsSync(REACT_TS_LESSONS_DIR)) {
    const files = fs.readdirSync(REACT_TS_LESSONS_DIR).filter(f => f.endsWith('.json'));
    for (const file of files) {
      try {
        const filePath = path.join(REACT_TS_LESSONS_DIR, file);
        const raw = fs.readFileSync(filePath, 'utf-8');
        const lesson = JSON.parse(raw);
        allLessons.push(lesson);
      } catch (err) {
        console.warn(`Failed to load React TypeScript lesson from ${file}:`, err.message);
      }
    }
  }
  
  // If we have lessons loaded, return them
  if (allLessons.length > 0) {
    return allLessons;
  }
  
  // Fallback to lessons.json
  if (fs.existsSync(LESSONS_FILE)) {
    const raw = fs.readFileSync(LESSONS_FILE, 'utf-8');
    const parsed = JSON.parse(raw);
    return parsed.lessons || [];
  }
  
  return [];
}

/**
 * Find lesson by id
 */
function findLessonById(lessons, lessonId) {
  return lessons.find(l => l.id === lessonId);
}

/**
 * Find step by id inside a lesson
 */
function findStepById(lesson, stepId) {
  return lesson.flow.find(s => s.stepId === stepId);
}

/**
 * Get next step based on current step + choice
 */
function getNextStep(lesson, currentStep, choiceLabel) {
  // 1. Explicit choice-based navigation
  if (currentStep.choices && choiceLabel) {
    const choice = currentStep.choices.find(
      c => c.label === choiceLabel
    );
    if (!choice) return null;
    return findStepById(lesson, choice.next);
  }

  // 2. Explicit "next" pointer
  if (currentStep.next) {
    return findStepById(lesson, currentStep.next);
  }

  // 3. Implicit linear flow (DEFAULT FIX)
  const index = lesson.flow.findIndex(
    s => s.stepId === currentStep.stepId
  );

  if (index === -1) return null;

  return lesson.flow[index + 1] || null;
}

module.exports = {
  loadLessons,
  findLessonById,
  findStepById,
  getNextStep
};
