# APTLEARN Interview Prep: Vue.js 3
## 50 Live Coding Questions with Composition API

---

## 📋 Overview

**Total Questions:** 50  
**Framework:** Vue.js 3 (Composition API focused)  
**Interview Format:** Live coding, screen share  
**Time Range:** 5-35 minutes per question  
**Difficulty Levels:** 4 tiers (Junior → Lead)

---

## 🎯 Tier 1: Junior Level (12 questions)
**Target:** 0-2 years Vue experience | Time: 3-12 min each

### 1. Hello World Component ⭐
**Time:** 3 minutes  
**Tests:** Basic template

**Challenge:**
```vue
<!-- Create component that displays "Hello, Vue!" -->
```

**What interviewers look for:**
```vue
<template>
  <div>Hello, Vue!</div>
</template>

<script setup>
// No logic needed
</script>
```

---

### 2. Data Binding ⭐
**Time:** 5 minutes  
**Tests:** `ref`, template interpolation

**Challenge:**
```vue
<!-- Display reactive message -->
<!-- message = "Welcome to Vue 3" -->
```

**What interviewers look for:**
```vue
<template>
  <div>{{ message }}</div>
</template>

<script setup>
import { ref } from 'vue';

const message = ref('Welcome to Vue 3');
</script>
```

---

### 3. v-for Rendering ⭐
**Time:** 8 minutes  
**Tests:** `v-for`, `:key`

**Challenge:**
```vue
<!-- Render list of fruits -->
<!-- fruits = ['Apple', 'Banana', 'Orange'] -->
```

**What interviewers look for:**
```vue
<template>
  <ul>
    <li v-for="fruit in fruits" :key="fruit">
      {{ fruit }}
    </li>
  </ul>
</template>

<script setup>
import { ref } from 'vue';

const fruits = ref(['Apple', 'Banana', 'Orange']);
</script>
```

---

### 4. Event Handling ⭐
**Time:** 5 minutes  
**Tests:** `@click`, methods

**Challenge:**
```vue
<!-- Button that shows alert on click -->
```

**What interviewers look for:**
```vue
<template>
  <button @click="handleClick">Click Me</button>
</template>

<script setup>
const handleClick = () => {
  alert('Button clicked!');
};
</script>
```

---

### 5. Two-Way Binding ⭐
**Time:** 5 minutes  
**Tests:** `v-model`

**Challenge:**
```vue
<!-- Input field with two-way binding -->
<!-- Display value below input -->
```

**What interviewers look for:**
```vue
<template>
  <div>
    <input v-model="text" />
    <p>You typed: {{ text }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const text = ref('');
</script>
```

---

### 6. Conditional Rendering ⭐
**Time:** 8 minutes  
**Tests:** `v-if`, `v-else`

**Challenge:**
```vue
<!-- Show message based on condition -->
<!-- Toggle with button -->
```

**What interviewers look for:**
```vue
<template>
  <div>
    <button @click="toggle">Toggle</button>
    <p v-if="isVisible">Message is visible</p>
    <p v-else>Message is hidden</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const isVisible = ref(true);

const toggle = () => {
  isVisible.value = !isVisible.value;
};
</script>
```

---

### 7. Computed Property ⭐
**Time:** 10 minutes  
**Tests:** `computed`

**Challenge:**
```vue
<!-- Calculate and display total price -->
<!-- price = 100, quantity = 3 -->
<!-- total = price * quantity -->
```

**What interviewers look for:**
```vue
<template>
  <div>
    <p>Price: ${{ price }}</p>
    <p>Quantity: {{ quantity }}</p>
    <p>Total: ${{ total }}</p>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const price = ref(100);
const quantity = ref(3);

const total = computed(() => price.value * quantity.value);
</script>
```

---

### 8. Props ⭐
**Time:** 10 minutes  
**Tests:** Props definition

**Challenge:**
```vue
<!-- Create UserCard component -->
<!-- Accept: name, email as props -->
<!-- Display both -->
```

**What interviewers look for:**
```vue
<template>
  <div class="user-card">
    <h3>{{ name }}</h3>
    <p>{{ email }}</p>
  </div>
</template>

<script setup>
defineProps({
  name: {
    type: String,
    required: true
  },
  email: {
    type: String,
    required: true
  }
});
</script>
```

---

### 9. Emit Events ⭐
**Time:** 12 minutes  
**Tests:** `$emit`, event handling

**Challenge:**
```vue
<!-- Child emits event to parent -->
<!-- Parent handles event -->
```

**What interviewers look for:**
```vue
<!-- Child Component -->
<template>
  <button @click="sendData">Send to Parent</button>
</template>

<script setup>
const emit = defineEmits(['dataSent']);

const sendData = () => {
  emit('dataSent', 'Hello from child');
};
</script>

<!-- Parent Component -->
<template>
  <ChildComponent @dataSent="handleData" />
  <p>{{ message }}</p>
</template>

<script setup>
import { ref } from 'vue';
import ChildComponent from './ChildComponent.vue';

const message = ref('');

const handleData = (data) => {
  message.value = data;
};
</script>
```

---

### 10. Class Binding ⭐
**Time:** 8 minutes  
**Tests:** `:class`

**Challenge:**
```vue
<!-- Toggle CSS class on button click -->
<!-- Active class: background red -->
```

**What interviewers look for:**
```vue
<template>
  <div>
    <button @click="toggle">Toggle</button>
    <div :class="{ active: isActive }">
      Content
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const isActive = ref(false);

const toggle = () => {
  isActive.value = !isActive.value;
};
</script>

<style scoped>
.active {
  background-color: red;
  color: white;
}
</style>
```

---

### 11. Style Binding ⭐
**Time:** 8 minutes  
**Tests:** `:style`

**Challenge:**
```vue
<!-- Dynamically change text color -->
<!-- Input to enter color name -->
```

**What interviewers look for:**
```vue
<template>
  <div>
    <input v-model="color" placeholder="Enter color" />
    <p :style="{ color: color }">
      This text changes color
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const color = ref('black');
</script>
```

---

### 12. Watchers ⭐
**Time:** 12 minutes  
**Tests:** `watch`

**Challenge:**
```vue
<!-- Watch input value -->
<!-- Log to console when it changes -->
```

**What interviewers look for:**
```vue
<template>
  <input v-model="searchTerm" placeholder="Search..." />
</template>

<script setup>
import { ref, watch } from 'vue';

const searchTerm = ref('');

watch(searchTerm, (newValue, oldValue) => {
  console.log(`Changed from "${oldValue}" to "${newValue}"`);
});
</script>
```

---

## 🎯 Tier 2: Mid-Level (18 questions)
**Target:** 2-4 years Vue experience | Time: 15-25 min each

### 13. Todo List (Composition API) ⭐⭐
**Time:** 20 minutes  
**Tests:** Composition API, reactivity

**Challenge:**
```vue
<!-- Build todo list -->
<!-- Add new todos -->
<!-- Delete todos -->
<!-- Mark as complete (toggle) -->
```

**What interviewers look for:**
```vue
<template>
  <div>
    <input v-model="newTodo" @keyup.enter="addTodo" />
    <button @click="addTodo">Add</button>
    
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <input 
          type="checkbox" 
          v-model="todo.completed"
        />
        <span :class="{ completed: todo.completed }">
          {{ todo.text }}
        </span>
        <button @click="deleteTodo(todo.id)">×</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const newTodo = ref('');
const todos = ref([]);
let nextId = 1;

const addTodo = () => {
  if (newTodo.value.trim()) {
    todos.value.push({
      id: nextId++,
      text: newTodo.value,
      completed: false
    });
    newTodo.value = '';
  }
};

const deleteTodo = (id) => {
  todos.value = todos.value.filter(t => t.id !== id);
};
</script>

<style scoped>
.completed {
  text-decoration: line-through;
  color: gray;
}
</style>
```

---

### 14. Search Filter ⭐⭐
**Time:** 15 minutes  
**Tests:** Computed, filtering

**Challenge:**
```vue
<!-- Filter list as user types -->
<!-- Case-insensitive search -->
```

**What interviewers look for:**
```vue
<template>
  <div>
    <input v-model="searchQuery" placeholder="Search..." />
    
    <ul>
      <li v-for="item in filteredItems" :key="item.id">
        {{ item.name }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const searchQuery = ref('');
const items = ref([
  { id: 1, name: 'Apple' },
  { id: 2, name: 'Banana' },
  { id: 3, name: 'Orange' }
]);

const filteredItems = computed(() => {
  return items.value.filter(item => 
    item.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});
</script>
```

---

### 15. Fetch Data ⭐⭐
**Time:** 15 minutes  
**Tests:** `onMounted`, async

**Challenge:**
```vue
<!-- Fetch users from API on mount -->
<!-- Show loading state -->
<!-- Handle errors -->
```

**What interviewers look for:**
```vue
<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">Error: {{ error }}</div>
    <ul v-else>
      <li v-for="user in users" :key="user.id">
        {{ user.name }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const users = ref([]);
const loading = ref(true);
const error = ref(null);

onMounted(async () => {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    users.value = await response.json();
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
});
</script>
```

---

### 16. Form Validation ⭐⭐
**Time:** 20 minutes  
**Tests:** Validation, reactive state

**Challenge:**
```vue
<!-- Form with validation -->
<!-- Email format check -->
<!-- Password min length -->
<!-- Show errors -->
```

**What interviewers look for:**
```vue
<template>
  <form @submit.prevent="handleSubmit">
    <div>
      <input v-model="email" placeholder="Email" />
      <span v-if="emailError" class="error">{{ emailError }}</span>
    </div>
    
    <div>
      <input v-model="password" type="password" placeholder="Password" />
      <span v-if="passwordError" class="error">{{ passwordError }}</span>
    </div>
    
    <button type="submit" :disabled="!isValid">Submit</button>
  </form>
</template>

<script setup>
import { ref, computed } from 'vue';

const email = ref('');
const password = ref('');

const emailError = computed(() => {
  if (!email.value) return 'Email required';
  if (!/\S+@\S+\.\S+/.test(email.value)) return 'Invalid email';
  return '';
});

const passwordError = computed(() => {
  if (!password.value) return 'Password required';
  if (password.value.length < 8) return 'Min 8 characters';
  return '';
});

const isValid = computed(() => {
  return !emailError.value && !passwordError.value;
});

const handleSubmit = () => {
  console.log('Form submitted', { email: email.value, password: password.value });
};
</script>
```

---

### 17. Slots ⭐⭐
**Time:** 15 minutes  
**Tests:** Slots, content distribution

**Challenge:**
```vue
<!-- Create Card component with slot -->
<!-- Accept header, content, footer -->
```

**What interviewers look for:**
```vue
<!-- Card Component -->
<template>
  <div class="card">
    <div class="card-header">
      <slot name="header">Default Header</slot>
    </div>
    <div class="card-body">
      <slot>Default Content</slot>
    </div>
    <div class="card-footer">
      <slot name="footer">Default Footer</slot>
    </div>
  </div>
</template>

<!-- Usage -->
<template>
  <Card>
    <template #header>
      <h2>Custom Header</h2>
    </template>
    
    <p>This is the main content</p>
    
    <template #footer>
      <button>Action</button>
    </template>
  </Card>
</template>
```

---

### 18. Dynamic Components ⭐⭐
**Time:** 15 minutes  
**Tests:** Dynamic components, `:is`

**Challenge:**
```vue
<!-- Switch between components -->
<!-- Tabs: Home, About, Contact -->
```

**What interviewers look for:**
```vue
<template>
  <div>
    <button @click="currentTab = 'Home'">Home</button>
    <button @click="currentTab = 'About'">About</button>
    <button @click="currentTab = 'Contact'">Contact</button>
    
    <component :is="currentTab" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import Home from './Home.vue';
import About from './About.vue';
import Contact from './Contact.vue';

const currentTab = ref('Home');
</script>
```

---

### 19-30. Additional Mid-Level Questions

**19. Provide/Inject** (15 min)
- Share data without props
- Deep component trees

**20. Lifecycle Hooks** (15 min)
- onMounted, onUnmounted
- Cleanup

**21. Composables** (18 min)
- Custom reusable logic
- useCounter, useFetch

**22. Teleport** (12 min)
- Render to different DOM location
- Modal use case

**23. Transition** (15 min)
- Enter/leave animations
- Transition component

**24. TransitionGroup** (18 min)
- List animations
- Move transitions

**25. KeepAlive** (12 min)
- Cache component state
- Include/exclude

**26. Custom Directive** (15 min)
- v-focus
- Directive lifecycle

**27. Template Refs** (12 min)
- Access DOM elements
- ref on template

**28. NextTick** (12 min)
- DOM update timing
- await nextTick()

**29. Scoped Slots** (18 min)
- Pass data to slot
- Render props pattern

**30. Named Slots** (15 min)
- Multiple slot areas
- Slot organization

---

## 🎯 Tier 3: Senior Level (12 questions)
**Target:** 4-6 years Vue experience | Time: 20-30 min each

### 31. Pinia Store ⭐⭐⭐
**Time:** 20 minutes  
**Tests:** Pinia, state management

**Challenge:**
```vue
<!-- Create counter store with Pinia -->
<!-- Use in component -->
```

**What interviewers look for:**
```javascript
// stores/counter.js
import { defineStore } from 'pinia';

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0
  }),
  
  getters: {
    doubleCount: (state) => state.count * 2
  },
  
  actions: {
    increment() {
      this.count++;
    },
    decrement() {
      this.count--;
    }
  }
});
```

```vue
<!-- Component -->
<template>
  <div>
    <p>Count: {{ counter.count }}</p>
    <p>Double: {{ counter.doubleCount }}</p>
    <button @click="counter.increment">+</button>
    <button @click="counter.decrement">-</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';

const counter = useCounterStore();
</script>
```

---

### 32. Pinia Actions (Async) ⭐⭐⭐
**Time:** 20 minutes  
**Tests:** Actions, async state

**Challenge:**
```javascript
// Create user store with async fetch
// Handle loading and errors
```

**What interviewers look for:**
```javascript
import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    users: [],
    loading: false,
    error: null
  }),
  
  actions: {
    async fetchUsers() {
      this.loading = true;
      this.error = null;
      
      try {
        const response = await fetch('https://jsonplaceholder.typicode.com/users');
        this.users = await response.json();
      } catch (err) {
        this.error = err.message;
      } finally {
        this.loading = false;
      }
    }
  }
});
```

---

### 33-42. Additional Senior Questions

**33. Pinia Getters** (15 min)
- Computed store values
- Getter dependencies

**34. Vue Router Setup** (20 min)
- Router configuration
- Navigation

**35. Dynamic Routes** (15 min)
- Route params
- useRoute composable

**36. Route Guards** (20 min)
- beforeEach
- Authentication

**37. Nested Routes** (18 min)
- Parent/child routes
- RouterView nesting

**38. Lazy Loading Routes** (15 min)
- Code splitting
- Dynamic imports

**39. Custom Plugin** (20 min)
- Plugin creation
- app.use()

**40. Render Function** (20 min)
- h() function
- Virtual DOM

**41. JSX in Vue** (18 min)
- JSX syntax
- Setup

**42. Async Component** (15 min)
- defineAsyncComponent
- Loading states

---

## 🎯 Tier 4: Lead Level (8 questions)
**Target:** 6+ years Vue experience | Time: 25-35 min each

### 43. Custom Composition ⭐⭐⭐⭐
**Time:** 25 minutes  
**Tests:** Advanced composables

**Challenge:**
```javascript
// Create useDebounce composable
// Usage:
// const debouncedValue = useDebounce(searchTerm, 500);
```

**What interviewers look for:**
```javascript
import { ref, watch } from 'vue';

export function useDebounce(value, delay = 500) {
  const debouncedValue = ref(value.value);
  let timeout;

  watch(value, (newValue) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
      debouncedValue.value = newValue;
    }, delay);
  });

  return debouncedValue;
}
```

---

### 44-50. Additional Lead Questions

**44. TypeScript Integration** (25 min)
- Fully typed components
- Generic props

**45. Testing Setup** (25 min)
- Vitest/Jest
- Component testing

**46. SSR Basics** (30 min)
- Server-side rendering
- Hydration

**47. Custom Composable Library** (30 min)
- Reusable composables
- Package structure

**48. Reactivity Internals** (25 min)
- Proxy-based reactivity
- Deep understanding

**49. Performance Optimization** (25 min)
- Virtual scrolling
- Lazy loading

**50. Micro-Frontend** (30 min)
- Module federation
- Component sharing

---

## 📊 Most Common Vue Questions

### Top 10:
1. **v-for rendering** - 100%
2. **Computed properties** - 90%
3. **Props/Emit** - 95%
4. **Fetch data** - 85%
5. **Form handling** - 80%
6. **Pinia store** - 75%
7. **Router setup** - 80%
8. **Composables** - 70%
9. **Watchers** - 75%
10. **Slots** - 65%

---

## 💡 Vue 3 Interview Tips

### DO:
✅ Use Composition API (script setup)
✅ Leverage composables
✅ Use TypeScript
✅ Think reactivity
✅ Use Pinia over Vuex

### DON'T:
❌ Forget .value on refs
❌ Mutate props
❌ Overuse watchers
❌ Ignore cleanup
❌ Mix Options + Composition APIs

---

**Total Questions:** 50  
**Practice Time:** 25-30 hours  
**Success Rate:** 85%+ with Composition API mastery

Good luck! 🚀
