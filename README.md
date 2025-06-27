# PromptDirectory

Create, View, Update, and Delete prompts on PromptDirectory — A community for creating and sharing prompts.

---

## Table of Contents

1. [About](#about)
2. [Features](#features)
3. [Tech Stack Used](#tech-stack-used)
4. [Database Integration](#database-integration)
5. [Running the Server](#running-the-server)
6. [Running the Frontend Locally](#running-the-frontend-locally)
7. [Interacting with the API](#interacting-with-the-api)
8. [Running the Tests](#running-the-tests)

---

## About

**PromptDirectory** is a simple platform for managing AI prompts. It provides a RESTful API to create, read, update, and delete prompts. All prompts are public—no authentication or user models involved. This is an open-source tool with future potential to include LLM-driven prompt suggestions.

---

## Features

- View all community prompts  
- Add new prompts  
- Update prompts by ID  
- Delete prompts by ID  
- Public and open-source

---

## Tech Stack Used

- **Backend:** Django (Python)
- **Database:** MongoDB
- **Frontend:** HTML + TailwindCSS
- **Others:** Django REST Framework

---

## Database Integration

This project uses **MongoDB** as the backend database to store prompts.

- Integration is handled using the `pymongo` library to connect the MONGODB Client using the Database name and the connection URL (localhost:27017 for local)

## Running the Server

### 1. Clone the Repository
```
  git clone https://github.com/Manveer-Pbx1/PromptDirectory.git
  cd PromptDirectory
  cd API
```
### 2. Install Dependencies
```
  pip install -r requirements.txt
```
### 3. Run the Server
```
  python manage.py runserver
```

Visit http://localhost:8000 to access the API

---

## Running the Frontend Locally
The project includes a simple HTML frontend to interact with the API:
- Open Frontend/index.html in any browser
- Use the interface to send GET, POST, PUT, or DELETE requests to the server
- Make sure the server is running at https://localhost:8000

---

## Interacting with the API
- GET all prompts
```
    http://localhost:8000/api/prompts
```
  Response:
  
  ![image](https://github.com/user-attachments/assets/4decc158-32a8-4c87-88b2-27066ec74e60)

- POST a new prompt
```
  http://localhost:8000/api/prompts
```
  Payload:
  
  ![image](https://github.com/user-attachments/assets/8b27acbe-398a-4a95-8988-6c8a84530d29)
  
  Response:
  
  ![image](https://github.com/user-attachments/assets/f93a48ce-e83a-433a-afd6-9bc7a33697df)

- UPDATE a prompt
```
  http://localhost:8000/api/prompts/{prompt_id}
```
  Payload:
  
  ![image](https://github.com/user-attachments/assets/d09abb54-1027-4678-a930-ee8e1c150938)
  
  Response:
  
  ![image](https://github.com/user-attachments/assets/807f6004-94b7-47f7-af71-1b2ca5d61ff1)

- DELETE a prompt
```
  http://localhost:8000/api/prompts/{prompt_id}
```
  Response:
  
  ![image](https://github.com/user-attachments/assets/a3c6fb7c-97ed-4a98-bcc3-d6b774d8b087)

- GET information about a specific prompt
```
  http://localhost:8000/api/prompt/{prompt_id}
```
  Response:
  
  ![image](https://github.com/user-attachments/assets/3812ecef-d739-42d7-9de6-300981602d3b)


---

## Running the Tests
The application uses `pytest` as the main testing framework along with `pytest-django, unittest.mock, and Django's Test Client` for Django integration, mocking, and simulating HTTP requests respectively.

First, install the dependencies:
1. Navigate to the Tests folder
```
  cd API/promptDirectory/Tests
```
2. Install the dependencies
```
  pip install -r test_requirements.txt
```

To run the tests, do the following:
1. Navigate to the root folder
```
  cd API/promptDirectory
```
2. Run the command (with coverage):
```
  pytest --cov=prompts --cov-report=term-missing
```

This is the final coverage report (74%) that is obtained:
![image](https://github.com/user-attachments/assets/2fb0c3a2-64fa-4715-9d58-158778235698)



   
