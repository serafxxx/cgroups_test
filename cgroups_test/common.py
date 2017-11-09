from rest_framework import status
from rest_framework.exceptions import APIException


class CgroupsError(APIException):
    """
    Exception class to use in API on any cgroups command fail
    """
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'Cgroups command failed.'
    default_code = 'cgroups_failed'