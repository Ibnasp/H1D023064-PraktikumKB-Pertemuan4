import random
import datetime

tasks = []

def add_task(task_name):
    task_id = random.randint(100, 999)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = {"id": task_id, "name": task_name, "time": timestamp}
    tasks.append(task)
    print(f"Tugas '{task_name}' ditambahkan dengan ID {task_id} pada {timestamp}")

def view_tasks():
    if not tasks:
        print("Tidak ada tugas.")
    else:
        print("\nDaftar Tugas:")
        for task in tasks:
            print(f"ID: {task['id']}, Nama: {task['name']}, Waktu: {task['time']}")

def remove_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Tugas dengan ID {task_id} telah dihapus.")
            return
    print("Tugas tidak ditemukan.")

while True:
    print("\nMenu:")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")
    
    choice = input("Pilih opsi: ")
    
    if choice == "1":
        task_name = input("Masukkan nama tugas: ")
        add_task(task_name)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_id = int(input("Masukkan ID tugas yang akan dihapus: "))
        remove_task(task_id)
    elif choice == "4":
        print("Terima kasih! Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
