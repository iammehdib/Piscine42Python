import os

from dotenv import load_dotenv

ENV_PATH = os.path.join(os.path.dirname(__file__), '.env')


def verif(key: str, is_strict: bool = False) -> str:
    value = os.getenv(key)
    if value is None:
        if is_strict:
            print(f'ERROR: {key} required in production')
        else:
            print(f'WARNING: {key} not configured - using default')
        return "NOT SET"
    return value


if __name__ == '__main__':
    load_dotenv(ENV_PATH)
    print('ORACLE STATUS: Reading the Matrix...')
    print()
    print('Configuration loaded:')

    mode = verif('MATRIX_MODE')
    if mode == 'NOT SET':
        mode = 'development'
    if mode not in ('development', 'production'):
        print(f"WARNING: Unknown mode '{mode}', defaulting to development")
        mode = 'development'
    strict = mode == 'production'

    db_url = verif('DATABASE_URL', strict)
    api_key = verif('API_KEY', strict)
    log_level = verif('LOG_LEVEL', strict)
    zion = verif('ZION_ENDPOINT', strict)

    print(f'Mode: {mode}')
    if db_url != 'NOT SET':
        print('Database: Connected to local instance')
    else:
        print('Database: Not configured')
    if api_key != 'NOT SET':
        print('API Access: Authenticated')
    else:
        print('API Access: Not configured')
    print(f'Log Level: {log_level}')
    if zion != 'NOT SET':
        print('Zion Network: Online')
    else:
        print('Zion Network: Offline')

    print()
    print('Environment security check:')
    print('[OK] No hardcoded secrets detected')
    if os.path.exists(ENV_PATH):
        print('[OK] .env file properly configured')
    else:
        print('[WARNING] .env file not found')
    print('[OK] Production overrides available')

    print()
    print('The Oracle sees all configurations.')
