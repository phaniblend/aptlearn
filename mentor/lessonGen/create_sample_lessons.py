#!/usr/bin/env python3
"""
Create 5 sample lessons following APT LEARN LESSON SPECIFICATION v1.0
For framework lessons: 25-30 steps, 600-700 lines, single language
"""
import json
from pathlib import Path

LESSON_GEN_DIR = Path(__file__).parent

def create_react_hello_world_lesson():
    """Create React Hello World Component lesson."""
    return {
        "id": "react-1-hello-world-component",
        "title": "Hello World Component",
        "technology": "React",
        "difficulty": "junior",
        "language": "javascript",
        "status": "draft",
        "metadata": {
            "time_estimate": "5 minutes",
            "tests": "Component basics, JSX syntax",
            "challenge_number": "1"
        },
        "flow": [
            {
                "stepId": "title",
                "mentorSays": "At the end of this lesson, you will be able to:\n\n1. Understand what React components are and how they work\n2. Create your first functional React component\n3. Use JSX syntax to define component structure\n4. Export and use components in your application\n5. Understand the relationship between components and the DOM",
                "action": "continue",
                "next": "problem-illustration"
            },
            {
                "stepId": "problem-illustration",
                "mentorSays": "Let's understand what creating a Hello World component means in React.\n\n**The Challenge:**\nCreate a React component that displays \"Hello World\" on the screen. This is the most fundamental React task - your first component!\n\n**What We're Building:**\nA simple, reusable component that renders text. When you use this component in your app, it will display \"Hello World\" wherever you place it.\n\n**Why This Matters:**\n\nReact is built entirely on components. Every piece of UI in a React application is a component. Understanding components is like understanding the alphabet before learning to read - it's absolutely fundamental.\n\n**Real-World Applications:**\n- Every React app starts with components\n- Components are reusable building blocks\n- Modern web apps (Facebook, Instagram, Netflix) are built with React components\n- Component-based architecture is the industry standard\n\n**Conceptual Foundation:**\n\nWHAT IS A COMPONENT?\nA component is like a custom HTML element that you create. Just like HTML has `<div>`, `<button>`, `<p>`, React lets you create your own elements like `<HelloWorld />`.\n\nThink of components like LEGO blocks:\n- Each block (component) is self-contained\n- You can combine blocks to build complex structures\n- Blocks can be reused anywhere\n- Blocks can contain other blocks\n\n**React Components vs HTML Elements:**\n\n```javascript\n// HTML element (built-in)\n<div>Hello World</div>\n\n// React component (you create it!)\n<HelloWorld />\n// Which renders: <div>Hello World</div>\n```\n\n**JSX - JavaScript XML:**\n\nReact uses JSX, which looks like HTML but is actually JavaScript. JSX lets you write HTML-like syntax that gets transformed into JavaScript function calls.\n\n```javascript\n// JSX (what you write)\nfunction HelloWorld() {\n  return <div>Hello World</div>;\n}\n\n// What it becomes (simplified)\nfunction HelloWorld() {\n  return React.createElement('div', null, 'Hello World');\n}\n```\n\n**Component Structure:**\n\nEvery React component follows this pattern:\n1. **Function Definition**: A JavaScript function\n2. **Return Statement**: Returns JSX (what to display)\n3. **Export**: Makes it available to other files\n\n**Step-by-Step Example:**\n\nLet's build a Hello World component:\n\n```javascript\n// Step 1: Import React (if needed in older React versions)\nimport React from 'react';\n\n// Step 2: Define the component function\nfunction HelloWorld() {\n  // Step 3: Return JSX\n  return (\n    <div>\n      <h1>Hello World</h1>\n    </div>\n  );\n}\n\n// Step 4: Export the component\nexport default HelloWorld;\n```\n\n**How to Use It:**\n\nOnce created, you can use your component anywhere:\n\n```javascript\n// In another component or App.js\nimport HelloWorld from './HelloWorld';\n\nfunction App() {\n  return (\n    <div>\n      <HelloWorld />\n      <HelloWorld />  {/* Can use it multiple times! */}\n    </div>\n  );\n}\n```\n\n**Key Concepts:**\n\n1. **Functional Components**: Modern React uses function components (not class components)\n2. **JSX Return**: Components return JSX, which describes what to render\n3. **Component Naming**: Use PascalCase (HelloWorld, not helloWorld)\n4. **Export Default**: Makes the component importable\n5. **Self-Contained**: Component includes everything it needs to render\n\n**What Makes This Special:**\n\nUnlike static HTML, React components are:\n- **Reusable**: Write once, use anywhere\n- **Composable**: Combine to build complex UIs\n- **Dynamic**: Can change based on data (we'll learn this later)\n- **Maintainable**: Each component is a separate piece\n\n**Common Patterns:**\n\n```javascript\n// Simple component\nfunction HelloWorld() {\n  return <h1>Hello World</h1>;\n}\n\n// Component with wrapper div\nfunction HelloWorld() {\n  return (\n    <div>\n      <h1>Hello World</h1>\n      <p>Welcome to React!</p>\n    </div>\n  );\n}\n\n// Component with fragment (no wrapper)\nfunction HelloWorld() {\n  return (\n    <>\n      <h1>Hello World</h1>\n      <p>Welcome to React!</p>\n    </>\n  );\n}\n```\n\n**Time estimate:** 5 minutes\n**Difficulty level:** Junior\n\nThis is your foundation - master this and you're ready to build amazing React applications!",
                "example": "// Example: Hello World Component\nfunction HelloWorld() {\n  return <h1>Hello World</h1>;\n}\n\nexport default HelloWorld;\n\n// Usage:\n<HelloWorld />",
                "action": "continue",
                "next": "thinking-challenge"
            },
            {
                "stepId": "thinking-challenge",
                "mentorSays": "Now that you understand what a component is, here's the real question:\n\nHow would YOU create your first React component?\n\nThink about it for a moment. What do you think you need to include?",
                "choices": [
                    {
                        "label": "I'll start with a basic function and build up",
                        "next": "explore-approach-1"
                    },
                    {
                        "label": "I want to see the complete solution directly",
                        "next": "explore-optimal"
                    },
                    {
                        "label": "I need more context about React",
                        "next": "problem-illustration"
                    }
                ]
            },
            {
                "stepId": "explore-approach-1",
                "mentorSays": "Perfect! Starting with a basic function is exactly the right approach. Let's build it step by step, then we'll see the complete solution.",
                "action": "continue",
                "next": "explore-optimal"
            },
            {
                "stepId": "explore-optimal",
                "mentorSays": "Excellent! Here's the optimal solution approach:\n\n```javascript\nimport React from 'react';\n\nfunction HelloWorld() {\n  return (\n    <div>\n      <h1>Hello World</h1>\n    </div>\n  );\n}\n\nexport default HelloWorld;\n```\n\nThis solution demonstrates React best practices:\n- Uses functional component syntax (modern React)\n- Returns JSX wrapped in a parent element\n- Properly exports for reuse\n- Clean, readable code\n\nNow let's build this together step by step!",
                "example": "import React from 'react';\n\nfunction HelloWorld() {\n  return (\n    <div>\n      <h1>Hello World</h1>\n    </div>\n  );\n}\n\nexport default HelloWorld;",
                "action": "continue",
                "next": "language-selection"
            },
            {
                "stepId": "language-selection",
                "mentorSays": "Great! Since this is a React JavaScript challenge, we'll use JavaScript. Let's start coding!",
                "action": "continue",
                "next": "component-check"
            },
            {
                "stepId": "component-check",
                "mentorSays": "Before we start coding, let me check: Do you understand what a React component is and how it differs from regular JavaScript functions?",
                "choices": [
                    {
                        "label": "Yes, I understand components",
                        "next": "jsx-check"
                    },
                    {
                        "label": "No, please explain",
                        "next": "component-explanation"
                    }
                ]
            },
            {
                "stepId": "component-explanation",
                "mentorSays": "Great question! Let me explain React components clearly.\n\n**What is a Component?**\n\nA React component is a JavaScript function that returns JSX (JavaScript XML). It's like a custom HTML element that you create.\n\n**Regular JavaScript Function:**\n```javascript\nfunction greet() {\n  return 'Hello';\n}\n// Returns a string\n```\n\n**React Component:**\n```javascript\nfunction Greet() {\n  return <h1>Hello</h1>;\n}\n// Returns JSX (what to display)\n```\n\n**Key Differences:**\n\n1. **Return Type**:\n   - Regular function: Returns data (string, number, object)\n   - Component: Returns JSX (describes UI)\n\n2. **Naming**:\n   - Regular function: camelCase (greet, calculateSum)\n   - Component: PascalCase (Greet, CalculateSum)\n\n3. **Usage**:\n   - Regular function: `greet()` - call it\n   - Component: `<Greet />` - use it like HTML\n\n**Example Comparison:**\n\n```javascript\n// Regular function\nfunction add(a, b) {\n  return a + b;\n}\nconst result = add(2, 3);  // Returns 5\n\n// React component\nfunction Add() {\n  return <div>2 + 3 = 5</div>;\n}\n// Use it: <Add />\n```\n\n**Why Components Matter:**\n\nComponents let you:\n- Create reusable UI pieces\n- Organize code logically\n- Build complex apps from simple parts\n- Update UI when data changes\n\n**Think of it this way:**\n- HTML gives you `<button>`, `<div>`, `<p>`\n- React lets you create `<UserCard>`, `<ProductList>`, `<Navigation>`\n- You build your own library of UI elements!\n\nNow you understand components - they're just functions that return JSX!",
                "example": "// Regular function\nfunction calculate() {\n  return 2 + 2;\n}\n\n// React component\nfunction Calculator() {\n  return <div>2 + 2 = 4</div>;\n}\n\n// Usage:\n<Calculator />",
                "action": "continue",
                "next": "jsx-check"
            },
            {
                "stepId": "jsx-check",
                "mentorSays": "Do you understand JSX syntax - the HTML-like code inside JavaScript?",
                "choices": [
                    {
                        "label": "Yes, I understand JSX",
                        "next": "export-check"
                    },
                    {
                        "label": "No, please explain",
                        "next": "jsx-explanation"
                    }
                ]
            },
            {
                "stepId": "jsx-explanation",
                "mentorSays": "JSX (JavaScript XML) is React's way of writing HTML inside JavaScript. It looks like HTML but it's actually JavaScript!\n\n**What is JSX?**\n\nJSX lets you write HTML-like syntax that React converts into JavaScript function calls.\n\n**JSX Example:**\n```javascript\nfunction Hello() {\n  return <h1>Hello World</h1>;\n}\n```\n\n**What It Becomes:**\n```javascript\nfunction Hello() {\n  return React.createElement('h1', null, 'Hello World');\n}\n```\n\n**JSX Rules:**\n\n1. **Must Return One Element:**\n```javascript\n// ❌ Wrong - multiple elements\nreturn (\n  <h1>Hello</h1>\n  <p>World</p>\n);\n\n// ✅ Right - wrapped in one element\nreturn (\n  <div>\n    <h1>Hello</h1>\n    <p>World</p>\n  </div>\n);\n```\n\n2. **Use className, not class:**\n```javascript\n// ❌ Wrong\n<div class=\"container\">\n\n// ✅ Right\n<div className=\"container\">\n```\n\n3. **Self-Closing Tags:**\n```javascript\n// ✅ Both are correct\n<img src=\"...\" />\n<br />\n```\n\n4. **JavaScript in JSX (Curly Braces):**\n```javascript\nconst name = 'World';\nreturn <h1>Hello {name}</h1>;  // Hello World\n```\n\n**JSX vs HTML:**\n\n| HTML | JSX |\n|------|-----|\n| `<div class=\"box\">` | `<div className=\"box\">` |\n| `<input>` | `<input />` |\n| `onclick=\"...\"` | `onClick={...}` |\n| `style=\"color: red\"` | `style={{color: 'red'}}` |\n\n**Why JSX?**\n\n- Looks familiar (like HTML)\n- Easy to read and write\n- Combines HTML and JavaScript\n- React handles the conversion\n\n**Example:**\n```javascript\nfunction Greeting() {\n  const name = 'Alice';\n  const age = 25;\n  \n  return (\n    <div>\n      <h1>Hello {name}!</h1>\n      <p>You are {age} years old</p>\n    </div>\n  );\n}\n```\n\nJSX is just HTML-like syntax in JavaScript - that's it!",
                "example": "// JSX example\nconst name = 'React';\nreturn (\n  <div className=\"container\">\n    <h1>Hello {name}!</h1>\n    <p>This is JSX</p>\n  </div>\n);",
                "action": "continue",
                "next": "export-check"
            },
            {
                "stepId": "export-check",
                "mentorSays": "Do you understand JavaScript exports and how to make components available to other files?",
                "choices": [
                    {
                        "label": "Yes, I understand exports",
                        "next": "coding-start-js"
                    },
                    {
                        "label": "No, please explain",
                        "next": "export-explanation"
                    }
                ]
            },
            {
                "stepId": "export-explanation",
                "mentorSays": "Exports let you share code between files. In React, you export components so other files can import and use them.\n\n**Why Export?**\n\nWhen you create a component in one file, you need to export it so other files can use it.\n\n**Export Default:**\n\n```javascript\n// HelloWorld.js\nfunction HelloWorld() {\n  return <h1>Hello World</h1>;\n}\n\nexport default HelloWorld;  // Export it!\n```\n\n**Import in Another File:**\n\n```javascript\n// App.js\nimport HelloWorld from './HelloWorld';  // Import it!\n\nfunction App() {\n  return <HelloWorld />;  // Use it!\n}\n```\n\n**How It Works:**\n\n1. **Create component** in HelloWorld.js\n2. **Export it** with `export default`\n3. **Import it** in another file with `import`\n4. **Use it** like `<HelloWorld />`\n\n**Example:**\n\n```javascript\n// components/Button.js\nfunction Button() {\n  return <button>Click Me</button>;\n}\n\nexport default Button;\n\n// App.js\nimport Button from './components/Button';\n\nfunction App() {\n  return (\n    <div>\n      <Button />\n      <Button />  {/* Can use multiple times! */}\n    </div>\n  );\n}\n```\n\n**Key Points:**\n\n- `export default` = export one main thing from file\n- `import X from './file'` = import the default export\n- File path must be correct\n- Component name in import can be different (but usually same)\n\n**Without Export:**\n```javascript\n// ❌ Can't use it in other files\nfunction HelloWorld() {\n  return <h1>Hello</h1>;\n}\n// No export = not available elsewhere\n```\n\n**With Export:**\n```javascript\n// ✅ Can use it anywhere\nfunction HelloWorld() {\n  return <h1>Hello</h1>;\n}\nexport default HelloWorld;  // Now available!\n```\n\nExport = make it available, Import = use it elsewhere!",
                "example": "// File: HelloWorld.js\nexport default function HelloWorld() {\n  return <h1>Hello World</h1>;\n}\n\n// File: App.js\nimport HelloWorld from './HelloWorld';\n\nfunction App() {\n  return <HelloWorld />;\n}",
                "action": "continue",
                "next": "coding-start-js"
            },
            {
                "stepId": "coding-start-js",
                "mentorSays": "Perfect! Now let's build the Hello World component step by step. We'll start with the basic structure and then add the implementation.",
                "action": "continue",
                "next": "coding-step-1-js"
            },
            {
                "stepId": "coding-step-1-js",
                "mentorSays": "First, let's import React. In modern React (17+), you don't always need this, but it's good practice and makes the code clearer.",
                "example": "import React from 'react';",
                "action": "continue",
                "next": "coding-step-2-js"
            },
            {
                "stepId": "coding-step-2-js",
                "mentorSays": "Now let's define our component function. We use PascalCase naming (HelloWorld, not helloWorld) for components.",
                "example": "import React from 'react';\n\nfunction HelloWorld() {\n  // Component body\n}",
                "action": "continue",
                "next": "coding-step-3-js"
            },
            {
                "stepId": "coding-step-3-js",
                "mentorSays": "Inside the function, we return JSX. Let's return a simple div with an h1 element containing \"Hello World\".",
                "example": "import React from 'react';\n\nfunction HelloWorld() {\n  return (\n    <div>\n      <h1>Hello World</h1>\n    </div>\n  );\n}",
                "action": "continue",
                "next": "coding-step-4-js"
            },
            {
                "stepId": "coding-step-4-js",
                "mentorSays": "Great! Now we need to export the component so it can be used in other files. We use `export default`.",
                "example": "import React from 'react';\n\nfunction HelloWorld() {\n  return (\n    <div>\n      <h1>Hello World</h1>\n    </div>\n  );\n}\n\nexport default HelloWorld;",
                "action": "continue",
                "next": "coding-complete-js"
            },
            {
                "stepId": "coding-complete-js",
                "mentorSays": "Perfect! Here's the complete solution with all the pieces together:",
                "example": "import React from 'react';\n\nfunction HelloWorld() {\n  return (\n    <div>\n      <h1>Hello World</h1>\n    </div>\n  );\n}\n\nexport default HelloWorld;\n\n// Usage in another file:\n// import HelloWorld from './HelloWorld';\n// <HelloWorld />",
                "action": "continue",
                "next": "test-code-js"
            },
            {
                "stepId": "test-code-js",
                "mentorSays": "Perfect! Now test your component. Create a file and use it:\n\n**Test Steps:**\n1. Save the component in `HelloWorld.js`\n2. Import it in your `App.js`\n3. Use it: `<HelloWorld />`\n4. Run your React app\n5. Verify \"Hello World\" appears on screen\n\n**Expected Result:**\nYou should see \"Hello World\" displayed as an h1 heading on your page.\n\n**Try These Variations:**\n- Change the text to something else\n- Add more elements inside the div\n- Use the component multiple times\n- Try different HTML elements (p, span, etc.)",
                "example": "// App.js\nimport HelloWorld from './HelloWorld';\n\nfunction App() {\n  return (\n    <div>\n      <HelloWorld />\n    </div>\n  );\n}\n\nexport default App;",
                "action": "continue",
                "next": "final"
            },
            {
                "stepId": "final",
                "mentorSays": "🎉 Well done! You've created your first React component!\n\n**Key Takeaways:**\n- React components are JavaScript functions that return JSX\n- Components use PascalCase naming (HelloWorld)\n- JSX looks like HTML but is JavaScript\n- Export components with `export default` to use them elsewhere\n- Components are reusable building blocks for React applications\n\n**What You've Learned:**\n- How to create a functional component\n- JSX syntax basics\n- Component export/import pattern\n- Component structure and organization\n\n**Next Steps:**\n- Try creating components with props (data passing)\n- Learn about component state\n- Explore event handling in components\n- Build more complex component compositions\n\n**Related Challenges:**\n- Props/Input Binding - Pass data to components\n- Event Handling - Make components interactive\n- State Management - Add dynamic behavior\n- Component Composition - Combine multiple components\n\nKeep practicing! Every React app is built from components like this one.",
                "action": "continue"
            }
        ]
    }

def create_angular_component_input_lesson():
    """Create Angular Component Input lesson."""
    return {
        "id": "angular-8-component-input",
        "title": "Component Input",
        "technology": "Angular",
        "difficulty": "junior",
        "language": "typescript",
        "status": "draft",
        "metadata": {
            "time_estimate": "12 minutes",
            "tests": "@Input decorator, parent-child communication",
            "challenge_number": "8"
        },
        "flow": [
            {
                "stepId": "title",
                "mentorSays": "At the end of this lesson, you will be able to:\n\n1. Understand Angular's component communication patterns\n2. Use the @Input() decorator to receive data from parent components\n3. Implement property binding to pass data from parent to child\n4. Create reusable components that accept data\n5. Understand unidirectional data flow in Angular",
                "action": "continue",
                "next": "problem-illustration"
            },
            {
                "stepId": "problem-illustration",
                "mentorSays": "Let's understand Angular component input and parent-child communication.\n\n**The Challenge:**\nCreate a child component that receives data from its parent component using the @Input() decorator. The parent should be able to pass data (like a user's name and email) to the child, and the child should display it.\n\n**What We're Building:**\nA reusable child component (UserCard) that displays user information. The parent component will pass user data to this child component, demonstrating Angular's data flow pattern.\n\n**Why This Matters:**\n\nComponent communication is fundamental to Angular. In real applications, you rarely build isolated components - they need to share data. Understanding @Input() is essential for:\n- Building reusable components\n- Creating component hierarchies\n- Implementing proper data flow\n- Following Angular best practices\n\n**Real-World Applications:**\n- Product cards that receive product data\n- User profiles that display user information\n- Data tables that receive row data\n- Dashboard widgets that receive configuration\n- Any component that needs to be reusable with different data\n\n**Conceptual Foundation:**\n\nANGULAR'S DATA FLOW:\nAngular follows unidirectional data flow: Parent → Child (one direction).\n\n```typescript\n// Parent Component\n@Component({\n  template: '<app-user-card [name]=\"userName\" />'\n})\n\n// Child Component\n@Component({\n  template: '<h3>{{ name }}</h3>'\n})\nexport class UserCardComponent {\n  @Input() name!: string;  // Receives data from parent\n}\n```\n\n**The @Input() Decorator:**\n\n@Input() marks a property as an input property. This means:\n- The property can receive data from a parent component\n- The data is passed via property binding `[property]=\"value\"`\n- The property is available in the child component's template\n\n**Component Communication Analogy:**\n\nThink of components like functions:\n\n```typescript\n// Function takes parameters\nfunction greet(name: string) {\n  return `Hello ${name}`;\n}\ngreet('Alice');  // Pass data\n\n// Component takes @Input properties\nclass UserCard {\n  @Input() name!: string;  // Receives data\n}\n<app-user-card [name]=\"'Alice'\" />  // Pass data\n```\n\n**Step-by-Step Example:**\n\nLet's build a UserCard component:\n\n```typescript\n// Child Component (user-card.component.ts)\nimport { Component, Input } from '@angular/core';\n\n@Component({\n  selector: 'app-user-card',\n  template: `\n    <div class=\"card\">\n      <h3>{{ name }}</h3>\n      <p>{{ email }}</p>\n    </div>\n  `,\n  standalone: true\n})\nexport class UserCardComponent {\n  @Input() name!: string;\n  @Input() email!: string;\n}\n```\n\n```typescript\n// Parent Component (app.component.ts)\nimport { Component } from '@angular/core';\nimport { UserCardComponent } from './user-card.component';\n\n@Component({\n  selector: 'app-root',\n  template: `\n    <app-user-card \n      [name]=\"'John Doe'\" \n      [email]=\"'john@example.com'\"\n    />\n  `,\n  standalone: true,\n  imports: [UserCardComponent]\n})\nexport class AppComponent {}\n```\n\n**Property Binding Syntax:**\n\n```typescript\n// Square brackets [property] indicate property binding\n[name]=\"'John'\"     // Pass string\n[name]=\"userName\"   // Pass variable\n[name]=\"getUser()\"  // Pass function result\n```\n\n**Key Concepts:**\n\n1. **@Input() Decorator**: Marks property to receive data\n2. **Property Binding**: `[property]=\"value\"` passes data\n3. **TypeScript Types**: Use `!` for required inputs, `?` for optional\n4. **Template Interpolation**: `{{ property }}` displays data\n5. **Standalone Components**: Modern Angular (no NgModule needed)\n\n**Multiple Inputs:**\n\n```typescript\n@Component({\n  selector: 'app-product-card',\n  template: `\n    <div>\n      <h3>{{ title }}</h3>\n      <p>Price: ${{ price }}</p>\n      <p>Stock: {{ inStock ? 'Available' : 'Out of Stock' }}</p>\n    </div>\n  `\n})\nexport class ProductCardComponent {\n  @Input() title!: string;\n  @Input() price!: number;\n  @Input() inStock!: boolean;\n}\n```\n\n**Optional vs Required Inputs:**\n\n```typescript\n// Required input (must be provided)\n@Input() name!: string;\n\n// Optional input (can be undefined)\n@Input() description?: string;\n```\n\n**Time estimate:** 12 minutes\n**Difficulty level:** Junior\n\nThis pattern is used in every Angular application - master it and you'll build reusable, maintainable components!",
                "example": "// Child Component\n@Component({\n  selector: 'app-user-card',\n  template: '<h3>{{ name }}</h3>'\n})\nexport class UserCardComponent {\n  @Input() name!: string;\n}\n\n// Parent Component\n<app-user-card [name]=\"'John'\" />",
                "action": "continue",
                "next": "thinking-challenge"
            },
            {
                "stepId": "thinking-challenge",
                "mentorSays": "Now that you understand component input, here's the real question:\n\nHow would YOU create a component that receives data from its parent?\n\nThink about it - what pieces do you need?",
                "choices": [
                    {
                        "label": "I'll start with the child component and add @Input",
                        "next": "explore-approach-1"
                    },
                    {
                        "label": "I want to see the complete solution",
                        "next": "explore-optimal"
                    },
                    {
                        "label": "I need more context",
                        "next": "problem-illustration"
                    }
                ]
            },
            {
                "stepId": "explore-approach-1",
                "mentorSays": "Perfect! Starting with the child component is the right approach. We'll add @Input properties, then show how the parent passes data.",
                "action": "continue",
                "next": "explore-optimal"
            },
            {
                "stepId": "explore-optimal",
                "mentorSays": "Excellent! Here's the optimal solution:\n\n```typescript\n// Child Component\nimport { Component, Input } from '@angular/core';\n\n@Component({\n  selector: 'app-user-card',\n  template: `\n    <div class=\"card\">\n      <h3>{{ name }}</h3>\n      <p>{{ email }}</p>\n    </div>\n  `,\n  standalone: true\n})\nexport class UserCardComponent {\n  @Input() name!: string;\n  @Input() email!: string;\n}\n\n// Parent Component\n@Component({\n  selector: 'app-parent',\n  template: `\n    <app-user-card \n      [name]=\"'John Doe'\" \n      [email]=\"'john@example.com'\"\n    />\n  `,\n  standalone: true,\n  imports: [UserCardComponent]\n})\nexport class ParentComponent {}\n```\n\nThis demonstrates Angular's unidirectional data flow pattern. Let's build it step by step!",
                "example": "// Complete parent-child communication example",
                "action": "continue",
                "next": "language-selection"
            },
            {
                "stepId": "language-selection",
                "mentorSays": "Great! Since this is an Angular challenge, we'll use TypeScript. Let's start coding!",
                "action": "continue",
                "next": "component-check"
            },
            {
                "stepId": "component-check",
                "mentorSays": "Before we start, let me check: Do you understand Angular components and the @Component decorator?",
                "choices": [
                    {
                        "label": "Yes, I understand components",
                        "next": "decorator-check"
                    },
                    {
                        "label": "No, please explain",
                        "next": "component-explanation"
                    }
                ]
            },
            {
                "stepId": "component-explanation",
                "mentorSays": "Angular components are the building blocks of Angular applications. Let me explain:\n\n**What is a Component?**\n\nA component in Angular consists of:\n1. **TypeScript Class**: Contains component logic\n2. **Template**: HTML that defines the view\n3. **Decorator**: @Component metadata\n4. **Styles**: Component-specific CSS (optional)\n\n**Basic Component Structure:**\n\n```typescript\nimport { Component } from '@angular/core';\n\n@Component({\n  selector: 'app-example',  // How you use it\n  template: '<h1>Hello</h1>',  // What it displays\n  standalone: true  // Modern Angular (no NgModule)\n})\nexport class ExampleComponent {\n  // Component logic here\n}\n```\n\n**The @Component Decorator:**\n\nThe @Component decorator tells Angular this class is a component. It provides metadata:\n- `selector`: HTML tag name (like `<app-example>`)\n- `template`: HTML template (what to display)\n- `standalone`: Modern Angular feature (makes component independent)\n\n**Component Usage:**\n\n```typescript\n// Define component\n@Component({\n  selector: 'app-greeting',\n  template: '<p>Hello World</p>',\n  standalone: true\n})\nexport class GreetingComponent {}\n\n// Use it in template\n<app-greeting></app-greeting>\n```\n\n**Components are Reusable:**\n\n```typescript\n// Use the same component multiple times\n<app-greeting></app-greeting>\n<app-greeting></app-greeting>\n<app-greeting></app-greeting>\n```\n\n**Key Points:**\n- Components are TypeScript classes\n- @Component decorator provides metadata\n- Template defines the view\n- Selector is how you use it\n- Standalone components are modern Angular\n\nNow you understand components - they're classes with templates!",
                "example": "@Component({\n  selector: 'app-example',\n  template: '<h1>Hello</h1>',\n  standalone: true\n})\nexport class ExampleComponent {}",
                "action": "continue",
                "next": "decorator-check"
            },
            {
                "stepId": "decorator-check",
                "mentorSays": "Do you understand TypeScript decorators like @Component and @Input?",
                "choices": [
                    {
                        "label": "Yes, I understand decorators",
                        "next": "property-binding-check"
                    },
                    {
                        "label": "No, please explain",
                        "next": "decorator-explanation"
                    }
                ]
            },
            {
                "stepId": "decorator-explanation",
                "mentorSays": "Decorators are special functions that modify classes, methods, or properties. In Angular, decorators provide metadata to the framework.\n\n**What are Decorators?**\n\nDecorators are functions prefixed with `@` that modify or add information to code.\n\n**Common Angular Decorators:**\n\n```typescript\n// @Component - Marks a class as a component\n@Component({\n  selector: 'app-user',\n  template: '...'\n})\nexport class UserComponent {}\n\n// @Input() - Marks a property to receive data from parent\n@Input() name!: string;\n\n// @Output() - Marks an EventEmitter to send data to parent\n@Output() clicked = new EventEmitter();\n\n// @Injectable() - Marks a class as a service\n@Injectable({\n  providedIn: 'root'\n})\nexport class DataService {}\n```\n\n**How @Input() Works:**\n\n```typescript\nclass UserCardComponent {\n  @Input() name!: string;  // Decorator marks this as input\n}\n```\n\nThe @Input() decorator:\n- Tells Angular this property can receive data\n- Enables property binding from parent\n- Makes the property available in template\n\n**Without Decorator:**\n```typescript\n// ❌ Can't receive data from parent\nclass UserCardComponent {\n  name!: string;  // Just a regular property\n}\n```\n\n**With Decorator:**\n```typescript\n// ✅ Can receive data from parent\nclass UserCardComponent {\n  @Input() name!: string;  // Input property\n}\n```\n\n**Decorator Syntax:**\n\n```typescript\n// Decorator before property\n@Input() name!: string;\n\n// Decorator before class\n@Component({...})\nexport class MyComponent {}\n\n// Decorator before method\n@HostListener('click')\nhandleClick() {}\n```\n\n**Key Points:**\n- Decorators start with `@`\n- They modify or add metadata\n- Angular uses them extensively\n- @Input() enables parent-child communication\n\nDecorators are Angular's way of adding special behavior to your code!",
                "example": "// @Input decorator example\nclass UserCardComponent {\n  @Input() name!: string;  // Receives data\n  @Input() age?: number;   // Optional input\n}\n\n// Usage:\n<app-user-card [name]=\"'John'\" />",
                "action": "continue",
                "next": "property-binding-check"
            },
            {
                "stepId": "property-binding-check",
                "mentorSays": "Do you understand property binding syntax `[property]=\"value\"` in Angular templates?",
                "choices": [
                    {
                        "label": "Yes, I understand property binding",
                        "next": "coding-start-ts"
                    },
                    {
                        "label": "No, please explain",
                        "next": "property-binding-explanation"
                    }
                ]
            },
            {
                "stepId": "property-binding-explanation",
                "mentorSays": "Property binding lets you set element or component properties dynamically. The square brackets `[property]` indicate property binding.\n\n**What is Property Binding?**\n\nProperty binding sets a property value from a component's data.\n\n**Syntax:**\n```html\n[property]=\"expression\"\n```\n\n**Examples:**\n\n```html\n<!-- Bind to HTML element property -->\n<img [src]=\"imageUrl\" />\n<button [disabled]=\"isDisabled\">Click</button>\n<div [hidden]=\"isHidden\">Content</div>\n\n<!-- Bind to component @Input property -->\n<app-user-card [name]=\"userName\" />\n<app-product [price]=\"productPrice\" />\n```\n\n**Property Binding vs Interpolation:**\n\n```html\n<!-- Interpolation: Display value -->\n<p>{{ userName }}</p>\n\n<!-- Property Binding: Set property -->\n<app-user-card [name]=\"userName\" />\n```\n\n**Different Binding Types:**\n\n```html\n<!-- String binding -->\n[title]=\"'Hello'\"\n[name]=\"userName\"\n\n<!-- Boolean binding -->\n[disabled]=\"true\"\n[hidden]=\"isHidden\"\n\n<!-- Number binding -->\n[count]=\"5\"\n[price]=\"productPrice\"\n\n<!-- Object binding -->\n[user]=\"currentUser\"\n```\n\n**Key Points:**\n- Square brackets `[]` indicate property binding\n- Expression inside quotes is evaluated\n- Can bind to HTML properties or component inputs\n- One-way binding (parent → child)\n\n**Example:**\n\n```typescript\n// Component\nexport class AppComponent {\n  userName = 'John';\n  isActive = true;\n}\n```\n\n```html\n<!-- Template -->\n<app-user-card [name]=\"userName\" />\n<button [disabled]=\"!isActive\">Submit</button>\n```\n\nProperty binding connects component data to template properties!",
                "example": "// Component\nexport class AppComponent {\n  userName = 'Alice';\n}\n\n// Template\n<app-user-card [name]=\"userName\" />",
                "action": "continue",
                "next": "coding-start-ts"
            },
            {
                "stepId": "coding-start-ts",
                "mentorSays": "Perfect! Now let's build the component input solution step by step. We'll create both the child and parent components.",
                "action": "continue",
                "next": "coding-step-1-ts"
            },
            {
                "stepId": "coding-step-1-ts",
                "mentorSays": "First, let's import the necessary Angular modules. We need Component and Input from @angular/core.",
                "example": "import { Component, Input } from '@angular/core';",
                "action": "continue",
                "next": "coding-step-2-ts"
            },
            {
                "stepId": "coding-step-2-ts",
                "mentorSays": "Now let's create the child component with the @Component decorator. We'll set up the selector and template.",
                "example": "import { Component, Input } from '@angular/core';\n\n@Component({\n  selector: 'app-user-card',\n  template: `\n    <div class=\"card\">\n      <h3>{{ name }}</h3>\n      <p>{{ email }}</p>\n    </div>\n  `,\n  standalone: true\n})\nexport class UserCardComponent {\n  // Properties will go here\n}",
                "action": "continue",
                "next": "coding-step-3-ts"
            },
            {
                "stepId": "coding-step-3-ts",
                "mentorSays": "Now let's add the @Input() properties. These will receive data from the parent component.",
                "example": "import { Component, Input } from '@angular/core';\n\n@Component({\n  selector: 'app-user-card',\n  template: `\n    <div class=\"card\">\n      <h3>{{ name }}</h3>\n      <p>{{ email }}</p>\n    </div>\n  `,\n  standalone: true\n})\nexport class UserCardComponent {\n  @Input() name!: string;\n  @Input() email!: string;\n}",
                "action": "continue",
                "next": "coding-step-4-ts"
            },
            {
                "stepId": "coding-step-4-ts",
                "mentorSays": "Great! Now let's create the parent component that will use our child component and pass data to it.",
                "example": "import { Component } from '@angular/core';\nimport { UserCardComponent } from './user-card.component';\n\n@Component({\n  selector: 'app-parent',\n  template: `\n    <app-user-card \n      [name]=\"'John Doe'\" \n      [email]=\"'john@example.com'\"\n    />\n  `,\n  standalone: true,\n  imports: [UserCardComponent]\n})\nexport class ParentComponent {}",
                "action": "continue",
                "next": "coding-complete-ts"
            },
            {
                "stepId": "coding-complete-ts",
                "mentorSays": "Perfect! Here's the complete solution with both components:",
                "example": "// user-card.component.ts (Child)\nimport { Component, Input } from '@angular/core';\n\n@Component({\n  selector: 'app-user-card',\n  template: `\n    <div class=\"card\">\n      <h3>{{ name }}</h3>\n      <p>{{ email }}</p>\n    </div>\n  `,\n  standalone: true\n})\nexport class UserCardComponent {\n  @Input() name!: string;\n  @Input() email!: string;\n}\n\n// parent.component.ts (Parent)\nimport { Component } from '@angular/core';\nimport { UserCardComponent } from './user-card.component';\n\n@Component({\n  selector: 'app-parent',\n  template: `\n    <app-user-card \n      [name]=\"'John Doe'\" \n      [email]=\"'john@example.com'\"\n    />\n  `,\n  standalone: true,\n  imports: [UserCardComponent]\n})\nexport class ParentComponent {}",
                "action": "continue",
                "next": "test-code-ts"
            },
            {
                "stepId": "test-code-ts",
                "mentorSays": "Perfect! Now test your components:\n\n**Test Steps:**\n1. Create both component files\n2. Import UserCardComponent in parent\n3. Use property binding to pass data\n4. Run your Angular app\n5. Verify the user card displays the name and email\n\n**Expected Result:**\nYou should see a card displaying \"John Doe\" and \"john@example.com\".\n\n**Try These Variations:**\n- Pass different names and emails\n- Add more @Input properties (age, phone, etc.)\n- Use multiple UserCard components with different data\n- Try binding to component properties instead of strings",
                "example": "// Test with different data\n<app-user-card \n  [name]=\"'Alice Smith'\" \n  [email]=\"'alice@example.com'\"\n/>\n\n<app-user-card \n  [name]=\"'Bob Johnson'\" \n  [email]=\"'bob@example.com'\"\n/>",
                "action": "continue",
                "next": "final"
            },
            {
                "stepId": "final",
                "mentorSays": "🎉 Well done! You've mastered Angular component input!\n\n**Key Takeaways:**\n- @Input() decorator marks properties that receive data from parent\n- Property binding `[property]=\"value\"` passes data from parent to child\n- Angular follows unidirectional data flow (parent → child)\n- Components become reusable when they accept inputs\n- TypeScript types ensure type safety for inputs\n\n**What You've Learned:**\n- How to create components that receive data\n- Property binding syntax and usage\n- Parent-child component communication\n- Reusable component patterns\n\n**Next Steps:**\n- Learn @Output() for child-to-parent communication\n- Explore two-way binding with ngModel\n- Build more complex component hierarchies\n- Practice with different data types (objects, arrays)\n\n**Related Challenges:**\n- Component Output - Send data from child to parent\n- Two-Way Binding - Bidirectional data flow\n- Event Handling - Make components interactive\n- Component Lifecycle - Understand component lifecycle hooks\n\nKeep practicing! Component communication is essential for building Angular applications.",
                "action": "continue"
            }
        ]
    }

# Continue with 3 more lessons...
# (I'll create the remaining 3 in the next part due to length)

if __name__ == '__main__':
    lessons = [
        create_react_hello_world_lesson(),
        create_angular_component_input_lesson(),
        # Add 3 more...
    ]
    
    for lesson in lessons:
        file_path = LESSON_GEN_DIR / lesson['technology'].lower() / f"{lesson['id']}.json"
        file_path.parent.mkdir(exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(lesson, f, indent=2, ensure_ascii=False)
        
        print(f"Created: {file_path}")

