const { spawn } = require('child_process');

// Function to call YOLOv8 Python script
const runYolov8Detection = (imagePath) => {
  return new Promise((resolve, reject) => {
    // Replace 'python3' with 'python' if that's how you access Python
    const pythonProcess = spawn('python3', ['yolov8_detect.py', imagePath]);

    pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
      resolve(data.toString());
    });

    pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
      reject(data.toString());
    });

    pythonProcess.on('close', (code) => {
      console.log(`child process exited with code ${code}`);
    });
  });
};

// Example usage
runYolov8Detection('path/to/your/image.jpg')
  .then(output => console.log(output))
  .catch(error => console.error(error));
