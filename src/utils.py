import os


def get_environment_variable(name) -> str:
    try:
        return os.environ.get(name)
    except KeyError:
        message = f"No variable added {name}"
        raise Exception(message)
