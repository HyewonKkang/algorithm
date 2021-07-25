#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX 26

using namespace std;
int N;
int x, y, nx, ny;
char apart[MAX][MAX];
bool visited[MAX][MAX] = { 0, };
vector<int> result;
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

int bfs(int i, int j) {
	queue<pair<int, int>> q;
	q.push({ i, j });
	visited[i][j] = 1;
	int cnt = 1;

	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
				if (visited[nx][ny] == 0 && apart[nx][ny] == '1') {
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
	cin >> N;
	for (int i = 0; i < N; i++) {
		string tmp;
		cin >> tmp;
		for (int j = 0; j < N; j++) {
			apart[i][j] = tmp[j];
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j] == 0 && apart[i][j] == '1') {
				int val = bfs(i, j);
				result.push_back(val);
			}
		}
	}
	cout << result.size() << endl;
	sort(result.begin(), result.end());
	for (int i = 0; i < result.size(); i++) {
		cout << result[i] << endl;
	}
}