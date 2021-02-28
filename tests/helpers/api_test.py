import aiohttp
import pytest

from smashtheque.helpers.api import *

@pytest.mark.parametrize('test_baseUrl,test_bearerToken,expected_baseUrl,expected_bearerToken', [
  (None, None, "", ""),
  ("", "toto", "", "toto"),
  ("https://example.com", None, "https://example.com", ""),
  ("https://example.com", "", "https://example.com", ""),
  ("https://example.com", "toto", "https://example.com", "toto")
])
async def test_init(test_baseUrl, test_bearerToken, expected_baseUrl, expected_bearerToken):
  await Api.init(baseUrl=test_baseUrl, bearerToken=test_bearerToken)
  assert Api.baseUrl == expected_baseUrl
  assert Api.bearerToken == expected_bearerToken
  assert isinstance(Api.client, aiohttp.client.ClientSession)

@pytest.mark.parametrize('test_baseUrl,test_path,expected', [
  (None, "toto", "/api/v1/toto"),
  ("", "toto", "/api/v1/toto"),
  ("https://example.com", None, "https://example.com/api/v1/"),
  ("https://example.com", "", "https://example.com/api/v1/"),
  ("https://example.com", "toto", "https://example.com/api/v1/toto")
])
async def test_url(test_baseUrl, test_path, expected):
  await Api.init(baseUrl=test_baseUrl, bearerToken=None)
  assert Api.url(test_path) == expected
