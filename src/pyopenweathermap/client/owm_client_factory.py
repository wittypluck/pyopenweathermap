import logging

from .free_client import OWMFreeClient
from .onecall_client import OWMOneCallClient
from .air_pollution_client import OWMAirPollutionClient


def create_owm_client(api_key, api_type, units="metric", lang='en'):
    logger = logging.getLogger(__name__)
    
    logger.info('Initializing OWMClient with api type: ' + str(api_type))
    if api_type == 'v3.0':
        return OWMOneCallClient(api_key, api_type, units, lang)
    if api_type == 'current' or api_type == 'forecast':
        return OWMFreeClient(api_key, api_type, units, lang)
    if api_type == 'air_pollution':
        return OWMAirPollutionClient(api_key)
    else:
        raise Exception('Unsupported API type ' + str(api_type))
