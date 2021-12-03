def get_fake_client():
    import requests
    import urllib3
    from google.api_core.client_options import ClientOptions
    from google.auth.credentials import AnonymousCredentials
    from google.cloud import storage
    my_http = requests.Session()
    my_http.verify = False # disable SSL validation
    urllib3.disable_warnings(
        urllib3.exceptions.InsecureRequestWarning
    ) # disable https warnings for https insecure certs

    client = storage.Client(
        credentials=AnonymousCredentials(),
        project="test",
        _http=my_http,
        client_options=ClientOptions(api_endpoint='https://fake-gcs-service:4443'),
    )
    return client