# IoT Device Fleet Manager

A dashboard to onboard, configure, and update firmware on ESP8266/ESP32 devices via MQTT.

## Features
- Device onboarding
- Remote configuration
- Firmware updates
- MQTT communication

## Setup
1. Clone the repository.
2. Install backend dependencies: `pip install -r backend/requirements.txt`.
3. Install frontend dependencies: `cd frontend && npm install`.
4. Run the backend: `python backend/app.py`.
5. Run the frontend: `npm start`.

## Usage
- Access the dashboard at `http://localhost:3000`.
- Use the API endpoints for device management.