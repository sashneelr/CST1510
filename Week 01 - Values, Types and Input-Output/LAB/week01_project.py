hostname = input("Enter hostname:")
used_gb = float(input("Enter gb used"))
total_gb = float(input("Enter gb total"))
free_gb = total_gb - used_gb
percentage_used = used_gb/total_gb*100

print("=====================")
print("Record Check -",hostname)
print("================")
print(f"used : {used_gb:>8.2f}")
print(f"total : {total_gb:>8.2f}")
print(f"free : {free_gb:>8.2f}")
print(f"percentage : {percentage_used:>8.2f} %")
print("=================")
