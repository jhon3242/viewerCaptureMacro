import pyautogui
import keyboard
import time

# 저장할 파일 경로
FILE_PATH = "./images/"

# 저장할 파일 타입
file_type = '.pdf';

# 저장할 페이지 개수
page_count = 726

LEFT_POSITION = ();
RIGHT_POSITION = ();


def shooting() :
	move_count = get_move_count();
	for i in range(move_count) :
		image = pyautogui.screenshot()
		image.save(FILE_PATH + str(i) + file_type);
		keyboard.send("right")
		time.sleep(0.2)


def get_move_count() :
	if page_count % 2 == 1 :
		return int(page_count / 2) + 1;
	return int(page_count / 2);


while True:
	if keyboard.is_pressed('enter'):
		shooting()
		print("success")
		break;
		

