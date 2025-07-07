# Task Tracker API

## Overview
Task Tracker is a FastAPI-based application for managing tasks with CRUD functionality. It uses PostgreSQL as the database and is fully containerized using Docker and Docker Compose.

## Features
- **GET /tasks/**: Retrieve a list of all tasks.
- **POST /tasks/**: Create a new task.
- **GET /tasks/{task_id}**: Get details of a specific task.
- **PUT /tasks/{task_id}**: Update a task.
- **DELETE /tasks/{task_id}**: Delete a task.

## Technologies Used
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker & Docker Compose

## Setup Instructions

### Prerequisites
- Docker
- Docker Compose

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd taskTrcker
   ```

2. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

3. Access the API documentation:
   Open your browser and navigate to `http://localhost:8000/docs`.

## Project Structure
```
app/
    api/
    models/
    repository/
    routers/
    schemas/
cmd/
    main.py
```

## License
This project is licensed under the MIT License.
