import aiohttp
import asyncio
import re

from .helpers.misc import *
from .errors import *
from .models.character import *
# from .models.player import *
# from .models.team import *

class Smashtheque:

  # ---------------------------------------------------------------------------
  # CHARACTERS
  # ---------------------------------------------------------------------------

  @classmethod
  async def getCharacters(self):
    characters = await Character.getAll()
    return characters

  # # ---------------------------------------------------------------------------
  # # TEAM
  # # ---------------------------------------------------------------------------

  # async def findTeamByShortName(self, short_name):
  #   await self.setSession()
  #   request_url = "{0}?by_short_name_like={1}".format(self.apiUrl("teams"), short_name)
  #   async with self._session.get(request_url) as response:
  #     # API success
  #     if response.status == 200:
  #       teams = await response.json()
  #       if teams != []:
  #         # puts values in cache before responding
  #         for team in teams:
  #           self._teams_cache[str(team["id"])] = team
  #         # respond
  #         return True, teams[0]
  #       else:
  #         return True, None
  #     # API failure
  #     return False, {}

  # async def findTeamById(self, team_id):
  #   await self.setSession()
  #   request_url = "{api_url}/{team_id}".format(api_url=self.apiUrl("teams"), team_id=team_id)
  #   async with self._session.get(request_url) as response:
  #     # API success
  #     if response.status == 200:
  #       team = await response.json()
  #       return True, team
  #     # API failure
  #     return False, {}

  # async def updateTeam(self, team_id, data):
  #   await self.setSession()
  #   payload = {"team": data}
  #   request_url = "{0}/{1}".format(self.apiUrl("teams"), team_id)
  #   async with self._session.patch(request_url, json=payload) as response:
  #     # API success
  #     if response.status == 200:
  #       team = await response.json()
  #       return True, team
  #     # API failures
  #     if response.status == 422:
  #       result = await response.json()
  #       err = Map(result)
  #       return False, err.errors
  #     return False, {}

  # # ---------------------------------------------------------------------------
  # # TOURNAMENT
  # # ---------------------------------------------------------------------------

  # async def findTournamentById(self, tournament_id):
  #   await self.setSession()
  #   request_url = f"{self.apiUrl('recurring_tournaments')}/{tournament_id}"
  #   async with self._session.get(request_url) as response:
  #     # API success
  #     if response.status == 200:
  #       tournament = await response.json()
  #       return True, tournament
  #     # API failures
  #     return False, {}

  # async def createTournamentEvent(self, data):
  #   await self.setSession()
  #   payload = {"tournament_event": data}
  #   request_url = self.api_url("tournament_events")
  #   async with self._session.post(request_url, json=payload) as r:
  #     if r.status == 201:
  #       return True, 'created'
  #     if r.status == 200:
  #       return True, 'updated'
  #     if r.status == 422:
  #       result = await r.json()
  #       err = Map(result)
  #       return False, err.errors
  #     return False, {}

  # # ---------------------------------------------------------------------------
  # # LOCATION
  # # ---------------------------------------------------------------------------

  # async def findLocationByName(self, name):
  #   await self.setSession()
  #   request_url = "{0}?by_name_like={1}".format(self.apiUrl("locations"), name)
  #   async with self._session.get(request_url) as response:
  #     if response.status == 200:
  #       locations = await response.json()
  #       if locations != []:
  #         # puts values in cache before responding
  #         for location in locations:
  #           self._locations_cache[str(location["id"])] = location
  #         return True, locations[0]
  #       else:
  #         return True, None
  #     return False, {}

  # async def createLocation(self, name, country=False):
  #   await self.setSession()
  #   payload = {"name": name}
  #   if country:
  #     payload["type"] = "Locations::Country"
  #   async with self._session.post(self.apiUrl("locations"), json=payload) as r:
  #     if r.status == 201:
  #       # location creation went fine
  #       return True, {}
  #     if r.status == 422:
  #       result = await r.json()
  #       err = Map(result)
  #       return False, err.errors
  #     return False, {}

  # # ---------------------------------------------------------------------------
  # # PLAYER
  # # ---------------------------------------------------------------------------

  # async def findPlayerById(self, player_id):
  #   await self.setSession()
  #   request_url = "{0}/{1}".format(self.apiUrl("players"), player_id)
  #   async with self._session.get(request_url) as response:
  #     player = await response.json()
  #     return player

  # async def findPlayerByIds(self, player_ids):
  #   players = []
  #   for player_id in player_ids:
  #     player = await self.findPlayerById(player_id)
  #     players.append(player)
  #   return players

  # async def findPlayerByDiscordId(self, discord_id):
  #   await self.setSession()
  #   request_url = "{0}?by_discord_id={1}".format(self.apiUrl("players"), discord_id)
  #   async with self._session.get(request_url) as response:
  #     players = await response.json()
  #     if len(players) > 0:
  #       return players[0]
  #     return None

  # async def findPlayersByNameLike(self, name):
  #   await self.setSession()
  #   request_url = "{0}?by_name_like={1}".format(self.apiUrl("players"), name)
  #   async with self._session.get(request_url) as response:
  #     players = await response.json()
  #     return players

  # async def createPlayer(self, player):
  #   await self.setSession()
  #   payload = {"player": player}
  #   async with self._session.post(self.apiUrl("players"), json=payload) as r:
  #     if r.status == 201:
  #       return True, {}
  #     if r.status == 422:
  #       result = await r.json()
  #       err = Map(result)
  #       return False, err.errors
  #     return False, {}

  # async def updatePlayer(self, player_id, data):
  #   await self.setSession()
  #   payload = {"player": data}
  #   player_url = "{0}/{1}".format(self.apiUrl("players"), player_id)
  #   async with self._session.patch(player_url, json=payload) as r:
  #     if r.status == 200:
  #       result = await r.json()
  #       return True, result
  #     if r.status == 422:
  #       result = await r.json()
  #       err = Map(result)
  #       return False, err.errors
  #     return False, {}

  # # ---------------------------------------------------------------------------
  # # DISCORD USER
  # # ---------------------------------------------------------------------------

  # async def findDiscordUserByDiscordId(self, discord_id):
  #   await self.setSession()
  #   request_url = "{api_url}/{discord_id}".format(api_url=self.apiUrl("discord_users"), discord_id=discord_id)
  #   async with self._session.get(request_url) as response:
  #     player = await response.json()
  #     return player if player != [] else None

  # # ---------------------------------------------------------------------------
  # # GENERAL
  # # ---------------------------------------------------------------------------

  # async def initCache(self):
  #   await self.fetchCharactersIfNeeded()

  # def unload(self):
  #   if self._session is not None:
  #     asyncio.create_task(self._session.close())
