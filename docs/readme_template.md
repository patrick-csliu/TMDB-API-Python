# Welcome to TMDB API Library

<a href="https://pypi.org/project/<package-name>"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/<package-name>"></a>

"TheMovieDB (TMDB) API Python Library: A comprehensive Python library for interacting with TheMovieDB API, enabling easy access to movie and TV show data, including details, ratings, and more. Simplify your movie-related projects with this powerful Python tool."

## Features

* Support TMDB API version 3 and 4 all available method. 
* Provide all fundamental parameters in TMDB api.
* Some method have parameter checking. ex: `True` > `true`
* Credential management. 

## Install

1. Install from PyPI
    ```shell
    pip install TMDB-Py
    ```

1. Download the latest release from {{insert_point.github_release}}
    ```shell
    pip install TMDB-Py-{{insert_point.version}}.tar.gz
    ```

## Getting Started

1. Set your credentials

    ```python
    from tmdbapi import credential
    credential.set_credential(api_key="your_api_key")
    ```
    ```python
    import tmdbapi
    tmdbapi.credential.set_credential(api_key="your_api_key")
    ```

2. You can simply access API version 3

    ```python
    from tmdbapi import api3
    api3.movies.details(155)
    ```

## Tutorial

