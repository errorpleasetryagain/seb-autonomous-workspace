# Authentication System Setup

## Files Created

### Core Auth Files
- `lib/auth.ts` - Authentication utilities (JWT signing/verification, cookie management, password validation)
- `middleware.ts` - Route protection middleware (redirects unauthenticated users to /login)
- `components/AuthProvider.tsx` - React context provider for auth state management
- `.env.local` - Environment variables (AUTH_PASSWORD, AUTH_SECRET, cookie settings)

### Login Page
- `app/login/page.tsx` - Login UI with password input

### API Routes
- `app/api/auth/check/route.ts` - Check authentication status
- `app/api/auth/login/route.ts` - Handle login and set session cookie
- `app/api/auth/logout/route.ts` - Handle logout and clear cookie

## Required Setup

### 1. Install Dependencies
```bash
npm install jose
```

### 2. Configure Environment
Edit `.env.local`:
```bash
AUTH_PASSWORD=your-secure-password
AUTH_SECRET=generate-a-random-secret-key-here
```

Generate a secure secret:
```bash
openssl rand -base64 32
```

### 3. Add AuthProvider to Root Layout
In `app/layout.tsx`:
```tsx
import { AuthProvider } from './components/AuthProvider';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <AuthProvider>
          {children}
        </AuthProvider>
      </body>
    </html>
  );
}
```

### 4. Add Logout Button (Optional)
```tsx
import { useAuth } from './components/AuthProvider';

function Header() {
  const { logout, isAuthenticated } = useAuth();
  
  if (!isAuthenticated) return null;
  
  return (
    <button onClick={logout}>Logout</button>
  );
}
```

## Security Features

- ✅ Password stored in environment variable (`.env.local`)
- ✅ JWT tokens with 24h expiration
- ✅ HTTP-only cookies (not accessible via JavaScript)
- ✅ Secure cookies in production
- ✅ Middleware protects all routes except `/login` and static files
- ✅ Server-side session validation

## Usage Flow

1. User visits any protected route → redirected to `/login`
2. User enters password → POST to `/api/auth/login`
3. If valid → JWT token set in HTTP-only cookie
4. Middleware validates token on subsequent requests
5. User clicks logout → cookie cleared, redirected to login
