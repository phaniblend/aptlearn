const express = require('express');
const router = express.Router();

const {
  loadLessons,
  findLessonById,
  findStepById,
  getNextStep
} = require('./lesson-engine');

/**
 * ------------------------
 * Start a lesson
 * ------------------------
 * body: { lessonId }
 */
router.post('/start', async (req, res) => {
  try {
    const { lessonId } = req.body;

    if (!lessonId) {
      return res.status(400).json({ error: 'lessonId is required' });
    }

    const lessons = await loadLessons();
    const lesson = findLessonById(lessons, lessonId);

    if (!lesson) {
      return res.status(404).json({ error: 'Lesson not found' });
    }

    const firstStep = lesson.flow[0];
    
    // Store progress in session
    if (req.session) {
      req.session.lessonId = lessonId;
      req.session.currentStepId = firstStep.stepId;
    }

    res.json({
      lessonId: lesson.id,
      step: firstStep
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Failed to start lesson' });
  }
});

/**
 * ------------------------
 * Advance lesson
 * ------------------------
 * body: { lessonId, currentStepId, choiceLabel }
 */
router.post('/next', async (req, res) => {
  try {
    const { lessonId, currentStepId, choiceLabel } = req.body;

    if (!lessonId || !currentStepId) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const lessons = await loadLessons();
    const lesson = findLessonById(lessons, lessonId);

    if (!lesson) {
      return res.status(404).json({ error: 'Lesson not found' });
    }

    const currentStep = findStepById(lesson, currentStepId);

    if (!currentStep) {
      return res.status(404).json({ error: 'Step not found' });
    }

    const nextStep = getNextStep(lesson, currentStep, choiceLabel);

    if (!nextStep) {
      // Clear lesson progress when done
      if (req.session) {
        req.session.lessonId = null;
        req.session.currentStepId = null;
      }
      return res.json({ done: true });
    }

    // Update session progress
    if (req.session) {
      req.session.currentStepId = nextStep.stepId;
    }

    res.json({
      lessonId: lesson.id,
      step: nextStep
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Failed to advance lesson' });
  }
});

module.exports = router;
