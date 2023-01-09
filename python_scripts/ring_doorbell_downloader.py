# obtain ring doorbell camera object
# replace the camera.front_door by your camera entity
ring_cam = hass.states.get("camera.front_door")

subdir_name = f"ring_{ring_cam.attributes.get('friendly_name')}"

# get video URL
data = {
    "url": ring_cam.attributes.get("video_url"),
    "subdir": subdir_name,
    "filename": ring_cam.attributes.get("friendly_name"),
}

# call downloader integration to save the video
hass.services.call("downloader", "download_file", data)