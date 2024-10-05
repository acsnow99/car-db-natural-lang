
def compile_prompt(prompt_file_name = './prompts/simple.txt'):
    with open('./prompts/init.txt') as init_file:
        init_prompt = init_file.read()
    with open(prompt_file_name) as prompt_file:
        core_prompt = prompt_file.read()

    return init_prompt + '\n' + core_prompt
