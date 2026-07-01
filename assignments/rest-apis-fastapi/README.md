# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a small RESTful API using the FastAPI framework to learn endpoint design, request validation with Pydantic, and basic CRUD operations.

## 📝 Tasks

### 🛠️	Implement CRUD endpoints

#### Description
Create endpoints to Create, Read, Update, and Delete a simple `Item` resource. Ensure endpoints return appropriate HTTP status codes and JSON responses.

#### Requirements
Completed program should:

- Expose endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, and `DELETE /items/{id}`.
- Return JSON responses with correct status codes (200, 201, 204, 400, 404 as appropriate).
- Validate request bodies using Pydantic models.

### 🛠️	Data models and validation

#### Description
Design a Pydantic `Item` model and use it to validate incoming POST/PUT requests. Enforce simple field constraints.

#### Requirements
Completed program should:

- Define an `Item` model with fields: `id: int`, `name: str`, `description: Optional[str]`, `price: float`.
- Enforce `name` to be non-empty and `price` to be greater than zero.
- Return validation errors with explanatory messages when input is invalid.

## Starter Files

- `starter-code.py` — minimal FastAPI app with example endpoints and an in-memory store.

## Example

Create an item (example):

```bash
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" \
  -d '{"id":1, "name":"Notebook", "description":"A spiral notebook", "price":4.5}'
```

Get all items:

```bash
curl http://127.0.0.1:8000/items
```

## Hints

- Install dependencies with `pip install fastapi uvicorn`.
- Run the app with: `uvicorn starter-code:app --reload`.
- Use `response_model` on route decorators to enforce output schema.
- Use an in-memory dict for storage in this exercise; persistence is not required.

## Learning Outcomes

- Understand RESTful endpoint design and common HTTP methods/status codes.
- Use FastAPI and Pydantic for request validation and automatic documentation.
- Practice writing simple integration examples using `curl` and running a local server.
