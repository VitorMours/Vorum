#!/usr/bin/env bash 



# This script is used to run flask application 


PORT=5000
LOCALHOST=127.0.0.1


echo "==================== Launching Flask Application ===================="



echo "FLASK_APP application: $FLASK_APP"



if [[ $FLASK_APP -eq "" ]]; then
  export FLASK_APP="src/__init__.py"

  echo $FLASK_APP

fi


