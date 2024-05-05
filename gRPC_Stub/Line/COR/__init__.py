import json
import os

information_centre_config = {
    "host": os.environ.get('INFORMATION_CENTRE_HOST'),
    "port": int(os.environ.get('INFORMATION_CENTRE_PORT'))
}
