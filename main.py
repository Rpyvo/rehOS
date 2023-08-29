import os
import random

def rehOS_random_number():
    return f"{random.randint(0, 2)}.{random.randint(1, 10)}.{random.randint(1, 30)}"

def run_rehOS():
    user_name = rehOS_random_number()

    while True:
        command = input(f"rehOS\\user\\root@{user_name} >> ")
        if command.lower() == "exit":
            break
        elif command.lower() == "rhelp":
            print("Kullanılabilir Komutlar:")
            print("- rhelp: Komut listesini gösterir")
            print("- exit: rehOS'tan çıkış yaparsınız")
            print("- setName: Kullanıcı adını değiştirir")
            print("- editFile: Dosya oluşturur veya düzenler")
        elif command.lower() == "setname":
            user_name = rehOS_random_number()
            print(f"Kullanıcı adınız başarıyla değiştirildi: root@{user_name}")
        elif command.lower() == "editfile":
            file_name = input("Dosya adı: ")
            content = input("Dosya içeriği: ")
            try:
                with open(file_name, "w") as file:
                    file.write(content)
                    print(f"Dosya başarıyla kaydedildi: {file_name}")
            except Exception as e:
                print(f"Dosya kaydedilirken hata oluştu: {e}")
        else:
            try:
                result = os.popen(command).read()
                print(result)
            except Exception as e:
                print(f"Hata: {e}")

if __name__ == "__main__":
    print("==================== rehOS işletim sistemine hoş geldiniz ====================")
    print("")
    run_rehOS()
