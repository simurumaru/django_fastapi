class EnvVariableMissingError(Exception):

    def __init__(self, variable_name: str):
        super().__init__(f"Environment variable '{variable_name}' is not set. Check your .env file.")
