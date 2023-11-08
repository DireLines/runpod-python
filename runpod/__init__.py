""" Allows runpod to be imported as a module. """

import os
import logging

from runpod import serverless
from runpod.serverless.modules.rp_logger import RunPodLogger
from runpod.endpoint import Endpoint
from runpod.endpoint import AsyncioEndpoint, AsyncioJob
from runpod.version import __version__
from runpod.api.ctl_commands import (
    get_user, update_user_settings,
    get_gpu, get_gpus,
    get_pod, get_pods, create_pod, stop_pod, resume_pod, terminate_pod,
    create_template,
    create_endpoint
)
from runpod.cli.groups.config.functions import set_credentials, check_credentials, get_credentials


# ------------------------------- Config Paths ------------------------------- #
SSH_KEY_PATH = os.path.expanduser('~/.runpod/ssh')


profile = "default"  # pylint: disable=invalid-name

_credentials = get_credentials(profile)
if _credentials is not None:
    api_key = _credentials['api_key']  # pylint: disable=invalid-name
else:
    api_key = None  # pylint: disable=invalid-name

api_url_base = "https://api.runpod.io"  # pylint: disable=invalid-name

endpoint_url_base = "https://api.runpod.ai/v2"  # pylint: disable=invalid-name


# --------------------------- Force Logging Levels --------------------------- #
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("uvicorn").setLevel(logging.WARNING)
