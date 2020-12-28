#include <iostream>
using namespace std;

int solution(string dartResult) {
	int answer = 0;
	int score[3];
	int cnt = -1;
	for (int i = 0; i < dartResult.size(); i++) {
		if (isdigit(dartResult[i])) {
			if (i > 0 && dartResult[i] == '0' ) {
				if (dartResult[i - 1]=='1') {
					score[cnt] = score[cnt] * 10;
				}
				else dartResult[i] - '0';
			}
			cnt++;
			int k = dartResult[i] - '0';
			score[cnt] = k;
		}
		else {
			if (isalpha(dartResult[i])) {
				if (dartResult[i] == 'S') {
				}
				else if (dartResult[i] == 'D') {
					score[cnt] = score[cnt] * score[cnt];
				}
				else if (dartResult[i] == 'T') {
					score[cnt] = score[cnt] * score[cnt] * score[cnt];
				}
			}
			else { //¹®ÀÚ
				if (dartResult[i] == '*') {
					if (cnt == 0) score[cnt] *= 2;
					else {
						score[cnt - 1] *= 2;
						score[cnt] *= 2;
					}
				}
				else if (dartResult[i] == '#') {
					score[cnt] = score[cnt] * (-1);
				}
			}
		}
	}
	for (int i = 0; i < 3; i++) {
		answer += score[i];
	}
	return answer;
}

int main() {
	cout << solution("1S*2T*3S") << endl;
}