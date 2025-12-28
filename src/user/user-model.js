/**
 * User Model for INPACT LEARN
 * Handles user data structure and business logic for freemium access
 */

/**
 * User Entity Structure
 */
class User {
  constructor(data = {}) {
    this.userId = data.userId || null;
    this.authProvider = data.authProvider || 'guest'; // 'guest' | 'email' | 'google' | 'github'
    this.email = data.email || null;
    this.createdAt = data.createdAt || new Date().toISOString();
    this.registrationDate = data.registrationDate || null;
    
    // Tracking
    this.lessonsVisited = data.lessonsVisited || []; // Array of lesson IDs (AL or CL)
    this.lessonsCompleted = data.lessonsCompleted || []; // Array of lesson IDs
    this.freeLessonsConsumedCount = data.freeLessonsConsumedCount || 0;
    this.permanentlyUnlockedLessons = data.permanentlyUnlockedLessons || []; // First 10 lessons (for registered users)
    this.paidLessons = data.paidLessons || []; // Array of { lessonId, purchasedAt, amount }
  }

  /**
   * Check if user can access a lesson
   * @param {string} lessonId - The lesson ID to check
   * @returns {Object} { canAccess: boolean, reason: string, requiresPayment: boolean }
   */
  canAccessLesson(lessonId) {
    // If already paid for, always accessible
    if (this.paidLessons.some(p => p.lessonId === lessonId)) {
      return {
        canAccess: true,
        reason: 'paid',
        requiresPayment: false
      };
    }

    // If permanently unlocked (first 10 for registered users), always accessible
    if (this.permanentlyUnlockedLessons.includes(lessonId)) {
      return {
        canAccess: true,
        reason: 'free_for_life',
        requiresPayment: false
      };
    }

    // Guest users: 5 free lessons
    if (this.authProvider === 'guest') {
      if (this.lessonsVisited.length < 5) {
        return {
          canAccess: true,
          reason: 'guest_free',
          requiresPayment: false
        };
      } else {
        return {
          canAccess: false,
          reason: 'guest_limit_reached',
          requiresPayment: false, // Registration required, not payment
          requiresRegistration: true
        };
      }
    }

    // Registered users: First 10 lessons free for life
    if (this.authProvider !== 'guest') {
      // Check if this is one of the first 10 lessons accessed
      if (this.permanentlyUnlockedLessons.length < 10) {
        // This will be unlocked permanently when accessed
        return {
          canAccess: true,
          reason: 'free_for_life',
          requiresPayment: false
        };
      }

      // After 10 free lessons, require payment
      if (this.freeLessonsConsumedCount >= 10) {
        return {
          canAccess: false,
          reason: 'payment_required',
          requiresPayment: true,
          price: 2.00
        };
      }
    }

    return {
      canAccess: false,
      reason: 'unknown',
      requiresPayment: false
    };
  }

  /**
   * Record lesson visit
   * @param {string} lessonId - The lesson ID visited
   * @param {string} lessonType - 'AL' (Algorithm Lesson) or 'CL' (Coding Challenge)
   */
  visitLesson(lessonId, lessonType = 'AL') {
    if (!this.lessonsVisited.includes(lessonId)) {
      this.lessonsVisited.push(lessonId);
    }

    // For registered users, first 10 lessons become permanently unlocked
    if (this.authProvider !== 'guest' && this.permanentlyUnlockedLessons.length < 10) {
      if (!this.permanentlyUnlockedLessons.includes(lessonId)) {
        this.permanentlyUnlockedLessons.push(lessonId);
        this.freeLessonsConsumedCount = this.permanentlyUnlockedLessons.length;
      }
    }
  }

  /**
   * Mark lesson as completed
   * @param {string} lessonId - The lesson ID completed
   */
  completeLesson(lessonId) {
    if (!this.lessonsCompleted.includes(lessonId)) {
      this.lessonsCompleted.push(lessonId);
    }
  }

  /**
   * Purchase lesson access
   * @param {string} lessonId - The lesson ID purchased
   * @param {number} amount - Amount paid (default $2.00)
   */
  purchaseLesson(lessonId, amount = 2.00) {
    if (!this.paidLessons.some(p => p.lessonId === lessonId)) {
      this.paidLessons.push({
        lessonId,
        purchasedAt: new Date().toISOString(),
        amount
      });
    }
  }

  /**
   * Convert to JSON for storage
   */
  toJSON() {
    return {
      userId: this.userId,
      authProvider: this.authProvider,
      email: this.email,
      createdAt: this.createdAt,
      registrationDate: this.registrationDate,
      lessonsVisited: this.lessonsVisited,
      lessonsCompleted: this.lessonsCompleted,
      freeLessonsConsumedCount: this.freeLessonsConsumedCount,
      permanentlyUnlockedLessons: this.permanentlyUnlockedLessons,
      paidLessons: this.paidLessons
    };
  }

  /**
   * Create from JSON
   */
  static fromJSON(data) {
    return new User(data);
  }
}

module.exports = { User };

