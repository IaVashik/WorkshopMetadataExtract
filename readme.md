<div align="center">
<img src="https://i.ibb.co/hYvQdk9/logo-back.png" alt="Logo" >

<h2 align="center">
    Discover. Download. Dominate! :D
</h2>
</div>

## Description:
Workshop Metadata Extract (WME) is a Python library that allows you to extract metadata from Steam Workshop files. It provides a convenient way to retrieve various details about workshop files such as the creator's information, file size, creation and update times, and more.


## Installation
Install the current version with PyPI:
```
pip install WorkshopMetadataExtract
```


## Usage
To use WME, follow these steps:

1. Import the WorkshopMetadataExtract module and set your Steam API key:

```python
import WorkshopMetadataExtract as WME

WME.API_KEY = "YOUR STEAM API KEY"
```

2. Create a WorkshopItem object with the workshop file URL:

```python
map_item = WME.WorkshopItem("WORKSHOP_FILE_URL")
```

3. Retrieve and work with the workshop file metadata. For example, to download the map:

```python
map_item.download_file("path_to_save/")
```

If you're not sure how to use it, check out the examples provided in the `Examples` folder.

## Functions and Descriptions
- `WorkshopItem.get_fileid()`: Returns the file ID as an integer.
- `WorkshopItem.get_creator_id()`: Returns the creator's ID as an integer.
- `WorkshopItem.get_creator_url()`: Returns the URL of the creator's Steam profile.
- `WorkshopItem.get_creator_name()`: Returns the creator's name.
- `WorkshopItem.get_creator_realname()`: Returns the creator's real name if available, otherwise returns None.
- `WorkshopItem.get_creator_avatar()`: Returns the URL of the creator's avatar image if available, otherwise returns None.
- `WorkshopItem.get_appid()`: Returns the Steam App ID associated with the workshop file as an integer.
- `WorkshopItem.get_file_size()`: Returns the file size in bytes as an integer.
- `WorkshopItem.get_filename()`: Returns the filename of the workshop file.
- `WorkshopItem.get_file_url()`: Returns the URL to download the workshop file, or None if the file URL is not available.
- `WorkshopItem.get_file_content()`: Returns the content of the workshop file as bytes, downloading it if necessary, or None if the file URL is not available.
- `WorkshopItem.download_file(path)`: Downloads the workshop file to the specified path and returns True if successful, False otherwise.
> **Note**
> The path must end with a folder and a symbol "/": WorkshopItem.download_file("example/")
- `WorkshopItem.get_preview_url()`: Returns the URL of the workshop file's preview image, or None if the preview URL is not available.
- `WorkshopItem.get_title()`: Returns the title of the workshop file.
- `WorkshopItem.get_description()`: Returns the description of the workshop file, or None if not available.
- `WorkshopItem.get_time_created()`: Returns the datetime the workshop file was created.
- `WorkshopItem.get_time_updated()`: Returns the datetime the workshop file was last updated.
- `WorkshopItem.get_map_tags()`: Returns a list of tags associated with the workshop file.
- `WorkshopItem.get_map_views()`: Returns the number of views of the workshop file.
- `WorkshopItem.get_map_followers()`: Returns the number of followers of the workshop file.
- `WorkshopItem.get_subscriptions()`: Returns the number of subscriptions to the workshop file.

## Steam API Key Information
In order to use this library, you need to provide your own Steam API key. To obtain an API key, visit the [Steam API Key registration page](https://steamcommunity.com/dev/apikey). Please note that due to Valve's policies, a Steam API key is mandatory. Additionally, if you want to download content from the workshop, you must have a copy of the game associated with the workshop file on your account :<

## License
WME is licensed under the [MIT License](https://github.com/example/project/blob/main/LICENSE). You are free to use, modify and share this library under the terms of the MIT License. The only condition is keeping the copyright notice, and stating whether or not the code was modified.