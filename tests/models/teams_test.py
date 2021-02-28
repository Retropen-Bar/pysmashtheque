from   aiohttp import web
import json
import pytest
from   unittest.mock import Mock

from smashtheque.errors import *
from smashtheque.helpers.api import *
from smashtheque.models.team import *


# FAKE SERVER

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

async def respondWithTeams(request):
  return web.Response(body=json.dumps(teams), content_type="application/json")
mockTeams = Mock(side_effect=respondWithTeams)

async def respondWithTeam(request):
  return web.Response(body=json.dumps(rb), content_type="application/json")
mockTeam = Mock(side_effect=respondWithTeam)

async def mock500(request):
  return web.Response(status=500)

# ---------------------------------------------------------------------------
# TESTS
# ---------------------------------------------------------------------------

async def test_getAll_success(aiohttp_client):
  await Api.init(baseUrl=None, bearerToken=None)
  # replace aiohttp ClientSession with a mock
  app = web.Application()
  app.router.add_get('/api/v1/teams', mockTeams)
  mock = await aiohttp_client(app)
  Api.setClient(mock)
  # test
  teams = await Team.getAll()
  assert len(teams) == 2
  assert isinstance(teams[0], Team)
  assert teams[0].name == "Rétropen-Bar"

async def test_getAll_failure(aiohttp_client):
  await Api.init(baseUrl=None, bearerToken=None)
  # replace aiohttp ClientSession with a mock
  app = web.Application()
  app.router.add_get('/api/v1/teams', mock500)
  mock = await aiohttp_client(app)
  Api.setClient(mock)
  # test
  with pytest.raises(ApiError):
    await Team.getAll()

async def test_byShortName_success(aiohttp_client):
  await Api.init(baseUrl=None, bearerToken=None)
  # replace aiohttp ClientSession with a mock
  app = web.Application()
  app.router.add_get('/api/v1/teams', mockTeams)
  mock = await aiohttp_client(app)
  Api.setClient(mock)
  # test
  initCallCount = mockTeams.call_count
  teams = await Team.byShortName('toto')
  assert mockTeams.call_count == initCallCount + 1
  assert len(teams) == 2
  assert isinstance(teams[0], Team)
  assert teams[0].name == "Rétropen-Bar"

async def test_find_success(aiohttp_client):
  await Api.init(baseUrl=None, bearerToken=None)
  # replace aiohttp ClientSession with a mock
  app = web.Application()
  app.router.add_get('/api/v1/teams/7', mockTeam)
  mock = await aiohttp_client(app)
  Api.setClient(mock)
  # test
  initCallCount = mockTeam.call_count
  team = await Team.find(7)
  assert mockTeam.call_count == initCallCount + 1
  assert isinstance(team, Team)
  assert team.short_name == "R-B"

async def test_update_success(aiohttp_client):
  await Api.init(baseUrl=None, bearerToken=None)
  # replace aiohttp ClientSession with a mock
  app = web.Application()
  app.router.add_patch('/api/v1/teams/7', mockTeam)
  mock = await aiohttp_client(app)
  Api.setClient(mock)
  # test
  initCallCount = mockTeam.call_count
  team = await Team.updateAttributes(7, {'name': 'fake'})
  assert mockTeam.call_count == initCallCount + 1
  assert isinstance(team, Team)
  assert team.short_name == "R-B"
