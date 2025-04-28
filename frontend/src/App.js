import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [devices, setDevices] = useState([]);

  useEffect(() => {
    axios.get('/devices').then(response => setDevices(response.data));
  }, []);

  return (
    <div>
      <h1>IoT Device Fleet Manager</h1>
      <ul>
        {devices.map(device => (
          <li key={device.device_id}>
            {device.device_id} - {device.firmware_version}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;