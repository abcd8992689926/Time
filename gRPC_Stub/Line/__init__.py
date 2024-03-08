import os
import sys

from Models.Config.MessageAPIConfig import MessageAPIConfig

sys.path.append('..\..\Libraries\python_common')

import file

test = file.json.load_config_as_model("test", MessageAPIConfig)
print(test)
