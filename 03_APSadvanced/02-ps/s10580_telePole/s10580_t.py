import sys
sys.stdin = open('input.txt', 'r')

'''
---문제 읽기-----
전봇대 두 개
N개의 전선(N >= 3)
끝점이 같은 경우 X, 교차는 O
몇 개의 교차점이 있는지 구하라
2초/15case => 400만번 연산
--------설계----------
!! 교차점이 언제 발생하는가
기존선-새선
: 새로운 선을 추가/저장할 때마다 비교 진행하기
시작: 기존<새
끝: 기존>새
or
시작: 기존<새
끝: 기존>새

- 자료구조
    - 기존 선으로 저장 할 리스트
- 알고리즘
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    wires = []
    cross_cnt = 0
    for _ in range(N):
        A, B = map(int, input().split())
