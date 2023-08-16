import WorkshopExplorer as WME

WME.API_KEY = "YOUR STEAM API KEY"

map_item = WME.WorkshopItem("https://steamcommunity.com/sharedfiles/filedetails/?id=2934902806")


print("File ID:", map_item.get_fileid())
print("Creator ID:", map_item.get_creator_id())
print("Creator URL:", map_item.get_creator_url())
print("Creator Name:", map_item.get_creator_name())
print("Creator Real Name:", map_item.get_creator_realname())
print("Creator Avatar URL:", map_item.get_creator_avatar())
print("Associated App ID:", map_item.get_appid())
print("File Size:", map_item.get_file_size())
print("File Name:", map_item.get_filename())
print("File URL:", map_item.get_file_url())
print("Preview URL:", map_item.get_preview_url())
print("Title:", map_item.get_title())
print("Description:", map_item.get_description())
print("Time Created:", map_item.get_time_created())
print("Time Updated:", map_item.get_time_updated())
print("Map Tags:", map_item.get_map_tags())
print(" Map Views:", map_item.get_map_views())
print("Map Followers:", map_item.get_map_followers())
print("Subscriptions:", map_item.get_subscriptions())

print("\nLoading the map...")
map_item.download_file("example_map/")


print("Search info_player_start id in the map...")
bsp_content = map_item.get_file_content()
content = bsp_content.decode("latin-1", errors="ignore").lower()

player_id = content.split('info_player_start"').pop().split("}")[0]
print(player_id.replace("\n", ""))