# Fraud Detection Web Application

## Overview
* Real-time fraud detection system using Flask and machine learning
* Processes financial transactions and predicts fraud probability
* Containerized solution with comprehensive logging


## project structure
```
flask_model_api/
├── app.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── templates/
  └── index.html
```
## Features
* Real-time fraud detection processing
* Machine learning model integration
* Comprehensive system logging
* Dockerized deployment support
* Clean web interface

## Technology Stack
* Backend: Flask
* ML: scikit-learn
* Data Processing: pandas
* Containerization: Docker
* Frontend: HTML/Bootstrap

## Installation

### Local Setup
```bash
   git clone https://github.com/Endekalu777/Enhanced-Fraud-Detection-for-E-commerce-and-Banking-Transactions.git
   cd Enhanced-Fraud-Detection-for-E-commerce-and-Banking-Transactions
   git checkout task4
   ```

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

## Docker setup
### Build image
docker build -t fraud-detection-app .

### Run container
docker run -p 5000:5000 fraud-detection-app

## License

This project is licensed under the MIT License. Refer to the LICENSE file for details.

## Author

Endekalu Simon

## Acknowledgments

This project utilizes Dash for the dashboard interface and Flask for the backend API. Special thanks to 10academy for providing the dataset and challenge for API design.

*Note: This represents the **task4** branch of the project, which includes specific features for the Fraud Detection Dashboard.* 😊