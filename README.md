# vis - VkImageSender
## A tiny script to send images to a VK user or a group chat

# Usage

`./vis.py [ARGS]`

or

`python3 vis.py [ARGS]` 

## Arguments
1. img_dir (str) - path to the directory with images that you want to send
2. ID (int) - id of a person/group chat; the script will send images there
3. IS_GROUP_CHAT (bool) - self-explanatory, api has a little difference in handling group chats 
4. TOKEN (str) - your API token; (see: https://vk.com/dev/access_token)