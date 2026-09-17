[app]
title = Snake Game
package.name = snakegame
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0
requirements = python3,kivy

# السطر الجديد لحل مشكلة البناء
p4a.branch = develop

orientation = portrait
fullscreen = 0

android.permissions = 
android.api = 33
android.ndk = 25b
android.accept_sdk_license = True

android.archs = arm64-v8a
