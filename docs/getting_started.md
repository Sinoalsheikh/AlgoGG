# Getting Started with lvlhub

## Overview

lvlhub is a powerful platform for creating and managing AI-powered virtual agents. This guide will help you get started with the basic setup and usage of the platform.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/lvlhub.git
cd lvlhub
```

2. Install dependencies:
```bash
pip install -e .
```

## Basic Usage

### 1. Initialize the Platform

```python
from lvlhub.src.core import LvlhubPlatform, SuiteType

# Initialize the platform
platform = LvlhubPlatform()
```

### 2. Create a User Profile

```python
# Define user details
demographics = {
    "industry": "technology",
    "company_size": "500+"
}
preferences = {
    "theme": "dark",
    "notifications": True
}

# Create user profile
profile = platform.core.create_user_profile(
    user_id="user123",
    suite_type=SuiteType.ENTERPRISE,
    demographics=demographics,
    preferences=preferences
)
```

### 3. Create a Session

```python
# Authentication data
auth_data = {
    "username": "user123",
    "password": "secure_password"
}

# Create session
session_token = platform.create_session("user123", auth_data)
```

### 4. Process Requests

```python
# Example recommendation request
request_data = {
    "type": "recommendation",
    "parameters": {
        "context": "work",
        "limit": 5
    }
}

# Get recommendations
recommendations = platform.process_request(session_token, request_data)
```

## Configuration

The platform can be configured using the `config.yaml` file in the `config` directory. Different environments (development, production, testing) can have different configurations.

### Environment Variables

For production, sensitive information should be set using environment variables:

- DB_HOST
- DB_PORT
- DB_NAME
- DB_USER
- DB_PASSWORD
- MONGODB_URI
- REDIS_HOST
- REDIS_PORT
- REDIS_PASSWORD
- JWT_SECRET
- ENCRYPTION_KEY
- GOOGLE_CLIENT_ID
- GOOGLE_CLIENT_SECRET
- GITHUB_CLIENT_ID
- GITHUB_CLIENT_SECRET

## Running Tests

```bash
python -m unittest discover lvlhub/tests
```

## Next Steps

- Check out the API documentation for detailed information about available endpoints and features
- Review the configuration options to customize the platform for your needs
- Explore the different suite types and their specific features
- Join our community for support and discussions

## Support

For issues and feature requests, please use our GitHub issue tracker or contact our support team at support@lvlhub.com.
