api_keys = {
    'DEVZ_SECRET_KEY': 'onekeytwokeythreekeyfour',
    'GOOGLE_API_KEY': 'your-api-key'
}

def generate_env_file():
    with open ('.env', 'w') as env_file:
        for k, v in api_keys.items():
            env_file.write(f'{k}="{v}"\n')

if __name__ == '__main__':
    generate_env_file()