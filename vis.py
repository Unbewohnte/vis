#!/usr/bin/env python3

'''

Copyright © 2021,2022 Kasyanov Nikolay Alexeevich (Unbewohnte (me@unbewohnte.xyz))

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''

import vk_api, os, random, datetime, argparse
from vk_api import VkUpload
from time import sleep


def has_image_extention(filename):
	filename = filename.lower()

	image_extentions = ["jpg","png","bmp","jpeg"]
	for image_extention in image_extentions:
		if image_extention in filename:
			return True

	return False

def sendImages(img_dir = ".", ID = 0, IS_GROUP_CHAT = False, TOKEN = ""):
	vk = vk_api.VkApi(token = TOKEN).get_api()

	files = os.listdir(img_dir)
	files.sort()

	counter = 1
	for filename in files:

		if has_image_extention(filename) == False:
			# file is probably not an image, so skipping
			continue

		# full path to the image
		path_to_image = img_dir + filename

		# upload via API
		upload = VkUpload(vk)
		upload_img = upload.photo_messages(photos = path_to_image)[0]

		# each message will contain "Counter : {number_of_}"
		MESSAGE = "▶ Counter  ┃{}┃ ◀".format(counter)
		# sending
		print("• {}: Sending {}...".format(counter,filename))

		if IS_GROUP_CHAT == False:
			try:
				vk.messages.send(user_id = ID ,message=MESSAGE,
							attachment = 'photo{}_{}'.format(upload_img['owner_id'],upload_img['id']),
							random_id = 0)
			except Exception as e:
				print(e)
				continue
		elif IS_GROUP_CHAT == True:
			try:
				vk.messages.send(chat_id = ID, message=MESSAGE,
								attachment='photo{}_{}'.format(upload_img['owner_id'],upload_img['id']),
								random_id = 0)
			except Exception as e:
				print(e)
				continue

		counter += 1

		# giving API a bit of rest
		sleep(random.uniform(3.0,4.0))
		pass


if __name__ == '__main__':
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument("imgs_dir_path", type=str, default=".")
	arg_parser.add_argument("id", type=int, default=0)
	arg_parser.add_argument("is_group_chat", type=bool, default=False)
	arg_parser.add_argument("token", type=str, default="")

	args = arg_parser.parse_args()


	sendImages(img_dir = args.imgs_dir_path, ID = args.id, IS_GROUP_CHAT = args.is_group_chat, TOKEN = args.token)
	pass