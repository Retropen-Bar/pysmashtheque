import aiohttp
import asyncio
import re

class Smashtheque:

  def __init__(self, apiBaseUrl, bearerToken):
    self.apiBaseUrl = "" if apiBaseUrl is None else apiBaseUrl
    self.bearerToken = "" if bearerToken is None else apiBaseUrl
    self._characters_cache = {}
    self._characters_names_cache = {}
    self._locations_cache = {}
    self._teams_cache = {}

  def apiUrl(self, collection):
    path = "" if collection is None else collection
    return f"{self.apiBaseUrl}/api/v1/{path}"

  # ---------------------------------------------------------------------------
  # SESSION
  # ---------------------------------------------------------------------------

  async def session(self):
    if self._session is None:
      headers = {
        "Authorization": f"Bearer {self.bearerToken}",
        "Content-Type": "application/json",
      }
      self._session = await aiohttp.ClientSession(headers=headers)
    return self._session

  async def apiGet(self, path):
    session = await self.session()
    async with session.get(self.apiUrl(path)) as response:
      return response

  # ---------------------------------------------------------------------------
  # CHARACTERS
  # ---------------------------------------------------------------------------

  async def fetchCharacters(self):
    async with self.apiGet("characters") as response:
      # API success
      if response.status == 200:
        characters = await response.json()
        # puts values in cache before responding
        for character in characters:
          self._characters_cache[str(character["id"])] = character
          self._characters_names_cache[normalize_str(character["name"])] = character["id"]
        # respond
        return True, characters

      # API failure
      return False, []
