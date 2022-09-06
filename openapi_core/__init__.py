"""OpenAPI core module"""
from openapi_core.spec import OpenAPIv30Spec
from openapi_core.validation.request.validators import RequestBodyValidator
from openapi_core.validation.request.validators import (
    RequestParametersValidator,
)
from openapi_core.validation.request.validators import RequestSecurityValidator
from openapi_core.validation.request.validators import RequestValidator
from openapi_core.validation.response.validators import ResponseDataValidator
from openapi_core.validation.response.validators import (
    ResponseHeadersValidator,
)
from openapi_core.validation.response.validators import ResponseValidator
from openapi_core.validation.shortcuts import validate_request
from openapi_core.validation.shortcuts import validate_response

__author__ = "Artur Maciag"
__email__ = "maciag.artur@gmail.com"
__version__ = "0.15.0a1"
__url__ = "https://github.com/p1c2u/openapi-core"
__license__ = "BSD 3-Clause License"

__all__ = [
    "OpenAPIv30Spec",
    "OpenAPIv3Spec",
    "OpenAPISpec",
    "validate_request",
    "validate_response",
    "RequestValidator",
    "ResponseValidator",
    "RequestBodyValidator",
    "RequestParametersValidator",
    "RequestSecurityValidator",
    "ResponseDataValidator",
    "ResponseHeadersValidator",
]

# aliases to the latest v3 version
OpenAPIv3Spec = OpenAPIv30Spec

# aliases to the latest version
OpenAPISpec = OpenAPIv3Spec
