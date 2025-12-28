# INPACT LEARN - Architecture Documentation

## Overview

**INPACT LEARN** (Interview Prep by Learning Algorithms & Coding Tests) is a freemium learning platform with transparent pricing and ethical access control.

## System Architecture

### Backend Structure

```
src/
├── server.js              # Main Express server
├── user/                  # User module
│   ├── user-model.js      # User entity and business logic
│   ├── user-storage.js    # File-based user storage
│   └── user-router.js     # User API endpoints
├── mentor/                # Lesson engine
│   ├── lesson-engine.js   # Lesson loading
│   ├── lesson-loader.js   # Lesson utilities
│   └── mentor-router.js   # Lesson API endpoints
└── ide/                   # IDE functionality
```

### Frontend Structure

```
ide-frontend/
├── index.html             # Landing page
├── algos.html            # Algorithm lessons list
├── interview-prep.html     # Coding challenges list
├── dashboard.html         # User dashboard
├── learn.html             # Interactive lesson viewer
└── assets/
    ├── styles.css         # Enterprise Neon theme
    ├── app.js             # Main app logic
    ├── algos.js           # Algorithms page logic
    ├── interview-prep.js  # Interview prep logic
    ├── dashboard.js       # Dashboard logic
    └── learn.js           # Lesson viewer logic
```

## Freemium Access Rules

### Guest Users
- **5 free lessons** (AL or CL) without registration
- On 6th lesson attempt → Registration prompt

### Registered Users (Free Account)
- **First 10 lessons accessed are FREE FOR LIFE**
- Lessons #1–#10 are permanently unlocked
- No expiry, no limits on these 10 lessons

### Paid Access
- From lesson #11 onward: **$2 per lesson**
- **One-time payment** → Lifetime access
- No subscriptions, no bundles, no hidden limits

## User Entity Schema

```javascript
{
  userId: string,
  authProvider: 'guest' | 'email' | 'google' | 'github',
  email: string | null,
  createdAt: ISO8601,
  registrationDate: ISO8601 | null,
  
  // Tracking
  lessonsVisited: string[],           // All lesson IDs visited
  lessonsCompleted: string[],          // Completed lesson IDs
  freeLessonsConsumedCount: number,    // Count of free lessons used
  permanentlyUnlockedLessons: string[], // First 10 lessons (free for life)
  paidLessons: [{                      // Purchased lessons
    lessonId: string,
    purchasedAt: ISO8601,
    amount: number
  }]
}
```

## API Endpoints

### User Endpoints (`/api/user`)

- `GET /me` - Get current user (creates guest if none)
- `POST /register` - Register new user
- `GET /access/:lessonId` - Check lesson access
- `POST /visit/:lessonId` - Record lesson visit
- `POST /complete/:lessonId` - Mark lesson complete
- `POST /purchase/:lessonId` - Purchase lesson access
- `GET /dashboard` - Get user dashboard data
- `POST /logout` - Logout user

### Mentor Endpoints (`/api/mentor`)

- `GET /lessons` - List all lessons
- `POST /start` - Start a lesson
- `POST /next` - Advance lesson step

## Access Control Logic

### `canAccessLesson(lessonId)`

Returns:
```javascript
{
  canAccess: boolean,
  reason: 'paid' | 'free_for_life' | 'guest_free' | 'guest_limit_reached' | 'payment_required',
  requiresPayment: boolean,
  requiresRegistration: boolean,
  price?: number
}
```

### Flow

1. **Check if paid** → Always accessible
2. **Check if permanently unlocked** → Always accessible
3. **Guest user** → Check if < 5 lessons visited
4. **Registered user** → Check if < 10 free lessons consumed
5. **Otherwise** → Requires payment ($2)

## Frontend Pages

### Landing Page (`/`)
- Hero section with transparent pricing
- Features showcase
- Statistics
- Clear call-to-action

### Algorithms Page (`/algos`)
- Filterable list of algorithm lessons
- Access badges (FREE, OWNED, $2.00, LOCKED)
- Access gates for locked lessons

### Interview Prep Page (`/interview-prep`)
- Technology tabs (React, Angular, Vue, etc.)
- Filterable coding challenges
- Same access control as algorithms

### Dashboard (`/dashboard`)
- Learning progress stats
- Free lessons remaining
- Permanently unlocked lessons list
- Purchased lessons list
- Pricing model explanation

### Lesson Viewer (`/learn/:lessonId`)
- Interactive step-by-step lesson
- Access check before loading
- Progress tracking
- Completion recording

## Design Theme

**Enterprise Neon Theme**
- Primary accent: Neon Green (`#39ff14`)
- Base: Black (`#000000`) / Off-white (`#f5f5f5`)
- Strong grid-based layout
- Bold typography
- Neon used only for emphasis

**UI Principles**
- Serious, transparent, engineer-first
- Calm confidence (no gimmicks)
- Clear pricing display everywhere
- No dark patterns

## Data Storage

### Users
- Location: `data/users/users.json`
- Format: JSON object keyed by userId
- In-memory cache for performance

### Lessons
- Location: `mentor/lessons/*.json` (Algorithm lessons)
- Location: `mentor/lessonGen/react/*.json` (React JS)
- Location: `mentor/lessonGen/react-typescript/*.json` (React TS)

## Session Management

- Uses Express sessions (cookie-based)
- Session ID stored in cookie `apt_sid`
- In-memory session store (can be upgraded to Redis)

## Payment Integration

**Current Status**: Placeholder implementation
- Purchase endpoint records payment
- In production, integrate with Stripe/PayPal
- Verify payment before unlocking lesson

## Security Considerations

1. **Session Security**
   - Secure cookies in production
   - HTTPS required for auth

2. **Payment Security**
   - Never store payment details
   - Use payment provider webhooks
   - Verify payments server-side

3. **Access Control**
   - All access checks server-side
   - Client-side checks are for UI only
   - Server validates on every lesson access

## Future Enhancements

1. **Authentication**
   - OAuth integration (Google, GitHub)
   - Email verification
   - Password reset

2. **Payment**
   - Stripe integration
   - Payment webhooks
   - Receipt generation

3. **Features**
   - Progress analytics
   - Learning paths
   - Certificates
   - Community features

## Development

### Start Server
```bash
cd C:\INPACT\aptlearn
node src/server.js
```

### Access
- Frontend: http://localhost:5000
- API: http://localhost:5000/api

### Testing
- Guest access: Start without registration
- Free lessons: Register and access first 10
- Paid lessons: Access 11th lesson triggers payment

## Notes

- All pricing rules are transparent and displayed
- No hidden fees or subscriptions
- One-time payments for lifetime access
- Ethical freemium model

