"""
11728 배열 합치기
"""

A, B = map(int, input().split())
array = []
array.extend(list(map(int, input().split())))
array.extend(list(map(int, input().split())))
array.sort()
print(*array, sep=' ')


# https://www.acmicpc.net/source/35744672
"""
    int n = ReadInt(), m = ReadInt(), v[n];
    for (int i = 0; i < n; i++) v[i] = ReadInt();
    for (int i = 0, j = 0; ; j++) {
        if (j == m) { while (i < n) WriteInt(v[i++]); break; }
        const int val = ReadInt();
        while (i < n && v[i] <= val) WriteInt(v[i++]);
        WriteInt(val);
    }
    write(1, w, q - w);
"""

# https://www.acmicpc.net/source/29596243
"""
int main ()
{
    n = getint(), m = getint();
    int a[n], b[m], i, j;
    for (i = 0; i < n; i++)
        a[i] = getint();
    for (j = 0; j < m; j++)
        b[j] = getint();

    for (i = j = 0; i < n && j < m; )
        if (a[i] < b[j]) {
            putint(a[i++]);
            putch(' ');
        } else {
            putint(b[j++]);
            putch(' ');
        }
"""
