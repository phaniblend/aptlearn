

const {
  loadLessons,
  findLessonById
} = require('./lesson-engine');

/**
 * Load all lessons (metadata only)
 */
async function getAllLessons() {
  const lessons = await loadLessons();
  return lessons.map(l => ({
    id: l.id,
    title: l.title,
    pattern: l.pattern,
    difficulty: l.difficulty,
    language: l.language,
    status: l.status
  }));
}

/**
 * Load full lesson by id
 */
async function getLessonById(lessonId) {
  const lessons = await loadLessons();
  const lesson = findLessonById(lessons, lessonId);

  if (!lesson) {
    throw new Error(`Lesson not found: ${lessonId}`);
  }

  return lesson;
}

module.exports = {
  getAllLessons,
  getLessonById
};
