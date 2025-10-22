# Simple Authentication System

This document describes the simplified authentication system implemented for the Price Rule Loader application.

## Overview

The authentication system provides simple access control for the Streamlit application with the following features:

- **Simple Login/Logout**: Basic username/password authentication
- **Environment Variable Configuration**: Credentials stored in environment variables
- **Session Management**: Session state maintained during app usage
- **Clean UI**: Minimal authentication interface

## Custom Credentials

You can set custom credentials using environment variables:

- `PRICE_LOADER_USERNAME` - Your custom username
- `PRICE_LOADER_PASSWORD` - Your custom password

## File Structure

```
src/
├── utils/
│   └── auth_utils.py          # Simple authentication functions
└── view/
    └── auth.py                # Authentication sidebar and helpers
```

## Key Components

### Authentication Utils (`src/utils/auth_utils.py`)
- `check_authentication()` - Main authentication function with login form
- `logout_user()` - Simple logout function
- `is_authenticated()` - Check authentication status

### Authentication Views (`src/view/auth.py`)
- `auth_sidebar()` - Display logout button in sidebar
- `require_login()` - Wrapper for authentication check

## Usage

### For Users
1. Navigate to the application
2. Enter your username and password on the login page
3. Access all application pages after authentication
4. Use the logout button in the sidebar when done

## Configuration

### Environment Variables
Create a `.env` file in the project root with your credentials:

```bash
PRICE_LOADER_USERNAME=your_username
PRICE_LOADER_PASSWORD=your_password
```

If no `.env` file is provided, the application uses default credentials.

## Integration

The authentication system is integrated into the main application (`loader_main.py`) and automatically:

1. Checks authentication status on page load
2. Redirects unauthenticated users to login page
3. Displays user info and logout option in sidebar
4. Protects sensitive pages like Price Rule Loader

## Troubleshooting

### Cannot Login
- Verify username and password are correct
- Check if `users.json` file exists and is readable
- Try using default admin credentials

### Session Expired
- Sessions automatically expire after 30 minutes
- Simply log in again to continue

### User Management Issues
- Only admin users can access user management
- Ensure you're logged in with admin role

## Security Considerations

1. **Change Default Password**: Always change the default admin password
2. **User File Security**: Protect the `users.json` file from unauthorized access
3. **HTTPS**: Use HTTPS in production environments
4. **Regular Updates**: Keep dependencies updated for security patches

## Future Enhancements

Potential improvements for the authentication system:

- Database storage instead of JSON files
- Password complexity requirements
- Account lockout after failed attempts
- Email verification for new users
- Two-factor authentication
- Audit logging for security events
