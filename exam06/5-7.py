pos = [0] * 8          # 각 열에 배치한 퀸의 위치
flag_a = [False] * 8   # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * 15  # 대각선 방향(↙↗)으로 퀸을 배치했는지 체크
flag_c = [False] * 15  # 대각선 방향( ↘↖)으로 퀸을 배치했는지 체크

def put() -> None:
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    """i 열의 알맞은 위치에 퀸을 놓기"""
    for j in range(8):
        if(
            not flag_a[j]           # j 행에 아직 퀸을 놓지 않았으면
            and not flag_b[i + j]       # 대각선 방향(↙↗)으로 퀸이 배치 되지 않았다면
            and not flag_c[i - j + 7]
        ): # 대각선 방향( ↘↖)으로 퀸이 배치 되지 않았다면
            pos[i] = j          # 퀸을 j 행에 놓기
            if i == 7:          # 모든 열에 퀸을 배치하는 것을 완료
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)      # 다음 열에 퀸을 놓기
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

set(0)