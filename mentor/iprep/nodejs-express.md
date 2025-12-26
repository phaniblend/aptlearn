# APTLEARN Interview Prep: Node.js / Express
## 55 Live Coding Questions for Backend Developers

---

## 📋 Overview

**Total Questions:** 55  
**Framework:** Node.js with Express  
**Interview Format:** Live coding, screen share  
**Time Range:** 5-40 minutes per question  
**Difficulty Levels:** 4 tiers (Junior → Lead)

---

## 🎯 Tier 1: Junior Level (12 questions)
**Target:** 0-2 years experience | Time: 5-15 min each

### 1. Hello World API ⭐
**Time:** 5 minutes  
**Tests:** Basic Express, routing

**Challenge:**
```javascript
// Create Express server that:
// - Listens on port 3000
// - GET / returns JSON: { message: "Hello World" }
// - Responds with 200 status code
```

**What interviewers look for:**
```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.status(200).json({ message: 'Hello World' });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

**Key points:**
- Express initialization
- Route definition
- JSON response
- Port listening

---

### 2. Route Parameters ⭐
**Time:** 8 minutes  
**Tests:** Params, routing

**Challenge:**
```javascript
// Create endpoint:
// GET /users/:id
// - Return user object with id
// - Example: /users/123 → { id: "123", message: "User found" }
```

**What interviewers look for:**
- `req.params` usage
- Parameter extraction
- Dynamic routing
- Response format

---

### 3. Query Parameters ⭐
**Time:** 10 minutes  
**Tests:** Query parsing

**Challenge:**
```javascript
// Create endpoint:
// GET /search?q=term&limit=10
// - Extract query params
// - Return them in response
// - Handle missing params with defaults
```

**What interviewers look for:**
- `req.query` usage
- Default values
- Query string parsing
- Parameter validation

---

### 4. POST Endpoint ⭐
**Time:** 10 minutes  
**Tests:** Body parsing, POST

**Challenge:**
```javascript
// Create endpoint:
// POST /users
// - Accept JSON body: { name, email }
// - Return created user with id
// - Use express.json() middleware
```

**What interviewers look for:**
```javascript
app.use(express.json());

app.post('/users', (req, res) => {
  const { name, email } = req.body;
  const user = {
    id: Date.now(),
    name,
    email
  };
  res.status(201).json(user);
});
```

**Key points:**
- Body parser middleware
- Request body access
- 201 Created status
- JSON response

---

### 5. Static JSON Data ⭐
**Time:** 5 minutes  
**Tests:** JSON response

**Challenge:**
```javascript
// Create endpoint:
// GET /products
// - Return array of products
// - Each product: { id, name, price }
// - At least 3 products
```

**What interviewers look for:**
- Array response
- Object structure
- Static data handling

---

### 6. Multiple Routes ⭐
**Time:** 10 minutes  
**Tests:** Route organization

**Challenge:**
```javascript
// Create these endpoints:
// GET /users → list of users
// GET /posts → list of posts
// GET /comments → list of comments
// - Each returns array of items
```

**What interviewers look for:**
- Multiple route definitions
- Consistent response format
- Code organization

---

### 7. HTTP Status Codes ⭐
**Time:** 10 minutes  
**Tests:** Status code knowledge

**Challenge:**
```javascript
// Create endpoint:
// GET /status/:code
// - Return appropriate status code
// - 200 for success
// - 404 for not found
// - 500 for error
// - Handle invalid codes
```

**What interviewers look for:**
- Status code usage
- `res.status()` method
- HTTP knowledge
- Error handling basics

---

### 8. Simple Middleware ⭐
**Time:** 12 minutes  
**Tests:** Middleware concept

**Challenge:**
```javascript
// Create logging middleware that:
// - Logs: [METHOD] PATH - TIMESTAMP
// - Runs on every request
// - Calls next() to continue
```

**What interviewers look for:**
```javascript
const logger = (req, res, next) => {
  console.log(`[${req.method}] ${req.path} - ${new Date().toISOString()}`);
  next();
};

app.use(logger);
```

**Key points:**
- Middleware function signature
- `next()` function
- `app.use()` for global middleware
- Request/response/next pattern

---

### 9. Error Response ⭐
**Time:** 10 minutes  
**Tests:** Error handling

**Challenge:**
```javascript
// Create 404 handler:
// - Catches all undefined routes
// - Returns: { error: "Not Found" }
// - Status: 404
// - Runs as last middleware
```

**What interviewers look for:**
```javascript
app.use((req, res) => {
  res.status(404).json({ error: 'Not Found' });
});
```

**Key points:**
- Catch-all route
- 404 handling
- Middleware order
- Error response format

---

### 10. Environment Variables ⭐
**Time:** 8 minutes  
**Tests:** dotenv, config

**Challenge:**
```javascript
// Setup environment variables:
// - Use dotenv package
// - Read PORT from .env
// - Default to 3000 if not set
// - Read API_KEY from .env
```

**What interviewers look for:**
```javascript
require('dotenv').config();

const PORT = process.env.PORT || 3000;
const API_KEY = process.env.API_KEY;

app.listen(PORT, () => {
  console.log(`Server on port ${PORT}`);
});
```

**Key points:**
- dotenv configuration
- `process.env` usage
- Default values
- Configuration management

---

### 11. CORS Setup ⭐
**Time:** 8 minutes  
**Tests:** CORS middleware

**Challenge:**
```javascript
// Enable CORS:
// - Use cors package
// - Allow all origins
// - Enable credentials
// - Allow specific headers
```

**What interviewers look for:**
```javascript
const cors = require('cors');

app.use(cors({
  origin: '*',
  credentials: true,
  allowedHeaders: ['Content-Type', 'Authorization']
}));
```

**Key points:**
- CORS middleware
- Configuration options
- Security implications
- Preflight requests

---

### 12. Request Validation ⭐
**Time:** 12 minutes  
**Tests:** Input validation

**Challenge:**
```javascript
// POST /users with validation:
// - name: required, min 2 chars
// - email: required, valid email format
// - Return 400 if validation fails
// - Return error messages
```

**What interviewers look for:**
```javascript
app.post('/users', (req, res) => {
  const { name, email } = req.body;
  const errors = [];

  if (!name || name.length < 2) {
    errors.push('Name must be at least 2 characters');
  }

  if (!email || !email.includes('@')) {
    errors.push('Valid email required');
  }

  if (errors.length > 0) {
    return res.status(400).json({ errors });
  }

  res.status(201).json({ name, email });
});
```

**Key points:**
- Input validation
- Error collection
- 400 Bad Request
- Validation messages

---

## 🎯 Tier 2: Mid-Level (20 questions)
**Target:** 2-4 years experience | Time: 15-25 min each

### 13. CRUD API (In-Memory) ⭐⭐
**Time:** 25-30 minutes  
**Tests:** REST principles, array manipulation

**Challenge:**
```javascript
// Build full CRUD for todos (in-memory array):
// GET /todos - list all
// GET /todos/:id - get one
// POST /todos - create (body: { title, completed })
// PUT /todos/:id - update
// DELETE /todos/:id - delete

// Requirements:
// - Proper status codes
// - Handle not found (404)
// - Validate input
// - Generate unique IDs
```

**What interviewers look for:**
```javascript
let todos = [];
let nextId = 1;

// GET all
app.get('/todos', (req, res) => {
  res.json(todos);
});

// GET one
app.get('/todos/:id', (req, res) => {
  const todo = todos.find(t => t.id === parseInt(req.params.id));
  if (!todo) {
    return res.status(404).json({ error: 'Todo not found' });
  }
  res.json(todo);
});

// POST create
app.post('/todos', (req, res) => {
  const { title, completed = false } = req.body;
  
  if (!title) {
    return res.status(400).json({ error: 'Title required' });
  }

  const todo = {
    id: nextId++,
    title,
    completed
  };
  todos.push(todo);
  res.status(201).json(todo);
});

// PUT update
app.put('/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = todos.findIndex(t => t.id === id);
  
  if (index === -1) {
    return res.status(404).json({ error: 'Todo not found' });
  }

  todos[index] = {
    ...todos[index],
    ...req.body,
    id // Keep original id
  };
  res.json(todos[index]);
});

// DELETE
app.delete('/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = todos.findIndex(t => t.id === id);
  
  if (index === -1) {
    return res.status(404).json({ error: 'Todo not found' });
  }

  todos.splice(index, 1);
  res.status(204).send();
});
```

**Key points:**
- REST conventions
- CRUD operations
- Array manipulation
- Error handling
- Status codes (200, 201, 204, 404)
- ID generation

**VERY common mid-level question**

---

### 14. Pagination ⭐⭐
**Time:** 15 minutes  
**Tests:** Array slicing, query params

**Challenge:**
```javascript
// GET /items?page=1&limit=10
// - Paginate results
// - Default: page=1, limit=10
// - Return: { data: [...], page, limit, total }
// - Handle out of range pages
```

**What interviewers look for:**
```javascript
app.get('/items', (req, res) => {
  const items = Array(100).fill(null).map((_, i) => ({ id: i + 1, name: `Item ${i + 1}` }));
  
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 10;
  
  const startIndex = (page - 1) * limit;
  const endIndex = startIndex + limit;
  
  const paginatedItems = items.slice(startIndex, endIndex);
  
  res.json({
    data: paginatedItems,
    page,
    limit,
    total: items.length,
    totalPages: Math.ceil(items.length / limit)
  });
});
```

**Key points:**
- Pagination math
- Query parameter parsing
- Metadata in response
- Edge cases

---

### 15. Search Endpoint ⭐⭐
**Time:** 15 minutes  
**Tests:** String filtering

**Challenge:**
```javascript
// GET /search?q=term
// - Search products by name
// - Case-insensitive
// - Return matching results
// - Handle empty search
```

**What interviewers look for:**
- String comparison
- Filter method
- Case handling
- Empty results

---

### 16. Sorting Endpoint ⭐⭐
**Time:** 18 minutes  
**Tests:** Array sorting, query params

**Challenge:**
```javascript
// GET /products?sort=price&order=asc
// - Sort by field (name, price)
// - Order: asc or desc
// - Default: sort by id, asc
// - Handle invalid sort fields
```

**What interviewers look for:**
```javascript
app.get('/products', (req, res) => {
  const { sort = 'id', order = 'asc' } = req.query;
  
  const validFields = ['id', 'name', 'price'];
  if (!validFields.includes(sort)) {
    return res.status(400).json({ error: 'Invalid sort field' });
  }

  const sorted = [...products].sort((a, b) => {
    if (order === 'asc') {
      return a[sort] > b[sort] ? 1 : -1;
    } else {
      return a[sort] < b[sort] ? 1 : -1;
    }
  });

  res.json(sorted);
});
```

**Key points:**
- Sorting logic
- Query parameter validation
- Ascending/descending
- Array spread (immutability)

---

### 17. Error Handling Middleware ⭐⭐
**Time:** 15 minutes  
**Tests:** Error middleware pattern

**Challenge:**
```javascript
// Create centralized error handler:
// - Catches all errors
// - Logs error details
// - Returns consistent error format
// - Different handling for dev/prod
```

**What interviewers look for:**
```javascript
// Error middleware (4 params!)
app.use((err, req, res, next) => {
  console.error(err.stack);

  const status = err.status || 500;
  const message = err.message || 'Internal Server Error';

  res.status(status).json({
    error: {
      message,
      ...(process.env.NODE_ENV === 'development' && { stack: err.stack })
    }
  });
});

// Usage in routes:
app.get('/error-test', (req, res, next) => {
  const error = new Error('Something went wrong');
  error.status = 400;
  next(error); // Pass to error handler
});
```

**Key points:**
- 4-parameter signature
- Error logging
- Environment-based responses
- Consistent format
- `next(error)` pattern

---

### 18. Authentication Middleware ⭐⭐
**Time:** 15 minutes  
**Tests:** Middleware, headers

**Challenge:**
```javascript
// Create auth middleware:
// - Check for API key in header
// - Header: Authorization: Bearer {key}
// - Valid key: "secret123"
// - Return 401 if missing/invalid
// - Attach user to req object
```

**What interviewers look for:**
```javascript
const authenticate = (req, res, next) => {
  const authHeader = req.headers.authorization;
  
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Unauthorized' });
  }

  const token = authHeader.split(' ')[1];
  
  if (token !== 'secret123') {
    return res.status(401).json({ error: 'Invalid token' });
  }

  req.user = { id: 1, name: 'Test User' };
  next();
};

// Protected route
app.get('/protected', authenticate, (req, res) => {
  res.json({ message: 'Access granted', user: req.user });
});
```

**Key points:**
- Header parsing
- Bearer token pattern
- 401 Unauthorized
- Request augmentation
- Middleware chaining

---

### 19. Rate Limiting ⭐⭐
**Time:** 20 minutes  
**Tests:** Rate limiting, middleware

**Challenge:**
```javascript
// Implement basic rate limiting:
// - Max 5 requests per minute per IP
// - Return 429 Too Many Requests when exceeded
// - Reset after 1 minute
// - Track by IP address
```

**What interviewers look for:**
```javascript
const rateLimit = {};

const rateLimiter = (req, res, next) => {
  const ip = req.ip;
  const now = Date.now();
  const windowMs = 60 * 1000; // 1 minute
  const maxRequests = 5;

  if (!rateLimit[ip]) {
    rateLimit[ip] = [];
  }

  // Remove old requests outside window
  rateLimit[ip] = rateLimit[ip].filter(time => now - time < windowMs);

  if (rateLimit[ip].length >= maxRequests) {
    return res.status(429).json({ error: 'Too many requests' });
  }

  rateLimit[ip].push(now);
  next();
};

app.use(rateLimiter);
```

**Key points:**
- Rate limiting concept
- IP tracking
- Time windows
- 429 status code
- Memory cleanup

**Alternative:** Use `express-rate-limit` package

---

### 20. File Upload ⭐⭐
**Time:** 20 minutes  
**Tests:** Multer, file handling

**Challenge:**
```javascript
// POST /upload
// - Accept file upload
// - Use multer middleware
// - Save to /uploads folder
// - Return file info
// - Validate file type (images only)
// - Max size: 5MB
```

**What interviewers look for:**
```javascript
const multer = require('multer');
const path = require('path');

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + path.extname(file.originalname));
  }
});

const upload = multer({
  storage,
  limits: { fileSize: 5 * 1024 * 1024 }, // 5MB
  fileFilter: (req, file, cb) => {
    const allowedTypes = /jpeg|jpg|png|gif/;
    const extname = allowedTypes.test(path.extname(file.originalname).toLowerCase());
    const mimetype = allowedTypes.test(file.mimetype);
    
    if (extname && mimetype) {
      cb(null, true);
    } else {
      cb(new Error('Only images allowed'));
    }
  }
});

app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }

  res.json({
    message: 'File uploaded',
    file: {
      filename: req.file.filename,
      size: req.file.size,
      path: req.file.path
    }
  });
});
```

**Key points:**
- Multer configuration
- Storage strategy
- File validation
- Size limits
- Error handling

---

### 21. CSV Export ⭐⭐
**Time:** 15 minutes  
**Tests:** CSV generation, streaming

**Challenge:**
```javascript
// GET /export/users
// - Export users as CSV
// - Headers: id, name, email
// - Proper CSV format
// - Set Content-Type and Content-Disposition
```

**What interviewers look for:**
```javascript
app.get('/export/users', (req, res) => {
  const users = [
    { id: 1, name: 'John', email: 'john@example.com' },
    { id: 2, name: 'Jane', email: 'jane@example.com' }
  ];

  const csv = [
    ['id', 'name', 'email'], // Header
    ...users.map(u => [u.id, u.name, u.email])
  ].map(row => row.join(',')).join('\n');

  res.setHeader('Content-Type', 'text/csv');
  res.setHeader('Content-Disposition', 'attachment; filename=users.csv');
  res.send(csv);
});
```

**Key points:**
- CSV format
- Headers configuration
- File download
- Data transformation

---

### 22. Request Logging ⭐⭐
**Time:** 10 minutes  
**Tests:** Logging middleware

**Challenge:**
```javascript
// Add morgan logging:
// - Log all requests
// - Use 'combined' format in production
// - Use 'dev' format in development
// - Write logs to file
```

**What interviewers look for:**
```javascript
const morgan = require('morgan');
const fs = require('fs');
const path = require('path');

// Create write stream
const accessLogStream = fs.createWriteStream(
  path.join(__dirname, 'access.log'),
  { flags: 'a' }
);

// Setup morgan
const format = process.env.NODE_ENV === 'production' ? 'combined' : 'dev';

app.use(morgan(format, {
  stream: accessLogStream
}));
```

**Key points:**
- Morgan middleware
- Format selection
- File streaming
- Environment config

---

### 23. Input Sanitization ⭐⭐
**Time:** 15 minutes  
**Tests:** Security, validation

**Challenge:**
```javascript
// POST /comment
// - Accept comment text
// - Sanitize HTML tags
// - Trim whitespace
// - Max 500 characters
// - Prevent XSS
```

**What interviewers look for:**
```javascript
const sanitizeHtml = require('sanitize-html');

app.post('/comment', (req, res) => {
  let { text } = req.body;

  // Sanitize
  text = sanitizeHtml(text, {
    allowedTags: [], // No HTML
    allowedAttributes: {}
  });

  // Trim
  text = text.trim();

  // Length check
  if (text.length > 500) {
    return res.status(400).json({ error: 'Comment too long' });
  }

  if (text.length === 0) {
    return res.status(400).json({ error: 'Comment required' });
  }

  res.json({ comment: text });
});
```

**Key points:**
- Input sanitization
- XSS prevention
- Validation
- Security awareness

---

### 24. JWT Token Generation ⭐⭐
**Time:** 20 minutes  
**Tests:** JWT, authentication

**Challenge:**
```javascript
// POST /login
// - Accept username, password
// - Validate credentials
// - Generate JWT token
// - Return token in response
```

**What interviewers look for:**
```javascript
const jwt = require('jsonwebtoken');

const SECRET = process.env.JWT_SECRET || 'secret';

app.post('/login', (req, res) => {
  const { username, password } = req.body;

  // Simple validation (in real app, check database)
  if (username === 'admin' && password === 'password') {
    const token = jwt.sign(
      { id: 1, username },
      SECRET,
      { expiresIn: '1h' }
    );

    res.json({ token });
  } else {
    res.status(401).json({ error: 'Invalid credentials' });
  }
});
```

**Key points:**
- JWT creation
- Payload structure
- Expiration
- Secret management

---

### 25. JWT Verification ⭐⭐
**Time:** 20 minutes  
**Tests:** JWT validation, protected routes

**Challenge:**
```javascript
// Create middleware to verify JWT:
// - Extract token from Authorization header
// - Verify token
// - Attach decoded data to req
// - Protect routes with middleware
```

**What interviewers look for:**
```javascript
const jwt = require('jsonwebtoken');

const verifyToken = (req, res, next) => {
  const authHeader = req.headers.authorization;

  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'No token provided' });
  }

  const token = authHeader.split(' ')[1];

  try {
    const decoded = jwt.verify(token, SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    res.status(401).json({ error: 'Invalid token' });
  }
};

// Protected route
app.get('/profile', verifyToken, (req, res) => {
  res.json({ user: req.user });
});
```

**Key points:**
- JWT verification
- Error handling
- Middleware pattern
- Protected routes

---

### 26. Password Hashing ⭐⭐
**Time:** 15 minutes  
**Tests:** Bcrypt, security

**Challenge:**
```javascript
// POST /register
// - Accept username, password
// - Hash password with bcrypt
// - Store user (in-memory)
// - Return success message
```

**What interviewers look for:**
```javascript
const bcrypt = require('bcrypt');

const users = [];

app.post('/register', async (req, res) => {
  const { username, password } = req.body;

  // Check if user exists
  if (users.find(u => u.username === username)) {
    return res.status(400).json({ error: 'User already exists' });
  }

  // Hash password
  const saltRounds = 10;
  const hashedPassword = await bcrypt.hash(password, saltRounds);

  // Save user
  users.push({
    id: users.length + 1,
    username,
    password: hashedPassword
  });

  res.status(201).json({ message: 'User registered' });
});

// Login comparison
app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const user = users.find(u => u.username === username);

  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  const match = await bcrypt.compare(password, user.password);

  if (match) {
    res.json({ message: 'Login successful' });
  } else {
    res.status(401).json({ error: 'Invalid credentials' });
  }
});
```

**Key points:**
- Bcrypt hashing
- Salt rounds
- Async operations
- Password comparison
- Security best practices

---

### 27-32. Additional Mid-Level Questions

**27. Session Management** (20 min)
- express-session
- Session store
- Cookie configuration

**28. Cookie Handling** (15 min)
- cookie-parser
- Signed cookies
- Cookie options

**29. Email Validation** (10 min)
- Regex patterns
- Validation library
- Error messages

**30. Response Caching** (20 min)
- Cache-Control headers
- In-memory cache
- Cache invalidation

**31. WebSocket Connection** (25 min)
- Socket.io setup
- Event handling
- Rooms and namespaces

**32. Streaming Response** (20 min)
- fs.createReadStream
- Pipe to response
- Large file handling

---

## 🎯 Tier 3: Senior Level (15 questions)
**Target:** 4-6 years experience | Time: 25-35 min each

### 33. Database CRUD (MongoDB) ⭐⭐⭐
**Time:** 30-35 minutes  
**Tests:** MongoDB, Mongoose schemas

**Challenge:**
```javascript
// Build CRUD API with MongoDB:
// - Connect to MongoDB
// - Define Mongoose schema for User
// - Implement all CRUD operations
// - Handle database errors
// - Use async/await
```

**What interviewers look for:**
```javascript
const mongoose = require('mongoose');

// Connect
mongoose.connect('mongodb://localhost/myapp', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// Schema
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  age: Number,
  createdAt: { type: Date, default: Date.now }
});

const User = mongoose.model('User', userSchema);

// CREATE
app.post('/users', async (req, res) => {
  try {
    const user = new User(req.body);
    await user.save();
    res.status(201).json(user);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// READ all
app.get('/users', async (req, res) => {
  try {
    const users = await User.find();
    res.json(users);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// READ one
app.get('/users/:id', async (req, res) => {
  try {
    const user = await User.findById(req.params.id);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    res.json(user);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// UPDATE
app.put('/users/:id', async (req, res) => {
  try {
    const user = await User.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true, runValidators: true }
    );
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    res.json(user);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// DELETE
app.delete('/users/:id', async (req, res) => {
  try {
    const user = await User.findByIdAndDelete(req.params.id);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    res.status(204).send();
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
```

**Key points:**
- Mongoose connection
- Schema definition
- CRUD with async/await
- Error handling
- Validation
- Query methods

**CRITICAL senior backend question**

---

### 34-47. Additional Senior Questions

**34. Database CRUD (PostgreSQL)** (30-35 min)
- pg or Sequelize
- SQL queries
- Prepared statements

**35. Database Relations** (30 min)
- 1-to-many relationships
- Joins
- Populate/include

**36. Transaction Handling** (25 min)
- Begin/commit/rollback
- Atomic operations
- Error recovery

**37. Database Migration** (20 min)
- Migration files
- Schema changes
- Version control

**38. Full Authentication System** (40 min)
- Register, login, logout
- Refresh tokens
- Password reset

**39. OAuth Integration** (35 min)
- Passport.js
- Google/GitHub OAuth
- Callback handling

**40. API Versioning** (20 min)
- /api/v1 vs /api/v2
- Version strategies
- Deprecation

**41. Request Throttling** (25 min)
- Redis-based rate limiting
- Per-user limits
- Sliding windows

**42. Image Processing** (25 min)
- Sharp library
- Resize images
- Format conversion

**43. Job Queue** (30 min)
- Bull/BullMQ
- Redis connection
- Worker processes

**44. Scheduled Tasks** (20 min)
- node-cron
- Cron expressions
- Background jobs

**45. GraphQL Server** (30 min)
- Apollo Server
- Schema definition
- Resolvers

**46. Microservices Communication** (30 min)
- HTTP between services
- Service discovery
- Error handling

**47. Event Emitters** (20 min)
- EventEmitter class
- Custom events
- Pub/sub pattern

---

## 🎯 Tier 4: Lead Level (8 questions)
**Target:** 6+ years experience | Time: 30-40 min each

### 48. API Gateway Pattern ⭐⭐⭐⭐
**Time:** 35 minutes  
**Tests:** Gateway pattern, routing

**Challenge:**
```javascript
// Build API gateway that:
// - Routes to multiple backend services
// - /users → users-service
// - /products → products-service
// - Add authentication
// - Add logging
// - Handle service failures
```

**Key concepts:**
- Proxy requests
- Service routing
- Centralized auth
- Load balancing
- Circuit breaker (bonus)

---

### 49-55. Additional Lead Questions

**49. Circuit Breaker** (30 min)
- Opossum library
- Failure thresholds
- Fallback responses

**50. Distributed Tracing** (25 min)
- Request ID propagation
- OpenTelemetry
- Trace context

**51. Custom ORM/Query Builder** (40 min)
- SQL generation
- Query chaining
- Type safety

**52. Streaming Data Processing** (30 min)
- Stream API
- Transform streams
- Memory efficiency

**53. WebSocket Chat Server** (40 min)
- Socket.io rooms
- Private messaging
- Online status

**54. API Documentation (Swagger)** (25 min)
- Swagger/OpenAPI
- Auto-generation
- Interactive docs

**55. Performance Monitoring** (20 min)
- APM tools
- Metrics collection
- Performance profiling

---

## 📊 Most Common Backend Questions

### Top 10 You'll See:
1. **CRUD API** - 100%
2. **Authentication** (JWT/sessions) - 90%
3. **Database integration** - 85%
4. **Error handling** - 80%
5. **File upload** - 70%
6. **Middleware** - 90%
7. **Validation** - 80%
8. **Pagination** - 60%
9. **CORS setup** - 70%
10. **Environment config** - 75%

---

## 💡 Backend Interview Tips

### DO:
✅ Handle errors properly
✅ Use async/await consistently
✅ Validate all inputs
✅ Think about security
✅ Consider scalability

### DON'T:
❌ Store passwords in plain text
❌ Ignore SQL injection
❌ Skip input validation
❌ Use synchronous file operations
❌ Forget error handling

---

**Total Questions:** 55  
**Practice Time:** 30-35 hours  
**Success Rate:** 80%+ with practice

Good luck! 🚀
