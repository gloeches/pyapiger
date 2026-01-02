#!/bin/sh
# entrypoint.sh

# Run the config generator
python config_generator.py

# Now, execute the command passed to this script (the Dockerfile's CMD)
exec "$@"
