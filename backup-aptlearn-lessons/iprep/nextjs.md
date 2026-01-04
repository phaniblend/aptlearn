# APTLEARN Interview Prep: Next.js
## 50 Live Coding Questions for Full-Stack React Development

---

## 📋 Overview

**Total Questions:** 50  
**Framework:** Next.js 14+ (App Router)  
**Interview Format:** Live coding, screen share  
**Time Range:** 5-40 minutes per question  
**Difficulty Levels:** 4 tiers (Junior → Lead)

---

## 🎯 Tier 1: Junior Level (10 questions)
**Target:** 0-2 years Next.js experience | Time: 5-15 min each

### 1. Hello World Page ⭐
**Time:** 5 minutes  
**Tests:** Basic routing

**Challenge:**
```typescript
// Create page at /hello that displays "Hello Next.js"
```

**What interviewers look for:**
```typescript
// app/hello/page.tsx
export default function HelloPage() {
  return <h1>Hello Next.js</h1>;
}
```

---

### 2. Dynamic Route ⭐
**Time:** 8 minutes  
**Tests:** Dynamic segments

**Challenge:**
```typescript
// Create /user/[id] route
// Display user ID from URL
```

**What interviewers look for:**
```typescript
// app/user/[id]/page.tsx
export default function UserPage({
  params
}: {
  params: { id: string }
}) {
  return <h1>User ID: {params.id}</h1>;
}
```

---

### 3. Link Navigation ⭐
**Time:** 8 minutes  
**Tests:** Next.js Link

**Challenge:**
```typescript
// Create home page with navigation links
// Link to /about and /contact
```

**What interviewers look for:**
```typescript
// app/page.tsx
import Link from 'next/link';

export default function Home() {
  return (
    <nav>
      <Link href="/about">About</Link>
      <Link href="/contact">Contact</Link>
    </nav>
  );
}
```

---

### 4. Image Component ⭐
**Time:** 10 minutes  
**Tests:** next/image optimization

**Challenge:**
```typescript
// Display optimized image
// Use Next.js Image component
```

**What interviewers look for:**
```typescript
import Image from 'next/image';

export default function LogoPage() {
  return (
    <Image
      src="/logo.png"
      alt="Logo"
      width={200}
      height={200}
      priority
    />
  );
}
```

---

### 5. Layout Component ⭐
**Time:** 10 minutes  
**Tests:** Layouts

**Challenge:**
```typescript
// Create root layout
// Include navigation
```

**What interviewers look for:**
```typescript
// app/layout.tsx
import Link from 'next/link';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <nav>
          <Link href="/">Home</Link>
          <Link href="/about">About</Link>
        </nav>
        <main>{children}</main>
      </body>
    </html>
  );
}
```

---

### 6. Metadata ⭐
**Time:** 8 minutes  
**Tests:** SEO metadata

**Challenge:**
```typescript
// Add page title and description
```

**What interviewers look for:**
```typescript
// app/about/page.tsx
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'About Us',
  description: 'Learn more about our company',
};

export default function AboutPage() {
  return <h1>About Us</h1>;
}
```

---

### 7. Client Component ⭐
**Time:** 10 minutes  
**Tests:** "use client" directive

**Challenge:**
```typescript
// Create counter with useState
// Must be client component
```

**What interviewers look for:**
```typescript
// app/counter/page.tsx
'use client';

import { useState } from 'react';

export default function CounterPage() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

---

### 8. Server Component ⭐
**Time:** 10 minutes  
**Tests:** Default server components

**Challenge:**
```typescript
// Fetch data in server component
// No "use client" needed
```

**What interviewers look for:**
```typescript
// app/users/page.tsx
async function getUsers() {
  const res = await fetch('https://jsonplaceholder.typicode.com/users');
  return res.json();
}

export default async function UsersPage() {
  const users = await getUsers();

  return (
    <ul>
      {users.map((user: any) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

---

### 9. Loading State ⭐
**Time:** 8 minutes  
**Tests:** loading.tsx

**Challenge:**
```typescript
// Add loading UI for page
```

**What interviewers look for:**
```typescript
// app/users/loading.tsx
export default function Loading() {
  return <div>Loading users...</div>;
}
```

---

### 10. Error Handling ⭐
**Time:** 10 minutes  
**Tests:** error.tsx

**Challenge:**
```typescript
// Add error boundary
```

**What interviewers look for:**
```typescript
// app/users/error.tsx
'use client';

export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <p>{error.message}</p>
      <button onClick={reset}>Try again</button>
    </div>
  );
}
```

---

## 🎯 Tier 2: Mid-Level (15 questions)
**Target:** 2-4 years Next.js experience | Time: 15-30 min each

### 11. Static Generation ⭐⭐
**Time:** 15 minutes  
**Tests:** generateStaticParams

**Challenge:**
```typescript
// Pre-render blog posts at build time
// /blog/[slug]
```

**What interviewers look for:**
```typescript
// app/blog/[slug]/page.tsx
interface Post {
  slug: string;
  title: string;
  content: string;
}

// Generate static paths at build time
export async function generateStaticParams() {
  const posts = await fetch('https://api.example.com/posts').then(res => res.json());
  
  return posts.map((post: Post) => ({
    slug: post.slug,
  }));
}

// Fetch data for each path
async function getPost(slug: string) {
  const res = await fetch(`https://api.example.com/posts/${slug}`);
  return res.json();
}

export default async function BlogPost({
  params
}: {
  params: { slug: string }
}) {
  const post = await getPost(params.slug);

  return (
    <article>
      <h1>{post.title}</h1>
      <div>{post.content}</div>
    </article>
  );
}
```

---

### 12. API Route ⭐⭐
**Time:** 15 minutes  
**Tests:** Route handlers

**Challenge:**
```typescript
// Create API endpoint
// GET /api/users
```

**What interviewers look for:**
```typescript
// app/api/users/route.ts
import { NextResponse } from 'next/server';

export async function GET() {
  const users = [
    { id: 1, name: 'John' },
    { id: 2, name: 'Jane' }
  ];

  return NextResponse.json(users);
}

export async function POST(request: Request) {
  const body = await request.json();
  
  // Process data
  console.log(body);

  return NextResponse.json({ success: true }, { status: 201 });
}
```

---

### 13. Server Actions ⭐⭐
**Time:** 20 minutes  
**Tests:** "use server" directive

**Challenge:**
```typescript
// Form submission with server action
```

**What interviewers look for:**
```typescript
// app/contact/page.tsx
import { revalidatePath } from 'next/cache';

async function submitForm(formData: FormData) {
  'use server';
  
  const name = formData.get('name');
  const email = formData.get('email');

  // Process form (save to DB, etc.)
  console.log({ name, email });

  // Revalidate if needed
  revalidatePath('/contact');
}

export default function ContactPage() {
  return (
    <form action={submitForm}>
      <input name="name" required />
      <input name="email" type="email" required />
      <button type="submit">Submit</button>
    </form>
  );
}
```

---

### 14. Middleware ⭐⭐
**Time:** 18 minutes  
**Tests:** middleware.ts

**Challenge:**
```typescript
// Add authentication middleware
// Redirect to /login if not authenticated
```

**What interviewers look for:**
```typescript
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('token');

  // Protect /dashboard routes
  if (request.nextUrl.pathname.startsWith('/dashboard')) {
    if (!token) {
      return NextResponse.redirect(new URL('/login', request.url));
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: '/dashboard/:path*',
};
```

---

### 15. Parallel Routes ⭐⭐
**Time:** 20 minutes  
**Tests:** @folder convention

**Challenge:**
```typescript
// Create dashboard with parallel team and analytics sections
```

**What interviewers look for:**
```typescript
// app/dashboard/layout.tsx
export default function DashboardLayout({
  children,
  team,
  analytics,
}: {
  children: React.ReactNode;
  team: React.ReactNode;
  analytics: React.ReactNode;
}) {
  return (
    <div>
      <div>{children}</div>
      <div className="grid grid-cols-2">
        <div>{team}</div>
        <div>{analytics}</div>
      </div>
    </div>
  );
}

// app/dashboard/@team/page.tsx
export default function TeamPage() {
  return <h2>Team Section</h2>;
}

// app/dashboard/@analytics/page.tsx
export default function AnalyticsPage() {
  return <h2>Analytics Section</h2>;
}
```

---

### 16. Intercepting Routes ⭐⭐
**Time:** 22 minutes  
**Tests:** (.)folder convention

**Challenge:**
```typescript
// Modal on same page, full page on refresh
```

**What interviewers look for:**
```typescript
// app/photos/[id]/page.tsx
export default function PhotoPage({
  params
}: {
  params: { id: string }
}) {
  return (
    <div>
      <h1>Photo {params.id}</h1>
      <img src={`/photos/${params.id}.jpg`} alt="Photo" />
    </div>
  );
}

// app/photos/(.)photo/[id]/page.tsx
export default function PhotoModal({
  params
}: {
  params: { id: string }
}) {
  return (
    <div className="modal">
      <h2>Photo {params.id} (Modal)</h2>
      <img src={`/photos/${params.id}.jpg`} alt="Photo" />
    </div>
  );
}
```

---

### 17. Streaming ⭐⭐
**Time:** 20 minutes  
**Tests:** Suspense, streaming

**Challenge:**
```typescript
// Stream slow component
```

**What interviewers look for:**
```typescript
// app/dashboard/page.tsx
import { Suspense } from 'react';

async function SlowComponent() {
  // Simulate slow data fetch
  await new Promise(resolve => setTimeout(resolve, 3000));
  return <div>Slow data loaded!</div>;
}

export default function DashboardPage() {
  return (
    <div>
      <h1>Dashboard</h1>
      
      <div>Fast content</div>
      
      <Suspense fallback={<div>Loading slow data...</div>}>
        <SlowComponent />
      </Suspense>
    </div>
  );
}
```

---

### 18-25. Additional Mid-Level Questions

**18. Route Groups** (15 min)
- (folder) organization
- Shared layouts

**19. Private Folders** (12 min)
- _folder convention
- Organization

**20. Environment Variables** (12 min)
- .env.local
- NEXT_PUBLIC_ prefix

**21. Font Optimization** (15 min)
- next/font/google
- Variable fonts

**22. Script Component** (12 min)
- next/script
- Loading strategies

**23. Redirects** (15 min)
- redirect() function
- permanentRedirect()

**24. Not Found** (12 min)
- not-found.tsx
- notFound() function

**25. Route Handlers** (18 min)
- CRUD API
- Request/Response

---

## 🎯 Tier 3: Senior Level (15 questions)
**Target:** 4-6 years Next.js experience | Time: 25-40 min each

### 26. Full-Stack CRUD ⭐⭐⭐
**Time:** 35 minutes  
**Tests:** API routes + DB integration

**Challenge:**
```typescript
// Complete CRUD for todos
// API routes + Prisma
```

**What interviewers look for:**
```typescript
// prisma/schema.prisma
model Todo {
  id        String   @id @default(uuid())
  title     String
  completed Boolean  @default(false)
  createdAt DateTime @default(now())
}

// app/api/todos/route.ts
import { NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';

export async function GET() {
  const todos = await prisma.todo.findMany();
  return NextResponse.json(todos);
}

export async function POST(request: Request) {
  const { title } = await request.json();
  
  const todo = await prisma.todo.create({
    data: { title }
  });

  return NextResponse.json(todo, { status: 201 });
}

// app/api/todos/[id]/route.ts
export async function PUT(
  request: Request,
  { params }: { params: { id: string } }
) {
  const { completed } = await request.json();
  
  const todo = await prisma.todo.update({
    where: { id: params.id },
    data: { completed }
  });

  return NextResponse.json(todo);
}

export async function DELETE(
  request: Request,
  { params }: { params: { id: string } }
) {
  await prisma.todo.delete({
    where: { id: params.id }
  });

  return NextResponse.json({ success: true });
}
```

---

### 27. Authentication ⭐⭐⭐
**Time:** 35 minutes  
**Tests:** NextAuth.js

**Challenge:**
```typescript
// Setup authentication
// Email/password + OAuth
```

**What interviewers look for:**
```typescript
// app/api/auth/[...nextauth]/route.ts
import NextAuth from 'next-auth';
import GoogleProvider from 'next-auth/providers/google';
import CredentialsProvider from 'next-auth/providers/credentials';

const handler = NextAuth({
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    }),
    CredentialsProvider({
      name: 'Credentials',
      credentials: {
        email: { label: "Email", type: "email" },
        password: { label: "Password", type: "password" }
      },
      async authorize(credentials) {
        // Validate credentials
        const user = await validateUser(credentials);
        return user || null;
      }
    })
  ],
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.id = user.id;
      }
      return token;
    },
    async session({ session, token }) {
      if (session.user) {
        session.user.id = token.id as string;
      }
      return session;
    }
  }
});

export { handler as GET, handler as POST };
```

---

### 28. Incremental Static Regeneration ⭐⭐⭐
**Time:** 25 minutes  
**Tests:** ISR, revalidate

**Challenge:**
```typescript
// Blog posts with ISR
// Revalidate every 60 seconds
```

**What interviewers look for:**
```typescript
// app/blog/[slug]/page.tsx
export const revalidate = 60; // Revalidate every 60 seconds

async function getPost(slug: string) {
  const res = await fetch(`https://api.example.com/posts/${slug}`, {
    next: { revalidate: 60 }
  });
  return res.json();
}

export default async function BlogPost({
  params
}: {
  params: { slug: string }
}) {
  const post = await getPost(params.slug);

  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </article>
  );
}
```

---

### 29-40. Additional Senior Questions

**29. On-Demand Revalidation** (20 min)
- revalidatePath
- revalidateTag

**30. Image Upload** (30 min)
- File handling
- Cloud storage

**31. Search Params** (20 min)
- useSearchParams
- Server-side search

**32. Internationalization** (30 min)
- i18n routing
- Multiple locales

**33. Caching Strategies** (25 min)
- Cache control
- Fetch options

**34. Optimistic Updates** (25 min)
- Client mutations
- Rollback

**35. Rate Limiting** (25 min)
- API protection
- Redis/Upstash

**36. Webhooks** (25 min)
- Handle external events
- Verify signatures

**37. File-based Routing** (20 min)
- Complex routes
- Route organization

**38. Metadata API** (20 min)
- Dynamic metadata
- OpenGraph

**39. Sitemap Generation** (18 min)
- sitemap.xml
- Dynamic routes

**40. RSS Feed** (20 min)
- RSS generation
- Content feed

---

## 🎯 Tier 4: Lead Level (10 questions)
**Target:** 6+ years Next.js experience | Time: 30-45 min each

### 41. Multi-Tenant Architecture ⭐⭐⭐⭐
**Time:** 40 minutes  
**Tests:** Advanced routing, DB isolation

**Challenge:**
```typescript
// Multi-tenant SaaS
// Each tenant: subdomain or path
```

**What interviewers look for:**
- Middleware for tenant resolution
- Database schema per tenant
- Shared/isolated data
- Performance optimization

---

### 42-50. Additional Lead Questions

**42. Edge Functions** (35 min)
- Edge runtime
- Geo-routing

**43. Streaming SSR** (30 min)
- Advanced streaming
- Partial hydration

**44. Custom Server** (35 min)
- Express integration
- WebSockets

**45. Monorepo Setup** (40 min)
- Turborepo
- Shared packages

**46. Performance Optimization** (35 min)
- Bundle analysis
- Code splitting

**47. Analytics Integration** (25 min)
- Vercel Analytics
- Custom events

**48. A/B Testing** (30 min)
- Feature flags
- Middleware routing

**49. SEO Optimization** (30 min)
- Complete SEO
- Structured data

**50. CI/CD Pipeline** (35 min)
- GitHub Actions
- Deployment

---

## 📊 Most Common Next.js Questions

### Top 10:
1. **Server vs Client Components** - 95%
2. **Data Fetching** - 100%
3. **API Routes** - 90%
4. **Dynamic Routes** - 95%
5. **Layouts** - 85%
6. **Server Actions** - 80%
7. **Middleware** - 75%
8. **Static Generation** - 85%
9. **Image Optimization** - 70%
10. **Authentication** - 80%

---

## 💡 Next.js Interview Tips

### DO:
✅ Master App Router
✅ Understand server components
✅ Use server actions
✅ Leverage caching
✅ Optimize images

### DON'T:
❌ Use "use client" everywhere
❌ Fetch data client-side
❌ Ignore SEO
❌ Skip error handling
❌ Forget loading states

---

## 🚀 Next.js-Specific Concepts

### Essential:
- Server Components (default)
- Client Components ("use client")
- Server Actions ("use server")
- Route Handlers (API)
- Streaming/Suspense

### Advanced:
- Parallel Routes
- Intercepting Routes
- Middleware
- Edge Runtime
- ISR/On-Demand Revalidation

---

**Total Questions:** 50  
**Practice Time:** 30-40 hours  
**Success Rate:** 85%+ with App Router mastery

Good luck! ▲
