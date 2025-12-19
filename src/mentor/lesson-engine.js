const fs = require('fs');
const path = require('path');

const LESSONS_FILE = path.join(__dirname, '..', '..', 'mentor', 'lessons.json');

/**
 * Load lessons from JSON file
 */
async function loadLessons() {
  const raw = fs.readFileSync(LESSONS_FILE, 'utf-8');
  const parsed = JSON.parse(raw);
  return parsed.lessons || [];
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
