# APTLEARN Interview Prep: React with JavaScript
## 75 Live Coding Questions for Full-Stack Development

---

## 📋 Overview

**Total Questions:** 75  
**Technology:** React with JavaScript  
**Interview Format:** Live coding, screen share  
**Time Range:** 5-45 minutes per question  
**Difficulty Levels:** 4 tiers (Junior → Lead)

---

## 🎯 Tier 1: Junior Level (20 questions)
**Target:** 0-2 years experience | Time: 5-15 min each

### 1. Hello World Component ⭐
**Time:** 5-15 min  
**Tests:** Component basics, JSX/template syntax

**Challenge:**
```javascript
// Create a React component for: Hello World Component
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
import React from 'react';

function HelloWorld() {
  return (
    <div>
      <h1>Hello World</h1>
    </div>
  );
}

export default HelloWorld;
```

---
### 2. Props/Input Binding ⭐
**Time:** 5-15 min  
**Tests:** Props, prop types, data passing

**Challenge:**
```javascript
// Create a React component for: Props/Input Binding
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
import React from 'react';

function Greeting({ name = 'Guest' }) {
  return <h1>Hello, {name}!</h1>;
}

export default Greeting;
```

---
### 3. Event Handling ⭐
**Time:** 5-15 min  
**Tests:** Event handlers, onClick/click events

**Challenge:**
```javascript
// Create a React component for: Event Handling
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Event Handling
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 4. State Management ⭐
**Time:** 5-15 min  
**Tests:** useState/reactive state, state updates

**Challenge:**
```javascript
// Create a React component for: State Management
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
import React, { useState } from 'react';

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

export default Counter;
```

---
### 5. List Rendering ⭐
**Time:** 5-15 min  
**Tests:** Array.map, keys, list rendering

**Challenge:**
```javascript
// Create a React component for: List Rendering
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: List Rendering
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 6. Conditional Rendering ⭐
**Time:** 5-15 min  
**Tests:** Ternary operator, && operator

**Challenge:**
```javascript
// Create a React component for: Conditional Rendering
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Conditional Rendering
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 7. Form Input Handling ⭐
**Time:** 5-15 min  
**Tests:** Controlled inputs, onChange

**Challenge:**
```javascript
// Create a React component for: Form Input Handling
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Form Input Handling
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 8. Two-Way Binding ⭐
**Time:** 5-15 min  
**Tests:** Controlled components, value binding

**Challenge:**
```javascript
// Create a React component for: Two-Way Binding
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Two-Way Binding
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 9. Component Lifecycle ⭐
**Time:** 5-15 min  
**Tests:** useEffect/ngOnInit, cleanup

**Challenge:**
```javascript
// Create a React component for: Component Lifecycle
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Component Lifecycle
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 10. CSS Styling ⭐
**Time:** 5-15 min  
**Tests:** Inline styles, style objects

**Challenge:**
```javascript
// Create a React component for: CSS Styling
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: CSS Styling
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 11. Click Counter ⭐
**Time:** 5-15 min  
**Tests:** State, event handling

**Challenge:**
```javascript
// Create a React component for: Click Counter
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Click Counter
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 12. Todo Item Component ⭐
**Time:** 5-15 min  
**Tests:** Props, conditional rendering

**Challenge:**
```javascript
// Create a React component for: Todo Item Component
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Todo Item Component
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 13. Show/Hide Toggle ⭐
**Time:** 5-15 min  
**Tests:** State toggle, conditional rendering

**Challenge:**
```javascript
// Create a React component for: Show/Hide Toggle
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Show/Hide Toggle
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 14. Parent-Child Communication ⭐
**Time:** 5-15 min  
**Tests:** Props, callbacks

**Challenge:**
```javascript
// Create a React component for: Parent-Child Communication
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Parent-Child Communication
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 15. Simple Form Validation ⭐
**Time:** 5-15 min  
**Tests:** Form validation, error messages

**Challenge:**
```javascript
// Create a React component for: Simple Form Validation
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Simple Form Validation
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 16. Array Filtering ⭐
**Time:** 5-15 min  
**Tests:** Array.filter, dynamic lists

**Challenge:**
```javascript
// Create a React component for: Array Filtering
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Array Filtering
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 17. Button Variants ⭐
**Time:** 5-15 min  
**Tests:** Props, conditional styling

**Challenge:**
```javascript
// Create a React component for: Button Variants
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Button Variants
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 18. Image Gallery ⭐
**Time:** 5-15 min  
**Tests:** Array rendering, image handling

**Challenge:**
```javascript
// Create a React component for: Image Gallery
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Image Gallery
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 19. Accordion Component ⭐
**Time:** 5-15 min  
**Tests:** State management, conditional rendering

**Challenge:**
```javascript
// Create a React component for: Accordion Component
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Accordion Component
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 20. Tab Component ⭐
**Time:** 5-15 min  
**Tests:** State, conditional rendering

**Challenge:**
```javascript
// Create a React component for: Tab Component
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Tab Component
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---

---

## 🎯 Tier 2: Mid-Level (25 questions)  
**Target:** 2-4 years experience | Time: 15-25 min each

### 21. Custom Hooks/Composables ⭐⭐
**Time:** 15-25 min  
**Tests:** Reusable logic, custom hooks

**Challenge:**
```javascript
// Create a React component for: Custom Hooks/Composables
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Custom Hooks/Composables
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 22. HTTP GET Request ⭐⭐
**Time:** 15-25 min  
**Tests:** Fetch/axios, async data loading

**Challenge:**
```javascript
// Create a React component for: HTTP GET Request
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: HTTP GET Request
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 23. HTTP POST with Form ⭐⭐
**Time:** 15-25 min  
**Tests:** Form submission, POST requests

**Challenge:**
```javascript
// Create a React component for: HTTP POST with Form
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: HTTP POST with Form
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 24. Error Handling ⭐⭐
**Time:** 15-25 min  
**Tests:** Try-catch, error states

**Challenge:**
```javascript
// Create a React component for: Error Handling
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Error Handling
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 25. Loading States ⭐⭐
**Time:** 15-25 min  
**Tests:** Loading indicators, async states

**Challenge:**
```javascript
// Create a React component for: Loading States
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Loading States
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 26. Routing Setup ⭐⭐
**Time:** 15-25 min  
**Tests:** Router configuration

**Challenge:**
```javascript
// Create a React component for: Routing Setup
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Routing Setup
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 27. Route Parameters ⭐⭐
**Time:** 15-25 min  
**Tests:** Dynamic routes, params

**Challenge:**
```javascript
// Create a React component for: Route Parameters
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Route Parameters
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 28. Nested Routes ⭐⭐
**Time:** 15-25 min  
**Tests:** Child routes, route hierarchy

**Challenge:**
```javascript
// Create a React component for: Nested Routes
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Nested Routes
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 29. Route Guards ⭐⭐
**Time:** 15-25 min  
**Tests:** Navigation guards, route protection

**Challenge:**
```javascript
// Create a React component for: Route Guards
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Route Guards
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 30. Form Validation (Advanced) ⭐⭐
**Time:** 15-25 min  
**Tests:** Complex validation rules

**Challenge:**
```javascript
// Create a React component for: Form Validation (Advanced)
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Form Validation (Advanced)
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 31. Debounced Search ⭐⭐
**Time:** 15-25 min  
**Tests:** Debouncing, performance

**Challenge:**
```javascript
// Create a React component for: Debounced Search
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Debounced Search
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 32. Infinite Scroll ⭐⭐
**Time:** 15-25 min  
**Tests:** Scroll detection, pagination

**Challenge:**
```javascript
// Create a React component for: Infinite Scroll
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Infinite Scroll
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 33. Pagination ⭐⭐
**Time:** 15-25 min  
**Tests:** Page navigation, data splitting

**Challenge:**
```javascript
// Create a React component for: Pagination
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Pagination
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 34. Modal/Dialog Component ⭐⭐
**Time:** 15-25 min  
**Tests:** Portal, overlay, focus trap

**Challenge:**
```javascript
// Create a React component for: Modal/Dialog Component
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Modal/Dialog Component
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 35. Dropdown with Outside Click ⭐⭐
**Time:** 15-25 min  
**Tests:** Event listeners, refs

**Challenge:**
```javascript
// Create a React component for: Dropdown with Outside Click
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Dropdown with Outside Click
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 36. Context API/Provide-Inject ⭐⭐
**Time:** 15-25 min  
**Tests:** Global state, dependency injection

**Challenge:**
```javascript
// Create a React component for: Context API/Provide-Inject
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Context API/Provide-Inject
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 37. Custom Directives/Pipes ⭐⭐
**Time:** 15-25 min  
**Tests:** Reusable directives, pipes

**Challenge:**
```javascript
// Create a React component for: Custom Directives/Pipes
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Custom Directives/Pipes
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 38. Lazy Loading ⭐⭐
**Time:** 15-25 min  
**Tests:** Code splitting, dynamic imports

**Challenge:**
```javascript
// Create a React component for: Lazy Loading
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Lazy Loading
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 39. Code Splitting ⭐⭐
**Time:** 15-25 min  
**Tests:** Bundle optimization

**Challenge:**
```javascript
// Create a React component for: Code Splitting
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Code Splitting
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 40. Local Storage Integration ⭐⭐
**Time:** 15-25 min  
**Tests:** Browser storage, persistence

**Challenge:**
```javascript
// Create a React component for: Local Storage Integration
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Local Storage Integration
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 41. WebSocket Connection ⭐⭐
**Time:** 15-25 min  
**Tests:** Real-time communication

**Challenge:**
```javascript
// Create a React component for: WebSocket Connection
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: WebSocket Connection
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 42. File Upload ⭐⭐
**Time:** 15-25 min  
**Tests:** File handling, FormData

**Challenge:**
```javascript
// Create a React component for: File Upload
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: File Upload
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 43. Drag and Drop ⭐⭐
**Time:** 15-25 min  
**Tests:** Drag events, data transfer

**Challenge:**
```javascript
// Create a React component for: Drag and Drop
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Drag and Drop
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 44. Multi-Step Form ⭐⭐
**Time:** 15-25 min  
**Tests:** Form state, navigation

**Challenge:**
```javascript
// Create a React component for: Multi-Step Form
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Multi-Step Form
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 45. Real-Time Validation ⭐⭐
**Time:** 15-25 min  
**Tests:** Live validation, feedback

**Challenge:**
```javascript
// Create a React component for: Real-Time Validation
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Real-Time Validation
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---

---

## 🎯 Tier 3: Senior Level (20 questions)
**Target:** 4-6 years experience | Time: 25-35 min each

### 46. State Management (Redux/NgRx) ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Global state, actions, reducers

**Challenge:**
```javascript
// Create a React component for: State Management (Redux/NgRx)
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: State Management (Redux/NgRx)
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 47. State with Async Actions ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Async state management

**Challenge:**
```javascript
// Create a React component for: State with Async Actions
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: State with Async Actions
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 48. Optimistic Updates ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** UI updates, rollback

**Challenge:**
```javascript
// Create a React component for: Optimistic Updates
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Optimistic Updates
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 49. Memoization/Performance ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** useMemo, useCallback, optimization

**Challenge:**
```javascript
// Create a React component for: Memoization/Performance
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Memoization/Performance
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 50. Virtual Scrolling ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Large lists, performance

**Challenge:**
```javascript
// Create a React component for: Virtual Scrolling
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Virtual Scrolling
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 51. Component Testing ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Unit tests, component testing

**Challenge:**
```javascript
// Create a React component for: Component Testing
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Component Testing
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 52. Integration Testing ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Component integration

**Challenge:**
```javascript
// Create a React component for: Integration Testing
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Integration Testing
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 53. E2E Testing Basics ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** End-to-end testing

**Challenge:**
```javascript
// Create a React component for: E2E Testing Basics
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: E2E Testing Basics
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 54. Custom Hooks Testing ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Hook testing, test utilities

**Challenge:**
```javascript
// Create a React component for: Custom Hooks Testing
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Custom Hooks Testing
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 55. Performance Profiling ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Performance analysis, optimization

**Challenge:**
```javascript
// Create a React component for: Performance Profiling
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Performance Profiling
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 56. Code-Splitting Strategy ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Bundle analysis, optimization

**Challenge:**
```javascript
// Create a React component for: Code-Splitting Strategy
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Code-Splitting Strategy
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 57. SSR Implementation ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Server-side rendering

**Challenge:**
```javascript
// Create a React component for: SSR Implementation
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: SSR Implementation
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 58. PWA Setup ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Progressive Web App

**Challenge:**
```javascript
// Create a React component for: PWA Setup
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: PWA Setup
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 59. Service Workers ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Offline support, caching

**Challenge:**
```javascript
// Create a React component for: Service Workers
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Service Workers
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 60. Accessibility (ARIA) ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** ARIA attributes, screen readers

**Challenge:**
```javascript
// Create a React component for: Accessibility (ARIA)
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Accessibility (ARIA)
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 61. Keyboard Navigation ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Keyboard events, focus management

**Challenge:**
```javascript
// Create a React component for: Keyboard Navigation
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Keyboard Navigation
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 62. Internationalization (i18n) ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Multi-language support

**Challenge:**
```javascript
// Create a React component for: Internationalization (i18n)
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Internationalization (i18n)
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 63. Theme Switching ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Dynamic theming, CSS variables

**Challenge:**
```javascript
// Create a React component for: Theme Switching
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Theme Switching
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 64. Advanced TypeScript Patterns ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Generics, utility types

**Challenge:**
```javascript
// Create a React component for: Advanced TypeScript Patterns
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Advanced TypeScript Patterns
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 65. Error Boundary ⭐⭐⭐
**Time:** 25-35 min  
**Tests:** Error handling, fallback UI

**Challenge:**
```javascript
// Create a React component for: Error Boundary
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Error Boundary
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---

---

## 🎯 Tier 4: Lead Level (10 questions)
**Target:** 6+ years experience | Time: 35-45 min each

### 66. Micro-Frontend Architecture ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Module federation, micro-frontends

**Challenge:**
```javascript
// Create a React component for: Micro-Frontend Architecture
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Micro-Frontend Architecture
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 67. Module Federation ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Shared modules, runtime integration

**Challenge:**
```javascript
// Create a React component for: Module Federation
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Module Federation
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 68. Design System Creation ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Component library, design tokens

**Challenge:**
```javascript
// Create a React component for: Design System Creation
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Design System Creation
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 69. Custom CLI Tool ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Code generation, tooling

**Challenge:**
```javascript
// Create a React component for: Custom CLI Tool
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Custom CLI Tool
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 70. Build Optimization ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Webpack/Vite optimization

**Challenge:**
```javascript
// Create a React component for: Build Optimization
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Build Optimization
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 71. Bundle Analysis ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Bundle size analysis

**Challenge:**
```javascript
// Create a React component for: Bundle Analysis
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Bundle Analysis
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 72. Monorepo Setup ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Workspace management, shared code

**Challenge:**
```javascript
// Create a React component for: Monorepo Setup
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Monorepo Setup
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 73. Custom Webpack/Vite Config ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** Build configuration

**Challenge:**
```javascript
// Create a React component for: Custom Webpack/Vite Config
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Custom Webpack/Vite Config
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 74. Advanced State Patterns ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** State machines, complex state

**Challenge:**
```javascript
// Create a React component for: Advanced State Patterns
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Advanced State Patterns
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
```

---
### 75. Performance Monitoring ⭐⭐⭐⭐
**Time:** 35-45 min  
**Tests:** APM, performance tracking

**Challenge:**
```javascript
// Create a React component for: Performance Monitoring
// Use functional component syntax
// Export the component
```

**What interviewers look for:**
```javascript
// Complete React solution for: Performance Monitoring
import React, { useState } from 'react';

function Component() {
  // Implementation here
  return <div>Solution</div>;
}

export default Component;
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
