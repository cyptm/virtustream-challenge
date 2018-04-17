#!/bin/bash

# Set home
FIB_SERVER_HOME=$PWD

# verify
echo "FIB_SERVER_HOME set to $FIB_SERVER_HOME"

echo "Setting up, enabling, and starting service"
SERVICE=fib_server.service
SERVICE_FILE=/etc/systemd/system/$SERVICE
cat $FIB_SERVER_HOME/deploy/fib_server.service > $SERVICE_FILE
ExecStart="ExecStart=$FIB_SERVER_HOME/virtustream_env/bin/python $FIB_SERVER_HOME/server.py"
echo  $ExecStart >> $SERVICE_FILE

systemctl daemon-reload
systemctl enable $SERVICE
systemctl start $SERVICE
