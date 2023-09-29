"""API v3 networks category

"""

from tmdbapi._core import Tmdb

# The names of keys in the dictionary might be incorrect,
# but the TMDB API documentation hasn't been corrected yet.
_NETWORKS_V3 = {
    "alternative-names-copy": {
        "method": "get",
        "params": [{"in": "path", "name": "network_id"}],
        "url": "/{network_id}/images",
    },
    "details-copy": {
        "method": "get",
        "params": [{"in": "path", "name": "network_id"}],
        "url": "/{network_id}/alternative_names",
    },
    "network-details": {
        "method": "get",
        "params": [{"in": "path", "name": "network_id"}],
        "url": "/{network_id}",
    },
}


class _Networks(Tmdb):

    def __init__(self, info_var):
        super().__init__()
        self.base_path = "/network"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url = url,
        )

_networks = _Networks(_NETWORKS_V3)


def details(network_id: int) -> dict:

    _networks.reset()
    _networks.use("network-details")
    _networks.load_path_arg(network_id=network_id)
    return _networks.request()


def alternative_names(network_id: int) -> dict:
    """Get the alternative names of a network.
    """
    _networks.reset()
    _networks.use("details-copy")
    _networks.load_path_arg(network_id=network_id)
    return _networks.request()


def images(network_id: int) -> dict:
    """Get the TV network logos by id.
    """
    _networks.reset()
    _networks.use("alternative-names-copy")
    _networks.load_path_arg(network_id=network_id)
    return _networks.request()
