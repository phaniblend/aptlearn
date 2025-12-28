# APTLEARN Interview Prep: NestJS (TypeScript)
## 75 Live Coding Questions for Full-Stack Development

---

## 📋 Overview

**Total Questions:** 75  
**Technology:** NestJS (TypeScript)  
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
```typescript
// Create a NestJS controller/service for: Hello World Endpoint
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 2. GET Endpoint with Params ⭐
**Time:** 5-15 min  
**Tests:** Route parameters, query params

**Challenge:**
```typescript
// Create a NestJS controller/service for: GET Endpoint with Params
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 3. POST Endpoint with Body ⭐
**Time:** 5-15 min  
**Tests:** Request body, POST handling

**Challenge:**
```typescript
// Create a NestJS controller/service for: POST Endpoint with Body
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 4. PUT Endpoint ⭐
**Time:** 5-15 min  
**Tests:** Update operations, PUT method

**Challenge:**
```typescript
// Create a NestJS controller/service for: PUT Endpoint
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 5. DELETE Endpoint ⭐
**Time:** 5-15 min  
**Tests:** Delete operations, DELETE method

**Challenge:**
```typescript
// Create a NestJS controller/service for: DELETE Endpoint
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 6. Middleware Basics ⭐
**Time:** 5-15 min  
**Tests:** Middleware, request pipeline

**Challenge:**
```typescript
// Create a NestJS controller/service for: Middleware Basics
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 7. Error Handling Middleware ⭐
**Time:** 5-15 min  
**Tests:** Error handling, error responses

**Challenge:**
```typescript
// Create a NestJS controller/service for: Error Handling Middleware
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 8. Environment Variables ⭐
**Time:** 5-15 min  
**Tests:** Config management, env vars

**Challenge:**
```typescript
// Create a NestJS controller/service for: Environment Variables
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 9. CORS Setup ⭐
**Time:** 5-15 min  
**Tests:** Cross-origin requests, CORS

**Challenge:**
```typescript
// Create a NestJS controller/service for: CORS Setup
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 10. Request Validation ⭐
**Time:** 5-15 min  
**Tests:** Input validation, validation middleware

**Challenge:**
```typescript
// Create a NestJS controller/service for: Request Validation
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 11. Response Formatting ⭐
**Time:** 5-15 min  
**Tests:** Response structure, JSON responses

**Challenge:**
```typescript
// Create a NestJS controller/service for: Response Formatting
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 12. Query Parameters ⭐
**Time:** 5-15 min  
**Tests:** Query string parsing

**Challenge:**
```typescript
// Create a NestJS controller/service for: Query Parameters
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 13. Path Parameters ⭐
**Time:** 5-15 min  
**Tests:** Route parameters, dynamic routes

**Challenge:**
```typescript
// Create a NestJS controller/service for: Path Parameters
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 14. Request Body Parsing ⭐
**Time:** 5-15 min  
**Tests:** Body parsing, JSON parsing

**Challenge:**
```typescript
// Create a NestJS controller/service for: Request Body Parsing
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 15. Static File Serving ⭐
**Time:** 5-15 min  
**Tests:** File serving, static assets

**Challenge:**
```typescript
// Create a NestJS controller/service for: Static File Serving
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 16. Simple Logging ⭐
**Time:** 5-15 min  
**Tests:** Logging, console logging

**Challenge:**
```typescript
// Create a NestJS controller/service for: Simple Logging
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 17. Health Check Endpoint ⭐
**Time:** 5-15 min  
**Tests:** Health checks, monitoring

**Challenge:**
```typescript
// Create a NestJS controller/service for: Health Check Endpoint
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 18. Basic Authentication ⭐
**Time:** 5-15 min  
**Tests:** Auth basics, username/password

**Challenge:**
```typescript
// Create a NestJS controller/service for: Basic Authentication
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 19. Password Hashing ⭐
**Time:** 5-15 min  
**Tests:** Password security, hashing

**Challenge:**
```typescript
// Create a NestJS controller/service for: Password Hashing
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 20. JWT Token Creation ⭐
**Time:** 5-15 min  
**Tests:** JWT, token generation

**Challenge:**
```typescript
// Create a NestJS controller/service for: JWT Token Creation
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---

---

## 🎯 Tier 2: Mid-Level (25 questions)  
**Target:** 2-4 years experience | Time: 15-25 min each

### 21. Database Connection ⭐⭐
**Time:** 15-25 min  
**Tests:** DB connection, connection pooling

**Challenge:**
```typescript
// Create a NestJS controller/service for: Database Connection
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 22. CRUD Operations ⭐⭐
**Time:** 15-25 min  
**Tests:** Create, read, update, delete

**Challenge:**
```typescript
// Create a NestJS controller/service for: CRUD Operations
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 23. One-to-Many Relationships ⭐⭐
**Time:** 15-25 min  
**Tests:** Database relationships

**Challenge:**
```typescript
// Create a NestJS controller/service for: One-to-Many Relationships
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 24. Many-to-Many Relationships ⭐⭐
**Time:** 15-25 min  
**Tests:** Junction tables, relationships

**Challenge:**
```typescript
// Create a NestJS controller/service for: Many-to-Many Relationships
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 25. Database Transactions ⭐⭐
**Time:** 15-25 min  
**Tests:** Transactions, ACID

**Challenge:**
```typescript
// Create a NestJS controller/service for: Database Transactions
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 26. Query Optimization ⭐⭐
**Time:** 15-25 min  
**Tests:** SQL optimization, indexes

**Challenge:**
```typescript
// Create a NestJS controller/service for: Query Optimization
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 27. Pagination ⭐⭐
**Time:** 15-25 min  
**Tests:** Pagination, limit/offset

**Challenge:**
```typescript
// Create a NestJS controller/service for: Pagination
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 28. Filtering and Sorting ⭐⭐
**Time:** 15-25 min  
**Tests:** Data filtering, sorting

**Challenge:**
```typescript
// Create a NestJS controller/service for: Filtering and Sorting
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 29. Search Functionality ⭐⭐
**Time:** 15-25 min  
**Tests:** Search, full-text search

**Challenge:**
```typescript
// Create a NestJS controller/service for: Search Functionality
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 30. File Upload Handling ⭐⭐
**Time:** 15-25 min  
**Tests:** File uploads, multipart/form-data

**Challenge:**
```typescript
// Create a NestJS controller/service for: File Upload Handling
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 31. JWT Authentication ⭐⭐
**Time:** 15-25 min  
**Tests:** JWT, token validation

**Challenge:**
```typescript
// Create a NestJS controller/service for: JWT Authentication
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 32. Refresh Tokens ⭐⭐
**Time:** 15-25 min  
**Tests:** Token refresh, security

**Challenge:**
```typescript
// Create a NestJS controller/service for: Refresh Tokens
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 33. Role-Based Access Control ⭐⭐
**Time:** 15-25 min  
**Tests:** RBAC, permissions

**Challenge:**
```typescript
// Create a NestJS controller/service for: Role-Based Access Control
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 34. API Versioning ⭐⭐
**Time:** 15-25 min  
**Tests:** Versioning, backward compatibility

**Challenge:**
```typescript
// Create a NestJS controller/service for: API Versioning
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 35. Rate Limiting ⭐⭐
**Time:** 15-25 min  
**Tests:** Rate limiting, throttling

**Challenge:**
```typescript
// Create a NestJS controller/service for: Rate Limiting
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 36. Caching (Redis) ⭐⭐
**Time:** 15-25 min  
**Tests:** Caching, Redis integration

**Challenge:**
```typescript
// Create a NestJS controller/service for: Caching (Redis)
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 37. Session Management ⭐⭐
**Time:** 15-25 min  
**Tests:** Sessions, session storage

**Challenge:**
```typescript
// Create a NestJS controller/service for: Session Management
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 38. Cookie Handling ⭐⭐
**Time:** 15-25 min  
**Tests:** Cookies, secure cookies

**Challenge:**
```typescript
// Create a NestJS controller/service for: Cookie Handling
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 39. Email Sending ⭐⭐
**Time:** 15-25 min  
**Tests:** Email, SMTP

**Challenge:**
```typescript
// Create a NestJS controller/service for: Email Sending
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 40. Background Jobs ⭐⭐
**Time:** 15-25 min  
**Tests:** Job queues, async processing

**Challenge:**
```typescript
// Create a NestJS controller/service for: Background Jobs
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 41. Scheduled Tasks ⭐⭐
**Time:** 15-25 min  
**Tests:** Cron jobs, scheduled tasks

**Challenge:**
```typescript
// Create a NestJS controller/service for: Scheduled Tasks
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 42. WebSocket Server ⭐⭐
**Time:** 15-25 min  
**Tests:** WebSockets, real-time

**Challenge:**
```typescript
// Create a NestJS controller/service for: WebSocket Server
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 43. Real-Time Chat ⭐⭐
**Time:** 15-25 min  
**Tests:** Real-time communication

**Challenge:**
```typescript
// Create a NestJS controller/service for: Real-Time Chat
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 44. API Documentation ⭐⭐
**Time:** 15-25 min  
**Tests:** OpenAPI, Swagger

**Challenge:**
```typescript
// Create a NestJS controller/service for: API Documentation
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 45. Input Sanitization ⭐⭐
**Time:** 15-25 min  
**Tests:** Security, XSS prevention

**Challenge:**
```typescript
// Create a NestJS controller/service for: Input Sanitization
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---

---

## 🎯 Tier 3: Senior Level (20 questions)
**Target:** 4-6 years experience | Time: 25-35 min each

### 46. OAuth2 Implementation ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** OAuth2, authentication flows

**Challenge:**
```typescript
// Create a NestJS controller/service for: OAuth2 Implementation
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 47. Microservices Communication ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Service communication, APIs

**Challenge:**
```typescript
// Create a NestJS controller/service for: Microservices Communication
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 48. Message Queue (RabbitMQ/Kafka) ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Message queues, async messaging

**Challenge:**
```typescript
// Create a NestJS controller/service for: Message Queue (RabbitMQ/Kafka)
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 49. Event-Driven Architecture ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Events, event sourcing

**Challenge:**
```typescript
// Create a NestJS controller/service for: Event-Driven Architecture
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 50. CQRS Pattern ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Command Query Responsibility Segregation

**Challenge:**
```typescript
// Create a NestJS controller/service for: CQRS Pattern
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 51. Repository Pattern ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Data access, abstraction

**Challenge:**
```typescript
// Create a NestJS controller/service for: Repository Pattern
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 52. Unit Testing ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Unit tests, test coverage

**Challenge:**
```typescript
// Create a NestJS controller/service for: Unit Testing
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 53. Integration Testing ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Integration tests, test databases

**Challenge:**
```typescript
// Create a NestJS controller/service for: Integration Testing
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 54. Test Coverage ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Code coverage, testing metrics

**Challenge:**
```typescript
// Create a NestJS controller/service for: Test Coverage
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 55. Database Migrations ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Migrations, schema changes

**Challenge:**
```typescript
// Create a NestJS controller/service for: Database Migrations
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 56. Database Seeding ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Seed data, test data

**Challenge:**
```typescript
// Create a NestJS controller/service for: Database Seeding
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 57. Multi-Tenancy ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Multi-tenant architecture

**Challenge:**
```typescript
// Create a NestJS controller/service for: Multi-Tenancy
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 58. Soft Deletes ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Soft deletes, data retention

**Challenge:**
```typescript
// Create a NestJS controller/service for: Soft Deletes
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 59. Audit Logging ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Audit trails, logging

**Challenge:**
```typescript
// Create a NestJS controller/service for: Audit Logging
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 60. Request Throttling ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Throttling, rate limiting

**Challenge:**
```typescript
// Create a NestJS controller/service for: Request Throttling
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 61. API Gateway ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Gateway pattern, routing

**Challenge:**
```typescript
// Create a NestJS controller/service for: API Gateway
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 62. Service Discovery ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Service registry, discovery

**Challenge:**
```typescript
// Create a NestJS controller/service for: Service Discovery
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 63. Circuit Breaker Pattern ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Resilience, fault tolerance

**Challenge:**
```typescript
// Create a NestJS controller/service for: Circuit Breaker Pattern
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 64. Distributed Tracing ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Tracing, observability

**Challenge:**
```typescript
// Create a NestJS controller/service for: Distributed Tracing
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 65. Performance Monitoring ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** APM, monitoring

**Challenge:**
```typescript
// Create a NestJS controller/service for: Performance Monitoring
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---

---

## 🎯 Tier 4: Lead Level (10 questions)
**Target:** 6+ years experience | Time: 35-45 min each

### 66. System Design (URL Shortener) ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** System design, scalability

**Challenge:**
```typescript
// Create a NestJS controller/service for: System Design (URL Shortener)
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 67. System Design (Chat App) ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Real-time systems, WebSockets

**Challenge:**
```typescript
// Create a NestJS controller/service for: System Design (Chat App)
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 68. Database Sharding ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Sharding, horizontal scaling

**Challenge:**
```typescript
// Create a NestJS controller/service for: Database Sharding
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 69. Read Replicas ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Replication, read scaling

**Challenge:**
```typescript
// Create a NestJS controller/service for: Read Replicas
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 70. Load Balancing ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Load balancers, distribution

**Challenge:**
```typescript
// Create a NestJS controller/service for: Load Balancing
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 71. Horizontal Scaling ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Scaling, infrastructure

**Challenge:**
```typescript
// Create a NestJS controller/service for: Horizontal Scaling
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 72. Deployment Strategies ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Blue-green, canary deployments

**Challenge:**
```typescript
// Create a NestJS controller/service for: Deployment Strategies
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 73. Container Orchestration ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Kubernetes, Docker

**Challenge:**
```typescript
// Create a NestJS controller/service for: Container Orchestration
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 74. CI/CD Pipeline ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Continuous integration, deployment

**Challenge:**
```typescript
// Create a NestJS controller/service for: CI/CD Pipeline
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
```

---
### 75. Security Best Practices ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Security, OWASP, vulnerabilities

**Challenge:**
```typescript
// Create a NestJS controller/service for: Security Best Practices
// Use decorators and dependency injection
// Include proper TypeScript types
```

**What interviewers look for:**
```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  getHello(): string {
    return 'Hello World';
  }
}
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
