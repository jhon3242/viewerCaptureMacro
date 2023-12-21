# ebook 자동 캡쳐 프로그램
![Alt text](<Dec-21-2023 15-43-04.gif>)


## 서론
ebook으로 책을 구매한 이후 굿노트에서 필기하면서 보고 싶었다.

pdf 로 구하고 싶었으나 pdf 파일을 구하려면 직접 캡처하는 것 말고는 딱히 방법이 없었다.

그래도 몇 백 페이지나 되는 책을 일일이 캡처하는 것은 여간 귀찮은 일이 아니다.

그래서 알아서 캡쳐해주는 프로그램을 만들게 되었다.

**물론, 책을 캡쳐하여 영리를 취하는 행위는 불법이다.**  
그러나 개인적인 목적으로 감상, 복습, 학습의 목적으로 파일 저장하여 출력하는 경우에는 저작권을 침해하는 경우가 아니라고 본다.  
따라서 행여나 해당 프로그램을 활용해서 영리 목적으로 판매 및 공유를 하는 일은 안 하는 게 좋다.

## 구현 과정

구현 과정은 매우 간단했지만 파이썬을 안한지 오래되었고 가상환경 설정 단계에서 애를 먹어서 조금 어려웠다.  
다만 코드는 매우 매우 간단하기 때문에 개발자라면 파이썬을 몰라도 충분히 이해 가능할 것이다.

## 전제사항

해당 프로그램을 사용하는데 전제되는 사항들은 다음과 같다.

1.  MAC(M1) 환경에서 동작한다. (윈도우에서도 동작할 수도 있지만 잘 모르겠다.)
2.  뷰어 프로그램을 전체화면으로 하여 캡쳐한다. (한 번의 캡처로 왼쪽페이지, 오른쪽페이지 둘 다 캡처한다.)
3.  뷰어 프로그램에서 "오른쪽" 방향키를 누르면 다음페이지로 넘어간다.

다음 위 3가지를 전제하여 돌아가도록 프로그램을 구현했다.  
(나는 맥북 M1을 사용했고, 뷰어 프로그램은 알라딘 ebook을 활용했다.)

## 사용 방법

사용 방법은 매우 간단하다.

### 1\. 깃을 클론 한다.

[https://github.com/jhon3242/viewerCaptureMacro](https://github.com/jhon3242/viewerCaptureMacro)

 [GitHub - jhon3242/viewerCaptureMacro: ebook 뷰어를 통해 책을 캡쳐하는 매크로 프로그램이다.

ebook 뷰어를 통해 책을 캡쳐하는 매크로 프로그램이다. Contribute to jhon3242/viewerCaptureMacro development by creating an account on GitHub.

github.com](https://github.com/jhon3242/viewerCaptureMacro)

해당 링크를 통해 레포지토리를 깃 클론하거나 다운로드 받는다.

### 2\. requirements.txt 에 있는 모듈들을 다운로드한다.

가상환경에서 다운로드할 것을 추천하지만 로컬에서 해도 큰 상관은 없다.

```
pip install -r requirements.txt
```

### 3\. main.py 에서 페이지 개수 등을 설정한다.

[##_Image|kage@c9tRMx/btsCq9r8XYz/Y4igQsS52l5IVpfVlHBS80/img.png|CDM|1.3|{"originWidth":1410,"originHeight":390,"style":"alignCenter"}_##]

저장할 경로, 저장할 파일 타입, 저장할 페이지 개수를 설정한다.

(저장할 페이지 개수만 설정해 줘도 된다.)

### 4\. 뷰어 프로그램을 킨다.

[##_Image|kage@bdTLp6/btsCl1CpHnO/UY7Z1URplRP2DWeUoYF45k/img.png|CDM|1.3|{"originWidth":3360,"originHeight":2100,"style":"alignCenter"}_##]

전체화면으로 뷰어 프로그램을 켜고 맨 처음 페이지로 이동시켜 둔다.  
(오른쪽 방향키 클릭 시 다음페이지로 넘어가는 것을 확인한다.)

### 5\. 캡처 프로그램을 실행한다.

```
sudo python main.py    
```

sudo를 통해 프로그램을 실행하지 않으면 에러가 발생한다.

### 6\. 뷰어 프로그램으로 돌아가 엔터키를 누른다.

그리고 뷰어 프로그램으로 돌아온 다음에 엔터키를 누른다.

그러면 자동으로 다음페이지로 이동하면서 캡처가 된다.

캡처된 파일은 파일 경로를 따로 수정하지 않았으면 images 폴더 안에 생성되어 있을 것이다.

![Alt text](<Dec-21-2023 15-43-04.gif>)
뷰어 페이지 이동 후 엔터키만 한 번 눌러주면 캡처 프로그램이 진행된다.

