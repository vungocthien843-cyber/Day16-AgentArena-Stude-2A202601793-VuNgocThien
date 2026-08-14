import os

f1 = 'tests/test_no_instructor_leak.py'
with open(f1, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('str(relative)', 'relative.as_posix()')
text = text.replace('str(p.relative_to(REPO_ROOT))', 'p.relative_to(REPO_ROOT).as_posix()')
text = text.replace('str(path.relative_to(REPO_ROOT))', 'path.relative_to(REPO_ROOT).as_posix()')
with open(f1, 'w', encoding='utf-8') as f:
    f.write(text)

f2 = 'tests/test_runner.py'
with open(f2, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('env={"PATH": "/usr/bin:/bin", "PYTHONHASHSEED": hashseed},', 'env={**__import__("os").environ, "PYTHONHASHSEED": hashseed, "PYTHONIOENCODING": "utf-8"},')
text = text.replace('env={"PATH": "/usr/bin:/bin"},', 'env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"},')
text = text.replace('env={"PATH": "/usr/bin:/bin", "ARENA_API_KEY": "x"},', 'env={**__import__("os").environ, "ARENA_API_KEY": "x", "PYTHONIOENCODING": "utf-8"},')
with open(f2, 'w', encoding='utf-8') as f:
    f.write(text)
