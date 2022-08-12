
print("DIMARnick telegram @Dilmurad_uz ")

from telethon.sync import TelegramClient
from telethon import functions, types
import time

try:
	file = open("@Dilmurad_uz.txt", 'r')
	pause = input('DIMARnick nikni 100 marotoba qilgandan sòng 36 sekund dam olish boladi.\n\nNIK ÒZGARTIRISH VAQTI - ')
	all_names = list()
	for line in file.readlines():
		all_names.extend(line.rstrip().split(' '))

	while True:
		for name in all_names:
			with TelegramClient('session', '10112075', '2b27e750b33f34f33b5063152cb9f42b') as client:
				client(functions.account.UpdateProfileRequest(first_name=str(name)))
			print('ISM OZGARTIRLDI ' + name)
			time.sleep(int(pause))
except Exception as e:
	print('XATOLIK -', e)
	wait = input('TAKROR QILISH UCHUN ENTER TUGMASINI BOSING:')
