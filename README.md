# Google Firebase Storage TKInter Upload Helper

## Usecase: Need a quick firebase cloud storage uploader for csv (file/folder)

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
1. ![image](https://user-images.githubusercontent.com/22400845/129329452-b5d85c9e-74b5-488a-af5f-a3b1c2c9cc86.png)
   
   Select CSV file, accepts multi file (but only CSV)
2. ![image](https://user-images.githubusercontent.com/22400845/129329584-ad7cc31b-e9d5-444f-94f2-959fb94c62af.png)

   If directory needed, select recursive function (Will upload all in directory)
3. ![image](https://user-images.githubusercontent.com/22400845/129329731-6c238b2e-c501-4f03-865d-164b074c8e7a.png)

   If extra (name) is input, will be placed on the back.
   
---
## Remarks
* If file exists, it will loop from 1 to n, and add _n to the back before file format and upload to the cloud.
