[app]

# (str) Title of your application
title = Laratek Pro1

# (str) Package name
package.name = laratekpro1

# (str) Package domain (needed for android packaging)
package.domain = org.laratek

# (str) Source files where the let's go is (relative to directory of spec)
source.dir = .

# (list) Source files to include
source.exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements (added requests and libraries for API calls)
requirements = python3,kivy,requests,urllib3,certifi,idna,charset_normalizer,idna

# (str) Supported orientations (locked to landscape to match camera sensor)
orientation = landscape

# (int) Fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (str) Supported architectures
android.archs = arm64-v8a

# Automatically accept Android SDK licenses so automated builds don't freeze/fail
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if build is run as root (0 = False, 1 = True)
warn_on_root = 1
