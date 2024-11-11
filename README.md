# Flask Greeting API

This is a simple RESTful API built using Flask. It provides a single `/greet` endpoint that returns a greeting message. The API accepts an optional query parameter `name`. If `name` is provided, it customizes the greeting message; otherwise, it defaults to `"Hello, World!"`.

## Getting Started

### Prerequisites

- Python 3.7 or later (for local installation)
- `pip` for package installation
- Docker running (for running the script in a container)

### Installation

#### Running Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/veo1/api-creation.git
   cd <api-creation>
    ```

2. **Set up a virtual environment (recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On macOS and Linux
    venv\Scripts\activate      # On Windows
    ```

3. **Install required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Running the application**:

To start the Flask API, run the following command:
    ```bash
    python api.py
    ```
The application will start a development server at `http://127.0.0.1:5000`.

#### Using Docker

Alternatively, you can run the API in a Docker container.
1. **Build the Docker image**:

    ```bash
    docker build -t greeting-api .
    ```
2. **Run the Docker image**: 
    ```bash
    docker run -p 5000:5000 greeting-api
    ```
The application will start a development server at `http://127.0.0.1:5000`.


### Using the API

You can test the API using `curl`, Postman, or a web browser.

#### Example Requests

- With a `name` parameter:
     ```bash
    curl "http://127.0.0.1:5000/greet?name=Anton"
    ```

    Expected Response:
    ```json
    {"message": "Hello, Anton!"}
    ```

- Without a `name` parameter:
    ```bash
    curl "http://127.0.0.1:5000/greet"
    ```

    Expected Response:
    ```json
    {"message": "Hello, World!"}
    ```

### Directory Structure
    ```
    ├── api.py              # Main application file containing the Flask API
    ├── requirements.txt    # List of Python dependencies
    ├── Dockerfile          # Docker configuration file (optional)
    ├── README.md           # Documentation file
    └── api.gif             # GIF of the API in action
    ```

#### File Descriptions

- `api.py`: Contains the Flask API implementation with a single endpoint `/greet`
- `requirements.txt`: List of Python dependencies.
- `Dockerfile`: Docker configuration file.
- `README.md`: Documentation file.
- `api.gif`: GIF of the API in action.