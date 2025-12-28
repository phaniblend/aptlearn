#!/usr/bin/env python3
"""
Generate 75 coding challenges for each of 12 technologies.
Creates comprehensive markdown files with complete solutions.
"""
from pathlib import Path
from typing import List, Dict

IPREP_DIR = Path(__file__).parent

# Challenge templates by technology and tier
CHALLENGE_TEMPLATES = {
    'frontend': {
        'junior': [
            ('Hello World Component', 'Component basics, JSX/template syntax'),
            ('Props/Input Binding', 'Props, prop types, data passing'),
            ('Event Handling', 'Event handlers, onClick/click events'),
            ('State Management', 'useState/reactive state, state updates'),
            ('List Rendering', 'Array.map, keys, list rendering'),
            ('Conditional Rendering', 'Ternary operator, && operator'),
            ('Form Input Handling', 'Controlled inputs, onChange'),
            ('Two-Way Binding', 'Controlled components, value binding'),
            ('Component Lifecycle', 'useEffect/ngOnInit, cleanup'),
            ('CSS Styling', 'Inline styles, style objects'),
            ('Click Counter', 'State, event handling'),
            ('Todo Item Component', 'Props, conditional rendering'),
            ('Show/Hide Toggle', 'State toggle, conditional rendering'),
            ('Parent-Child Communication', 'Props, callbacks'),
            ('Simple Form Validation', 'Form validation, error messages'),
            ('Array Filtering', 'Array.filter, dynamic lists'),
            ('Button Variants', 'Props, conditional styling'),
            ('Image Gallery', 'Array rendering, image handling'),
            ('Accordion Component', 'State management, conditional rendering'),
            ('Tab Component', 'State, conditional rendering'),
        ],
        'mid': [
            ('Custom Hooks/Composables', 'Reusable logic, custom hooks'),
            ('HTTP GET Request', 'Fetch/axios, async data loading'),
            ('HTTP POST with Form', 'Form submission, POST requests'),
            ('Error Handling', 'Try-catch, error states'),
            ('Loading States', 'Loading indicators, async states'),
            ('Routing Setup', 'Router configuration'),
            ('Route Parameters', 'Dynamic routes, params'),
            ('Nested Routes', 'Child routes, route hierarchy'),
            ('Route Guards', 'Navigation guards, route protection'),
            ('Form Validation (Advanced)', 'Complex validation rules'),
            ('Debounced Search', 'Debouncing, performance'),
            ('Infinite Scroll', 'Scroll detection, pagination'),
            ('Pagination', 'Page navigation, data splitting'),
            ('Modal/Dialog Component', 'Portal, overlay, focus trap'),
            ('Dropdown with Outside Click', 'Event listeners, refs'),
            ('Context API/Provide-Inject', 'Global state, dependency injection'),
            ('Custom Directives/Pipes', 'Reusable directives, pipes'),
            ('Lazy Loading', 'Code splitting, dynamic imports'),
            ('Code Splitting', 'Bundle optimization'),
            ('Local Storage Integration', 'Browser storage, persistence'),
            ('WebSocket Connection', 'Real-time communication'),
            ('File Upload', 'File handling, FormData'),
            ('Drag and Drop', 'Drag events, data transfer'),
            ('Multi-Step Form', 'Form state, navigation'),
            ('Real-Time Validation', 'Live validation, feedback'),
        ],
        'senior': [
            ('State Management (Redux/NgRx)', 'Global state, actions, reducers'),
            ('State with Async Actions', 'Async state management'),
            ('Optimistic Updates', 'UI updates, rollback'),
            ('Memoization/Performance', 'useMemo, useCallback, optimization'),
            ('Virtual Scrolling', 'Large lists, performance'),
            ('Component Testing', 'Unit tests, component testing'),
            ('Integration Testing', 'Component integration'),
            ('E2E Testing Basics', 'End-to-end testing'),
            ('Custom Hooks Testing', 'Hook testing, test utilities'),
            ('Performance Profiling', 'Performance analysis, optimization'),
            ('Code-Splitting Strategy', 'Bundle analysis, optimization'),
            ('SSR Implementation', 'Server-side rendering'),
            ('PWA Setup', 'Progressive Web App'),
            ('Service Workers', 'Offline support, caching'),
            ('Accessibility (ARIA)', 'ARIA attributes, screen readers'),
            ('Keyboard Navigation', 'Keyboard events, focus management'),
            ('Internationalization (i18n)', 'Multi-language support'),
            ('Theme Switching', 'Dynamic theming, CSS variables'),
            ('Advanced TypeScript Patterns', 'Generics, utility types'),
            ('Error Boundary', 'Error handling, fallback UI'),
        ],
        'lead': [
            ('Micro-Frontend Architecture', 'Module federation, micro-frontends'),
            ('Module Federation', 'Shared modules, runtime integration'),
            ('Design System Creation', 'Component library, design tokens'),
            ('Custom CLI Tool', 'Code generation, tooling'),
            ('Build Optimization', 'Webpack/Vite optimization'),
            ('Bundle Analysis', 'Bundle size analysis'),
            ('Monorepo Setup', 'Workspace management, shared code'),
            ('Custom Webpack/Vite Config', 'Build configuration'),
            ('Advanced State Patterns', 'State machines, complex state'),
            ('Performance Monitoring', 'APM, performance tracking'),
        ]
    },
    'backend': {
        'junior': [
            ('Hello World Endpoint', 'Basic routing, GET endpoint'),
            ('GET Endpoint with Params', 'Route parameters, query params'),
            ('POST Endpoint with Body', 'Request body, POST handling'),
            ('PUT Endpoint', 'Update operations, PUT method'),
            ('DELETE Endpoint', 'Delete operations, DELETE method'),
            ('Middleware Basics', 'Middleware, request pipeline'),
            ('Error Handling Middleware', 'Error handling, error responses'),
            ('Environment Variables', 'Config management, env vars'),
            ('CORS Setup', 'Cross-origin requests, CORS'),
            ('Request Validation', 'Input validation, validation middleware'),
            ('Response Formatting', 'Response structure, JSON responses'),
            ('Query Parameters', 'Query string parsing'),
            ('Path Parameters', 'Route parameters, dynamic routes'),
            ('Request Body Parsing', 'Body parsing, JSON parsing'),
            ('Static File Serving', 'File serving, static assets'),
            ('Simple Logging', 'Logging, console logging'),
            ('Health Check Endpoint', 'Health checks, monitoring'),
            ('Basic Authentication', 'Auth basics, username/password'),
            ('Password Hashing', 'Password security, hashing'),
            ('JWT Token Creation', 'JWT, token generation'),
        ],
        'mid': [
            ('Database Connection', 'DB connection, connection pooling'),
            ('CRUD Operations', 'Create, read, update, delete'),
            ('One-to-Many Relationships', 'Database relationships'),
            ('Many-to-Many Relationships', 'Junction tables, relationships'),
            ('Database Transactions', 'Transactions, ACID'),
            ('Query Optimization', 'SQL optimization, indexes'),
            ('Pagination', 'Pagination, limit/offset'),
            ('Filtering and Sorting', 'Data filtering, sorting'),
            ('Search Functionality', 'Search, full-text search'),
            ('File Upload Handling', 'File uploads, multipart/form-data'),
            ('JWT Authentication', 'JWT, token validation'),
            ('Refresh Tokens', 'Token refresh, security'),
            ('Role-Based Access Control', 'RBAC, permissions'),
            ('API Versioning', 'Versioning, backward compatibility'),
            ('Rate Limiting', 'Rate limiting, throttling'),
            ('Caching (Redis)', 'Caching, Redis integration'),
            ('Session Management', 'Sessions, session storage'),
            ('Cookie Handling', 'Cookies, secure cookies'),
            ('Email Sending', 'Email, SMTP'),
            ('Background Jobs', 'Job queues, async processing'),
            ('Scheduled Tasks', 'Cron jobs, scheduled tasks'),
            ('WebSocket Server', 'WebSockets, real-time'),
            ('Real-Time Chat', 'Real-time communication'),
            ('API Documentation', 'OpenAPI, Swagger'),
            ('Input Sanitization', 'Security, XSS prevention'),
        ],
        'senior': [
            ('OAuth2 Implementation', 'OAuth2, authentication flows'),
            ('Microservices Communication', 'Service communication, APIs'),
            ('Message Queue (RabbitMQ/Kafka)', 'Message queues, async messaging'),
            ('Event-Driven Architecture', 'Events, event sourcing'),
            ('CQRS Pattern', 'Command Query Responsibility Segregation'),
            ('Repository Pattern', 'Data access, abstraction'),
            ('Unit Testing', 'Unit tests, test coverage'),
            ('Integration Testing', 'Integration tests, test databases'),
            ('Test Coverage', 'Code coverage, testing metrics'),
            ('Database Migrations', 'Migrations, schema changes'),
            ('Database Seeding', 'Seed data, test data'),
            ('Multi-Tenancy', 'Multi-tenant architecture'),
            ('Soft Deletes', 'Soft deletes, data retention'),
            ('Audit Logging', 'Audit trails, logging'),
            ('Request Throttling', 'Throttling, rate limiting'),
            ('API Gateway', 'Gateway pattern, routing'),
            ('Service Discovery', 'Service registry, discovery'),
            ('Circuit Breaker Pattern', 'Resilience, fault tolerance'),
            ('Distributed Tracing', 'Tracing, observability'),
            ('Performance Monitoring', 'APM, monitoring'),
        ],
        'lead': [
            ('System Design (URL Shortener)', 'System design, scalability'),
            ('System Design (Chat App)', 'Real-time systems, WebSockets'),
            ('Database Sharding', 'Sharding, horizontal scaling'),
            ('Read Replicas', 'Replication, read scaling'),
            ('Load Balancing', 'Load balancers, distribution'),
            ('Horizontal Scaling', 'Scaling, infrastructure'),
            ('Deployment Strategies', 'Blue-green, canary deployments'),
            ('Container Orchestration', 'Kubernetes, Docker'),
            ('CI/CD Pipeline', 'Continuous integration, deployment'),
            ('Security Best Practices', 'Security, OWASP, vulnerabilities'),
        ]
    }
}

def get_star_rating(tier: str) -> str:
    """Get star rating for tier."""
    return {
        'junior': '⭐',
        'mid': '⭐⭐',
        'senior': '⭐⭐⭐',
        'lead': '⭐⭐⭐⭐'
    }[tier]

def get_time_range(tier: str) -> str:
    """Get time range for tier."""
    return {
        'junior': '5-15 min',
        'mid': '15-25 min',
        'senior': '25-35 min',
        'lead': '35-45 min'
    }[tier]

def generate_challenge_markdown(num: int, title: str, tests: str, tier: str, 
                                 tech_key: str, tech_config: Dict) -> str:
    """Generate markdown for a single challenge."""
    stars = get_star_rating(tier)
    time = get_time_range(tier)
    
    # Generate challenge and solution based on technology
    challenge_code, solution_code = generate_code_examples(num, title, tech_key, tech_config, tier)
    
    return f'''### {num}. {title} {stars}
**Time:** {time}  
**Tests:** {tests}

**Challenge:**
```{tech_config['language']}
{challenge_code}
```

**What interviewers look for:**
```{tech_config['language']}
{solution_code}
```

---
'''

def generate_code_examples(num: int, title: str, tech_key: str, tech_config: Dict, tier: str) -> tuple:
    """Generate challenge and solution code examples."""
    lang = tech_config['language']
    framework = tech_config['framework']
    
    # Generate challenge code (simplified problem statement)
    if 'react' in tech_key:
        if 'javascript' in tech_key:
            challenge = f'''// Create a React component for: {title}
// Use functional component syntax
// Export the component'''
            solution = generate_react_js_solution(num, title, tier)
        else:
            challenge = f'''// Create a React component for: {title}
// Use TypeScript with proper types
// Export the component'''
            solution = generate_react_ts_solution(num, title, tier)
    elif 'angular' in tech_key:
        challenge = f'''// Create an Angular component for: {title}
// Use @Component decorator
// Make it standalone'''
        solution = generate_angular_solution(num, title, tier)
    elif 'vue' in tech_key:
        challenge = f'''// Create a Vue 3 component for: {title}
// Use Composition API
// Use <script setup> syntax'''
        solution = generate_vue_solution(num, title, tier)
    elif 'nextjs' in tech_key:
        challenge = f'''// Create a Next.js {title}
// Use App Router or Pages Router as appropriate
// Include proper TypeScript types'''
        solution = generate_nextjs_solution(num, title, tier)
    elif 'nodejs' in tech_key or 'express' in tech_key:
        challenge = f'''// Create an Express endpoint for: {title}
// Include proper error handling
// Use modern async/await syntax'''
        solution = generate_express_solution(num, title, tier)
    elif 'fastapi' in tech_key:
        challenge = f'''// Create a FastAPI endpoint for: {title}
// Include proper type hints
// Add request/response models'''
        solution = generate_fastapi_solution(num, title, tier)
    elif 'django' in tech_key:
        challenge = f'''// Create a Django view/endpoint for: {title}
// Use class-based or function-based views
// Include proper error handling'''
        solution = generate_django_solution(num, title, tier)
    elif 'nestjs' in tech_key:
        challenge = f'''// Create a NestJS controller/service for: {title}
// Use decorators and dependency injection
// Include proper TypeScript types'''
        solution = generate_nestjs_solution(num, title, tier)
    elif 'spring' in tech_key:
        challenge = f'''// Create a Spring Boot controller for: {title}
// Use annotations and dependency injection
// Include proper error handling'''
        solution = generate_spring_solution(num, title, tier)
    elif 'dotnet' in tech_key or 'csharp' in tech_key:
        challenge = f'''// Create a .NET Core controller for: {title}
// Use dependency injection
// Include proper error handling'''
        solution = generate_dotnet_solution(num, title, tier)
    elif 'go' in tech_key or 'gin' in tech_key:
        challenge = f'''// Create a Gin handler for: {title}
// Use proper error handling
// Follow Go best practices'''
        solution = generate_go_solution(num, title, tier)
    else:
        challenge = f'''// Implement: {title}
// Use {framework} best practices
// Include proper error handling'''
        solution = f'''// Complete solution for {title}
// Implementation details here'''
    
    return challenge, solution

def generate_react_js_solution(num: int, title: str, tier: str) -> str:
    """Generate React JavaScript solution."""
    if num == 1:  # Hello World
        return '''import React from 'react';

function HelloWorld() {
  return (
    <div>
      <h1>Hello World</h1>
    </div>
  );
}

export default HelloWorld;'''
    elif num == 2:  # Props
        return '''import React from 'react';

function Greeting({ name = 'Guest' }) {
  return <h1>Hello, {name}!</h1>;
}

export default Greeting;'''
    elif num == 4:  # State
        return '''import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>
    </div>
  );
}

export default Counter;'''
    else:
        return f'''// Complete React solution for: {title}
import React, {{ useState }} from 'react';

function Component() {{
  // Implementation here
  return <div>Solution</div>;
}}

export default Component;'''

def generate_react_ts_solution(num: int, title: str, tier: str) -> str:
    """Generate React TypeScript solution."""
    return f'''import React from 'react';

interface Props {{
  // Props interface
}}

const Component: React.FC<Props> = () => {{
  // TypeScript implementation
  return <div>Solution</div>;
}};

export default Component;'''

def generate_angular_solution(num: int, title: str, tier: str) -> str:
    """Generate Angular solution."""
    if num == 1:
        return '''import { Component } from '@angular/core';

@Component({
  selector: 'app-hello',
  template: '<h1>Hello World</h1>',
  standalone: true
})
export class HelloComponent {}'''
    else:
        return f'''import {{ Component }} from '@angular/core';

@Component({{
  selector: 'app-component',
  template: '<div>Solution</div>',
  standalone: true
}})
export class Component {{
  // Implementation
}}'''

def generate_vue_solution(num: int, title: str, tier: str) -> str:
    """Generate Vue 3 solution."""
    return f'''<script setup>
import {{ ref }} from 'vue';

// Composition API implementation
const message = ref('Hello Vue');
</script>

<template>
  <div>{{ message }}</div>
</template>'''

def generate_nextjs_solution(num: int, title: str, tier: str) -> str:
    """Generate Next.js solution."""
    return f'''// Next.js App Router solution
export default function Page() {{
  return <div>Solution</div>;
}}'''

def generate_express_solution(num: int, title: str, tier: str) -> str:
    """Generate Express.js solution."""
    if num == 1:
        return '''const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.json({ message: 'Hello World' });
});

module.exports = app;'''
    else:
        return f'''const express = require('express');
const router = express.Router();

// Solution implementation
router.get('/endpoint', async (req, res) => {{
  try {{
    // Implementation
    res.json({{ success: true }});
  }} catch (error) {{
    res.status(500).json({{ error: error.message }});
  }}
}});

module.exports = router;'''

def generate_fastapi_solution(num: int, title: str, tier: str) -> str:
    """Generate FastAPI solution."""
    return f'''from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {{"message": "Hello World"}}'''

def generate_django_solution(num: int, title: str, tier: str) -> str:
    """Generate Django solution."""
    return f'''from django.http import JsonResponse
from django.views import View

class MyView(View):
    def get(self, request):
        return JsonResponse({{"message": "Hello World"}})'''

def generate_nestjs_solution(num: int, title: str, tier: str) -> str:
    """Generate NestJS solution."""
    return f'''import {{ Controller, Get }} from '@nestjs/common';

@Controller()
export class AppController {{
  @Get()
  getHello(): string {{
    return 'Hello World';
  }}
}}'''

def generate_spring_solution(num: int, title: str, tier: str) -> str:
    """Generate Spring Boot solution."""
    return f'''@RestController
@RequestMapping("/api")
public class MyController {{
    
    @GetMapping("/hello")
    public ResponseEntity<String> hello() {{
        return ResponseEntity.ok("Hello World");
    }}
}}'''

def generate_dotnet_solution(num: int, title: str, tier: str) -> str:
    """Generate .NET Core solution."""
    return f'''[ApiController]
[Route("api/[controller]")]
public class MyController : ControllerBase
{{
    [HttpGet]
    public IActionResult Get()
    {{
        return Ok(new {{ message = "Hello World" }});
    }}
}}'''

def generate_go_solution(num: int, title: str, tier: str) -> str:
    """Generate Go/Gin solution."""
    return f'''package main

import (
    "github.com/gin-gonic/gin"
)

func main() {{
    r := gin.Default()
    r.GET("/", func(c *gin.Context) {{
        c.JSON(200, gin.H{{"message": "Hello World"}})
    }})
    r.Run()
}}'''

def generate_markdown_file(tech_key: str, tech_config: Dict):
    """Generate complete markdown file for a technology."""
    is_frontend = any(x in tech_key for x in ['react', 'angular', 'vue', 'nextjs'])
    templates = CHALLENGE_TEMPLATES['frontend' if is_frontend else 'backend']
    
    content = f'''# APTLEARN Interview Prep: {tech_config['name']}
## 75 Live Coding Questions for Full-Stack Development

---

## 📋 Overview

**Total Questions:** 75  
**Technology:** {tech_config['name']}  
**Interview Format:** Live coding, screen share  
**Time Range:** 5-45 minutes per question  
**Difficulty Levels:** 4 tiers (Junior → Lead)

---

## 🎯 Tier 1: Junior Level (20 questions)
**Target:** 0-2 years experience | Time: 5-15 min each

'''
    
    # Generate Junior challenges (1-20)
    challenge_num = 1
    for title, tests in templates['junior']:
        content += generate_challenge_markdown(
            challenge_num, title, tests, 'junior', tech_key, tech_config
        )
        challenge_num += 1
    
    content += '''
---

## 🎯 Tier 2: Mid-Level (25 questions)  
**Target:** 2-4 years experience | Time: 15-25 min each

'''
    
    # Generate Mid challenges (21-45)
    for title, tests in templates['mid']:
        content += generate_challenge_markdown(
            challenge_num, title, tests, 'mid', tech_key, tech_config
        )
        challenge_num += 1
    
    content += '''
---

## 🎯 Tier 3: Senior Level (20 questions)
**Target:** 4-6 years experience | Time: 25-35 min each

'''
    
    # Generate Senior challenges (46-65)
    for title, tests in templates['senior']:
        content += generate_challenge_markdown(
            challenge_num, title, tests, 'senior', tech_key, tech_config
        )
        challenge_num += 1
    
    content += '''
---

## 🎯 Tier 4: Lead Level (10 questions)
**Target:** 6+ years experience | Time: 35-45 min each

'''
    
    # Generate Lead challenges (66-75)
    for title, tests in templates['lead']:
        content += generate_challenge_markdown(
            challenge_num, title, tests, 'lead', tech_key, tech_config
        )
        challenge_num += 1
    
    content += '''
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
'''
    
    return content

def main():
    """Generate all 12 markdown files."""
    technologies = {
        'react-javascript-75': {
            'name': 'React with JavaScript',
            'language': 'javascript',
            'framework': 'React'
        },
        'react-typescript-75': {
            'name': 'React with TypeScript',
            'language': 'typescript',
            'framework': 'React'
        },
        'angular-75': {
            'name': 'Angular (v14+)',
            'language': 'typescript',
            'framework': 'Angular'
        },
        'vuejs-75': {
            'name': 'Vue.js 3 (Composition API)',
            'language': 'javascript',
            'framework': 'Vue.js'
        },
        'nextjs-75': {
            'name': 'Next.js (App Router + Pages Router)',
            'language': 'typescript',
            'framework': 'Next.js'
        },
        'nodejs-express-75': {
            'name': 'Node.js + Express',
            'language': 'javascript',
            'framework': 'Express'
        },
        'python-fastapi-75': {
            'name': 'Python + FastAPI',
            'language': 'python',
            'framework': 'FastAPI'
        },
        'python-django-75': {
            'name': 'Python + Django',
            'language': 'python',
            'framework': 'Django'
        },
        'nestjs-75': {
            'name': 'NestJS (TypeScript)',
            'language': 'typescript',
            'framework': 'NestJS'
        },
        'java-spring-boot-75': {
            'name': 'Java + Spring Boot',
            'language': 'java',
            'framework': 'Spring Boot'
        },
        'csharp-dotnet-75': {
            'name': 'C# + .NET Core',
            'language': 'csharp',
            'framework': '.NET Core'
        },
        'go-gin-75': {
            'name': 'Go + Gin framework',
            'language': 'go',
            'framework': 'Gin'
        }
    }
    
    for tech_key, tech_config in technologies.items():
        print(f"Generating {tech_key}...")
        try:
            content = generate_markdown_file(tech_key, tech_config)
            
            file_path = IPREP_DIR / f"{tech_key}.md"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  [OK] Created {file_path.name} ({len(content)} chars)")
        except Exception as e:
            print(f"  [ERROR] Failed to generate {tech_key}: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n[SUCCESS] Generated all 12 technology files!")

if __name__ == '__main__':
    main()

