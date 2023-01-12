#!/bin/bash

# Get the value of the TARGET and EXECUTION_ID environment variable
cidr="$TARGET"
name="$EXECUTION_ID"

# Create the config file
echo '{
    "name": "'"$name"'",
    "cidr": "'"$cidr"'",
    "port_list": "full_ports"
}' > /tmp/config.json
