#!/usr/bin/env python3
"""Chạy trong CI sau `npx cap add android`: khoá dọc, chép MainActivity, đặt versionCode."""
import os, re, shutil, sys
run = os.environ.get("GITHUB_RUN_NUMBER", "1")
man = "android/app/src/main/AndroidManifest.xml"
s = open(man, encoding="utf8").read()
if "screenOrientation" not in s:
    s = s.replace("<activity", '<activity\n            android:screenOrientation="portrait"', 1)
open(man, "w", encoding="utf8").write(s)
dst = "android/app/src/main/java/vn/linhthu/tamdia/MainActivity.java"
os.makedirs(os.path.dirname(dst), exist_ok=True)
shutil.copy("tools/android/MainActivity.java", dst)
g = "android/app/build.gradle"
t = open(g, encoding="utf8").read()
t = re.sub(r"versionCode\s+\d+", "versionCode " + run, t, 1)
open(g, "w", encoding="utf8").write(t)
print("patched; versionCode", run)
