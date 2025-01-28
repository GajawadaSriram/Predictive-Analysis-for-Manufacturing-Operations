# Project Name

## Description
A short description of your project, what it does, and its goals. This should give the reader an idea of what the project is about and why it's useful.

Example:
This project provides an API to predict machine downtime based on temperature and runtime data. It allows uploading data, training a model, and making predictions about machine failures.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [API Endpoints](#api-endpoints)
4. [Technologies Used](#technologies-used)
5. [Contributing](#contributing)
6. [License](#license)

## Installation
### Prerequisites
- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

### Steps
1. Clone this repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```

4. The app will be hosted locally at `http://127.0.0.1:5000/`.

## Usage
Once the app is running locally, you can access the web interface via your browser.

### How to Use the Web Interface:
1. **Upload Data**: Go to the web page and upload a CSV file with machine data (Temperature, Run Time, and Downtime).
2. **Train Model**: After uploading the data, click on **Start Training** to train the model.
3. **Make Prediction**: After training, input the **Temperature** and **Run Time** values, and click **Predict Downtime** to get the downtime prediction.

## API Endpoints

### 1. **/upload**
- **Method**: `POST`
- **Description**: Upload a CSV file with data for training.
- **Request**: 
    - `multipart/form-data` (File upload)
- **Response**: 
    - Message indicating whether the upload was successful or failed.

### 2. **/train**
- **Method**: `POST`
- **Description**: Train the model with the uploaded dataset.
- **Response**: 
    - Accuracy and F1 score after training.

### 3. **/predict**
- **Method**: `POST`
- **Description**: Predict machine downtime based on provided **Temperature** and **Run Time**.
- **Request**:
    - JSON body with `Temperature` and `Run_Time`
- **Response**:
    - Predicted `Downtime` and confidence level (`Confidence`).

## Technologies Used
- **Flask**: Python web framework for building the API.
- **Pandas**: Data manipulation.
- **Scikit-learn**: Machine learning library for training models.
- **DecisionTreeClassifier**: Model used for downtime prediction.

## Contributing
We welcome contributions! Please fork this repository and submit pull requests with improvements or bug fixes.

### Steps:
1. Fork the repository.
2. Clone your forked repository.
3. Create a new branch (`git checkout -b feature-branch`).
4. Commit your changes (`git commit -am 'Added new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.


