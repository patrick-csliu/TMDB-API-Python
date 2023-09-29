"""API v3 companies category

"""

from tmdbapi._core import Tmdb


_COMPANIES_V3 = {
    "company-alternative-names": {
        "method": "get",
        "params": [{"in": "path", "name": "company_id"}],
        "url": "/alternative_names",
    },
    "company-details": {
        "method": "get",
        "params": [{"in": "path", "name": "company_id"}],
        "url": "",
    },
    "company-images": {
        "method": "get",
        "params": [{"in": "path", "name": "company_id"}],
        "url": "/images",
    },
}


class _Companies(Tmdb):

    def __init__(self, info_var):
        super().__init__()
        self.base_path = "/company/{company_id}"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url = url,
        )

_companies = _Companies(_COMPANIES_V3)


def alternative_names(company_id: int) -> dict:

    _companies.reset()
    _companies.use("company-alternative-names")
    _companies.load_path_arg(company_id=company_id)
    return _companies.request()


def details(company_id: int) -> dict:
    """Get the company details by ID.
    """
    _companies.reset()
    _companies.use("company-details")
    _companies.load_path_arg(company_id=company_id)
    return _companies.request()


def images(company_id: int) -> dict:
    """Get the company logos by id.
    """
    _companies.reset()
    _companies.use("company-images")
    _companies.load_path_arg(company_id=company_id)
    return _companies.request()
