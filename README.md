# Welcome to TMDB API Library

[![PyPI - Version](https://img.shields.io/pypi/v/TMDB-Py)](https://pypi.org/project/TMDB-Py)
![GitHub license](https://img.shields.io/github/license/patrick-csliu/TMDB-API-Python)

TMDB API Python Library: A comprehensive Python library for interacting with TheMovieDB API, enabling easy access to movie and TV show data, including details, ratings, and more. Simplify your movie-related projects with this powerful Python tool.

* [TMDB API Getting Started](https://developer.themoviedb.org/docs)
* [Information about TMDB API](https://developer.themoviedb.org/openapi): Include meta data about the TMDB API and methods, request format.
* [Contribution Bible - TMDB](https://www.themoviedb.org/bible)

## Features

* Supports both TMDB API version 3 and 4, including all methods.
* Provide all parameters in TMDB API methods.
* Includes parameter checking for methods.
* Offers credential management.

## Installation

1. Install from PyPI
    ```shell
    pip install TMDB-Py
    ```

1. Download the latest release from [Release v1.1.1](https://github.com/patrick-csliu/TMDB-API-Python/releases/tag/v1.1.1)
    ```shell
    pip install TMDB-Py-1.1.1.tar.gz
    ```

## Getting Started

1. Set your credentials

    The simplest way is to provide an API key. An API key authorizes access to TMDB API version 3. If an access token is given, it allows access to both version 3 and version 4.

    ```python
    import tmdbapi

    cred = tmdbapi.Credential() # Initialize a credential management object
    cred.set(api_key="your_api_key") # Set the API key
    tmdbapi.setting.use_cred(cred) # Load the credential
    ```

2. Now, You can now access API version 3 easily:

    ```python
    from tmdbapi import api3, pprint
    
    response = api3.movies.details(155) # Send the request
    pprint(response) # Pretty print the response
    ```

3. To access both version 3 and 4, you need to set access_token.

    ```python
    cred.set(access_token="your_access_token",
             account_object_id="your_account_object_id")
    response = tmdbapi.api4.account.favorite_movies() # Get a list of your favorite movies.
    pprint(response)
    ```
    > [!NOTE]  
    > In version 3, accessing account catalog methods generally requires both the `account_id` and `session_id`, with the exception of `api3.account.details`, which does not need the `account_id`. In version 4, you require the `account_object_id`

## Contributing

Thank you for considering contributing to the TMDB API Library! Your contributions are highly valued and can help make this project even more powerful.

### Ways to Contribute

#### 1. Reporting Issues

If you discover any bugs, issues, or have suggestions for improvements, please open an issue. When reporting issues, be sure to provide detailed information about the problem, including steps to reproduce it.

#### 2. Adding Tests

Robust test coverage is crucial for maintaining a stable project. You can contribute by adding more test cases to ensure that the code behaves correctly in various scenarios. We use pytest for testing.

#### 3. Implementing High-Level Functions

If you have ideas for high-level functions that can improve the library's usability or provide new features, feel free to implement them and create a pull request.

#### 4. Adding Features and Enhancements

Contributions that introduce new features or enhance existing ones are always welcome.

## Tutorial

* ### Credential Management

    The credential management provides methods to save and load credentials from files and manage credentials in system environment variables.
    * #### Set the credential

        ```python
        import tmdbapi

        cred = tmdbapi.Credential() # Initialize credential management object

        # You can also provide multiple pieces of information at once
        cred.set(api_key="your_api_key",
                access_token="your_access_token",
                session_id="your_access_token",)
        ```
        >  All available information:  
        > *access_token*,
        > *api_key*,
        > *session_id*,
        > *account_id*,
        > *account_object_id*

        > [!Note]  
        > To obtain your `account_id`, use the `api3.account.details` method (requires `session_id`; if the `access_token` is provided, the `session_id` can be optional). If neither `session_id` nor `access_token` is provided, when needed, it will automatically start the generation process. Alternatively, you can generate it using `tmdbapi.integration.auth.create_session_id()`.
        > 
        > To acquire your `account_object_id`, you need to generate a "write" `access_token`. This process will return both the `account_object_id` and the "write" `access_token`.
        
        > [!Note]  
        > The original `access_token` provided by the TMDB API only allows reading. If you need to perform operations such as managing lists, you must generate a "write" `access_token` using `tmdbapi.integration.auth.create_session_id()`. Remember to keep it.

    * #### Save credentials to a file:

        ```python
        # Choose one option:
        cred.save("path/to/file") # For unencrypted storage
        cred.save_encrypt("path/to/file") # For encrypted storage
        ```

    * #### With this file, next time you can load credentials from this file:

        ```python
        cred = tmdbapi.Credential() # Create a new credential object
        cred.load("path/to/file") # Load the credential file (unencrypted)
        cred.load_encrypt("path/to/file") # Load the encrypted credential file
        ```

    * #### In some case you would like to put and get this credential information on environment variable:

        ```python
        cred.cred.cred_to_env() # put on environment variables
        cred.load_env_var() # load from environment variables
        ```

* ### Settings

    * #### Load the credential:

        After setting up the credential object, TMDB API still needs to be aware of your credentials. You must add them to the settings:
        ```python
        tmdbapi.setting.use_cred(cred) # Inform TMDB API that you are using these credentials
        ```

    * #### Choose what you want to use for authorization when sending a request:

        > [!NOTE]  
        > The API key is used only for version 3 of the API. An access token can be used for both versions. When using an API key, some methods in version 3 require a session ID.
        ```python
        # If access token was given you can set use_access_token to True
        tmdbapi.setting.use_access_token(True)
        ```
        > [!NOTE]  
        > When you provide the access token in the credential object, it will set the `use_access_token` to True by default when you load the credential in the settings using `setting.use_cred()`

    * #### Set the request timeout:

        ```python
        tmdbapi.setting.timeout(5) # Set a timeout to 5 seconds
        ```

    * #### Set the default language:

        When you request method have language parameter and no language given, it will use the default language to the parameter.
        ```python
        tmdbapi.setting.language('en-US') # Set the default language to 'en-US'
        ```

    * #### Set the default region (works similarly to default language):

        ```python
        tmdbapi.setting.region('US') # Set the default region to 'US'
        ```

    * #### Choose whether to use cookies or not:

        More information: [requests.Session](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects)
        ```python
        tmdbapi.setting.use_session(True) # Use requests.Session()
        tmdbapi.setting.use_session(False) # Send requests without cookies
        ```

    * #### Enable or disable the logging:

        ```python
        tmdbapi.setting.log('directory/to/save/the/log') # Enable the log file output
        tmdbapi.setting.log(None) # Disable the log file output (Default)
        ```
        To change the log level:
        ```
        import logging
        tmdbapi.LOGGER.setLevel(logging.INFO) # Change the log level to INFO
        ```
        > [!WARNING]  
        > Keep your logs safe and do not share them with others.
        > Due to the TMDB API's practice of including the API key and session ID in the URL, these details may be logged.
        Further when you change the logger level to `DEBUG`, it will also recode send headers, where the access token is.

* ### API Library

    * #### tmdbapi.api3

        TMDB API version 3 methods and endpoints. Import the `api3` sub-package to access the modules. Each module contains a category of methods, and each function in the module is an API method, with categories matching those of the TMDB API.
        ```python
        from tmdbapi import api3
        api3.catalog_name.method_name()
        ```

    * #### tmdbapi.api4

        TMDB API version 4 methods and endpoints, structured and used in the same way as `api3`.
        ```python
        from tmdbapi import api4
        api4.catalog_name.method_name()
        ```

    * #### tmdbapi.integration

        This section provides high-level functions and integration features to simplify interactions with TMDB.
        ```python
        # Example
        from tmdbapi.integration import auth
        auth.create_access_token()
        ```

## Known Issues

### Issue: Error when Using `api3.lists.delete`

When using the `api3.lists.delete` request to delete a list on TheMovieDB, you may encounter the following error response:

```
response 500 - Internal Server Error
response json:
{
    "success": false,
    "status_code": 11,
    "status_message": "Internal error: Something went wrong, contact TMDb."
}
```
The error is at TMDB API, please use api4 instead, or you may need to catch the exception.
[Issue on TMDB support](https://www.themoviedb.org/talk/6302b1c7fb5299007a7676ff)

## Unit Test

Run unit test:
```shell
python run_test.py
```
