class Solution:

    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0

        paths = [[s[0]]]
        for i in range(1, len(s)):
            flag = int(s[i - 1]) == 1 or int(s[i - 1]) == 2 and int(s[i]) <= 6
            tmp_paths = []
            for path in paths:
                if s[i] != '0':
                    tmp_paths.append(path + [s[i]])
                if len(path[-1]) == 1 and flag:
                    tmp_paths.append(path[:-1] + [path[-1] + s[i]])

            paths = tmp_paths

        return len(paths)


res = Solution().numDecodings('120')
print(res)
