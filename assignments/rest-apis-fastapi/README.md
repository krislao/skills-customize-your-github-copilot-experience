# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using FastAPI and Pydantic to practice endpoint design, request validation, and CRUD operations.

## 📝 Tasks

### 🛠️	Implement REST CRUD endpoints

#### Description
Create endpoints to create, read, update, and delete a simple `Item` resource. Return JSON responses with the correct HTTP status codes.

#### Requirements
Completed program should:

- Provide endpoints for `POST /items`, `GET /items/{id}`, `PUT /items/{id}`, and `DELETE /items/{id}`.
- Return a created item with a unique ID when a new item is posted.
- Return a `404` error when a requested item does not exist.
- Return `204` or a suitable success response for delete operations.

### 🛠️	Validate item data with Pydantic

#### Description
Define a Pydantic model for the `Item` resource and use it to validate incoming request bodies.

#### Requirements
Completed program should:

- Use a Pydantic model with fields `id: int`, `name: str`, `description: str | None`, and `price: float`.
- Enforce that `name` is non-empty and `price` is greater than zero.
- Return validation errors when request data is invalid.
