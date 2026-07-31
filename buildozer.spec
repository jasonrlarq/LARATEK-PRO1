[app]

# (str) Title of your application
title = Laratek Pro1

# (str) Package name
package.name = laratekpro1

# (str) Package domain (needed for android packaging)
package.domain = org.laratek

# (str) Source files where the let's go is (relative to directory of spec)
source.dir = .

# (list) Source files to include (let's include everything needed)
source.exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Fullscreen
fullscreen = 0

# (list) Permissions
#android.permissions = INTERNET

# (str) Supported architectures
android.archs = arm64-v8a

# Automatically accept Android SDK licenses so automated builds don't freeze/fail
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if build is run as root (0 = False, 1 = True)
warn_on_root = 1
