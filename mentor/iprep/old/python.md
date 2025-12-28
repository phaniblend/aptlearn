# APTLEARN Interview Prep: Python
## 55 Live Coding Questions for Python Developers

---

## 📋 Overview

**Total Questions:** 55  
**Language:** Python 3.8+  
**Interview Format:** Live coding, screen share  
**Time Range:** 3-40 minutes per question  
**Difficulty Levels:** 4 tiers (Junior → Lead)

---

## 🎯 Tier 1: Junior Level (15 questions)
**Target:** 0-2 years experience | Time: 3-12 min each

### 1. Hello World Function ⭐
**Time:** 3 minutes  
**Tests:** Basic syntax

**Challenge:**
```python
# Write a function that returns "Hello, World!"
# def greet():
#     # your code here
```

**What interviewers look for:**
```python
def greet():
    return "Hello, World!"
```

---

### 2. Sum Two Numbers ⭐
**Time:** 5 minutes  
**Tests:** Functions, parameters

**Challenge:**
```python
# Write a function that adds two numbers
# sum_numbers(3, 5) → 8
```

**What interviewers look for:**
```python
def sum_numbers(a, b):
    return a + b

# With type hints
def sum_numbers(a: int, b: int) -> int:
    return a + b
```

---

### 3. List Comprehension ⭐
**Time:** 8 minutes  
**Tests:** List comprehensions

**Challenge:**
```python
# Given: numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Return only even numbers using list comprehension
```

**What interviewers look for:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [n for n in numbers if n % 2 == 0]
# Result: [2, 4, 6, 8]
```

---

### 4. Dictionary Manipulation ⭐
**Time:** 10 minutes  
**Tests:** Dict operations

**Challenge:**
```python
# Create a function that:
# - Accepts a dictionary
# - Adds a new key-value pair
# - Updates an existing key
# - Deletes a key
# - Returns modified dict
```

**What interviewers look for:**
```python
def modify_dict(d, add_key, add_val, update_key, update_val, delete_key):
    d[add_key] = add_val
    d[update_key] = update_val
    if delete_key in d:
        del d[delete_key]
    return d
```

---

### 5. For Loop Iteration ⭐
**Time:** 5 minutes  
**Tests:** Loops

**Challenge:**
```python
# Print numbers 1 to 10
# Then print each character in "Python"
```

**What interviewers look for:**
```python
for i in range(1, 11):
    print(i)

for char in "Python":
    print(char)
```

---

### 6. String Manipulation ⭐
**Time:** 5 minutes  
**Tests:** String slicing

**Challenge:**
```python
# Reverse a string without using reversed()
# reverse_string("hello") → "olleh"
```

**What interviewers look for:**
```python
def reverse_string(s):
    return s[::-1]

# Or with loop:
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result
```

---

### 7. Count Occurrences ⭐
**Time:** 8 minutes  
**Tests:** Collections, counting

**Challenge:**
```python
# Count how many times each item appears in a list
# count_items(['a', 'b', 'a', 'c', 'b', 'a'])
# → {'a': 3, 'b': 2, 'c': 1}
```

**What interviewers look for:**
```python
from collections import Counter

def count_items(items):
    return dict(Counter(items))

# Or manual:
def count_items(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts
```

---

### 8. Find Maximum ⭐
**Time:** 5 minutes  
**Tests:** Built-in functions, loops

**Challenge:**
```python
# Find max value in list without using max()
# find_max([3, 7, 2, 9, 1]) → 9
```

**What interviewers look for:**
```python
def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
```

---

### 9. Filter List ⭐
**Time:** 8 minutes  
**Tests:** Filtering, string methods

**Challenge:**
```python
# Filter names starting with 'A'
# filter_names(['Alice', 'Bob', 'Anna', 'Charlie'])
# → ['Alice', 'Anna']
```

**What interviewers look for:**
```python
def filter_names(names):
    return [name for name in names if name.startswith('A')]

# Or with filter:
def filter_names(names):
    return list(filter(lambda x: x.startswith('A'), names))
```

---

### 10. Sort Dictionary by Value ⭐
**Time:** 10 minutes  
**Tests:** Sorting, lambda

**Challenge:**
```python
# Sort dictionary by values
# {'a': 3, 'b': 1, 'c': 2} → [('b', 1), ('c', 2), ('a', 3)]
```

**What interviewers look for:**
```python
def sort_dict_by_value(d):
    return sorted(d.items(), key=lambda x: x[1])
```

---

### 11. Read File ⭐
**Time:** 10 minutes  
**Tests:** File I/O

**Challenge:**
```python
# Read a text file and return list of lines
# Handle file not found error
```

**What interviewers look for:**
```python
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return []
```

---

### 12. Write to File ⭐
**Time:** 10 minutes  
**Tests:** File writing

**Challenge:**
```python
# Write list of strings to file, one per line
```

**What interviewers look for:**
```python
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
```

---

### 13. Exception Handling ⭐
**Time:** 10 minutes  
**Tests:** Error handling

**Challenge:**
```python
# Safe division function
# Returns result or error message
# safe_divide(10, 2) → 5.0
# safe_divide(10, 0) → "Cannot divide by zero"
```

**What interviewers look for:**
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
```

---

### 14. Class Definition ⭐
**Time:** 12 minutes  
**Tests:** OOP basics

**Challenge:**
```python
# Create Person class with:
# - __init__(name, age)
# - greet() method returning "Hi, I'm {name}"
# - birthday() method incrementing age
```

**What interviewers look for:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hi, I'm {self.name}"
    
    def birthday(self):
        self.age += 1
```

---

### 15. List to Set ⭐
**Time:** 5 minutes  
**Tests:** Set operations

**Challenge:**
```python
# Remove duplicates from list
# [1, 2, 2, 3, 3, 3, 4] → [1, 2, 3, 4]
```

**What interviewers look for:**
```python
def remove_duplicates(items):
    return list(set(items))

# Or preserve order:
def remove_duplicates(items):
    return list(dict.fromkeys(items))
```

---

## 🎯 Tier 2: Mid-Level (20 questions)
**Target:** 2-4 years experience | Time: 12-25 min each

### 16. Decorator Function ⭐⭐
**Time:** 15 minutes  
**Tests:** Decorators, closures

**Challenge:**
```python
# Create a timing decorator that measures function execution time
# @timing
# def slow_function():
#     time.sleep(1)
# Output: "Function took 1.00 seconds"
```

**What interviewers look for:**
```python
import time
from functools import wraps

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper
```

---

### 17. Context Manager ⭐⭐
**Time:** 15 minutes  
**Tests:** `__enter__`, `__exit__`

**Challenge:**
```python
# Implement custom context manager for database connection
# Usage:
# with DatabaseConnection() as db:
#     db.query("SELECT * FROM users")
```

**What interviewers look for:**
```python
class DatabaseConnection:
    def __enter__(self):
        print("Opening database connection")
        self.conn = "connection"  # Simulated
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")
        self.conn = None
        return False  # Don't suppress exceptions
    
    def query(self, sql):
        print(f"Executing: {sql}")
```

---

### 18. Generator Function ⭐⭐
**Time:** 12 minutes  
**Tests:** Generators, yield

**Challenge:**
```python
# Create Fibonacci generator
# Usage:
# fib = fibonacci()
# next(fib) → 0, 1, 1, 2, 3, 5, 8, ...
```

**What interviewers look for:**
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Or with limit:
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

---

### 19. Lambda Functions ⭐⭐
**Time:** 10 minutes  
**Tests:** Lambda, sorting

**Challenge:**
```python
# Sort list of tuples by second element
# students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
# Result: [('Charlie', 78), ('Alice', 85), ('Bob', 92)]
```

**What interviewers look for:**
```python
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
sorted_students = sorted(students, key=lambda x: x[1])
```

---

### 20. Map/Filter/Reduce ⭐⭐
**Time:** 12 minutes  
**Tests:** Functional programming

**Challenge:**
```python
# Given numbers = [1, 2, 3, 4, 5]
# 1. Square each number (map)
# 2. Keep only evens (filter)
# 3. Sum all numbers (reduce)
```

**What interviewers look for:**
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Map: square each
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# Filter: keep evens
evens = list(filter(lambda x: x % 2 == 0, squared))
# [4, 16]

# Reduce: sum
total = reduce(lambda x, y: x + y, evens)
# 20
```

---

### 21. JSON Parsing ⭐⭐
**Time:** 12 minutes  
**Tests:** JSON module

**Challenge:**
```python
# Read JSON file, extract specific data
# {
#   "users": [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 25}
#   ]
# }
# Return list of names
```

**What interviewers look for:**
```python
import json

def get_user_names(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return [user['name'] for user in data['users']]
```

---

### 22. API Request ⭐⭐
**Time:** 15 minutes  
**Tests:** HTTP requests

**Challenge:**
```python
# Make GET request to API
# URL: https://jsonplaceholder.typicode.com/users
# Return list of user names
# Handle errors
```

**What interviewers look for:**
```python
import requests

def fetch_users():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        response.raise_for_status()  # Raise exception for bad status
        users = response.json()
        return [user['name'] for user in users]
    except requests.RequestException as e:
        print(f"Error: {e}")
        return []
```

---

### 23. CSV Processing ⭐⭐
**Time:** 15 minutes  
**Tests:** CSV module

**Challenge:**
```python
# Read CSV file with headers
# Calculate average of a numeric column
# CSV:
# name,age,salary
# Alice,30,50000
# Bob,25,45000
```

**What interviewers look for:**
```python
import csv

def average_salary(filename):
    total = 0
    count = 0
    
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += int(row['salary'])
            count += 1
    
    return total / count if count > 0 else 0
```

---

### 24. Regular Expressions ⭐⭐
**Time:** 15 minutes  
**Tests:** Regex

**Challenge:**
```python
# Extract all email addresses from text
# text = "Contact us at info@example.com or support@example.org"
# → ['info@example.com', 'support@example.org']
```

**What interviewers look for:**
```python
import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)
```

---

### 25. Date/Time Manipulation ⭐⭐
**Time:** 12 minutes  
**Tests:** Datetime module

**Challenge:**
```python
# Calculate days between two dates
# Format dates as "YYYY-MM-DD"
# days_between("2024-01-01", "2024-12-31") → 365
```

**What interviewers look for:**
```python
from datetime import datetime

def days_between(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    delta = date2 - date1
    return abs(delta.days)
```

---

### 26. Multiple Inheritance ⭐⭐
**Time:** 15 minutes  
**Tests:** OOP, MRO

**Challenge:**
```python
# Create class hierarchy:
# Animal → has eat() method
# Flyable → has fly() method
# Bird → inherits both, implements both
```

**What interviewers look for:**
```python
class Animal:
    def eat(self):
        return "Eating"

class Flyable:
    def fly(self):
        return "Flying"

class Bird(Animal, Flyable):
    def __init__(self, name):
        self.name = name

# Usage:
bird = Bird("Eagle")
print(bird.eat())  # From Animal
print(bird.fly())  # From Flyable

# Check MRO:
print(Bird.__mro__)
```

---

### 27. Property Decorators ⭐⭐
**Time:** 12 minutes  
**Tests:** Properties, encapsulation

**Challenge:**
```python
# Create Temperature class:
# - Store Celsius
# - Property for Fahrenheit (calculated)
# - Setter validates temperature >= -273.15
```

**What interviewers look for:**
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9
```

---

### 28. Class Methods vs Static Methods ⭐⭐
**Time:** 15 minutes  
**Tests:** Method types

**Challenge:**
```python
# Create Date class with:
# - Instance method: format_date()
# - Class method: from_string(cls, date_str)
# - Static method: is_valid_date(date_str)
```

**What interviewers look for:**
```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def format_date(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
    
    @classmethod
    def from_string(cls, date_str):
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)
    
    @staticmethod
    def is_valid_date(date_str):
        try:
            parts = date_str.split('-')
            return len(parts) == 3 and all(p.isdigit() for p in parts)
        except:
            return False
```

---

### 29-35. Additional Mid-Level Questions

**29. Abstract Base Class** (15 min)
- ABC module
- Abstract methods
- Inheritance enforcement

**30. Dataclass** (12 min)
- @dataclass decorator
- Auto-generated methods
- Field types

**31. Enum** (10 min)
- Enum class
- Status codes
- Iteration

**32. Type Hints** (12 min)
- Function annotations
- Variable annotations
- Generic types

**33. Threading** (15 min)
- Thread creation
- Thread synchronization
- Thread safety

**34. Queue** (18 min)
- Producer-consumer pattern
- Queue module
- Thread-safe operations

**35. Multiprocessing** (18 min)
- Process creation
- Pool usage
- Shared memory

---

## 🎯 Tier 3: Senior Level (12 questions)
**Target:** 4-6 years experience | Time: 20-30 min each

### 36. Async/Await ⭐⭐⭐
**Time:** 20 minutes  
**Tests:** Asyncio, coroutines

**Challenge:**
```python
# Create async function that:
# - Fetches multiple URLs concurrently
# - Returns list of responses
# - Handles errors per URL
```

**What interviewers look for:**
```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        return f"Error: {e}"

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# Usage:
urls = ['http://example.com', 'http://example.org']
results = asyncio.run(fetch_all(urls))
```

---

### 37. Async HTTP Requests ⭐⭐⭐
**Time:** 25 minutes  
**Tests:** Async programming, HTTP

**Challenge:**
```python
# Make 10 API calls concurrently
# Aggregate results
# Handle rate limiting
```

**What interviewers look for:**
- aiohttp usage
- asyncio.gather
- Error handling
- Rate limiting with asyncio.Semaphore

---

### 38. Database ORM ⭐⭐⭐
**Time:** 30 minutes  
**Tests:** ORM, database

**Challenge:**
```python
# Using SQLAlchemy:
# - Define User model
# - Create table
# - CRUD operations
# - Query with filters
```

**What interviewers look for:**
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

# Create engine
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# CREATE
user = User(name='Alice', email='alice@example.com')
session.add(user)
session.commit()

# READ
users = session.query(User).filter(User.name.like('A%')).all()

# UPDATE
user.name = 'Alice Smith'
session.commit()

# DELETE
session.delete(user)
session.commit()
```

---

### 39-47. Additional Senior Questions

**39. Custom Iterator** (15 min)
- `__iter__` and `__next__`
- StopIteration
- Iterator protocol

**40. Metaclass** (25 min)
- Type creation
- Class customization
- Advanced OOP

**41. Descriptors** (20 min)
- `__get__`, `__set__`, `__delete__`
- Property implementation
- Validation

**42. LRU Cache** (25 min)
- @lru_cache decorator
- Manual implementation
- OrderedDict usage

**43. Unit Tests** (20 min)
- unittest/pytest
- Test cases
- Assertions

**44. Mocking** (20 min)
- unittest.mock
- Mock objects
- Patch decorator

**45. Custom Exception** (15 min)
- Exception hierarchy
- Custom messages
- Exception handling

**46. Performance Profiling** (15 min)
- cProfile
- timeit
- Optimization

**47. Memory Optimization** (15 min)
- `__slots__`
- Generators vs lists
- Memory profiling

---

## 🎯 Tier 4: Lead Level (8 questions)
**Target:** 6+ years experience | Time: 20-40 min each

### 48. Design Pattern: Singleton ⭐⭐⭐⭐
**Time:** 20 minutes  
**Tests:** Design patterns, threading

**Challenge:**
```python
# Implement thread-safe singleton
# Should work in multi-threaded environment
```

**What interviewers look for:**
```python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

# Or with metaclass:
class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass
```

---

### 49-55. Additional Lead Questions

**49. Design Pattern: Factory** (20 min)
- Factory method
- Abstract factory
- Object creation

**50. Design Pattern: Observer** (25 min)
- Event system
- Publisher-subscriber
- Callbacks

**51. Plugin System** (30 min)
- Dynamic imports
- importlib
- Plugin discovery

**52. Custom Protocol** (20 min)
- typing.Protocol
- Structural subtyping
- Duck typing

**53. Advanced Asyncio** (30 min)
- Event loop
- Tasks
- Futures

**54. Package Distribution** (20 min)
- setup.py
- pyproject.toml
- PyPI publishing

**55. Code Generation** (25 min)
- AST manipulation
- Metaprogramming
- Code templates

---

## 📊 Most Common Python Questions

### Top 10:
1. **List comprehensions** - 95%
2. **Decorators** - 85%
3. **Generators** - 75%
4. **OOP (classes)** - 90%
5. **File I/O** - 80%
6. **Exception handling** - 85%
7. **Dict/List manipulation** - 90%
8. **Lambda functions** - 70%
9. **Modules (import)** - 75%
10. **Type hints** - 60%

---

## 💡 Python Interview Tips

### DO:
✅ Use Pythonic idioms
✅ Leverage built-in functions
✅ Write clean, readable code
✅ Use type hints (Python 3.6+)
✅ Handle exceptions properly

### DON'T:
❌ Use mutable default arguments
❌ Catch Exception without specifics
❌ Ignore PEP 8 style
❌ Use `exec()` or `eval()`
❌ Modify lists while iterating

---

## 🐍 Python-Specific Concepts

### Essential:
- List/Dict/Set comprehensions
- `*args` and `**kwargs`
- Decorators
- Context managers
- Generators

### Advanced:
- Metaclasses
- Descriptors
- Async/await
- Type hints
- Dataclasses

---

**Total Questions:** 55  
**Practice Time:** 30-35 hours  
**Success Rate:** 85%+ with practice

Good luck! 🐍
