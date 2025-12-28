# APTLEARN Interview Prep: Node.js + Express
## 75 Live Coding Questions for Full-Stack Development

---

## 📋 Overview

**Total Questions:** 75  
**Technology:** Node.js + Express  
**Interview Format:** Live coding, screen share  
**Time Range:** 5-45 minutes per question  
**Difficulty Levels:** 4 tiers (Junior → Lead)

---

## 🎯 Tier 1: Junior Level (20 questions)
**Target:** 0-2 years experience | Time: 5-15 min each

### 1. Hello World Endpoint ⭐
**Time:** 5-15 min  
**Tests:** Basic routing, GET endpoint

**Challenge:**
```javascript
// Create an Express endpoint for: Hello World Endpoint
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.json({ message: 'Hello World' });
});

module.exports = app;
```

---
### 2. GET Endpoint with Params ⭐
**Time:** 5-15 min  
**Tests:** Route parameters, query params

**Challenge:**
```javascript
// Create an Express endpoint for: GET Endpoint with Params
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 3. POST Endpoint with Body ⭐
**Time:** 5-15 min  
**Tests:** Request body, POST handling

**Challenge:**
```javascript
// Create an Express endpoint for: POST Endpoint with Body
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 4. PUT Endpoint ⭐
**Time:** 5-15 min  
**Tests:** Update operations, PUT method

**Challenge:**
```javascript
// Create an Express endpoint for: PUT Endpoint
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 5. DELETE Endpoint ⭐
**Time:** 5-15 min  
**Tests:** Delete operations, DELETE method

**Challenge:**
```javascript
// Create an Express endpoint for: DELETE Endpoint
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 6. Middleware Basics ⭐
**Time:** 5-15 min  
**Tests:** Middleware, request pipeline

**Challenge:**
```javascript
// Create an Express endpoint for: Middleware Basics
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 7. Error Handling Middleware ⭐
**Time:** 5-15 min  
**Tests:** Error handling, error responses

**Challenge:**
```javascript
// Create an Express endpoint for: Error Handling Middleware
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 8. Environment Variables ⭐
**Time:** 5-15 min  
**Tests:** Config management, env vars

**Challenge:**
```javascript
// Create an Express endpoint for: Environment Variables
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 9. CORS Setup ⭐
**Time:** 5-15 min  
**Tests:** Cross-origin requests, CORS

**Challenge:**
```javascript
// Create an Express endpoint for: CORS Setup
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 10. Request Validation ⭐
**Time:** 5-15 min  
**Tests:** Input validation, validation middleware

**Challenge:**
```javascript
// Create an Express endpoint for: Request Validation
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 11. Response Formatting ⭐
**Time:** 5-15 min  
**Tests:** Response structure, JSON responses

**Challenge:**
```javascript
// Create an Express endpoint for: Response Formatting
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 12. Query Parameters ⭐
**Time:** 5-15 min  
**Tests:** Query string parsing

**Challenge:**
```javascript
// Create an Express endpoint for: Query Parameters
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 13. Path Parameters ⭐
**Time:** 5-15 min  
**Tests:** Route parameters, dynamic routes

**Challenge:**
```javascript
// Create an Express endpoint for: Path Parameters
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 14. Request Body Parsing ⭐
**Time:** 5-15 min  
**Tests:** Body parsing, JSON parsing

**Challenge:**
```javascript
// Create an Express endpoint for: Request Body Parsing
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 15. Static File Serving ⭐
**Time:** 5-15 min  
**Tests:** File serving, static assets

**Challenge:**
```javascript
// Create an Express endpoint for: Static File Serving
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 16. Simple Logging ⭐
**Time:** 5-15 min  
**Tests:** Logging, console logging

**Challenge:**
```javascript
// Create an Express endpoint for: Simple Logging
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 17. Health Check Endpoint ⭐
**Time:** 5-15 min  
**Tests:** Health checks, monitoring

**Challenge:**
```javascript
// Create an Express endpoint for: Health Check Endpoint
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 18. Basic Authentication ⭐
**Time:** 5-15 min  
**Tests:** Auth basics, username/password

**Challenge:**
```javascript
// Create an Express endpoint for: Basic Authentication
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 19. Password Hashing ⭐
**Time:** 5-15 min  
**Tests:** Password security, hashing

**Challenge:**
```javascript
// Create an Express endpoint for: Password Hashing
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 20. JWT Token Creation ⭐
**Time:** 5-15 min  
**Tests:** JWT, token generation

**Challenge:**
```javascript
// Create an Express endpoint for: JWT Token Creation
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---

---

## 🎯 Tier 2: Mid-Level (25 questions)  
**Target:** 2-4 years experience | Time: 15-25 min each

### 21. Database Connection ⭐⭐
**Time:** 15-25 min  
**Tests:** DB connection, connection pooling

**Challenge:**
```javascript
// Create an Express endpoint for: Database Connection
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 22. CRUD Operations ⭐⭐
**Time:** 15-25 min  
**Tests:** Create, read, update, delete

**Challenge:**
```javascript
// Create an Express endpoint for: CRUD Operations
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 23. One-to-Many Relationships ⭐⭐
**Time:** 15-25 min  
**Tests:** Database relationships

**Challenge:**
```javascript
// Create an Express endpoint for: One-to-Many Relationships
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 24. Many-to-Many Relationships ⭐⭐
**Time:** 15-25 min  
**Tests:** Junction tables, relationships

**Challenge:**
```javascript
// Create an Express endpoint for: Many-to-Many Relationships
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 25. Database Transactions ⭐⭐
**Time:** 15-25 min  
**Tests:** Transactions, ACID

**Challenge:**
```javascript
// Create an Express endpoint for: Database Transactions
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 26. Query Optimization ⭐⭐
**Time:** 15-25 min  
**Tests:** SQL optimization, indexes

**Challenge:**
```javascript
// Create an Express endpoint for: Query Optimization
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 27. Pagination ⭐⭐
**Time:** 15-25 min  
**Tests:** Pagination, limit/offset

**Challenge:**
```javascript
// Create an Express endpoint for: Pagination
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 28. Filtering and Sorting ⭐⭐
**Time:** 15-25 min  
**Tests:** Data filtering, sorting

**Challenge:**
```javascript
// Create an Express endpoint for: Filtering and Sorting
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 29. Search Functionality ⭐⭐
**Time:** 15-25 min  
**Tests:** Search, full-text search

**Challenge:**
```javascript
// Create an Express endpoint for: Search Functionality
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 30. File Upload Handling ⭐⭐
**Time:** 15-25 min  
**Tests:** File uploads, multipart/form-data

**Challenge:**
```javascript
// Create an Express endpoint for: File Upload Handling
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 31. JWT Authentication ⭐⭐
**Time:** 15-25 min  
**Tests:** JWT, token validation

**Challenge:**
```javascript
// Create an Express endpoint for: JWT Authentication
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 32. Refresh Tokens ⭐⭐
**Time:** 15-25 min  
**Tests:** Token refresh, security

**Challenge:**
```javascript
// Create an Express endpoint for: Refresh Tokens
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 33. Role-Based Access Control ⭐⭐
**Time:** 15-25 min  
**Tests:** RBAC, permissions

**Challenge:**
```javascript
// Create an Express endpoint for: Role-Based Access Control
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 34. API Versioning ⭐⭐
**Time:** 15-25 min  
**Tests:** Versioning, backward compatibility

**Challenge:**
```javascript
// Create an Express endpoint for: API Versioning
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 35. Rate Limiting ⭐⭐
**Time:** 15-25 min  
**Tests:** Rate limiting, throttling

**Challenge:**
```javascript
// Create an Express endpoint for: Rate Limiting
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 36. Caching (Redis) ⭐⭐
**Time:** 15-25 min  
**Tests:** Caching, Redis integration

**Challenge:**
```javascript
// Create an Express endpoint for: Caching (Redis)
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 37. Session Management ⭐⭐
**Time:** 15-25 min  
**Tests:** Sessions, session storage

**Challenge:**
```javascript
// Create an Express endpoint for: Session Management
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 38. Cookie Handling ⭐⭐
**Time:** 15-25 min  
**Tests:** Cookies, secure cookies

**Challenge:**
```javascript
// Create an Express endpoint for: Cookie Handling
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 39. Email Sending ⭐⭐
**Time:** 15-25 min  
**Tests:** Email, SMTP

**Challenge:**
```javascript
// Create an Express endpoint for: Email Sending
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 40. Background Jobs ⭐⭐
**Time:** 15-25 min  
**Tests:** Job queues, async processing

**Challenge:**
```javascript
// Create an Express endpoint for: Background Jobs
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 41. Scheduled Tasks ⭐⭐
**Time:** 15-25 min  
**Tests:** Cron jobs, scheduled tasks

**Challenge:**
```javascript
// Create an Express endpoint for: Scheduled Tasks
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 42. WebSocket Server ⭐⭐
**Time:** 15-25 min  
**Tests:** WebSockets, real-time

**Challenge:**
```javascript
// Create an Express endpoint for: WebSocket Server
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 43. Real-Time Chat ⭐⭐
**Time:** 15-25 min  
**Tests:** Real-time communication

**Challenge:**
```javascript
// Create an Express endpoint for: Real-Time Chat
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 44. API Documentation ⭐⭐
**Time:** 15-25 min  
**Tests:** OpenAPI, Swagger

**Challenge:**
```javascript
// Create an Express endpoint for: API Documentation
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 45. Input Sanitization ⭐⭐
**Time:** 15-25 min  
**Tests:** Security, XSS prevention

**Challenge:**
```javascript
// Create an Express endpoint for: Input Sanitization
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---

---

## 🎯 Tier 3: Senior Level (20 questions)
**Target:** 4-6 years experience | Time: 25-35 min each

### 46. OAuth2 Implementation ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** OAuth2, authentication flows

**Challenge:**
```javascript
// Create an Express endpoint for: OAuth2 Implementation
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 47. Microservices Communication ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Service communication, APIs

**Challenge:**
```javascript
// Create an Express endpoint for: Microservices Communication
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 48. Message Queue (RabbitMQ/Kafka) ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Message queues, async messaging

**Challenge:**
```javascript
// Create an Express endpoint for: Message Queue (RabbitMQ/Kafka)
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 49. Event-Driven Architecture ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Events, event sourcing

**Challenge:**
```javascript
// Create an Express endpoint for: Event-Driven Architecture
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 50. CQRS Pattern ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Command Query Responsibility Segregation

**Challenge:**
```javascript
// Create an Express endpoint for: CQRS Pattern
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 51. Repository Pattern ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Data access, abstraction

**Challenge:**
```javascript
// Create an Express endpoint for: Repository Pattern
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 52. Unit Testing ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Unit tests, test coverage

**Challenge:**
```javascript
// Create an Express endpoint for: Unit Testing
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 53. Integration Testing ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Integration tests, test databases

**Challenge:**
```javascript
// Create an Express endpoint for: Integration Testing
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 54. Test Coverage ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Code coverage, testing metrics

**Challenge:**
```javascript
// Create an Express endpoint for: Test Coverage
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 55. Database Migrations ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Migrations, schema changes

**Challenge:**
```javascript
// Create an Express endpoint for: Database Migrations
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 56. Database Seeding ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Seed data, test data

**Challenge:**
```javascript
// Create an Express endpoint for: Database Seeding
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 57. Multi-Tenancy ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Multi-tenant architecture

**Challenge:**
```javascript
// Create an Express endpoint for: Multi-Tenancy
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 58. Soft Deletes ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Soft deletes, data retention

**Challenge:**
```javascript
// Create an Express endpoint for: Soft Deletes
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 59. Audit Logging ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Audit trails, logging

**Challenge:**
```javascript
// Create an Express endpoint for: Audit Logging
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 60. Request Throttling ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Throttling, rate limiting

**Challenge:**
```javascript
// Create an Express endpoint for: Request Throttling
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 61. API Gateway ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Gateway pattern, routing

**Challenge:**
```javascript
// Create an Express endpoint for: API Gateway
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 62. Service Discovery ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Service registry, discovery

**Challenge:**
```javascript
// Create an Express endpoint for: Service Discovery
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 63. Circuit Breaker Pattern ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Resilience, fault tolerance

**Challenge:**
```javascript
// Create an Express endpoint for: Circuit Breaker Pattern
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 64. Distributed Tracing ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Tracing, observability

**Challenge:**
```javascript
// Create an Express endpoint for: Distributed Tracing
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 65. Performance Monitoring ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** APM, monitoring

**Challenge:**
```javascript
// Create an Express endpoint for: Performance Monitoring
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---

---

## 🎯 Tier 4: Lead Level (10 questions)
**Target:** 6+ years experience | Time: 35-45 min each

### 66. System Design (URL Shortener) ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** System design, scalability

**Challenge:**
```javascript
// Create an Express endpoint for: System Design (URL Shortener)
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 67. System Design (Chat App) ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Real-time systems, WebSockets

**Challenge:**
```javascript
// Create an Express endpoint for: System Design (Chat App)
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 68. Database Sharding ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Sharding, horizontal scaling

**Challenge:**
```javascript
// Create an Express endpoint for: Database Sharding
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 69. Read Replicas ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Replication, read scaling

**Challenge:**
```javascript
// Create an Express endpoint for: Read Replicas
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 70. Load Balancing ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Load balancers, distribution

**Challenge:**
```javascript
// Create an Express endpoint for: Load Balancing
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 71. Horizontal Scaling ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Scaling, infrastructure

**Challenge:**
```javascript
// Create an Express endpoint for: Horizontal Scaling
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 72. Deployment Strategies ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Blue-green, canary deployments

**Challenge:**
```javascript
// Create an Express endpoint for: Deployment Strategies
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 73. Container Orchestration ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Kubernetes, Docker

**Challenge:**
```javascript
// Create an Express endpoint for: Container Orchestration
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 74. CI/CD Pipeline ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Continuous integration, deployment

**Challenge:**
```javascript
// Create an Express endpoint for: CI/CD Pipeline
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---
### 75. Security Best Practices ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Security, OWASP, vulnerabilities

**Challenge:**
```javascript
// Create an Express endpoint for: Security Best Practices
// Include proper error handling
// Use modern async/await syntax
```

**What interviewers look for:**
```javascript
const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {
  try {
    // Implementation
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

---

---

## 📊 Question Distribution

**By Category:**
- Fundamentals: 15 questions
- Intermediate Concepts: 20 questions  
- Advanced Patterns: 20 questions
- Architecture & Performance: 12 questions
- Real-world Scenarios: 8 questions

**By Type:**
- Component/Function Building: 30%
- State Management: 15%
- API/Backend Integration: 20%
- Testing & Quality: 10%
- Performance & Optimization: 10%
- Architecture & Design: 15%
