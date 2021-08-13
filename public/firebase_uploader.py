import tkinter.filedialog
import tkinter as tk
import os


from typing_extensions import IntVar
from firebase_admin import credentials, initialize_app, storage

# Init firebase with your credentials
cred = credentials.Certificate("../private/serviceAccountKey.json")
initialize_app(cred, {"storageBucket": "streetsafe-mmu.appspot.com"})


fields = "Extra Name", "CSV File", "Recursive"


def fetch(entries):

    final_filelist = []
    upload_file = []
    global final_url
    final_url = []
    if entries[1][1].get() == 1:
        for filename in os.listdir(os.path.dirname(csv_file[0])):
            name, ext = os.path.splitext(filename)
            if ext == ".csv":
                final_filelist.append(filename)
    else:
        for i in csv_file:
            name, ext = os.path.splitext(i)
            if ext == ".csv":
                final_filelist.append(i)

    if entries[0][1].get() != "":
        for i in final_filelist:
            name, ext = os.path.splitext(i)
            data_file_list = os.path.basename(i)
            sub_name, _ = os.path.splitext(data_file_list)
            sub_name = sub_name + "_" + entries[0][1].get() + ext
            upload_file.append([i, sub_name])
    else:
        for i in final_filelist:
            name, ext = os.path.splitext(i)
            data_file_list = os.path.basename(i)
            sub_name, _ = os.path.splitext(data_file_list)
            sub_name = sub_name + ext
            upload_file.append([i, sub_name])

    for i in range(len(upload_file)):
        fn = "iot/" + upload_file[i][1]
        bucket = storage.bucket()
        blob = bucket.blob(fn)

        fileExists = blob.exists()

        counter = 1
        if fileExists:
            sub_name, ext = os.path.splitext(fn)
            new_fn = sub_name + "_" + "0" + ext

        while fileExists:
            first_part = new_fn.rsplit("_", 1)[0]
            last_part = new_fn.rsplit("_", 1)[1]
            middle_part, ext = os.path.splitext(last_part)
            fn = first_part + "_" + str(counter) + ext
            blob = bucket.blob(fn)
            fileExists = blob.exists()
            counter += 1

        blob.upload_from_filename(upload_file[i][0])
        blob.make_public()
        final_url.append(blob.public_url)

    print(final_url)
    modal()


def modal():
    pop = tk.Toplevel(root)
    pop.title("Link to Download")
    pop.config(bg="white")
    for i in final_url:
        text1 = tkinter.Text(pop, state=tkinter.DISABLED, height=3)
        text1.config(state=tkinter.NORMAL)
        text1.insert(1.0, i)
        text1.config(state=tkinter.DISABLED)
        text1.bind("<Button>", lambda event: text1.focus_set())
        text1.pack()


def callback():
    global csv_file
    path = tk.filedialog.askopenfilenames(
        title="Select file", filetypes=(("CSV Files", "*.csv"),)
    )

    csv_file = list(path)

    entry.delete(0, tk.END)
    entry.insert(0, path)


root = tk.Tk()
root.title("Google Firebase Storage Upload Helper")
entries = []
csv_file = []

for field in fields:
    if field == "CSV File":
        frame = tk.Frame(root)
        frame.pack(fill=tk.X)

        lbl = tk.Label(frame, text=field, width=20, anchor="w")
        lbl.pack(side=tk.LEFT, padx=5, pady=5)

        btn = tk.Button(frame, text="Browse", command=callback)
        btn.pack(side=tk.LEFT, padx=5, pady=5)

        entry = tk.Entry(frame)
        entry.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

    elif field == "Recursive":
        frame = tk.Frame(root)
        frame.pack(fill=tk.X)

        lbl = tk.Label(frame, text=field, width=20, anchor="w")
        lbl.pack(side=tk.LEFT, padx=5, pady=5)

        btn_var = tk.IntVar()
        recursive_btn = tk.Checkbutton(frame, variable=btn_var)
        recursive_btn.pack(side=tk.LEFT, fill=tk.X, padx=5, expand=True)

        entries.append((field, btn_var))

    else:
        frame = tk.Frame(root)
        frame.pack(fill=tk.X)

        lbl = tk.Label(frame, text=field, width=20, anchor="w")
        lbl.pack(side=tk.LEFT, padx=5, pady=5)

        entry = tk.Entry(frame)
        entry.pack(fill=tk.X, padx=5, expand=True)

        entries.append((field, entry))


root.bind("<Return>", (lambda event, e=entries: fetch(e)))
frame = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
frame.pack(fill=tk.BOTH, expand=True)

closeButton = tk.Button(root, text="Close", command=root.quit)
closeButton.pack(side=tk.RIGHT, padx=10, pady=5)
okButton = tk.Button(root, text="Upload", command=(lambda e=entries: fetch(e)))
okButton.pack(side=tk.RIGHT)
root.mainloop()

