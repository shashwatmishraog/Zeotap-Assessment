# App1: Rule Engine Web Application

## Overview

The Rule Engine Web Application is a simple 3-tier application that determines user eligibility based on various attributes like age, department, income, and experience. It utilizes an Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, and modification of these rules. The application is built with a React frontend, a FastAPI backend, and uses a virtual environment for Python dependencies.

## Features

- Create individual rules using a simple UI.
- Combine multiple rules into a single AST.
- Evaluate user eligibility based on provided attributes.
- Handle errors and validate rules dynamically.
- Easy setup and deployment.

## Table of Contents

- [Technologies Used](#technologies-used-app1)
- [Folder Structure](#folder-structure-app1)
- [Setup Instructions](#setup-instructions-app1)
- [API Endpoints](#api-endpoints-app1)
- [Usage](#usage-app1)
- [Contributing](#contributing-app1)
- [License](#license-app1)

## Technologies Used (App1)

- **Frontend**: React, Axios
- **Backend**: FastAPI
- **Python**: 3.8+
- **Node.js**: 14+
- **Virtual Environment**: venv
- **Package Manager**: npm

## Folder Structure (App1)

```plaintext
rule-engine-webapp/
├── backend/
│   ├── main.py                # Main FastAPI application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── rule_parser.py      # Rule parsing and evaluation logic
│   └── venv/                  # Python virtual environment
│
└── frontend/
    ├── public/
    ├── src/
    │   ├── App.js             # Main application component
    │   ├── components/        # React components
    │   ├── services/          # API service for fetching data
    │   └── index.js           # Entry point of the React application
    ├── package.json           # NPM package configuration
    └── package-lock.json      # Dependency lock file
```

## Setup Instructions (App1)

### Backend Setup

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   ```

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn
   ```

4. **Run the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

   Your backend should now be running at `http://localhost:8000`.

### Frontend Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run the React application**:
   ```bash
   npm start
   ```

   Your frontend should now be accessible at `http://localhost:3000`.

## API Endpoints (App1)

### Create Rule

- **Endpoint**: `/create_rule/`
- **Method**: `POST`
- **Body**: 
  ```json
  {
      "rule_string": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
  }
  ```

### Combine Rules

- **Endpoint**: `/combine_rules/`
- **Method**: `POST`
- **Body**: 
  ```json
  [
      "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing'))",
      "((age > 30 AND department = 'Marketing'))"
  ]
  ```

### Evaluate Rule

- **Endpoint**: `/evaluate_rule/`
- **Method**: `POST`
- **Body**: 
  ```json
  {
      "rule_ast": { /* AST representation */ },
      "data": {
          "age": 35,
          "department": "Sales",
          "salary": 60000,
          "experience": 3
      }
  }
  ```

## Usage (App1)

1. **Open your browser and navigate to** `http://localhost:3000`.
2. **Use the provided UI** to create rules, combine them, and evaluate eligibility based on attributes.

## Error Handling (App1)

The application includes error handling for:
- Invalid rule strings or data formats (e.g., missing operators, invalid comparisons).
- Validation for attributes to be part of a catalog.

## Contributing (App1)

Contributions are welcome! Please open an issue or submit a pull request if you'd like to enhance this application.

## License (App1)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# App2: TechWeath


## Live Demo

Ready to check out the weather in real-time? Visit the deployed TechWeath application:
[Project URL APP 2]((https://app2-zeotap.netlify.app/))

## Features

* Seamless Location Detection: Automatically displays weather conditions based on your current location, using the Geolocation API.
* Global Search: Look up the weather in any city worldwide using the convenient search bar.
* Responsive Design: Enjoy a smooth user experience on any device, be it a desktop, tablet, or mobile phone.
* Up-to-the-Minute Data: Get the latest weather information with the power of the OpenWeather API.

## Technologies Used (App2)

* ReactJS: Builds the user interface with a robust and flexible frontend framework.
* OpenWeather API: Provides accurate and real-time weather data for your application.
* Geolocation API: Pinpoints your current location for a personalized weather experience.
* Axios: Enables streamlined communication with the OpenWeather API through HTTP requests.

## Getting Started (Optional)

If you'd like to contribute to the development of TechWeath or run the project locally, here's a guide:

### Prerequisites

* Node.js: Download and install Node.js from the official website ([https://nodejs.org/](https://nodejs.org/)).
* npm or yarn: Choose one of these package managers:
    * npm: Comes bundled with Node.js by default.
    * yarn: An alternative package manager with additional features ([https://yarnpkg.com/en/](https://yarnpkg.com/en/)).

### Installation

1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/techweath.git
   ```
2. Navigate to the project directory:
   ```bash
   cd techweath
   ```
3. Install dependencies:
   ```bash
   npm install  # or yarn install
   ``'
