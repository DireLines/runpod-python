''' Allows endpoints to be imported as a module. '''

from runpod.endpoint.runner import Endpoint, Job
from runpod.endpoint.asyncio.asyncio_runner import Endpoint as AsyncioEndpoint
from runpod.endpoint.asyncio.asyncio_runner import Job as AsyncioJob
