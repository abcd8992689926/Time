import json


class Json:
    def load_config_as_model(config_file_name: str, model_name):
        with open(config_file_name, 'r') as file:
            content = json.load(file)
            return model_name(**content)
