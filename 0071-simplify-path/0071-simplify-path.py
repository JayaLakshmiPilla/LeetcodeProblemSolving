class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')
        
        for part in parts:
            if part == '' or part == '.':
                continue  # Ignore empty parts or current directory symbol
            elif part == '..':
                if stack:
                    stack.pop()  # Move one directory up
            else:
                stack.append(part)  # Valid directory/file name
        
        return '/' + '/'.join(stack)
