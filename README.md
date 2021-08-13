# Google Firebase Storage TKInter Upload Helper

## Usecase: Need a quick firebase cloud storage uploader for csv (file/folder)

\
&nbsp;

---

## How to use?

1. Generate your serviceAccountKey.json
   1. Goto https://console.firebase.google.com/u/0/
   2. Select your project
   3. On the navigation drawer, select the project overview
   4. Select "Project settings"
   5. On the new page, Select Service Accounts
   6. Download file and rename to serviceAccountKey.json
2. Create a folder called private (same directory as public)
3. Move serviceAccountKey.json to private
4. Change storageBucket to your bucket name accordingly.
5. Run "python public/firebase_uploader.py"

---

## Screenshots
