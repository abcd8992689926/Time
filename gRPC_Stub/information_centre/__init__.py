import os
import sys

sys.path.append(r'..\..\Libraries\python_common')
sys.path.append(r'..\..\gRPC_Server')

from log.models.config import LogConfig

logConfig = LogConfig(
    host=os.environ.get('LOG_HOST'),
    port=int(os.environ.get('LOG_PORT'))
)
connection_string = os.environ.get('CONNECTION_STRING')
