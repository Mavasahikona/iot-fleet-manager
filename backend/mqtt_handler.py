import paho.mqtt.client as mqtt

class MQTTHandler:
    def __init__(self, broker, port, topic):
        self.client = mqtt.Client()
        self.client.connect(broker, port)
        self.topic = topic

    def publish_firmware_update(self, device_id, firmware_data):
        self.client.publish(f"{self.topic}/{device_id}/update", firmware_data)