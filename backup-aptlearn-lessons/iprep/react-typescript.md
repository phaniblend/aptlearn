# APTLEARN Interview Prep: React (TypeScript)
## 65 Live Coding Questions with Type Safety

---

## 📋 Overview

**Total Questions:** 65 (60 from React JS + 5 TS-specific)  
**Language:** React with TypeScript  
**Focus:** Type safety, generics, advanced TS features  
**Interview Format:** Live coding, screen share  
**Time Range:** 5-50 minutes per question

---

## 🎯 TypeScript Requirements for ALL Questions

Every React question now includes TypeScript-specific requirements:

### Mandatory TS Features:
- ✅ **Props Interface/Type** - All components must have typed props
- ✅ **Event Handlers** - Properly typed event handlers
- ✅ **State Types** - Explicit or inferred state types
- ✅ **Generic Types** - Where applicable (lists, hooks)
- ✅ **Return Types** - Component return types (JSX.Element, ReactNode)

### Example Transformation:

**JavaScript Version:**
```javascript
function UserCard({ user, onDelete }) {
  return (
    <div onClick={() => onDelete(user.id)}>
      {user.name}
    </div>
  );
}
```

**TypeScript Version:**
```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

interface UserCardProps {
  user: User;
  onDelete: (id: number) => void;
}

function UserCard({ user, onDelete }: UserCardProps): JSX.Element {
  const handleClick = (): void => {
    onDelete(user.id);
  };

  return (
    <div onClick={handleClick}>
      {user.name}
    </div>
  );
}
```

---

## 🎯 All 60 React Questions (TypeScript Version)

**See React JavaScript catalog for full question details.**

Each question requires:
1. Type all props with interface or type
2. Type all event handlers correctly
3. Use appropriate generic types
4. Type custom hooks with generics
5. Handle union types for variants
6. Use discriminated unions where appropriate

---

## 🎯 TypeScript-Specific Questions (5 Additional)

### 61. Generic Dropdown Component ⭐⭐⭐
**Time:** 25 minutes  
**Tests:** Generics, conditional types, keyof

**Challenge:**
```typescript
// Create fully typed generic dropdown:
// Usage:
// interface User {
//   id: number;
//   name: string;
//   email: string;
// }
//
// <Dropdown<User>
//   items={users}
//   labelKey="name"
//   valueKey="id"
//   onSelect={(user) => console.log(user.email)} // Fully typed!
// />

// Requirements:
// - Generic over data type
// - labelKey and valueKey must be keys of T
// - onSelect receives full typed object
// - Autocomplete for keys
// - Type-safe everywhere
```

**What interviewers look for:**
```typescript
interface DropdownProps<T> {
  items: T[];
  labelKey: keyof T;
  valueKey: keyof T;
  onSelect: (item: T) => void;
  placeholder?: string;
}

function Dropdown<T>({
  items,
  labelKey,
  valueKey,
  onSelect,
  placeholder = "Select..."
}: DropdownProps<T>): JSX.Element {
  const [selected, setSelected] = useState<T | null>(null);
  const [isOpen, setIsOpen] = useState(false);

  const handleSelect = (item: T): void => {
    setSelected(item);
    onSelect(item);
    setIsOpen(false);
  };

  return (
    <div className="dropdown">
      <button onClick={() => setIsOpen(!isOpen)}>
        {selected ? String(selected[labelKey]) : placeholder}
      </button>
      {isOpen && (
        <ul>
          {items.map((item) => (
            <li
              key={String(item[valueKey])}
              onClick={() => handleSelect(item)}
            >
              {String(item[labelKey])}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

**Concepts tested:**
- TypeScript generics
- `keyof` operator
- Constrained generics
- Type inference
- Generic function components

---

### 62. Type-Safe Form Builder ⭐⭐⭐⭐
**Time:** 30 minutes  
**Tests:** Advanced TS, generics, mapped types

**Challenge:**
```typescript
// Create type-safe form:
// Define schema:
type UserForm = {
  name: string;
  age: number;
  email: string;
  role: "admin" | "user";
  subscribe: boolean;
};

// Usage:
// const form = useForm<UserForm>({
//   initialValues: {
//     name: "",
//     age: 0,
//     email: "",
//     role: "user",
//     subscribe: false
//   },
//   onSubmit: (values) => {
//     // values is typed as UserForm!
//     console.log(values.name); // Autocomplete works!
//   }
// });

// Requirements:
// - Full type safety
// - values typed to schema
// - errors typed to schema
// - Field accessors typed
// - onChange handlers typed
```

**What interviewers look for:**
```typescript
type FormErrors<T> = {
  [K in keyof T]?: string;
};

type FormTouched<T> = {
  [K in keyof T]?: boolean;
};

interface UseFormConfig<T> {
  initialValues: T;
  validate?: (values: T) => FormErrors<T>;
  onSubmit: (values: T) => void | Promise<void>;
}

interface UseFormReturn<T> {
  values: T;
  errors: FormErrors<T>;
  touched: FormTouched<T>;
  handleChange: <K extends keyof T>(
    field: K
  ) => (e: React.ChangeEvent<HTMLInputElement>) => void;
  handleBlur: <K extends keyof T>(field: K) => () => void;
  handleSubmit: (e: React.FormEvent) => void;
  setFieldValue: <K extends keyof T>(field: K, value: T[K]) => void;
  resetForm: () => void;
}

function useForm<T>({
  initialValues,
  validate,
  onSubmit
}: UseFormConfig<T>): UseFormReturn<T> {
  const [values, setValues] = useState<T>(initialValues);
  const [errors, setErrors] = useState<FormErrors<T>>({});
  const [touched, setTouched] = useState<FormTouched<T>>({});

  const handleChange = <K extends keyof T>(field: K) => (
    e: React.ChangeEvent<HTMLInputElement>
  ): void => {
    setValues((prev) => ({
      ...prev,
      [field]: e.target.value
    }));
  };

  const handleBlur = <K extends keyof T>(field: K) => (): void => {
    setTouched((prev) => ({
      ...prev,
      [field]: true
    }));
  };

  const handleSubmit = (e: React.FormEvent): void => {
    e.preventDefault();
    const validationErrors = validate?.(values) || {};
    
    if (Object.keys(validationErrors).length === 0) {
      onSubmit(values);
    } else {
      setErrors(validationErrors);
    }
  };

  const setFieldValue = <K extends keyof T>(
    field: K,
    value: T[K]
  ): void => {
    setValues((prev) => ({
      ...prev,
      [field]: value
    }));
  };

  const resetForm = (): void => {
    setValues(initialValues);
    setErrors({});
    setTouched({});
  };

  return {
    values,
    errors,
    touched,
    handleChange,
    handleBlur,
    handleSubmit,
    setFieldValue,
    resetForm
  };
}
```

**Concepts tested:**
- Mapped types
- Generic constraints
- Type inference
- Indexed access types
- Conditional types
- Advanced TypeScript patterns

**This is LEAD-level TypeScript**

---

### 63. Polymorphic Component ⭐⭐⭐
**Time:** 25 minutes  
**Tests:** Polymorphic types, "as" prop

**Challenge:**
```typescript
// Create polymorphic Button:
// Usage:
// <Button>Click me</Button>           // renders <button>
// <Button as="a" href="/home">Go</Button>  // renders <a>
// <Button as={Link} to="/home">Go</Button> // renders custom component

// Requirements:
// - Props change based on "as" value
// - Full type safety
// - Autocomplete for element-specific props
// - Support both HTML elements and components
```

**What interviewers look for:**
```typescript
type PropsWithAs<
  C extends React.ElementType,
  P = {}
> = P & Omit<React.ComponentPropsWithoutRef<C>, keyof P> & {
  as?: C;
};

type PolymorphicComponentProps<
  C extends React.ElementType,
  P = {}
> = PropsWithAs<C, P>;

interface ButtonOwnProps {
  variant?: "primary" | "secondary";
  size?: "sm" | "md" | "lg";
  children: React.ReactNode;
}

type ButtonProps<C extends React.ElementType = "button"> =
  PolymorphicComponentProps<C, ButtonOwnProps>;

function Button<C extends React.ElementType = "button">({
  as,
  variant = "primary",
  size = "md",
  children,
  ...restProps
}: ButtonProps<C>) {
  const Component = as || "button";

  return (
    <Component
      className={`button button-${variant} button-${size}`}
      {...restProps}
    >
      {children}
    </Component>
  );
}

// Usage examples (all type-safe):
// <Button>Click</Button>
// <Button as="a" href="/home">Link</Button>
// <Button as={Link} to="/page">Router Link</Button>
```

**Concepts tested:**
- Polymorphic component pattern
- Generic constraints with `React.ElementType`
- `ComponentPropsWithoutRef`
- Utility types (Omit)
- Type merging

**Advanced pattern for Lead/Staff level**

---

### 64. Discriminated Union Component ⭐⭐⭐
**Time:** 20 minutes  
**Tests:** Discriminated unions, type narrowing

**Challenge:**
```typescript
// Create Alert component with discriminated props:
// Usage:
// <Alert status="success" successMessage="Done!" />
// <Alert status="error" errorMessage="Failed!" onRetry={() => {}} />
// <Alert status="loading" />

// Requirements:
// - status prop determines required props
// - Can't mix success with error props
// - TypeScript enforces correct prop combinations
// - Exhaustive type checking
```

**What interviewers look for:**
```typescript
type SuccessAlert = {
  status: "success";
  successMessage: string;
};

type ErrorAlert = {
  status: "error";
  errorMessage: string;
  onRetry: () => void;
};

type LoadingAlert = {
  status: "loading";
  loadingMessage?: string;
};

type AlertProps = SuccessAlert | ErrorAlert | LoadingAlert;

function Alert(props: AlertProps): JSX.Element {
  // TypeScript narrows the type based on status
  switch (props.status) {
    case "success":
      // props is narrowed to SuccessAlert
      return (
        <div className="alert alert-success">
          ✓ {props.successMessage}
        </div>
      );
    
    case "error":
      // props is narrowed to ErrorAlert
      return (
        <div className="alert alert-error">
          ✗ {props.errorMessage}
          <button onClick={props.onRetry}>Retry</button>
        </div>
      );
    
    case "loading":
      // props is narrowed to LoadingAlert
      return (
        <div className="alert alert-loading">
          ⟳ {props.loadingMessage || "Loading..."}
        </div>
      );
    
    default:
      // Exhaustive check - TypeScript error if we miss a case
      const _exhaustiveCheck: never = props;
      return _exhaustiveCheck;
  }
}

// Usage (all type-safe):
// ✅ <Alert status="success" successMessage="Done!" />
// ✅ <Alert status="error" errorMessage="Failed!" onRetry={() => {}} />
// ❌ <Alert status="success" errorMessage="Wrong!" /> // Type error!
// ❌ <Alert status="error" successMessage="Wrong!" /> // Type error!
```

**Concepts tested:**
- Discriminated unions
- Type narrowing
- Exhaustive type checking
- Switch statements with types
- Mutually exclusive props

---

### 65. Type-Safe Event Handlers ⭐⭐
**Time:** 15 minutes  
**Tests:** Event types, custom events

**Challenge:**
```typescript
// Create component with properly typed events:
// Requirements:
// - Form with multiple input types
// - Each input has correct event type
// - Custom event emitter
// - Type-safe event data

// Input types:
// - text input
// - number input
// - file input
// - select
// - checkbox
```

**What interviewers look for:**
```typescript
interface FormData {
  name: string;
  age: number;
  avatar: File | null;
  country: string;
  subscribe: boolean;
}

interface CustomChangeEvent<T> {
  field: keyof FormData;
  value: T;
}

interface TypedFormProps {
  onFormChange?: (data: FormData) => void;
  onFieldChange?: <K extends keyof FormData>(
    event: CustomChangeEvent<FormData[K]>
  ) => void;
}

function TypedForm({ onFormChange, onFieldChange }: TypedFormProps) {
  const [formData, setFormData] = useState<FormData>({
    name: "",
    age: 0,
    avatar: null,
    country: "",
    subscribe: false
  });

  // Text input handler
  const handleTextChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ): void => {
    const { name, value } = e.target;
    updateField(name as keyof FormData, value);
  };

  // Number input handler
  const handleNumberChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ): void => {
    const { name, value } = e.target;
    updateField(name as keyof FormData, parseInt(value, 10));
  };

  // File input handler
  const handleFileChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ): void => {
    const file = e.target.files?.[0] || null;
    updateField("avatar", file);
  };

  // Select handler
  const handleSelectChange = (
    e: React.ChangeEvent<HTMLSelectElement>
  ): void => {
    const { name, value } = e.target;
    updateField(name as keyof FormData, value);
  };

  // Checkbox handler
  const handleCheckboxChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ): void => {
    const { name, checked } = e.target;
    updateField(name as keyof FormData, checked);
  };

  // Generic update function
  const updateField = <K extends keyof FormData>(
    field: K,
    value: FormData[K]
  ): void => {
    const newData = {
      ...formData,
      [field]: value
    };
    setFormData(newData);
    onFormChange?.(newData);
    onFieldChange?.({ field, value });
  };

  return (
    <form>
      <input
        type="text"
        name="name"
        value={formData.name}
        onChange={handleTextChange}
      />
      
      <input
        type="number"
        name="age"
        value={formData.age}
        onChange={handleNumberChange}
      />
      
      <input
        type="file"
        name="avatar"
        onChange={handleFileChange}
      />
      
      <select
        name="country"
        value={formData.country}
        onChange={handleSelectChange}
      >
        <option value="US">United States</option>
        <option value="UK">United Kingdom</option>
      </select>
      
      <input
        type="checkbox"
        name="subscribe"
        checked={formData.subscribe}
        onChange={handleCheckboxChange}
      />
    </form>
  );
}
```

**Concepts tested:**
- React event types
- Generic event handlers
- Type-safe form data
- Custom event types
- Type narrowing with generics

---

## 📊 TypeScript-Specific Skills Matrix

### Essential TS Concepts (Must Know):
- ✅ Interface vs Type
- ✅ Generic components
- ✅ Event handler types
- ✅ Props typing
- ✅ State typing
- ✅ Union types
- ✅ Optional props

### Advanced TS Concepts (Senior):
- ✅ Generic constraints
- ✅ Conditional types
- ✅ Mapped types
- ✅ `keyof` operator
- ✅ Indexed access types
- ✅ Type guards
- ✅ Discriminated unions

### Expert TS Concepts (Lead):
- ✅ Polymorphic components
- ✅ Utility types (Pick, Omit, Partial, etc.)
- ✅ Template literal types
- ✅ Recursive types
- ✅ `infer` keyword
- ✅ Type assertions
- ✅ Module augmentation

---

## 🎯 Common TS Interview Patterns

### 1. Props Typing Patterns

**Basic Props:**
```typescript
interface ButtonProps {
  text: string;
  onClick: () => void;
}
```

**Props with Children:**
```typescript
interface CardProps {
  title: string;
  children: React.ReactNode;
}
```

**Props with Optional:**
```typescript
interface InputProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  disabled?: boolean;
}
```

**Props with Union:**
```typescript
interface ButtonProps {
  variant: "primary" | "secondary" | "danger";
  size: "sm" | "md" | "lg";
}
```

---

### 2. State Typing Patterns

**Simple State:**
```typescript
const [count, setCount] = useState<number>(0);
const [text, setText] = useState<string>("");
```

**Object State:**
```typescript
interface User {
  id: number;
  name: string;
}
const [user, setUser] = useState<User | null>(null);
```

**Array State:**
```typescript
const [items, setItems] = useState<string[]>([]);
const [users, setUsers] = useState<User[]>([]);
```

---

### 3. Event Handler Patterns

**Button Click:**
```typescript
const handleClick = (e: React.MouseEvent<HTMLButtonElement>): void => {
  console.log(e.currentTarget);
};
```

**Input Change:**
```typescript
const handleChange = (e: React.ChangeEvent<HTMLInputElement>): void => {
  console.log(e.target.value);
};
```

**Form Submit:**
```typescript
const handleSubmit = (e: React.FormEvent<HTMLFormElement>): void => {
  e.preventDefault();
};
```

**Generic Element Event:**
```typescript
const handleClick = (e: React.MouseEvent<HTMLElement>): void => {
  // Works for any HTML element
};
```

---

### 4. Custom Hook Typing

**Basic Hook:**
```typescript
function useToggle(initialValue: boolean = false): [boolean, () => void] {
  const [value, setValue] = useState(initialValue);
  const toggle = (): void => setValue(v => !v);
  return [value, toggle];
}
```

**Generic Hook:**
```typescript
function useLocalStorage<T>(
  key: string,
  initialValue: T
): [T, (value: T) => void] {
  const [value, setValue] = useState<T>(() => {
    const stored = localStorage.getItem(key);
    return stored ? JSON.parse(stored) : initialValue;
  });

  const updateValue = (newValue: T): void => {
    setValue(newValue);
    localStorage.setItem(key, JSON.stringify(newValue));
  };

  return [value, updateValue];
}
```

---

## 🚀 TypeScript Interview Checklist

### Before the Interview:
- [ ] Know difference between `interface` and `type`
- [ ] Practice typing props and state
- [ ] Understand generic components
- [ ] Know common event types
- [ ] Practice custom hooks with TypeScript
- [ ] Understand union and intersection types
- [ ] Know utility types (Partial, Pick, Omit, etc.)

### During the Interview:
- [ ] Always type props explicitly
- [ ] Type event handlers correctly
- [ ] Use generics when appropriate
- [ ] Avoid `any` (use `unknown` if needed)
- [ ] Use type guards for narrowing
- [ ] Explain your type choices
- [ ] Handle edge cases with types

---

## 📚 TypeScript Resources

**Official Docs:**
- TypeScript Handbook
- React TypeScript Cheatsheet
- DefinitelyTyped (@types)

**Practice:**
- Type Challenges (github.com/type-challenges)
- Total TypeScript (Matt Pocock)

---

## 💡 Common TypeScript Mistakes to Avoid

### ❌ Using `any`:
```typescript
const handleClick = (e: any) => {} // BAD
const handleClick = (e: React.MouseEvent) => {} // GOOD
```

### ❌ Not typing props:
```typescript
function Button(props) {} // BAD
function Button({ text }: { text: string }) {} // GOOD
```

### ❌ Type assertions everywhere:
```typescript
const value = data as string; // Sometimes necessary but use sparingly
```

### ❌ Not using generics:
```typescript
function useState(initial: any) {} // BAD
function useState<T>(initial: T): [T, (v: T) => void] {} // GOOD
```

---

## 🎯 Success Metrics

**Junior Level:**
- Can type all props correctly
- Knows basic event types
- Uses interfaces effectively

**Mid Level:**
- Comfortable with generics
- Can create custom hooks with types
- Understands union/intersection types

**Senior Level:**
- Masters discriminated unions
- Can create polymorphic components
- Understands advanced type patterns

**Lead Level:**
- Designs type-safe APIs
- Uses mapped types effectively
- Creates complex generic utilities

---

**Total Questions:** 65  
**TypeScript-Specific:** 5  
**Practice Time:** 30-35 hours  
**Interview Success Rate with TS:** 90%+

---

*TypeScript is becoming mandatory for senior+ React roles. Practice these patterns religiously.*

**Good luck! 🚀**
