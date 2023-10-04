
## Getting Start

1. First set up your credential.

    The simplest way is give api_key, for api_key can have authorization access TMDB API version3. If access_token given the version3 and version4 both can access.

    ```python
    import tmdbapi
    cred = tmdbapi.Credential() # initialize credential management object
    cred.set(api_key="your_api_key") # set api_key
    
    # You can also give multiple information.
    cred.set(api_key="your_api_key",
             access_token="your_access_token",
             session_id="your_access_token",)
    ```

2. Load the credential

    ```python
    tmdbapi.setting.use_cred(cred)
    ```

3. Now you can use use the API

    ```python
    from tmdbapi import api3, pprint    # import api3, and pretty print
    response = api3.account.details()   # method method in version3 account category
    pprint(response) # print json format with ident
    ```

## Tutorial

### Credential Management

The credential management provide save and load file, and also can put the credential in system environment variable, and get them out.

- ### tmdbapi.Credential (or tmdbapi.creds.Credential)

    - #### set (method)

        Set API credentials. 
        
        * All information:
        
            * access_token
            * api_key
            * session_id
            * account_id
            * account_object_id

    - #### save (method)

        Save the credentials to file.
        

    This function stores the provided credentials in module global 
    variables. To persist the credentials in a file, use 
    `save_credentials()` after loading them.

    Parameters
    ----------
    access_token : str, optional
        The Bearer token. If provided, it will be used as the access 
        token in API version 3 (api3) by default. To change the API key
        , use `settings(use_access_token=False)`.
    api_key : str, optional
        The API key for TMDB API version 3. If an access_token is provided, 
        there is no need for an api_key. For more information, 
        see: https://developer.themoviedb.org/docs/authentication-application.
    session_id : str, optional
        An ID granting permission to access resources.
    account_id : int, optional
        The TMDB API version 3 account ID.
    account_object_id : str, optional
        The TMDB API version 4 account ID.

