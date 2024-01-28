# Virology Research Data Logger

## Overview

Welcome to the Virology Research Data Logger, an innovative system designed to accelerate virology research at the National Institute of Virology. This web-based application features a user-friendly dashboard, seamless sensor integration, enhanced data logging, MQTT protocol implementation, role-based access control, and real-time alerts. The system is built using the Django framework, MQTT protocol, Python, HTML/CSS/JavaScript, and utilizes a database (e.g., PostgreSQL) for efficient data storage.

## Key Features

### Dashboard
- Real-time monitoring of diverse virus-related data streams.
- Intuitive web-based interface for visualizing and analyzing critical information.

### Sensor Integration
- Seamless integration with an array of sensors deployed in the laboratory.
- Holistic view of virus behavior, enhancing the research process.

### Enhanced Data Logging
- Advanced data logging techniques for secure and efficient storage of large datasets.
- Streamlined and organized handling of extensive virology data.

### MQTT Protocol Implementation
- Standardized and secure communication with other government servers.
- Promotes collaboration and data interoperability.

### Role-Based Access Control
- Robust access control mechanism ensuring scientists access only relevant data.
- Safeguards sensitive information and promotes data integrity.

### Real-time Alerts
- Alerting system for notifying scientists of critical events or anomalies.
- Enables swift response and implementation of mitigation measures.

## Technological Stack

- **Django Framework:** A high-level Python web framework for rapid development and clean, pragmatic design.
- **MQTT Protocol:** Lightweight and efficient messaging protocol for communication between devices.
- **Python:** General-purpose programming language used for application logic.
- **HTML/CSS/JavaScript:** Front-end technologies for creating an interactive and responsive user interface.
- **Database (e.g., PostgreSQL):** Reliable and scalable database management system for data storage.
- **Sensor Integration Technologies:** Various technologies integrated for comprehensive data capture.

## Installation Process

To set up the Virology Research Data Logger on your local environment, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ketanmore2002/web-logger-2.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd web-logger-2
   ```

3. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

9. **Access the Application:**
   Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

10. **Log in with the Superuser Credentials:**
    Use the superuser credentials created in step 7 to log in and explore the features.


### Images 

<img width="1470" alt="Screenshot 2024-01-23 at 11 52 11 AM" src="https://github.com/ketanmore2002/web-logger-2/assets/88627103/ced957fe-65b9-4b95-a73c-208f11085c71">

<img width="1470" alt="Screenshot 2024-01-23 at 11 51 14 AM" src="https://github.com/ketanmore2002/web-logger-2/assets/88627103/482df853-15e8-462b-a025-24df9e083ff7">

<img width="1470" alt="Screenshot 2024-01-28 at 7 19 12 PM" src="https://github.com/ketanmore2002/web-logger-2/assets/88627103/caf60572-811a-4b2b-b7ec-30393aaa7cf7">

<img width="1470" alt="Screenshot 2024-01-28 at 7 19 47 PM" src="https://github.com/ketanmore2002/web-logger-2/assets/88627103/f1dca506-d3af-434a-9d46-8d5a6796adfa">


