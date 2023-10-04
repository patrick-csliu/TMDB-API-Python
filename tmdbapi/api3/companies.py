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
        self.category_path = "/company/{company_id}"
        self.info_var = info_var

    def request(self) -> dict:
        url = self.build_url(3)
        return self.request_raw(
            url=url,
        )


def alternative_names(company_id: int) -> dict:
    companies = _Companies(_COMPANIES_V3)
    companies.reset()
    companies.use("company-alternative-names")
    companies.load_path_arg(company_id=company_id)
    return companies.request()


def details(company_id: int) -> dict:
    """Get the company details by ID."""
    companies = _Companies(_COMPANIES_V3)
    companies.reset()
    companies.use("company-details")
    companies.load_path_arg(company_id=company_id)
    return companies.request()


def images(company_id: int) -> dict:
    """Get the company logos by id."""
    companies = _Companies(_COMPANIES_V3)
    companies.reset()
    companies.use("company-images")
    companies.load_path_arg(company_id=company_id)
    return companies.request()
