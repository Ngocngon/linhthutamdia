#!/usr/bin/env python3
"""Chạy trong CI (và có thể chạy tay) trước khi dựng APK: vá www/index.html cho vỏ Android.
Idempotent. Chép app-shim.js vào www/, chuẩn hoá thẻ meta viewport, chèn thẻ script nạp sớm."""
import re, shutil, sys
p = "www/index.html"
s = open(p, encoding="utf8").read()
VP = '<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">'
if re.search(r'<meta[^>]+name=["\']viewport["\'][^>]*>', s, re.I):
    s = re.sub(r'<meta[^>]+name=["\']viewport["\'][^>]*>', VP, s, count=1, flags=re.I)
else:
    s = s.replace("<head>", "<head>\n" + VP, 1)
TAG = '<script src="app-shim.js"></script>'
if TAG not in s:
    s = re.sub(r'(<meta[^>]+viewport[^>]*>)', r'\1\n' + TAG, s, count=1, flags=re.I)
open(p, "w", encoding="utf8").write(s)
shutil.copy("tools/android/app-shim.js", "www/app-shim.js")
print("patched www/index.html + www/app-shim.js")
