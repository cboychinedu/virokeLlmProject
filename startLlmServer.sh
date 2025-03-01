#!/bin/bash

# Define the python variables
PYTHON_SCRIPT="./PythonLLmServer/app.py" 
LOG_FILE="llm_server.log"
PID_FILE="llm_server.pid"
PYTHON_EXEC="python" 

# Define the Node.js variables
NODE_SCRIPT="./NodejsServer/app.js"
NODE_APP_NAME="nodejs-server"

# Function to start the Python server
start_server() {
    if [ -f "$PID_FILE" ]; then
        echo "LLM Model Server is already running. PID: $(cat $PID_FILE)"
        exit 1
    fi

    echo "Starting LLM Model Server..."
    nohup $PYTHON_EXEC $PYTHON_SCRIPT > $LOG_FILE 2>&1 & echo $! > $PID_FILE
    echo "Server started with PID: $(cat $PID_FILE)"
}

# Function to stop the Python server
stop_server() {
    if [ ! -f "$PID_FILE" ]; then
        echo "No running LLM Model Server found."
        exit 1
    fi

    PID=$(cat $PID_FILE)
    echo "Stopping LLM Model Server (PID: $PID)..."
    kill $PID && rm -f $PID_FILE
    echo "Server stopped successfully."
}

# Function to check Python server status
status_server() {
    if [ -f "$PID_FILE" ]; then
        echo "LLM Model Server is running. PID: $(cat $PID_FILE)"
    else
        echo "LLM Model Server is not running."
    fi
}

# Function to start the Node.js server using PM2
start_node() {
    echo "Starting Node.js server with PM2..."
    pm2 start $NODE_SCRIPT --name $NODE_APP_NAME
    echo "Node.js server started."
}

# Function to stop the Node.js server using PM2
stop_node() {
    echo "Stopping Node.js server with PM2..."
    pm2 stop $NODE_APP_NAME && pm2 delete $NODE_APP_NAME
    echo "Node.js server stopped."
}

# Function to check Node.js server status
status_node() {
    pm2 status $NODE_APP_NAME
}

# Main control logic
case "$1" in
    start)
        start_server
        start_node
        ;;
    stop)
        stop_server
        stop_node
        ;;
    restart)
        stop_server
        stop_node
        sleep 2
        start_server
        start_node
        ;;
    status)
        status_server
        status_node
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
        ;;
esac
