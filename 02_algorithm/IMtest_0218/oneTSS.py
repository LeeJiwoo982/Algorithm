import socket

WIDTH = 254
HEIGHT = 127
RADIUS = 5.73 / 2   #공의 반지름

HOLES = [[0,0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
NUMBER_OF_BALLS = 6
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

# 흰공, 공, 공, 공, 공, 검은공
# 가까운 목적공을 찾는다
balls[0] #흰공
balls[5] #검은공
balls[0] = [63, 63]
balls[0][0] #흰공의 x좌표
balls[0][1] #흰공의 y좌표

balls[5] = [191, 63]

#if 내가 선이면:
#   1, 3번 처리 후 8번 마지막 처리
#   if 1번 공 있다면:
#각도계산 탄젠트: 아크탄젠트-(델타와이/델타엑스)-둘다 부호가 같으면 양수-아크탄젠트2는 360고려해서 계산산
#else: #내가 후

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '파이썬플레이어'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))  #서버연결
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))    #서버에 데이터 전송
print('Ready to play!\n--------------------')
#응답: 공의 위치 좌표 파싱
# 해석 후 코드 작성
# 작성 코드 응답 전송
sock.close()
print('Connection Closed.\n--------------------')