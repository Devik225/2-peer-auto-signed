const { spawn } = require('child_process');
const path = require('path');

// Construct the absolute path to the Python executable
const pythonExecutable = 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python39\\python.exe';

// const childPython = spawn(pythonExecutable, ['--version']);
// const childPython = spawn(pythonExecutable, ['rtds.py']);
const childPython = spawn(pythonExecutable, ['rtds.py', 'RTDS2']);


childPython.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
});

childPython.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
});

childPython.on('close', (code) => {
    console.log(`child process exited with code: ${code}`);
});