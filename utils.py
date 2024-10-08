import json

def compile_prompt(prompt_init_file_name = './prompts/init.txt', prompt_file_name = './prompts/simple.txt'):
    if (prompt_file_name != ''):
        with open(prompt_init_file_name) as init_file:
            init_prompt = init_file.read()
        with open(prompt_file_name) as prompt_file:
            core_prompt = prompt_file.read()

        return init_prompt + '\n' + core_prompt
    else:
        with open(prompt_init_file_name) as init_file:
            return init_file.read()


def get_api_key(config_file):
    try:
        with open(config_file, 'r') as file:
            config = json.load(file) 

        api_key = config.get('apiKey')

        if api_key is not None:
            return api_key
        else:
            raise KeyError("apiKey not found in the configuration file.")

    except FileNotFoundError:
        print(f"Error: The file '{config_file}' was not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the configuration file.")
    except Exception as e:
        print(f"An error occurred: {e}")
