"""API v3 tv episode groups category

"""

from tmdbapi._core import Tmdb

_TV_EPISODE_GROUPS_V3 = {
    "tv-episode-group-details": {
        "method": "get",
        "params": [{"in": "path", "name": "tv_episode_group_id"}],
        "url": "/{tv_episode_group_id}",
    }
}


class _Group(Tmdb):
    def __init__(self, info_var):
        super().__init__()
        self.category_path = "/tv/episode_group"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def details(tv_episode_group_id: str) -> dict:
    """Get the details of a TV episode group."""
    group = _Group(_TV_EPISODE_GROUPS_V3)
    group.reset()
    group.use("tv-episode-group-details")
    group.load_path_arg(tv_episode_group_id=tv_episode_group_id)
    return group.request()
