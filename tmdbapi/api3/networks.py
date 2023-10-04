"""API v3 networks category

The network id is available at: http://files.tmdb.org/p/exports/tv_network_ids_MM_DD_YYYY.json.gz
More information: https://developer.themoviedb.org/docs/daily-id-exports
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
        self.category_path = "/network"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def details(network_id: int) -> dict:
    networks = _Networks(_NETWORKS_V3)
    networks.reset()
    networks.use("network-details")
    networks.load_path_arg(network_id=network_id)
    return networks.request()


def alternative_names(network_id: int) -> dict:
    """Get the alternative names of a network."""
    networks = _Networks(_NETWORKS_V3)
    networks.reset()
    networks.use("details-copy")
    networks.load_path_arg(network_id=network_id)
    return networks.request()


def images(network_id: int) -> dict:
    """Get the TV network logos by id."""
    networks = _Networks(_NETWORKS_V3)
    networks.reset()
    networks.use("alternative-names-copy")
    networks.load_path_arg(network_id=network_id)
    return networks.request()
