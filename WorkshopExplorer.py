import os
import requests
import datetime
from typing import List, Union

API_KEY = None

class WorkshopItem:
    def __init__(self, map_link: str) -> None:
        """ 
            Initialize WorkshopItem object with the given map_link
            Extract the id from map_link and store it as an attribute
        """

        if API_KEY is None:
            raise ValueError("WorkshopItem: You didn't specify the Steam Api Key!")
        
        self.map_link = map_link
        self.id = map_link.split("id=").pop().split("&")[0]
        
        # Fetch workshop file info for the given id using the Steam API key from .env
        self.data = self._workshop_file_info(self.id, API_KEY)

        # Initialize attributes to None
        self.time_created: Union[None, datetime.datetime] = None
        self.time_updated: Union[None, datetime.datetime] = None
        self.file_content: Union[None, bytes] = None
        self.author_data: Union[None, dict] = None
        

    def get_fileid(self) -> int:
        """Returns the file ID as an integer."""
        return int(self.id)


    def get_creator_id(self) -> int:
        """Returns the creator's ID as an integer."""
        return int(self.data["creator"])
    

    def get_creator_url(self) -> str:
        """Returns the URL of the creator's Steam profile."""
        return f"https://steamcommunity.com/profiles/{self.get_creator_id()}"
    

    def get_creator_name(self) -> str:
        """Returns the creator's name."""
        if self.author_data is None:
            url = self.get_creator_url()
            self.author_data = self._workshop_author_info(url, API_KEY)
        return self.author_data["personaname"]
    

    def get_creator_realname(self) -> Union[str, None]:
        """Returns the creator's real name if available, otherwise returns None."""
        if self.author_data is None:
            url = self.get_creator_url()
            self.author_data = self._workshop_author_info(url, API_KEY)
        return self.author_data.get("realname", None)
    

    def get_creator_avatar(self) -> Union[str, None]:
        """Returns the URL of the creator's avatar image if available, otherwise returns None."""
        if self.author_data is None:
            url = self.get_creator_url()
            self.author_data = self._workshop_author_info(url, API_KEY)
        return self.author_data.get("avatarfull", None)


    def get_appid(self) -> int:
        """Returns the Steam App ID associated with the workshop file as an integer"""
        return int(self.data["creator_appid"])


    def get_file_size(self) -> int:
        """Returns the file size in bytes as an integer."""
        return int(self.data["file_size"])


    def get_filename(self) -> str:
        """Returns the filename of the workshop file."""
        return self.data["filename"].split("/").pop()


    def get_file_url(self) -> Union[str, None]:
        """Returns the URL to download the workshop file, or None if the file URL is not available."""
        return self.data.get("file_url", None)


    def get_file_content(self) -> Union[bytes, None]:
        """
            Returns the content of the workshop file as bytes, downloading it if necessary.
            Returns None if the file url is not available.
        """
        if self.file_content is None:
            url = self.get_file_url()
            if url is None:
                return None
            
            response = requests.get(url)
        
            if response.status_code == 200:
                self.file_content = response.content
            else:
                print("File upload error. Status code:", response.status_code)
                return None
        return self.file_content


    def download_file(self, path: str) -> bool:
        """
            Downloads the workshop file to the specified path.
            Returns True if the file was successfully downloaded, False otherwise.
        """
        map_content = self.get_file_content()
        map_name = self.get_filename()

        if map_content is None:
            return False

        if not os.path.exists(path):
            os.makedirs(path)

        with open(f"{path}{map_name}", "wb") as file:
            file.write(map_content)

        return True


    def get_preview_url(self) -> Union[str, None]:
        """Returns the URL of the workshop file's preview image, or None if the preview URL is not available."""
        return self.data.get("preview_url", None)


    def get_title(self) -> str:
        """Returns the title of the workshop file."""
        return self.data["title"]


    def get_description(self) -> Union[str, None]:
        """
            Returns the description of the workshop file.
            Returns None if the description is empty or not available.
        """
        description = self.data["file_description"]
        if description == "":
            return None
        return description


    def get_time_created(self) -> datetime.datetime:
        """Returns the datetime the workshop file was created."""
        if self.time_created is None:
            timestamp = self.data["time_created"]
            self.time_created = datetime.datetime.fromtimestamp(timestamp)
        return self.time_created


    def get_time_updated(self) -> datetime.datetime:
        """Returns the datetime the workshop file was last updated."""
        if self.time_updated is None:
            timestamp = self.data["time_updated"]
            self.time_updated = datetime.datetime.fromtimestamp(timestamp)
        return self.time_updated


    def get_map_tags(self) -> List[str]:
        """Returns a list of tags associated with the workshop file."""
        tags = []
        for item in self.data.get("tags", []):
            tags.append(item['tag'])
        return tags
    

    def get_map_views(self) -> int:
        """Returns the number of views of the workshop file."""
        return self.data["views"]
    

    def get_map_followers(self) -> int:
        """Returns the number of followers of the workshop file."""
        return self.data["followers"]
    

    def get_subscriptions(self) -> int:
        """Returns the number of subscriptions to the workshop file."""
        return self.data["subscriptions"]
    


    def _workshop_file_info(self, file_id: str, api_key: str) -> dict:
        """
            Fetches workshop file information using the provided file_id and API key.
            Returns the workshop file details as a dictionary.
        """
        url = f"https://api.steampowered.com/IPublishedFileService/GetDetails/v1/?publishedfileids[0]={file_id}&key={api_key}"
        
        data = self._internet_request(url)
        if len(data) == 0:
            raise ValueError("WorkshopItem: Error receiving data. Check that the API key are correct.")
        
        data = data["response"]["publishedfiledetails"][0]

        if data["result"] != 1:
            raise ValueError("WorkshopItem: Error receiving data. Check that the file_id are correct.")
        
        # Return the workshop file details
        return data
    

    def _workshop_author_info(self, user_id: int, api_key: str) -> dict:
        """
            Fetches the author's information using the provided user_id and API key.
            Returns the author's details as a dictionary.
        """
        url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={api_key}&steamids={user_id}"
        data = self._internet_request(url)
        if len(data) == 0:
            return {}
        
        
        # Return the user file details
        return data["response"]["players"][0]
    

    @staticmethod
    def _internet_request(url:str) -> dict:
        """
            Sends an HTTP GET request to the specified URL and returns the response as a dictionary.
            If the request fails or the response is not valid JSON, an empty dictionary is returned.
        """
        response = requests.get(url)
        if response.status_code != 200:
            return {}
        
        data = response.json()
        return data