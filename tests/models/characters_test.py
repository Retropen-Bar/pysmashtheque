from   aiohttp import web
import json
import pytest
from   unittest.mock import Mock

from smashtheque.errors import *
from smashtheque.helpers.api import *
from smashtheque.models.character import *


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

async def respondWithCharacters(request):
  return web.Response(body=json.dumps(characters), content_type="application/json")
mockCharacters = Mock(side_effect=respondWithCharacters)

async def mock500(request):
  return web.Response(status=500)

# ---------------------------------------------------------------------------
# TESTS
# ---------------------------------------------------------------------------

async def test_getAll_success(aiohttp_client):
  await Api.init(baseUrl=None, bearerToken=None)
  # replace aiohttp ClientSession with a mock
  app = web.Application()
  app.router.add_get('/api/v1/characters', mockCharacters)
  mock = await aiohttp_client(app)
  Api.setClient(mock)
  # test
  characters = await Character.getAll()
  assert len(characters) == 2
  assert isinstance(characters[0], Character)
  assert characters[0].name == "Yoshi"

async def test_getAll_failure(aiohttp_client):
  await Api.init(baseUrl=None, bearerToken=None)
  # replace aiohttp ClientSession with a mock
  app = web.Application()
  app.router.add_get('/api/v1/characters', mock500)
  mock = await aiohttp_client(app)
  Api.setClient(mock)
  # test
  with pytest.raises(ApiError):
    await Character.getAll()
