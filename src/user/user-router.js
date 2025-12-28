/**
 * User Router - API endpoints for user management and access control
 */
const express = require('express');
const router = express.Router();
const { getUserById, getOrCreateUser, createUser, updateUser, mergeGuestProgress } = require('./user-storage');
const { User } = require('./user-model');

/**
 * Get current user (from session)
 */
router.get('/me', (req, res) => {
  try {
    const userId = req.session?.userId;
    
    if (!userId) {
      // Create guest user
      const guestUser = getOrCreateUser(null, { authProvider: 'guest' });
      req.session.userId = guestUser.userId;
      
      return res.json({
        user: guestUser.toJSON(),
        isGuest: true
      });
    }
    
    const user = getUserById(userId);
    if (!user) {
      // Create new guest if session exists but user doesn't
      const guestUser = getOrCreateUser(null, { authProvider: 'guest' });
      req.session.userId = guestUser.userId;
      
      return res.json({
        user: guestUser.toJSON(),
        isGuest: true
      });
    }
    
    res.json({
      user: user.toJSON(),
      isGuest: user.authProvider === 'guest'
    });
  } catch (err) {
    console.error('Error getting user:', err);
    res.status(500).json({ error: 'Failed to get user' });
  }
});

/**
 * Register new user
 */
router.post('/register', (req, res) => {
  try {
    const { email, password, authProvider = 'email' } = req.body;
    
    if (!email && authProvider === 'email') {
      return res.status(400).json({ error: 'Email is required' });
    }
    
    // Create new user
    const newUser = createUser({
      email,
      authProvider,
      registrationDate: new Date().toISOString()
    });
    
    // Merge guest progress if exists
    const guestUserId = req.session?.userId;
    if (guestUserId && getUserById(guestUserId)?.authProvider === 'guest') {
      mergeGuestProgress(guestUserId, newUser.userId);
    }
    
    // Update session
    req.session.userId = newUser.userId;
    
    res.json({
      user: newUser.toJSON(),
      message: 'Registration successful'
    });
  } catch (err) {
    console.error('Error registering user:', err);
    res.status(500).json({ error: 'Registration failed' });
  }
});

/**
 * Check lesson access
 */
router.get('/access/:lessonId', (req, res) => {
  try {
    const { lessonId } = req.params;
    const userId = req.session?.userId;
    
    if (!userId) {
      // Guest user - check access
      const guestUser = getOrCreateUser(null, { authProvider: 'guest' });
      req.session.userId = guestUser.userId;
      
      const access = guestUser.canAccessLesson(lessonId);
      return res.json({
        ...access,
        user: guestUser.toJSON()
      });
    }
    
    const user = getUserById(userId);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    
    const access = user.canAccessLesson(lessonId);
    res.json({
      ...access,
      user: user.toJSON()
    });
  } catch (err) {
    console.error('Error checking access:', err);
    res.status(500).json({ error: 'Failed to check access' });
  }
});

/**
 * Visit lesson (track access)
 */
router.post('/visit/:lessonId', (req, res) => {
  try {
    const { lessonId } = req.params;
    const { lessonType = 'AL' } = req.body;
    const userId = req.session?.userId;
    
    if (!userId) {
      const guestUser = getOrCreateUser(null, { authProvider: 'guest' });
      req.session.userId = guestUser.userId;
      guestUser.visitLesson(lessonId, lessonType);
      updateUser(guestUser.userId, guestUser);
      
      return res.json({
        user: guestUser.toJSON(),
        message: 'Lesson visit recorded'
      });
    }
    
    const user = getUserById(userId);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    
    // Check access before allowing visit
    const access = user.canAccessLesson(lessonId);
    if (!access.canAccess) {
      return res.status(403).json({
        error: 'Access denied',
        ...access
      });
    }
    
    user.visitLesson(lessonId, lessonType);
    updateUser(userId, user);
    
    res.json({
      user: user.toJSON(),
      message: 'Lesson visit recorded'
    });
  } catch (err) {
    console.error('Error recording visit:', err);
    res.status(500).json({ error: 'Failed to record visit' });
  }
});

/**
 * Complete lesson
 */
router.post('/complete/:lessonId', (req, res) => {
  try {
    const { lessonId } = req.params;
    const userId = req.session?.userId;
    
    if (!userId) {
      return res.status(401).json({ error: 'Authentication required' });
    }
    
    const user = getUserById(userId);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    
    user.completeLesson(lessonId);
    updateUser(userId, user);
    
    res.json({
      user: user.toJSON(),
      message: 'Lesson completed'
    });
  } catch (err) {
    console.error('Error completing lesson:', err);
    res.status(500).json({ error: 'Failed to complete lesson' });
  }
});

/**
 * Purchase lesson access
 */
router.post('/purchase/:lessonId', (req, res) => {
  try {
    const { lessonId } = req.params;
    const { paymentId, amount = 2.00 } = req.body;
    const userId = req.session?.userId;
    
    if (!userId || !getUserById(userId)) {
      return res.status(401).json({ error: 'Authentication required' });
    }
    
    const user = getUserById(userId);
    if (user.authProvider === 'guest') {
      return res.status(403).json({ error: 'Registration required before purchase' });
    }
    
    // In production, verify payment with payment provider
    // For now, we'll just record the purchase
    
    user.purchaseLesson(lessonId, amount);
    updateUser(userId, user);
    
    res.json({
      user: user.toJSON(),
      message: 'Lesson purchased successfully',
      lessonId,
      amount
    });
  } catch (err) {
    console.error('Error purchasing lesson:', err);
    res.status(500).json({ error: 'Purchase failed' });
  }
});

/**
 * Get user dashboard data
 */
router.get('/dashboard', (req, res) => {
  try {
    const userId = req.session?.userId;
    
    if (!userId) {
      return res.status(401).json({ error: 'Authentication required' });
    }
    
    const user = getUserById(userId);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    
    res.json({
      user: user.toJSON(),
      stats: {
        totalVisited: user.lessonsVisited.length,
        totalCompleted: user.lessonsCompleted.length,
        freeLessonsRemaining: user.authProvider === 'guest' 
          ? Math.max(0, 5 - user.lessonsVisited.length)
          : Math.max(0, 10 - user.freeLessonsConsumedCount),
        permanentlyUnlocked: user.permanentlyUnlockedLessons.length,
        paidLessons: user.paidLessons.length
      }
    });
  } catch (err) {
    console.error('Error getting dashboard:', err);
    res.status(500).json({ error: 'Failed to get dashboard' });
  }
});

/**
 * Logout
 */
router.post('/logout', (req, res) => {
  try {
    if (req.session) {
      req.session.userId = null;
      req.session.destroy();
    }
    res.json({ message: 'Logged out successfully' });
  } catch (err) {
    console.error('Error logging out:', err);
    res.status(500).json({ error: 'Failed to logout' });
  }
});

module.exports = router;

