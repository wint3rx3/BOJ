import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 박스 수
        int M = sc.nextInt(); // 색상 수
        int[][] arr = new int[N][M];

        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                arr[i][j] = sc.nextInt();

        int ans = N - 1; // 최악의 경우 N-1번 이동

        for (int joker = -1; joker < N; joker++) {
            boolean[] used = new boolean[M];
            int cnt = 0;

            for (int i = 0; i < N; i++) {
                if (i == joker) continue; // 조커 박스는 건너뜀

                int flag = 0;
                for (int j = 0; j < M; j++) {
                    if (arr[i][j] != 0) flag++;
                }

                if (flag == 0) continue; // 비어있으면 이동 X

                if (flag == 1) {
                    int color = -1;
                    for (int j = 0; j < M; j++) {
                        if (arr[i][j] != 0) {
                            color = j;
                            break;
                        }
                    }
                    if (used[color]) {
                        cnt++; // 이미 쓰인 색이면 이동 필요
                    } else {
                        used[color] = true;
                    }
                } else {
                    cnt++; // 두 색 이상이면 무조건 이동
                }
            }

            ans = Math.min(ans, cnt);
        }

        System.out.println(ans);
    }
}
