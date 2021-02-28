import aiohttp
import asyncio
import re
import urllib.parse

# from .helpers.misc import *
from ..errors import *

class Api:

  baseUrl = None
  bearerToken = None
  client = None

  @classmethod
  async def init(self, baseUrl, bearerToken):
    self.baseUrl = "" if baseUrl is None else baseUrl
    self.bearerToken = "" if bearerToken is None else bearerToken
    headers = {
      "Authorization": f"Bearer {self.bearerToken}",
      "Content-Type": "application/json",
    }
    async with aiohttp.ClientSession(headers=headers) as client:
      self.client = client

  @classmethod
  def getClient(self):
    if self.client is None:
      raise DetailedError("Smashtheque not initialized")
    return self.client

  @classmethod
  def setClient(self, client):
    self.client = client

  @classmethod
  def url(self, _path):
    path = "" if _path is None else _path
    return f"{self.baseUrl}/api/v1/{path}"

  # ---------------------------------------------------------------------------
  # HELPERS
  # ---------------------------------------------------------------------------

  @classmethod
  async def get(self, path, query=None):
    url = self.url(path)
    if query is not None:
      url = url + "?" + urllib.parse.urlencode(query)
    async with self.getClient().get(url) as response:
      # success
      if response.status == 200:
        data = await response.json()
        return data

      # 404
      if response.status == 404:
        error = await NotFoundError.create(response)
        raise error

      # any other error
      raise ApiError(response)

  @classmethod
  async def post(self, path, body):
    async with self.getClient().post(self.url(path), json=body) as response:
      # success
      if response.status == 200 or response.status == 201:
        data = await response.json()
        return data

      # 422
      if response.status == 422:
        error = await UnprocessableEntityError.create(response)
        raise error

      # any other error
      raise ApiError(response)

  @classmethod
  async def patch(self, path, body):
    async with self.getClient().patch(self.url(path), json=body) as response:
      # success
      if response.status == 200:
        data = await response.json()
        return data

      # 422
      if response.status == 422:
        error = await UnprocessableEntityError.create(response)
        raise error

      # any other error
      raise ApiError(response)
