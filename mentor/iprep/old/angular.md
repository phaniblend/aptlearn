# APTLEARN Interview Prep: Angular
## 50 Live Coding Questions for Enterprise Development

---

## 📋 Overview

**Total Questions:** 50  
**Framework:** Angular (v14+)  
**Interview Format:** Live coding, screen share  
**Time Range:** 5-35 minutes per question  
**Difficulty Levels:** 4 tiers (Junior → Lead)

---

## 🎯 Tier 1: Junior Level (12 questions)
**Target:** 0-2 years Angular experience | Time: 5-15 min each

### 1. Hello Component ⭐
**Time:** 5 minutes  
**Tests:** Component basics

**Challenge:**
```typescript
// Create component that displays "Hello Angular"
```

**What interviewers look for:**
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-hello',
  template: '<h1>Hello Angular</h1>',
  standalone: true
})
export class HelloComponent {}
```

---

### 2. Data Binding ⭐
**Time:** 5 minutes  
**Tests:** Interpolation

**Challenge:**
```typescript
// Display message property in template
```

**What interviewers look for:**
```typescript
@Component({
  selector: 'app-message',
  template: '<p>{{ message }}</p>',
  standalone: true
})
export class MessageComponent {
  message = 'Welcome to Angular';
}
```

---

### 3. Property Binding ⭐
**Time:** 8 minutes  
**Tests:** `[property]`

**Challenge:**
```typescript
// Bind to img src and button disabled
```

**What interviewers look for:**
```typescript
@Component({
  selector: 'app-binding',
  template: `
    <img [src]="imageUrl" />
    <button [disabled]="isDisabled">Click</button>
  `,
  standalone: true
})
export class BindingComponent {
  imageUrl = 'assets/logo.png';
  isDisabled = true;
}
```

---

### 4. Event Binding ⭐
**Time:** 8 minutes  
**Tests:** `(event)`

**Challenge:**
```typescript
// Handle button click
```

**What interviewers look for:**
```typescript
@Component({
  selector: 'app-click',
  template: `
    <button (click)="handleClick()">Click Me</button>
    <p>{{ message }}</p>
  `,
  standalone: true
})
export class ClickComponent {
  message = '';

  handleClick() {
    this.message = 'Button clicked!';
  }
}
```

---

### 5. Two-Way Binding ⭐
**Time:** 10 minutes  
**Tests:** `[(ngModel)]`

**Challenge:**
```typescript
// Create input with two-way binding
```

**What interviewers look for:**
```typescript
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-input',
  template: `
    <input [(ngModel)]="name" />
    <p>Hello {{ name }}</p>
  `,
  standalone: true,
  imports: [FormsModule]
})
export class InputComponent {
  name = '';
}
```

---

### 6. ngFor Directive ⭐
**Time:** 10 minutes  
**Tests:** `*ngFor`

**Challenge:**
```typescript
// Loop through items array
```

**What interviewers look for:**
```typescript
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-list',
  template: `
    <ul>
      <li *ngFor="let item of items">{{ item }}</li>
    </ul>
  `,
  standalone: true,
  imports: [NgFor]
})
export class ListComponent {
  items = ['Item 1', 'Item 2', 'Item 3'];
}
```

---

### 7. ngIf Directive ⭐
**Time:** 8 minutes  
**Tests:** `*ngIf`

**Challenge:**
```typescript
// Show/hide content conditionally
```

**What interviewers look for:**
```typescript
import { NgIf } from '@angular/common';

@Component({
  selector: 'app-toggle',
  template: `
    <button (click)="toggle()">Toggle</button>
    <p *ngIf="isVisible">This is visible</p>
  `,
  standalone: true,
  imports: [NgIf]
})
export class ToggleComponent {
  isVisible = true;

  toggle() {
    this.isVisible = !this.isVisible;
  }
}
```

---

### 8. Component Input ⭐
**Time:** 12 minutes  
**Tests:** `@Input()`

**Challenge:**
```typescript
// Child component receives data from parent
```

**What interviewers look for:**
```typescript
// Child Component
@Component({
  selector: 'app-user-card',
  template: `
    <div class="card">
      <h3>{{ name }}</h3>
      <p>{{ email }}</p>
    </div>
  `,
  standalone: true
})
export class UserCardComponent {
  @Input() name!: string;
  @Input() email!: string;
}

// Parent Component
@Component({
  selector: 'app-parent',
  template: `
    <app-user-card 
      [name]="'John Doe'" 
      [email]="'john@example.com'"
    />
  `,
  standalone: true,
  imports: [UserCardComponent]
})
export class ParentComponent {}
```

---

### 9. Component Output ⭐
**Time:** 12 minutes  
**Tests:** `@Output()`, `EventEmitter`

**Challenge:**
```typescript
// Child emits event to parent
```

**What interviewers look for:**
```typescript
import { Component, Output, EventEmitter } from '@angular/core';

// Child
@Component({
  selector: 'app-child',
  template: `<button (click)="send()">Send</button>`,
  standalone: true
})
export class ChildComponent {
  @Output() dataSent = new EventEmitter<string>();

  send() {
    this.dataSent.emit('Hello from child');
  }
}

// Parent
@Component({
  selector: 'app-parent',
  template: `
    <app-child (dataSent)="handleData($event)" />
    <p>{{ message }}</p>
  `,
  standalone: true,
  imports: [ChildComponent]
})
export class ParentComponent {
  message = '';

  handleData(data: string) {
    this.message = data;
  }
}
```

---

### 10. Pipes ⭐
**Time:** 10 minutes  
**Tests:** Built-in pipes

**Challenge:**
```typescript
// Use date, currency, uppercase pipes
```

**What interviewers look for:**
```typescript
import { DatePipe, CurrencyPipe, UpperCasePipe } from '@angular/common';

@Component({
  selector: 'app-pipes',
  template: `
    <p>{{ today | date:'fullDate' }}</p>
    <p>{{ price | currency }}</p>
    <p>{{ name | uppercase }}</p>
  `,
  standalone: true,
  imports: [DatePipe, CurrencyPipe, UpperCasePipe]
})
export class PipesComponent {
  today = new Date();
  price = 99.99;
  name = 'angular';
}
```

---

### 11. ngClass ⭐
**Time:** 10 minutes  
**Tests:** `[ngClass]`

**Challenge:**
```typescript
// Dynamic CSS classes
```

**What interviewers look for:**
```typescript
import { NgClass } from '@angular/common';

@Component({
  selector: 'app-class',
  template: `
    <div [ngClass]="{ 
      'active': isActive,
      'disabled': isDisabled 
    }">
      Content
    </div>
    <button (click)="toggle()">Toggle</button>
  `,
  standalone: true,
  imports: [NgClass],
  styles: [`
    .active { background: green; }
    .disabled { opacity: 0.5; }
  `]
})
export class ClassComponent {
  isActive = true;
  isDisabled = false;

  toggle() {
    this.isActive = !this.isActive;
  }
}
```

---

### 12. ngStyle ⭐
**Time:** 10 minutes  
**Tests:** `[ngStyle]`

**Challenge:**
```typescript
// Dynamic inline styles
```

**What interviewers look for:**
```typescript
import { NgStyle } from '@angular/common';

@Component({
  selector: 'app-style',
  template: `
    <div [ngStyle]="{ 
      'color': textColor,
      'font-size.px': fontSize 
    }">
      Styled text
    </div>
  `,
  standalone: true,
  imports: [NgStyle]
})
export class StyleComponent {
  textColor = 'red';
  fontSize = 20;
}
```

---

## 🎯 Tier 2: Mid-Level (18 questions)
**Target:** 2-4 years Angular experience | Time: 15-25 min each

### 13. Service Creation ⭐⭐
**Time:** 15 minutes  
**Tests:** `@Injectable`, DI

**Challenge:**
```typescript
// Create data service with methods
```

**What interviewers look for:**
```typescript
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private data: string[] = [];

  getData() {
    return this.data;
  }

  addData(item: string) {
    this.data.push(item);
  }

  removeData(index: number) {
    this.data.splice(index, 1);
  }
}

// Component using service
@Component({
  selector: 'app-consumer',
  template: `
    <ul>
      <li *ngFor="let item of items">{{ item }}</li>
    </ul>
  `,
  standalone: true,
  imports: [NgFor]
})
export class ConsumerComponent {
  items: string[];

  constructor(private dataService: DataService) {
    this.items = this.dataService.getData();
  }
}
```

---

### 14. HTTP Request ⭐⭐
**Time:** 18 minutes  
**Tests:** HttpClient, observables

**Challenge:**
```typescript
// GET data from API
// Handle loading and errors
```

**What interviewers look for:**
```typescript
import { Component, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgIf, NgFor } from '@angular/common';

interface User {
  id: number;
  name: string;
}

@Component({
  selector: 'app-users',
  template: `
    <div *ngIf="loading">Loading...</div>
    <div *ngIf="error">Error: {{ error }}</div>
    <ul *ngIf="!loading && !error">
      <li *ngFor="let user of users">{{ user.name }}</li>
    </ul>
  `,
  standalone: true,
  imports: [NgIf, NgFor]
})
export class UsersComponent {
  private http = inject(HttpClient);
  
  users: User[] = [];
  loading = true;
  error: string | null = null;

  ngOnInit() {
    this.http.get<User[]>('https://jsonplaceholder.typicode.com/users')
      .subscribe({
        next: (data) => {
          this.users = data;
          this.loading = false;
        },
        error: (err) => {
          this.error = err.message;
          this.loading = false;
        }
      });
  }
}
```

---

### 15. Reactive Forms ⭐⭐
**Time:** 20 minutes  
**Tests:** FormBuilder, FormGroup

**Challenge:**
```typescript
// Build form with FormBuilder
// Name and email fields
```

**What interviewers look for:**
```typescript
import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-form',
  template: `
    <form [formGroup]="userForm" (ngSubmit)="onSubmit()">
      <input formControlName="name" placeholder="Name" />
      <input formControlName="email" placeholder="Email" />
      <button type="submit" [disabled]="!userForm.valid">
        Submit
      </button>
    </form>
  `,
  standalone: true,
  imports: [ReactiveFormsModule]
})
export class FormComponent {
  private fb = inject(FormBuilder);

  userForm = this.fb.group({
    name: ['', Validators.required],
    email: ['', [Validators.required, Validators.email]]
  });

  onSubmit() {
    console.log(this.userForm.value);
  }
}
```

---

### 16. Form Validation ⭐⭐
**Time:** 20 minutes  
**Tests:** Validators, error display

**Challenge:**
```typescript
// Add validation and show errors
```

**What interviewers look for:**
```typescript
import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { NgIf } from '@angular/common';

@Component({
  selector: 'app-validated-form',
  template: `
    <form [formGroup]="form" (ngSubmit)="onSubmit()">
      <div>
        <input formControlName="email" />
        <div *ngIf="email.invalid && email.touched" class="error">
          <span *ngIf="email.errors?.['required']">Email required</span>
          <span *ngIf="email.errors?.['email']">Invalid email</span>
        </div>
      </div>
      
      <div>
        <input formControlName="password" type="password" />
        <div *ngIf="password.invalid && password.touched" class="error">
          <span *ngIf="password.errors?.['required']">Password required</span>
          <span *ngIf="password.errors?.['minlength']">Min 8 characters</span>
        </div>
      </div>
      
      <button type="submit" [disabled]="form.invalid">Submit</button>
    </form>
  `,
  standalone: true,
  imports: [ReactiveFormsModule, NgIf]
})
export class ValidatedFormComponent {
  private fb = inject(FormBuilder);

  form = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(8)]]
  });

  get email() {
    return this.form.get('email')!;
  }

  get password() {
    return this.form.get('password')!;
  }

  onSubmit() {
    if (this.form.valid) {
      console.log(this.form.value);
    }
  }
}
```

---

### 17-30. Additional Mid-Level Questions

**17. Custom Validator** (18 min)
- ValidatorFn
- Custom validation logic

**18. Template-Driven Forms** (18 min)
- ngModel
- Form validation

**19. Routing Setup** (15 min)
- RouterModule
- Route configuration

**20. Route Parameters** (15 min)
- ActivatedRoute
- Params subscription

**21. Child Routes** (18 min)
- Nested routing
- Children array

**22. Route Guards** (20 min)
- CanActivate
- Authentication

**23. Lazy Loading** (18 min)
- loadChildren
- Code splitting

**24. Custom Pipe** (15 min)
- @Pipe decorator
- Transform method

**25. Lifecycle Hooks** (15 min)
- ngOnInit, ngOnDestroy
- Cleanup

**26. ViewChild** (15 min)
- Template reference
- Access child component

**27. ContentChild** (15 min)
- Content projection
- ng-content

**28. Structural Directive** (20 min)
- Custom *directive
- TemplateRef

**29. Attribute Directive** (18 min)
- HostListener
- HostBinding

**30. RxJS Operators** (20 min)
- map, filter, switchMap
- Observable chains

---

## 🎯 Tier 3: Senior Level (12 questions)
**Target:** 4-6 years Angular experience | Time: 25-35 min each

### 31. NgRx Store ⭐⭐⭐
**Time:** 30 minutes  
**Tests:** State management, NgRx

**Challenge:**
```typescript
// Setup NgRx store for counter
// Actions, reducers, selectors
```

**What interviewers look for:**
```typescript
// counter.actions.ts
import { createAction } from '@ngrx/store';

export const increment = createAction('[Counter] Increment');
export const decrement = createAction('[Counter] Decrement');
export const reset = createAction('[Counter] Reset');

// counter.reducer.ts
import { createReducer, on } from '@ngrx/store';
import * as CounterActions from './counter.actions';

export interface CounterState {
  count: number;
}

const initialState: CounterState = {
  count: 0
};

export const counterReducer = createReducer(
  initialState,
  on(CounterActions.increment, (state) => ({ count: state.count + 1 })),
  on(CounterActions.decrement, (state) => ({ count: state.count - 1 })),
  on(CounterActions.reset, () => initialState)
);

// counter.selectors.ts
import { createFeatureSelector, createSelector } from '@ngrx/store';
import { CounterState } from './counter.reducer';

export const selectCounterState = createFeatureSelector<CounterState>('counter');

export const selectCount = createSelector(
  selectCounterState,
  (state) => state.count
);

// Component
import { Component, inject } from '@angular/core';
import { Store } from '@ngrx/store';
import { increment, decrement, reset } from './counter.actions';
import { selectCount } from './counter.selectors';

@Component({
  selector: 'app-counter',
  template: `
    <p>Count: {{ count$ | async }}</p>
    <button (click)="increment()">+</button>
    <button (click)="decrement()">-</button>
    <button (click)="reset()">Reset</button>
  `,
  standalone: true,
  imports: [AsyncPipe]
})
export class CounterComponent {
  private store = inject(Store);
  
  count$ = this.store.select(selectCount);

  increment() {
    this.store.dispatch(increment());
  }

  decrement() {
    this.store.dispatch(decrement());
  }

  reset() {
    this.store.dispatch(reset());
  }
}
```

---

### 32-42. Additional Senior Questions

**32. NgRx Effects** (25 min)
- Side effects
- API calls in effects

**33. NgRx Selectors** (20 min)
- Memoized selectors
- Combining selectors

**34. Interceptors** (20 min)
- HTTP interceptor
- Auth token

**35. Resolver** (18 min)
- Route data preload
- Resolve interface

**36. Guards (Multiple)** (25 min)
- CanActivate, CanDeactivate
- Auth + unsaved changes

**37. Dynamic Forms** (30 min)
- Generate from config
- FormArray

**38. Custom Form Control** (25 min)
- ControlValueAccessor
- Integration

**39. Change Detection** (20 min)
- OnPush strategy
- Performance

**40. Signals** (20 min)
- Angular signals (v16+)
- Reactive state

**41. Standalone Components** (18 min)
- No NgModule
- Imports array

**42. Testing** (25 min)
- Component testing
- TestBed

---

## 🎯 Tier 4: Lead Level (8 questions)
**Target:** 6+ years Angular experience | Time: 30-40 min each

### 43-50. Lead Questions

**43. Micro-Frontend** (35 min)
- Module Federation
- Angular architecture

**44. SSR Setup** (30 min)
- Angular Universal
- Hydration

**45. Custom Schematics** (30 min)
- Code generation
- Angular CLI

**46. Monorepo (Nx)** (35 min)
- Workspace setup
- Libraries

**47. Advanced RxJS** (30 min)
- Custom operators
- Complex streams

**48. Performance Audit** (30 min)
- Bundle analysis
- Optimization

**49. Accessibility** (25 min)
- ARIA
- Keyboard nav

**50. Security** (25 min)
- XSS prevention
- CSP

---

## 📊 Most Common Angular Questions

### Top 10:
1. **Component basics** - 100%
2. **Services + DI** - 95%
3. **Reactive Forms** - 90%
4. **HTTP requests** - 90%
5. **Routing** - 85%
6. **NgRx/State** - 75%
7. **RxJS operators** - 80%
8. **Directives** - 70%
9. **Pipes** - 65%
10. **Lifecycle hooks** - 80%

---

## 💡 Angular Interview Tips

### DO:
✅ Use standalone components
✅ Leverage dependency injection
✅ Master RxJS
✅ Use TypeScript features
✅ Follow style guide

### DON'T:
❌ Subscribe without unsubscribe
❌ Ignore memory leaks
❌ Skip error handling
❌ Overuse services
❌ Forget async pipe

---

**Total Questions:** 50  
**Practice Time:** 30-35 hours  
**Success Rate:** 80%+ with Angular mastery

Good luck! 🅰️
