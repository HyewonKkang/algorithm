#include <iostream>
#include <vector>
#include <queue>
#define MAX 101

using namespace std;

int N, M;
char soldiers[MAX][MAX];
bool visited[MAX][MAX];
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

int bfs(int i, int j, char c, int N, int M) {
	queue<pair<int, int>> q;
	q.push({ i, j });
	visited[i][j] = 1;
	int cnt = 1;

	while (!q.empty()){
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx >= 0 && nx < M && ny >= 0 && ny < N){
				if (visited[nx][ny] == 0 && soldiers[nx][ny] == c) {
					visited[nx][ny] = 1;
					q.push({ nx, ny });
					cnt++;
				}
			}
		} 
	}
	return cnt;
}

int main() {
	int N, M;
	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		string tmp;
		cin >> tmp;
		for (int j = 0; j < N; j++) {
			soldiers[i][j] = tmp[j];
		}
	}

	int W = 0;
	int B = 0;
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j] == 0) {
				int value = bfs(i, j, soldiers[i][j], N , M);
				if (soldiers[i][j] == 'W') {
					W += value * value;
				}
					
				else {
					B += value * value;
				}
			}
		}
	}

	cout << W << ' ' << B;
}