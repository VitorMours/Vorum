#!/usr/bin/env bash 



# This script is used to run flask application 
# by executing only one command, and wih no need to configure the system


# Global variables of the program



InstallingRequirements () {
  echo "==================== Installing Requirements ===================="
  
  # Ensure that we have a virtual environment folder
  python -m venv venv
  
  # Activate virtual environment (Cross-platform fix)
  if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows (Git Bash, Cygwin, etc.)
    source venv/Scripts/activate
  else
    # Linux/MacOS
    source venv/bin/activate
  fi

  # Install the requirements
  pip install -r requirements.txt
}


Launching () {
  echo "==================== Launching Flask Application ===================="

  # Check if FLASK_APP is set, and set it if not
  if [[ -z "$FLASK_APP" ]]; then
    export FLASK_APP="src/__init__.py"
    echo "The application path established in FLASK_APP is: $FLASK_APP"
  fi

  # Run the Flask app
  flask run
}



InstallingRequirements
Launching
