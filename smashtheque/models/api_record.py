from collections import UserDict
from collections.abc import Mapping

from ..helpers.api import Api

class ApiRecord(UserDict):

  def __getattr__(self, attr):
    return self.data[attr]

  @classmethod
  async def getAll(self, query=None):
    items = await Api.get(self.api_path, query=query)
    records = []
    for item in items:
      record = self(item)
      records.append(record)
    return records

  @classmethod
  async def find(self, id):
    item = await Api.get(f"{self.api_path}/{id}")
    return self(item)

  @classmethod
  async def updateAttributes(self, id, data):
    payload = {}
    payload[self.singular_resource] = data
    item = await Api.patch(f"{self.api_path}/{id}", payload)
    return self(item)
