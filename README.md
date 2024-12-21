## Installation

Follow these steps to set up and run the backend API locally.

### Prerequisites

-   Python 3.10 or higher
-   `pip` (Python package manager)

### Step 1: Install dependencies

Once the virtual environment is set up, install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 2: Start the FastAPI server

Once the dependencies are installed, you can start the FastAPI server using Uvicorn. Run the following command:

```bash
uvicorn app.main:app --reload
```

-   **`app.main:app`**: Refers to the FastAPI instance defined in `main.py` (inside the `app` folder).
-   **`--reload`**: Enables auto-reloading during development.

The server will start, and you can access the API at `http://127.0.0.1:8000`.


## API Endpoints

### 1. **POST /analyze-csv/**

-   **Description**: Upload a CSV file containing text data, and the API will return sentiment analysis results.
-   **Request Body**: A `multipart/form-data` request containing the CSV file.
-   **Response**: JSON object containing sentiment results.
