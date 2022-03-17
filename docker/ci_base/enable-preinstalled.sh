#!/bin/bash
# Read in the file of environment settings
. /preinstalled/setup.bash
# Then run the CMD
exec "$@"
