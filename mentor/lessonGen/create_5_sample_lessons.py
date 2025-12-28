#!/usr/bin/env python3
"""
Create 5 sample lessons following APT LEARN LESSON SPECIFICATION v1.0
Framework lessons: 25-30 steps, 600-700 lines, single language
"""
import json
from pathlib import Path

LESSON_GEN_DIR = Path(__file__).parent

def create_react_hello_world():
    """Lesson 1: React Hello World Component"""
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
                    {"label": "I'll start with a basic function and build up", "next": "explore-approach-1"},
                    {"label": "I want to see the complete solution directly", "next": "explore-optimal"},
                    {"label": "I need more context about React", "next": "problem-illustration"}
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
                    {"label": "Yes, I understand components", "next": "jsx-check"},
                    {"label": "No, please explain", "next": "component-explanation"}
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
                    {"label": "Yes, I understand JSX", "next": "export-check"},
                    {"label": "No, please explain", "next": "jsx-explanation"}
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
                    {"label": "Yes, I understand exports", "next": "function-check"},
                    {"label": "No, please explain", "next": "export-explanation"}
                ]
            },
            {
                "stepId": "export-explanation",
                "mentorSays": "Exports let you share code between files. In React, you export components so other files can import and use them.\n\n**Why Export?**\n\nWhen you create a component in one file, you need to export it so other files can use it.\n\n**Export Default:**\n\n```javascript\n// HelloWorld.js\nfunction HelloWorld() {\n  return <h1>Hello World</h1>;\n}\n\nexport default HelloWorld;  // Export it!\n```\n\n**Import in Another File:**\n\n```javascript\n// App.js\nimport HelloWorld from './HelloWorld';  // Import it!\n\nfunction App() {\n  return <HelloWorld />;  // Use it!\n}\n```\n\n**How It Works:**\n\n1. **Create component** in HelloWorld.js\n2. **Export it** with `export default`\n3. **Import it** in another file with `import`\n4. **Use it** like `<HelloWorld />`\n\n**Example:**\n\n```javascript\n// components/Button.js\nfunction Button() {\n  return <button>Click Me</button>;\n}\n\nexport default Button;\n\n// App.js\nimport Button from './components/Button';\n\nfunction App() {\n  return (\n    <div>\n      <Button />\n      <Button />  {/* Can use multiple times! */}\n    </div>\n  );\n}\n```\n\n**Key Points:**\n\n- `export default` = export one main thing from file\n- `import X from './file'` = import the default export\n- File path must be correct\n- Component name in import can be different (but usually same)\n\n**Without Export:**\n```javascript\n// ❌ Can't use it in other files\nfunction HelloWorld() {\n  return <h1>Hello</h1>;\n}\n// No export = not available elsewhere\n```\n\n**With Export:**\n```javascript\n// ✅ Can use it anywhere\nfunction HelloWorld() {\n  return <h1>Hello</h1>;\n}\nexport default HelloWorld;  // Now available!\n```\n\nExport = make it available, Import = use it elsewhere!",
                "example": "// File: HelloWorld.js\nexport default function HelloWorld() {\n  return <h1>Hello World</h1>;\n}\n\n// File: App.js\nimport HelloWorld from './HelloWorld';\n\nfunction App() {\n  return <HelloWorld />;\n}",
                "action": "continue",
                "next": "function-check"
            },
            {
                "stepId": "function-check",
                "mentorSays": "Do you understand JavaScript functions and how to define them?",
                "choices": [
                    {"label": "Yes, I understand functions", "next": "return-check"},
                    {"label": "No, please explain", "next": "function-explanation"}
                ]
            },
            {
                "stepId": "function-explanation",
                "mentorSays": "Functions are reusable blocks of code. In React, components ARE functions!\n\n**What is a Function?**\n\nA function is a block of code that performs a task. You can call it multiple times.\n\n**Function Syntax:**\n\n```javascript\n// Function declaration\nfunction greet() {\n  return 'Hello';\n}\n\n// Call the function\ngreet();  // Returns 'Hello'\n```\n\n**Functions with Parameters:**\n\n```javascript\nfunction greet(name) {\n  return `Hello ${name}`;\n}\n\ngreet('Alice');  // Returns 'Hello Alice'\n```\n\n**React Components are Functions:**\n\n```javascript\n// Regular function\nfunction add(a, b) {\n  return a + b;\n}\n\n// React component (also a function!)\nfunction HelloWorld() {\n  return <h1>Hello World</h1>;\n}\n```\n\n**Key Points:**\n- Functions are reusable code blocks\n- Components are special functions that return JSX\n- Both use the `function` keyword\n- Both can be called/used\n\nFunctions are the building blocks of JavaScript and React!",
                "example": "// Regular function\nfunction calculate() {\n  return 2 + 2;\n}\n\n// React component function\nfunction Component() {\n  return <div>Hello</div>;\n}",
                "action": "continue",
                "next": "return-check"
            },
            {
                "stepId": "return-check",
                "mentorSays": "Do you understand the return statement and how components must return JSX?",
                "choices": [
                    {"label": "Yes, I understand return", "next": "coding-start-js"},
                    {"label": "No, please explain", "next": "return-explanation"}
                ]
            },
            {
                "stepId": "return-explanation",
                "mentorSays": "The return statement sends a value back from a function. In React components, we return JSX.\n\n**What is Return?**\n\nThe `return` statement gives back a value from a function.\n\n**Examples:**\n\n```javascript\n// Return a number\nfunction add(a, b) {\n  return a + b;  // Returns the sum\n}\n\n// Return a string\nfunction greet() {\n  return 'Hello';  // Returns the string\n}\n\n// Return JSX (React component)\nfunction HelloWorld() {\n  return <h1>Hello World</h1>;  // Returns JSX\n}\n```\n\n**Return in Components:**\n\nComponents MUST return JSX:\n\n```javascript\nfunction HelloWorld() {\n  return (  // Must have return!\n    <div>\n      <h1>Hello World</h1>\n    </div>\n  );\n}\n```\n\n**Return Rules:**\n\n1. **Always return JSX** in components\n2. **Return one element** (wrap multiple in a div)\n3. **Use parentheses** for multi-line JSX\n\n**Key Points:**\n- `return` gives back a value\n- Components return JSX\n- JSX describes what to display\n\nReturn is how components tell React what to show!",
                "example": "// Component with return\nfunction HelloWorld() {\n  return <h1>Hello World</h1>;\n}\n\n// Multi-line return\nfunction HelloWorld() {\n  return (\n    <div>\n      <h1>Hello</h1>\n      <p>World</p>\n    </div>\n  );\n}",
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

# Continue with remaining 4 lessons...
# Due to length, I'll create them in a separate continuation

if __name__ == '__main__':
    lessons = [
        ("react", create_react_hello_world()),
        # Will add 4 more...
    ]
    
    for tech, lesson in lessons:
        tech_dir = LESSON_GEN_DIR / tech
        tech_dir.mkdir(exist_ok=True)
        
        file_path = tech_dir / f"{lesson['id']}.json"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(lesson, f, indent=2, ensure_ascii=False)
        
        print(f"Created: {file_path} ({len(lesson['flow'])} steps)")

