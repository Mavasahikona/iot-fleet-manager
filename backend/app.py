from flask import Flask, jsonify, request
from mqtt_handler import MQTTHandler
from models import Device
import config

app = Flask(__name__)

# Initialize MQTT handler
mqtt_handler = MQTTHandler(config.MQTT_BROKER, config.MQTT_PORT, config.MQTT_TOPIC)

@app.route('/devices', methods=['GET'])
def get_devices():
    devices = Device.query.all()
    return jsonify([device.to_dict() for device in devices])

@app.route('/devices', methods=['POST'])
def add_device():
    data = request.json
    device = Device(device_id=data['device_id'], firmware_version=data['firmware_version'])
    db.session.add(device)
    db.session.commit()
    return jsonify(device.to_dict()), 201

@app.route('/devices/<device_id>/update', methods=['POST'])
def update_firmware(device_id):
    firmware_file = request.files['firmware']
    mqtt_handler.publish_firmware_update(device_id, firmware_file.read())
    return jsonify({"status": "update initiated"}), 200

if __name__ == '__main__':
    app.run(debug=True)