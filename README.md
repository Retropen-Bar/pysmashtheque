# Smashtheque API wrapper

## Installing

**Python 3.5.3 or higher is required**

To install the library, you can just run the following command:

# Linux/macOS
python3 -m pip install -U smashtheque

# Windows
py -3 -m pip install -U smashtheque

## Using

For instance:
```
smashtheque = Smashtheque(apiBaseUrl="https://www.smashtheque.fr", bearerToken="MYTOKEN")
result, data = await smashtheque.fetchCharacters()
if result:
  print("Unable to fetch characters")
else:
  print(f"Fetched {len(data)} characters")
```
