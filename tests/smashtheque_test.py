from   aiohttp import web
import json
import pytest
from   unittest.mock import Mock

from smashtheque.smashtheque import Smashtheque
from smashtheque.errors import *
from smashtheque.models.character import *
from smashtheque.models.player import *
from smashtheque.models.team import *


# FAKE SERVER

yoshi = {
  "id": 13,
  "name": "Yoshi",
  "emoji": "1234"
}
bowser = {
  "id": 42,
  "name": "Bowser",
  "emoji": "5678"
}
characters = [yoshi, bowser]

rb = {
  "id": 7,
  "short_name": "R-B",
  "name": "Rétropen-Bar"
}
cew = {
  "id": 9,
  "short_name": "CEW",
  "name": "Caramel Ecchi Waysen"
}
teams = [rb, cew]

hsh = {
  "id": 1337,
  "name": "Happy Smash Hour"
}
tournaments = [hsh]

dijon = {
  "id": 21,
  "name": "Dijon"
}
paris = {
  "id": 75,
  "name": "Paris"
}
locations = [dijon, paris]

async def respondWithCharacters(request):
  return web.Response(body=json.dumps(characters), content_type="application/json")
mockCharacters = Mock(side_effect=respondWithCharacters)

async def respondWithTeams(request):
  return web.Response(body=json.dumps(teams), content_type="application/json")
mockTeams = Mock(side_effect=respondWithTeams)

async def respondWithTeam(request):
  return web.Response(body=json.dumps(rb), content_type="application/json")
mockTeam = Mock(side_effect=respondWithTeam)

async def respondWithTournament(request):
  return web.Response(body=json.dumps(hsh), content_type="application/json")
mockTournament = Mock(side_effect=respondWithTournament)

async def respondWithLocations(request):
  return web.Response(body=json.dumps(locations), content_type="application/json")
mockLocations = Mock(side_effect=respondWithLocations)

async def mock500(request):
  return web.Response(status=500)

# TESTS


# # ---------------------------------------------------------------------------
# # TEAM
# # ---------------------------------------------------------------------------



# # -----------------------------------------------------------------------------
# # TOURNAMENT
# # -----------------------------------------------------------------------------

# async def test_findTournamentById(aiohttp_client):
#   apiClient = Smashtheque(apiBaseUrl=None, bearerToken=None)
#   # replace aiohttp ClientSession with a mock
#   app = web.Application()
#   app.router.add_get('/api/v1/recurring_tournaments/1337', mockTournament)
#   apiClient._session = await aiohttp_client(app)
#   # test
#   initCallCount = mockTournament.call_count
#   result, details = await apiClient.findTournamentById(1337)
#   assert mockTournament.call_count == initCallCount + 1
#   assert result
#   assert details["name"] == "Happy Smash Hour"


# #   async def createTournamentEvent(self, data):
# #     payload = {"tournament_event": data}
# #     request_url = self.api_url("tournament_events")
# #     async with self._session.post(request_url, json=payload) as r:
# #       if r.status == 201:
# #         return True, 'created'
# #       if r.status == 200:
# #         return True, 'updated'
# #       if r.status == 422:
# #         result = await r.json()
# #         err = Map(result)
# #         return False, err.errors
# #       return False, {}

# # -----------------------------------------------------------------------------
# # LOCATION
# # -----------------------------------------------------------------------------

# async def test_findLocationByName(aiohttp_client):
#   apiClient = Smashtheque(apiBaseUrl=None, bearerToken=None)
#   # replace aiohttp ClientSession with a mock
#   app = web.Application()
#   app.router.add_get('/api/v1/locations', mockLocations)
#   apiClient._session = await aiohttp_client(app)
#   # test
#   initCallCount = mockLocations.call_count
#   result, details = await apiClient.findLocationByName("dijon")
#   assert mockLocations.call_count == initCallCount + 1
#   assert len(apiClient._locations_cache) == 2
#   assert apiClient._locations_cache["21"]["name"] == "Dijon"
#   assert result
#   assert details["name"] == "Dijon"

# #   async def findLocationByName(self, name):
# #     request_url = "{0}?by_name_like={1}".format(self.apiUrl("locations"), name)
# #     async with self._session.get(request_url) as response:
# #       locations = await response.json()
# #       if locations != []:
# #         # puts values in cache before responding
# #         for location in locations:
# #           self._locations_cache[str(location["id"])] = location
# #         return locations[0]
# #       else:
# #         return None

# #   async def createLocation(self, name, country=False):
# #     payload = {"name": name}
# #     if country:
# #       payload["type"] = "Locations::Country"
# #     async with self._session.post(self.apiUrl("locations"), json=payload) as r:
# #       if r.status == 201:
# #         # location creation went fine
# #         return True, {}
# #       if r.status == 422:
# #         result = await r.json()
# #         err = Map(result)
# #         return False, err.errors
# #       return False, {}

# #   # ---------------------------------------------------------------------------
# #   # PLAYER
# #   # ---------------------------------------------------------------------------

# #   async def findPlayerById(self, player_id):
# #     request_url = "{0}/{1}".format(self.apiUrl("players"), player_id)
# #     async with self._session.get(request_url) as response:
# #       player = await response.json()
# #       return player

# #   async def findPlayerByIds(self, player_ids):
# #     players = []
# #     for player_id in player_ids:
# #       player = await self.findPlayerById(player_id)
# #       players.append(player)
# #     return players

# #   async def findPlayerByDiscordId(self, discord_id):
# #     request_url = "{0}?by_discord_id={1}".format(self.apiUrl("players"), discord_id)
# #     async with self._session.get(request_url) as response:
# #       players = await response.json()
# #       if len(players) > 0:
# #         return players[0]
# #       return None

# #   async def findPlayersByNameLike(self, name):
# #     request_url = "{0}?by_name_like={1}".format(self.apiUrl("players"), name)
# #     async with self._session.get(request_url) as response:
# #       players = await response.json()
# #       return players

# #   async def createPlayer(self, player):
# #     payload = {"player": player}
# #     async with self._session.post(self.apiUrl("players"), json=payload) as r:
# #       if r.status == 201:
# #         return True, {}
# #       if r.status == 422:
# #         result = await r.json()
# #         err = Map(result)
# #         return False, err.errors
# #       return False, {}

# #   async def updatePlayer(self, player_id, data):
# #     payload = {"player": data}
# #     player_url = "{0}/{1}".format(self.apiUrl("players"), player_id)
# #     async with self._session.patch(player_url, json=payload) as r:
# #       if r.status == 200:
# #         result = await r.json()
# #         return True, result
# #       if r.status == 422:
# #         result = await r.json()
# #         err = Map(result)
# #         return False, err.errors
# #       return False, {}

# #   # ---------------------------------------------------------------------------
# #   # DISCORD USER
# #   # ---------------------------------------------------------------------------

# #   async def findDiscordUserByDiscordId(self, discord_id):
# #     request_url = "{api_url}/{discord_id}".format(api_url=self.apiUrl("discord_users"), discord_id=discord_id)
# #     async with self._session.get(request_url) as response:
# #       player = await response.json()
# #       return player if player != [] else None

# #   # ---------------------------------------------------------------------------
# #   # GENERAL
# #   # ---------------------------------------------------------------------------

# #   async def initCache(self):
# #     await self.fetchCharactersIfNeeded()

# #   def unload(self):
# #     asyncio.create_task(self._session.close())
