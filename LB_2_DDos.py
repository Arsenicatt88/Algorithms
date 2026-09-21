import random
import time

СКОЛЬКО = 100

logs = []
for i in range(СКОЛЬКО):
    ip = f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    status = random.choice([200, 200, 200, 404, 500, 403, 301])
    logs.append({"ip": ip, "status": status})

print(f"Создано логов: {len(logs)}\n")

print("ДО ОБРАБОТКИ:")
for log in logs:
    print(f"  {log['ip']:<18} | {log['status']}")
print()

start_counting = time.perf_counter()

korziny_statusov = []
for i in range(500):
    korziny_statusov.append([])

for log in logs:
    korziny_statusov[log["status"] - 100].append(log)

logs_po_statusu = []
for korzina in korziny_statusov:
    for log in korzina:
        logs_po_statusu.append(log)

time_counting = time.perf_counter() - start_counting

start_radix = time.perf_counter()

gruppy = []
tekushiy_status = None
tekushaya_gruppa = []
for log in logs_po_statusu:
    if log["status"] != tekushiy_status:
        if tekushaya_gruppa:
            gruppy.append(tekushaya_gruppa)
        tekushiy_status = log["status"]
        tekushaya_gruppa = [log]
    else:
        tekushaya_gruppa.append(log)
if tekushaya_gruppa:
    gruppy.append(tekushaya_gruppa)

tekushiy_spisok = []
for gruppa in gruppy:
    dlya_sortirovki = gruppa
    for nomer_chasti in [3, 2, 1, 0]:
        korziny_ip = []
        for i in range(256):
            korziny_ip.append([])

        for log in dlya_sortirovki:
            chasti = log["ip"].split(".")
            korziny_ip[int(chasti[nomer_chasti])].append(log)

        dlya_sortirovki = []
        for korzina in korziny_ip:
            for log in korzina:
                dlya_sortirovki.append(log)

    for log in dlya_sortirovki:
        tekushiy_spisok.append(log)

time_radix = time.perf_counter() - start_radix
time_total = time_counting + time_radix

print("ПОСЛЕ ОБРАБОТКИ (по статусу, затем по IP):")
for log in tekushiy_spisok:
    print(f"  {log['ip']:<18} | {log['status']}")
print()

status_count = {}
for log in tekushiy_spisok:
    s = log["status"]
    status_count[s] = status_count.get(s, 0) + 1

ip_count = {}
for log in tekushiy_spisok:
    ip = log["ip"]
    ip_count[ip] = ip_count.get(ip, 0) + 1

top_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:5]

print("ПО СТАТУСАМ:")
for s in sorted(status_count.keys()):
    print(f"  {s}: {status_count[s]}")

print("\nТОП-5 IP:")
for ip, count in top_ips:
    print(f"  {ip:<18} — {count}")

print(f"\nВремя: Counting {time_counting:.4f} сек | Radix {time_radix:.4f} сек | Итого {time_total:.4f} сек")