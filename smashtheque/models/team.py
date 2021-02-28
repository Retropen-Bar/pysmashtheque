from .api_record import *

class Team(ApiRecord):

  api_path = "teams"
  singular_resource = "team"

  @classmethod
  async def byShortName(self, short_name):
    records = await self.getAll(query={'by_short_name_like': short_name})
    return records
