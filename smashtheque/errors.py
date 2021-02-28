class Error(Exception):
  """Base class for exceptions in this module."""
  pass

class DetailedError(Error):
  """Exception raised for errors with a message.

  Attributes:
    message -- error description
  """

  def __init__(self, message):
    self.message = message

class ApiError(Error):
  """Exception raised for errors in a GET request.

  Attributes:
    response -- response object
  """

  def __init__(self, response):
    self.response = response

class NotFoundError(Error):
  """Exception raised for 404 errors in a request.

  Attributes:
    response -- response object
  """

  def __init__(self, response):
    self.response = response

class UnprocessableEntityError(Error):
  """Exception raised for 422 errors in a POST request.

  Attributes:
    response -- response object
    errors -- Map object containing errors
  """

  def __init__(self, response, errors):
    self.response = response
    self.errors = errors

  @classmethod
  async def create(self, response):
    body = await response.json()
    errors = body['errors']
    return UnprocessableEntityError(response, errors)
