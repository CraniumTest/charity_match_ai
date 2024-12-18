# README for CharityMatch AI Platform Prototype

## Overview

The CharityMatch AI Platform is a prototype designed to assist potential donors and volunteers in finding non-profit organizations that align with their personal preferences and values. It employs machine learning techniques to personalize recommendations for users.

## Features

- **Personalized Recommendations**: The platform utilizes a machine learning model to suggest non-profit organizations based on user input.
- **Web-based Interface**: A RESTful API allows users to request recommendations through HTTP.

## Project Structure

- `data/`: This directory contains sample data for non-profit organizations which the recommendation model uses to generate suggestions.
- `src/`: This directory includes the main application files and essential components such as the Flask app (`main.py`), machine learning model (`models.py`), utility functions (`utils.py`), and recommendation logic (`recommender.py`).
- `tests/`: Contains unit tests that ensure the recommendation functionality operates as expected.

## Setup Instructions

### Installation

1. **Clone the Repository**
   - Begin by cloning the project repository to your local machine.

2. **Install Dependencies**
   - Navigate to the project folder and install the required Python packages using Pip:

     ```bash
     pip install -r requirements.txt
     ```

### Running the Application

1. **Start the Server**
   - Launch the Flask application by executing the following command from the `src` directory:

     ```bash
     python main.py
     ```

2. **Accessing the API**
   - Use a tool like Postman or Curl to send a POST request to `http://127.0.0.1:5000/recommend` with JSON input representing user preferences.

## Testing

- Run the unit tests contained in the `tests` directory to ensure that the recommendation system functions correctly. These tests focus on the recommendation logic.

## Future Improvements

- **Data Validation and Error Handling**: Enhance input data processing to manage errors and unexpected inputs gracefully.
- **Model Enhancement**: Improve the breadth of features used by the machine learning model, such as incorporating more user data points and expanding non-profit characteristics.
- **User Interface**: Develop a user-friendly graphical interface to supplement the API, making the platform accessible to non-technical users.

The CharityMatch AI Platform prototype is a scalable and robust starting point for deploying a full-featured solution connecting individuals with impactful non-profit opportunities.
