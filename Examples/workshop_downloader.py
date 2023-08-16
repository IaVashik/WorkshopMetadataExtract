import WorkshopMetadataExtract as WME
WME.set_api_key("your api key")


def download(path, url):
    map_item = WME.WorkshopItem(url)
    print(f"Downloading the \"{map_item.get_title()}\" map....")
    map_item.download_file(path)

links = [
    "https://steamcommunity.com/sharedfiles/filedetails/?id=2718933105",
    "https://steamcommunity.com/sharedfiles/filedetails/?id=2972861651",
    "https://steamcommunity.com/sharedfiles/filedetails/?id=2980848615",
    # WORKSHOP LINKS
]

path = "test/"

for url in links:
    download(path, url)