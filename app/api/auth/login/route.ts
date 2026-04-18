import { NextResponse } from 'next/server';
import { signToken, setAuthCookie, validatePassword } from '../../../../lib/auth';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { password } = body;

    if (!password) {
      return NextResponse.json(
        { error: 'Password is required' },
        { status: 400 }
      );
    }

    const isValid = await validatePassword(password);

    if (!isValid) {
      return NextResponse.json(
        { error: 'Invalid password' },
        { status: 401 }
      );
    }

    // Create session token
    const token = await signToken({
      authenticated: true,
      timestamp: Date.now(),
    });

    // Create response with cookie
    const response = NextResponse.json({ success: true });
    setAuthCookie(response, token);

    return response;
  } catch (error) {
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}
