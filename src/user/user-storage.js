/**
 * User Storage - Simple file-based storage for users
 * In production, this would be replaced with a database
 */
const fs = require('fs');
const path = require('path');
const { User } = require('./user-model');

const USERS_DIR = path.join(__dirname, '..', '..', 'data', 'users');
const USERS_FILE = path.join(USERS_DIR, 'users.json');

// Ensure users directory exists
if (!fs.existsSync(USERS_DIR)) {
  fs.mkdirSync(USERS_DIR, { recursive: true });
}

// In-memory cache
let usersCache = new Map();

/**
 * Load all users from file
 */
function loadUsers() {
  if (fs.existsSync(USERS_FILE)) {
    try {
      const data = fs.readFileSync(USERS_FILE, 'utf-8');
      const usersData = JSON.parse(data);
      usersCache.clear();
      
      for (const [userId, userData] of Object.entries(usersData)) {
        usersCache.set(userId, User.fromJSON(userData));
      }
    } catch (err) {
      console.error('Error loading users:', err);
      usersCache.clear();
    }
  }
}

/**
 * Save all users to file
 */
function saveUsers() {
  try {
    const usersData = {};
    for (const [userId, user] of usersCache.entries()) {
      usersData[userId] = user.toJSON();
    }
    fs.writeFileSync(USERS_FILE, JSON.stringify(usersData, null, 2), 'utf-8');
  } catch (err) {
    console.error('Error saving users:', err);
  }
}

/**
 * Get user by ID
 */
function getUserById(userId) {
  if (!userId) return null;
  return usersCache.get(userId) || null;
}

/**
 * Get or create user
 */
function getOrCreateUser(userId, userData = {}) {
  if (!userId) {
    // Generate guest ID
    userId = `guest_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }

  let user = usersCache.get(userId);
  
  if (!user) {
    user = new User({
      userId,
      ...userData
    });
    usersCache.set(userId, user);
    saveUsers();
  }
  
  return user;
}

/**
 * Create new user (for registration)
 */
function createUser(userData) {
  const userId = userData.userId || `user_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  
  const user = new User({
    userId,
    authProvider: userData.authProvider || 'email',
    email: userData.email,
    createdAt: new Date().toISOString(),
    registrationDate: new Date().toISOString(),
    ...userData
  });
  
  usersCache.set(userId, user);
  saveUsers();
  
  return user;
}

/**
 * Update user
 */
function updateUser(userId, updates) {
  const user = usersCache.get(userId);
  if (!user) return null;
  
  // Merge updates
  Object.assign(user, updates);
  saveUsers();
  
  return user;
}

/**
 * Merge guest progress into user account
 */
function mergeGuestProgress(guestUserId, registeredUserId) {
  const guestUser = usersCache.get(guestUserId);
  const registeredUser = usersCache.get(registeredUserId);
  
  if (!guestUser || !registeredUser) {
    return null;
  }
  
  // Merge lessons visited
  for (const lessonId of guestUser.lessonsVisited) {
    if (!registeredUser.lessonsVisited.includes(lessonId)) {
      registeredUser.lessonsVisited.push(lessonId);
    }
  }
  
  // Merge lessons completed
  for (const lessonId of guestUser.lessonsCompleted) {
    if (!registeredUser.lessonsCompleted.includes(lessonId)) {
      registeredUser.lessonsCompleted.push(lessonId);
    }
  }
  
  // Recalculate permanently unlocked lessons
  // First 10 lessons visited become permanently unlocked
  const allVisited = [...new Set(registeredUser.lessonsVisited)];
  registeredUser.permanentlyUnlockedLessons = allVisited.slice(0, 10);
  registeredUser.freeLessonsConsumedCount = registeredUser.permanentlyUnlockedLessons.length;
  
  saveUsers();
  
  // Optionally delete guest user
  usersCache.delete(guestUserId);
  saveUsers();
  
  return registeredUser;
}

// Load users on startup
loadUsers();

module.exports = {
  getUserById,
  getOrCreateUser,
  createUser,
  updateUser,
  mergeGuestProgress,
  loadUsers,
  saveUsers
};

