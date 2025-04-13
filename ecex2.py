import socket

def is_ip_available(ip, port=80, timeout=2):
    try:
        socket.setdefaulttimeout(timeout)
        conn = socket.create_connection((ip, port))
        conn.close()
        return True
    except Exception:
        return False

def calc_ip_criterion(ip):
    try:
        bytes_list = [int(part) for part in ip.split('.')]
        if len(bytes_list) != 4:
            raise ValueError("Неверный формат IP-адреса.")
        sum_first = bytes_list[0] + bytes_list[1]
        sum_second = bytes_list[2] + bytes_list[3]
        return sum_first, sum_second, (sum_first == sum_second)
    except Exception as e:
        print(f"Ошибка в обработке IP {ip}: {e}")
        return None, None, False

def process_ips(ip_list):
    results = []
    for ip in ip_list:
        available = is_ip_available(ip)
        availability_str = "доступен" if available else "недоступен"
        
        sum_first, sum_second, criterion_met = calc_ip_criterion(ip)
        description = f"Сумма первых байт = {sum_first}, сумма вторых байт = {sum_second}"

        results.append((ip, availability_str, criterion_met, description))
    
    return results

if __name__ == "__main__":
    # Пример списка IP
    ip_addresses = [
        "93.184.216.34",   
        "142.250.68.78",   
        "151.101.1.69",    
        "192.0.2.1",       
        "198.51.100.2"    
    ]

    results = process_ips(ip_addresses)
    print("IPv4-адрес, критерий доступности, признак (Суммы байт)")
    for ip, availability, criterion, desc in results:
        print(f"{ip}, {availability}, {criterion} ({desc})")
