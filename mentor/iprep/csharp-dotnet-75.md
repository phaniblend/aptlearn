# APTLEARN Interview Prep: C# + .NET Core
## 75 Live Coding Questions for Full-Stack Development

---

## 📋 Overview

**Total Questions:** 75  
**Technology:** C# + .NET Core  
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
```csharp
// Create a .NET Core controller for: Hello World Endpoint
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 2. GET Endpoint with Params ⭐
**Time:** 5-15 min  
**Tests:** Route parameters, query params

**Challenge:**
```csharp
// Create a .NET Core controller for: GET Endpoint with Params
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 3. POST Endpoint with Body ⭐
**Time:** 5-15 min  
**Tests:** Request body, POST handling

**Challenge:**
```csharp
// Create a .NET Core controller for: POST Endpoint with Body
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 4. PUT Endpoint ⭐
**Time:** 5-15 min  
**Tests:** Update operations, PUT method

**Challenge:**
```csharp
// Create a .NET Core controller for: PUT Endpoint
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 5. DELETE Endpoint ⭐
**Time:** 5-15 min  
**Tests:** Delete operations, DELETE method

**Challenge:**
```csharp
// Create a .NET Core controller for: DELETE Endpoint
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 6. Middleware Basics ⭐
**Time:** 5-15 min  
**Tests:** Middleware, request pipeline

**Challenge:**
```csharp
// Create a .NET Core controller for: Middleware Basics
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 7. Error Handling Middleware ⭐
**Time:** 5-15 min  
**Tests:** Error handling, error responses

**Challenge:**
```csharp
// Create a .NET Core controller for: Error Handling Middleware
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 8. Environment Variables ⭐
**Time:** 5-15 min  
**Tests:** Config management, env vars

**Challenge:**
```csharp
// Create a .NET Core controller for: Environment Variables
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 9. CORS Setup ⭐
**Time:** 5-15 min  
**Tests:** Cross-origin requests, CORS

**Challenge:**
```csharp
// Create a .NET Core controller for: CORS Setup
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 10. Request Validation ⭐
**Time:** 5-15 min  
**Tests:** Input validation, validation middleware

**Challenge:**
```csharp
// Create a .NET Core controller for: Request Validation
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 11. Response Formatting ⭐
**Time:** 5-15 min  
**Tests:** Response structure, JSON responses

**Challenge:**
```csharp
// Create a .NET Core controller for: Response Formatting
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 12. Query Parameters ⭐
**Time:** 5-15 min  
**Tests:** Query string parsing

**Challenge:**
```csharp
// Create a .NET Core controller for: Query Parameters
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 13. Path Parameters ⭐
**Time:** 5-15 min  
**Tests:** Route parameters, dynamic routes

**Challenge:**
```csharp
// Create a .NET Core controller for: Path Parameters
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 14. Request Body Parsing ⭐
**Time:** 5-15 min  
**Tests:** Body parsing, JSON parsing

**Challenge:**
```csharp
// Create a .NET Core controller for: Request Body Parsing
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 15. Static File Serving ⭐
**Time:** 5-15 min  
**Tests:** File serving, static assets

**Challenge:**
```csharp
// Create a .NET Core controller for: Static File Serving
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 16. Simple Logging ⭐
**Time:** 5-15 min  
**Tests:** Logging, console logging

**Challenge:**
```csharp
// Create a .NET Core controller for: Simple Logging
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 17. Health Check Endpoint ⭐
**Time:** 5-15 min  
**Tests:** Health checks, monitoring

**Challenge:**
```csharp
// Create a .NET Core controller for: Health Check Endpoint
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 18. Basic Authentication ⭐
**Time:** 5-15 min  
**Tests:** Auth basics, username/password

**Challenge:**
```csharp
// Create a .NET Core controller for: Basic Authentication
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 19. Password Hashing ⭐
**Time:** 5-15 min  
**Tests:** Password security, hashing

**Challenge:**
```csharp
// Create a .NET Core controller for: Password Hashing
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 20. JWT Token Creation ⭐
**Time:** 5-15 min  
**Tests:** JWT, token generation

**Challenge:**
```csharp
// Create a .NET Core controller for: JWT Token Creation
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
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
```csharp
// Create a .NET Core controller for: Database Connection
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 22. CRUD Operations ⭐⭐
**Time:** 15-25 min  
**Tests:** Create, read, update, delete

**Challenge:**
```csharp
// Create a .NET Core controller for: CRUD Operations
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 23. One-to-Many Relationships ⭐⭐
**Time:** 15-25 min  
**Tests:** Database relationships

**Challenge:**
```csharp
// Create a .NET Core controller for: One-to-Many Relationships
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 24. Many-to-Many Relationships ⭐⭐
**Time:** 15-25 min  
**Tests:** Junction tables, relationships

**Challenge:**
```csharp
// Create a .NET Core controller for: Many-to-Many Relationships
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 25. Database Transactions ⭐⭐
**Time:** 15-25 min  
**Tests:** Transactions, ACID

**Challenge:**
```csharp
// Create a .NET Core controller for: Database Transactions
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 26. Query Optimization ⭐⭐
**Time:** 15-25 min  
**Tests:** SQL optimization, indexes

**Challenge:**
```csharp
// Create a .NET Core controller for: Query Optimization
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 27. Pagination ⭐⭐
**Time:** 15-25 min  
**Tests:** Pagination, limit/offset

**Challenge:**
```csharp
// Create a .NET Core controller for: Pagination
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 28. Filtering and Sorting ⭐⭐
**Time:** 15-25 min  
**Tests:** Data filtering, sorting

**Challenge:**
```csharp
// Create a .NET Core controller for: Filtering and Sorting
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 29. Search Functionality ⭐⭐
**Time:** 15-25 min  
**Tests:** Search, full-text search

**Challenge:**
```csharp
// Create a .NET Core controller for: Search Functionality
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 30. File Upload Handling ⭐⭐
**Time:** 15-25 min  
**Tests:** File uploads, multipart/form-data

**Challenge:**
```csharp
// Create a .NET Core controller for: File Upload Handling
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 31. JWT Authentication ⭐⭐
**Time:** 15-25 min  
**Tests:** JWT, token validation

**Challenge:**
```csharp
// Create a .NET Core controller for: JWT Authentication
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 32. Refresh Tokens ⭐⭐
**Time:** 15-25 min  
**Tests:** Token refresh, security

**Challenge:**
```csharp
// Create a .NET Core controller for: Refresh Tokens
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 33. Role-Based Access Control ⭐⭐
**Time:** 15-25 min  
**Tests:** RBAC, permissions

**Challenge:**
```csharp
// Create a .NET Core controller for: Role-Based Access Control
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 34. API Versioning ⭐⭐
**Time:** 15-25 min  
**Tests:** Versioning, backward compatibility

**Challenge:**
```csharp
// Create a .NET Core controller for: API Versioning
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 35. Rate Limiting ⭐⭐
**Time:** 15-25 min  
**Tests:** Rate limiting, throttling

**Challenge:**
```csharp
// Create a .NET Core controller for: Rate Limiting
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 36. Caching (Redis) ⭐⭐
**Time:** 15-25 min  
**Tests:** Caching, Redis integration

**Challenge:**
```csharp
// Create a .NET Core controller for: Caching (Redis)
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 37. Session Management ⭐⭐
**Time:** 15-25 min  
**Tests:** Sessions, session storage

**Challenge:**
```csharp
// Create a .NET Core controller for: Session Management
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 38. Cookie Handling ⭐⭐
**Time:** 15-25 min  
**Tests:** Cookies, secure cookies

**Challenge:**
```csharp
// Create a .NET Core controller for: Cookie Handling
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 39. Email Sending ⭐⭐
**Time:** 15-25 min  
**Tests:** Email, SMTP

**Challenge:**
```csharp
// Create a .NET Core controller for: Email Sending
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 40. Background Jobs ⭐⭐
**Time:** 15-25 min  
**Tests:** Job queues, async processing

**Challenge:**
```csharp
// Create a .NET Core controller for: Background Jobs
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 41. Scheduled Tasks ⭐⭐
**Time:** 15-25 min  
**Tests:** Cron jobs, scheduled tasks

**Challenge:**
```csharp
// Create a .NET Core controller for: Scheduled Tasks
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 42. WebSocket Server ⭐⭐
**Time:** 15-25 min  
**Tests:** WebSockets, real-time

**Challenge:**
```csharp
// Create a .NET Core controller for: WebSocket Server
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 43. Real-Time Chat ⭐⭐
**Time:** 15-25 min  
**Tests:** Real-time communication

**Challenge:**
```csharp
// Create a .NET Core controller for: Real-Time Chat
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 44. API Documentation ⭐⭐
**Time:** 15-25 min  
**Tests:** OpenAPI, Swagger

**Challenge:**
```csharp
// Create a .NET Core controller for: API Documentation
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 45. Input Sanitization ⭐⭐
**Time:** 15-25 min  
**Tests:** Security, XSS prevention

**Challenge:**
```csharp
// Create a .NET Core controller for: Input Sanitization
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
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
```csharp
// Create a .NET Core controller for: OAuth2 Implementation
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 47. Microservices Communication ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Service communication, APIs

**Challenge:**
```csharp
// Create a .NET Core controller for: Microservices Communication
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 48. Message Queue (RabbitMQ/Kafka) ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Message queues, async messaging

**Challenge:**
```csharp
// Create a .NET Core controller for: Message Queue (RabbitMQ/Kafka)
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 49. Event-Driven Architecture ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Events, event sourcing

**Challenge:**
```csharp
// Create a .NET Core controller for: Event-Driven Architecture
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 50. CQRS Pattern ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Command Query Responsibility Segregation

**Challenge:**
```csharp
// Create a .NET Core controller for: CQRS Pattern
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 51. Repository Pattern ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Data access, abstraction

**Challenge:**
```csharp
// Create a .NET Core controller for: Repository Pattern
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 52. Unit Testing ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Unit tests, test coverage

**Challenge:**
```csharp
// Create a .NET Core controller for: Unit Testing
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 53. Integration Testing ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Integration tests, test databases

**Challenge:**
```csharp
// Create a .NET Core controller for: Integration Testing
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 54. Test Coverage ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Code coverage, testing metrics

**Challenge:**
```csharp
// Create a .NET Core controller for: Test Coverage
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 55. Database Migrations ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Migrations, schema changes

**Challenge:**
```csharp
// Create a .NET Core controller for: Database Migrations
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 56. Database Seeding ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Seed data, test data

**Challenge:**
```csharp
// Create a .NET Core controller for: Database Seeding
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 57. Multi-Tenancy ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Multi-tenant architecture

**Challenge:**
```csharp
// Create a .NET Core controller for: Multi-Tenancy
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 58. Soft Deletes ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Soft deletes, data retention

**Challenge:**
```csharp
// Create a .NET Core controller for: Soft Deletes
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 59. Audit Logging ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Audit trails, logging

**Challenge:**
```csharp
// Create a .NET Core controller for: Audit Logging
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 60. Request Throttling ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Throttling, rate limiting

**Challenge:**
```csharp
// Create a .NET Core controller for: Request Throttling
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 61. API Gateway ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Gateway pattern, routing

**Challenge:**
```csharp
// Create a .NET Core controller for: API Gateway
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 62. Service Discovery ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Service registry, discovery

**Challenge:**
```csharp
// Create a .NET Core controller for: Service Discovery
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 63. Circuit Breaker Pattern ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Resilience, fault tolerance

**Challenge:**
```csharp
// Create a .NET Core controller for: Circuit Breaker Pattern
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 64. Distributed Tracing ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Tracing, observability

**Challenge:**
```csharp
// Create a .NET Core controller for: Distributed Tracing
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 65. Performance Monitoring ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** APM, monitoring

**Challenge:**
```csharp
// Create a .NET Core controller for: Performance Monitoring
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
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
```csharp
// Create a .NET Core controller for: System Design (URL Shortener)
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 67. System Design (Chat App) ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Real-time systems, WebSockets

**Challenge:**
```csharp
// Create a .NET Core controller for: System Design (Chat App)
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 68. Database Sharding ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Sharding, horizontal scaling

**Challenge:**
```csharp
// Create a .NET Core controller for: Database Sharding
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 69. Read Replicas ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Replication, read scaling

**Challenge:**
```csharp
// Create a .NET Core controller for: Read Replicas
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 70. Load Balancing ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Load balancers, distribution

**Challenge:**
```csharp
// Create a .NET Core controller for: Load Balancing
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 71. Horizontal Scaling ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Scaling, infrastructure

**Challenge:**
```csharp
// Create a .NET Core controller for: Horizontal Scaling
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 72. Deployment Strategies ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Blue-green, canary deployments

**Challenge:**
```csharp
// Create a .NET Core controller for: Deployment Strategies
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 73. Container Orchestration ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Kubernetes, Docker

**Challenge:**
```csharp
// Create a .NET Core controller for: Container Orchestration
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 74. CI/CD Pipeline ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Continuous integration, deployment

**Challenge:**
```csharp
// Create a .NET Core controller for: CI/CD Pipeline
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
    }
}
```

---
### 75. Security Best Practices ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Security, OWASP, vulnerabilities

**Challenge:**
```csharp
// Create a .NET Core controller for: Security Best Practices
// Use dependency injection
// Include proper error handling
```

**What interviewers look for:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new { message = "Hello World" });
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
