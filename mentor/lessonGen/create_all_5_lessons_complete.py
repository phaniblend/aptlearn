#!/usr/bin/env python3
"""
Create 5 complete sample lessons following APT LEARN SPECIFICATION v1.0
Each lesson: 25-30 steps, 600-700 lines, comprehensive content
"""
import json
from pathlib import Path

LESSON_GEN_DIR = Path(__file__).parent

def create_react_hello_world():
    """Lesson 1: React Hello World Component"""
    # Already created in separate file - will load it
    pass

def create_angular_component_input():
    """Lesson 2: Angular Component Input - Complete"""
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
                    {"label": "I'll start with the child component and add @Input", "next": "explore-approach-1"},
                    {"label": "I want to see the complete solution", "next": "explore-optimal"},
                    {"label": "I need more context", "next": "problem-illustration"}
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
                    {"label": "Yes, I understand components", "next": "decorator-check"},
                    {"label": "No, please explain", "next": "component-explanation"}
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
                    {"label": "Yes, I understand decorators", "next": "property-binding-check"},
                    {"label": "No, please explain", "next": "decorator-explanation"}
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
                    {"label": "Yes, I understand property binding", "next": "typescript-check"},
                    {"label": "No, please explain", "next": "property-binding-explanation"}
                ]
            },
            {
                "stepId": "property-binding-explanation",
                "mentorSays": "Property binding lets you set element or component properties dynamically. The square brackets `[property]` indicate property binding.\n\n**What is Property Binding?**\n\nProperty binding sets a property value from a component's data.\n\n**Syntax:**\n```html\n[property]=\"expression\"\n```\n\n**Examples:**\n\n```html\n<!-- Bind to HTML element property -->\n<img [src]=\"imageUrl\" />\n<button [disabled]=\"isDisabled\">Click</button>\n<div [hidden]=\"isHidden\">Content</div>\n\n<!-- Bind to component @Input property -->\n<app-user-card [name]=\"userName\" />\n<app-product [price]=\"productPrice\" />\n```\n\n**Property Binding vs Interpolation:**\n\n```html\n<!-- Interpolation: Display value -->\n<p>{{ userName }}</p>\n\n<!-- Property Binding: Set property -->\n<app-user-card [name]=\"userName\" />\n```\n\n**Different Binding Types:**\n\n```html\n<!-- String binding -->\n[title]=\"'Hello'\"\n[name]=\"userName\"\n\n<!-- Boolean binding -->\n[disabled]=\"true\"\n[hidden]=\"isHidden\"\n\n<!-- Number binding -->\n[count]=\"5\"\n[price]=\"productPrice\"\n\n<!-- Object binding -->\n[user]=\"currentUser\"\n```\n\n**Key Points:**\n- Square brackets `[]` indicate property binding\n- Expression inside quotes is evaluated\n- Can bind to HTML properties or component inputs\n- One-way binding (parent → child)\n\n**Example:**\n\n```typescript\n// Component\nexport class AppComponent {\n  userName = 'John';\n  isActive = true;\n}\n```\n\n```html\n<!-- Template -->\n<app-user-card [name]=\"userName\" />\n<button [disabled]=\"!isActive\">Submit</button>\n```\n\nProperty binding connects component data to template properties!",
                "example": "// Component\nexport class AppComponent {\n  userName = 'Alice';\n}\n\n// Template\n<app-user-card [name]=\"userName\" />",
                "action": "continue",
                "next": "typescript-check"
            },
            {
                "stepId": "typescript-check",
                "mentorSays": "Do you understand TypeScript type annotations and the `!` operator for required properties?",
                "choices": [
                    {"label": "Yes, I understand TypeScript types", "next": "coding-start-ts"},
                    {"label": "No, please explain", "next": "typescript-explanation"}
                ]
            },
            {
                "stepId": "typescript-explanation",
                "mentorSays": "TypeScript adds types to JavaScript. In Angular, we use types to make our code safer and clearer.\n\n**What is TypeScript?**\n\nTypeScript is JavaScript with types. Types tell you what kind of data a variable can hold.\n\n**Basic Types:**\n\n```typescript\n// String type\nlet name: string = 'John';\n\n// Number type\nlet age: number = 25;\n\n// Boolean type\nlet isActive: boolean = true;\n\n// Array type\nlet items: string[] = ['a', 'b', 'c'];\n```\n\n**The `!` Operator (Non-null Assertion):**\n\nThe `!` operator tells TypeScript: \"I promise this value will be set, don't worry about it being undefined.\"\n\n```typescript\n// Without ! - TypeScript thinks it might be undefined\n@Input() name?: string;  // Optional, might be undefined\n\n// With ! - TypeScript knows it will be set\n@Input() name!: string;  // Required, will be provided\n```\n\n**Why Use `!` for @Input()?**\n\nWhen you use `@Input() name!: string`, you're telling TypeScript:\n- This property WILL receive a value from the parent\n- Don't require initialization in the constructor\n- Trust that the parent will provide it\n\n**Example:**\n\n```typescript\n// Component with @Input\n@Component({\n  selector: 'app-user-card',\n  template: '<h3>{{ name }}</h3>'\n})\nexport class UserCardComponent {\n  @Input() name!: string;  // ! means \"will be provided\"\n  @Input() email?: string;  // ? means \"optional\"\n}\n```\n\n**Type Safety Benefits:**\n\n```typescript\n// TypeScript catches errors at compile time\n@Input() name!: string;\n\n// Later in code:\nthis.name.toUpperCase();  // ✅ TypeScript knows name is string\nthis.name = 123;  // ❌ Error! Can't assign number to string\n```\n\n**Key Points:**\n- TypeScript adds type safety\n- `!` means \"definitely assigned\"\n- `?` means \"optional\"\n- Types help catch errors early\n\nTypeScript makes Angular code safer and more maintainable!",
                "example": "// TypeScript with @Input\n@Component({\n  selector: 'app-user-card',\n  template: '<h3>{{ name }}</h3>'\n})\nexport class UserCardComponent {\n  @Input() name!: string;  // Required\n  @Input() age?: number;   // Optional\n}",
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

# Continue with remaining 3 lessons...
# Due to length, I'll create them in a continuation

if __name__ == '__main__':
    lessons = [
        ("angular", create_angular_component_input()),
        # Will add remaining 3...
    ]
    
    for tech, lesson in lessons:
        tech_dir = LESSON_GEN_DIR / tech
        tech_dir.mkdir(exist_ok=True)
        
        file_path = tech_dir / f"{lesson['id']}.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(lesson, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Created: {file_path.name} ({len(lesson['flow'])} steps)")

