#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Configuration file """

import json

# script parameters
max_err = 20
min_id = 1                          # first message
max_id = -1                         # no limit
sleeptime = 0.1                     # 0.1 seconds sleep between message downloads
output_folder = './conversations/'  # output folder
messages_dump_cnt = 100             # number of messages dumped to periodically write on disk

# classes for messages
text_class = 'tgme_widget_message_text'
photo_class = 'tgme_widget_message_photo_wrap'
video_class = 'tgme_widget_message_video_wrap'
voice_class = 'tgme_widget_message_voice'
link_class = 'tgme_widget_message_link_preview'
link_title_class = 'link_preview_site_name'
link_description_class = 'link_preview_description'
link_preview_class = 'link_preview_right_image'
author_class = 'tgme_widget_message_owner_name'
service_class = 'message_media_not_supported_label'
sticker_class = 'tgme_widget_message_sticker'
forward_class = 'tgme_widget_message_forwarded_from_name'

# message object
message_object = """
{
    "datetime": "",
    "name": "",
    "username": "",
    "quote": "",
    "deleted": "0",
    "msg": "",
    "photo": "",
    "video": "",
    "voice": "",
    "fwd_name": "",
    "fwd_username": "",
    "link": {
        "title": "",
        "description": "",
        "preview": ""
    }
}
"""
message_object = json.loads(message_object)
