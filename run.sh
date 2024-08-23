#!/usr/bin/env bash 



# This script is used to run flask application 
# by executing only one command, and wih no need to configure the system


# Global variables of the program
PORT=5000
LOCALHOST=127.0.0.1



Launching () {

  echo "==================== Launching Flask Application ===================="
  if [[ $FLASK_APP -eq "" ]]; then

    export FLASK_APP="src/__init__.py"
    echo "The aplication path established in FLASK_APP is: $FLASK_APP"
  fi

  flask run
}






Launching
