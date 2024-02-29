<img src="[example.png](https://ibb.co/ZBgH5ZL)" alt="Example Image" style="height: 100px; width:100px;"/>
# FastAPI - First Database

This is a simple FastAPI application that simulates a database of students. It allows you to perform basic CRUD operations (Create, Read, Update, Delete) on the student data.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/Tanvir-yzu/FastAPI.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI application:

    ```
    uvicorn myapi:app --reload
    ```

2. Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view the API documentation.

## API Endpoints

- `GET /`: Returns the name of the database.
- `GET /get-student/{student_id}`: Returns the details of a student with the given ID.
- `GET /get-student-by-name/{student_id}`: Returns the details of a student with the given name.
- `POST /create-student/{student_id}`: Creates a new student with the given ID and details.
- `PUT /update-student/{student_id}`: Updates the details of a student with the given ID.
- `DELETE /delete-student/{student_id}`: Deletes the student with the given ID.

## Data Structure

The student data is stored in a dictionary in the `myapi.py` file. Each student is represented as a dictionary with keys `name`, `age`, and `class`.

## Models

The `Student` and `updatedStudent` models are defined in the `myapi.py` file. These models are used to validate the data sent to the API.

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- [Uvicorn](https://www.uvicorn.org/): A lightning-fast ASGI server implementation, using uvloop and httptools.

## License

This project is licensed under the terms of the MIT license.
