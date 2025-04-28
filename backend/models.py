from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True)
    device_id = Column(String, unique=True)
    firmware_version = Column(String)

    def to_dict(self):
        return {"device_id": self.device_id, "firmware_version": self.firmware_version}