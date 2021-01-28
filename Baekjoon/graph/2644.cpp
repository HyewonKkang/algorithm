#include <iostream>
#include <queue>
#define MAX 101

using namespace std;

vector<int> adj[MAX];

int bfs(int start, int end) {
	int distance[MAX] = { 0 };
	queue<int> q;

	q.push(start);

	while (!q.empty()) {
		int n = q.front();
		q.pop();

		if (n == end)
			return distance[end];

		for (int i = 0; i < adj[n].size(); i++) {
			int val = adj[n][i];
			if (!distance[val]) {
				q.push(val);
				distance[val] = distance[n] + 1;
			}
		}
	}
	return -1;
}

int main() {
	int n, start, end, m;

	cin >> n;
	cin >> start >> end;
	cin >> m;

	for(int i=0; i<m; i++){
		int p, c;
		cin >> p >> c;
		adj[p].push_back(c);
		adj[c].push_back(p);
	}
	cout << bfs(start, end);

	return 0;
}