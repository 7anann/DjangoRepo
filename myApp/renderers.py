from rest_framework.renderers import JSONRenderer


class MyProjectJSONRenderer(JSONRenderer):
    # This identifies the custom "flavor" of JSON for your project
    media_type = "application/vnd.myproject.v2+json"
    format = "vnd.myproject.v2+json"


from rest_framework import versioning


class MyProjectHeaderVersioning(versioning.AcceptHeaderVersioning):
    # This tells Django: "The version is part of the media type"
    # It will look for the 'v2' inside 'application/vnd.myproject.v2+json'
    pass
