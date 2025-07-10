with open('/var/log/auth.log', 'r') as file:
    lines= file.readlines()
ssh_lines= [line for line in lines if 'ssh' in line]
with open('ssh_lines.log','w') as file:
    file.writelines(ssh_lines)