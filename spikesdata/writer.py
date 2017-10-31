import os

from spikesdata.utils import ConfigFileNotFound


def write_config(content, file_name):
    """
    Write configurations to the given file name.

    Parameters
    ----------
    file_name: str
        File name to be written.
    content: object
        ConfigParser object
    """
    sml_conf_file = os.path.expanduser('~' + os.sep + file_name)

    if os.path.isfile(sml_conf_file):
        with open(sml_conf_file, 'w') as config_file:
            content.write(config_file)
    else:
        raise ConfigFileNotFound("Make sure Config file is available at " + sml_conf_file)
