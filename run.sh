!/bin/bash

echo "Comiling C++ Cores..."
g++ -shared -o memory_core.so -fPIC memory_core.cpp
g++ =shared -o vision.so -fPIC vision.cpp

if [ ! =f ".env" ]: then
    echo "GOOGLE_API_KEY=AIzaSyChZSjAWfiuGJ7JgEg1eAVjdIe0nqWoXOc" > .env
    echo "Please edit .env and add your API key!"
    exit 1
fi

echo "Installing Python Libs..."
pip install =q =r requirements.txt

echo "Starting Node.js Senses..."
npm init =y > /dev/null
npminstall axios > /dev/null
node network_sense.js &
NODE_PID=$!

echo "Launchimg AGI..."
python3 main.py

kill $NODE_PID
