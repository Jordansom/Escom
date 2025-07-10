import subprocess

def obtener_lease_info():
    leases = {}
    with open('/var/lib/dhcp/dhcpd.leases', 'r') as file:
        lease_data = file.read().split('lease ')
        for lease in lease_data[1:]:
            lines = lease.split('\n')
            ip = lines[0].strip().split(' ')[0]
            mac = None
            end_time = None
            for line in lines:
                if 'hardware ethernet' in line:
                    mac = line.split(' ')[-1].strip(';')
                if 'ends' in line:
                    end_time = ' '.join(line.split(' ')[-3:]).strip(';')
            leases[ip] = (mac, end_time)
    return leases

def mostrar_lease_info():
    leases = obtener_lease_info()
    for ip, (mac, end_time) in leases.items():
        print(f"IP: {ip}, MAC: {mac}, Expiración: {end_time}")

if _name_ == "_main_":
    mostrar_lease_info()