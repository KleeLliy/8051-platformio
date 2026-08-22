import os
import subprocess
import sys
import serial.tools.list_ports

"""获取系统中的所有串口号"""
def get_serial_ports():
    serial_ports = [port.device for port in serial.tools.list_ports.comports()]
    if serial_ports:
        return serial_ports

    print("无法获取串口号，请确认是否正常连接！")
    return None


"""跨平台执行命令（列表形式）"""
def run_cmd(cmd):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    subprocess.run(cmd, shell=False, check=True)




# ==================== Windows 开发配置 ====================
def Windows_init():
    """Windows平台初始化烧录命令"""
    serial_ports = get_serial_ports()
    if not serial_ports:
        return []  # 无串口返回空列表

    # 参数配置
    # 虚拟环境python可执行文件（路径）
    python = r".venv\Scripts\python.exe"
    # 烧录工具（模块）
    upload_tool = "stcgal"
    # BSL通信协议版本
    BSL = "auto"
    # 固件路径
    bin_path = r".pio\build\STC89C52RC\firmware.hex"


    # 为每个串口生成独立的烧录命令
    cmds = []
    for port in serial_ports:
        cmd = [
            python,
            "-m", upload_tool,  # 让python以模块方式运行stcgal，即执行stcgal包内的__main__.py
            "-P", BSL,  # BSL通信协议版本
            "-p", port, # 绑定当前串口
            bin_path    # 固件路径
        ]
        cmds.append(cmd)

    # 命令示例
    # .venv\Scripts\python.exe -m stcgal -P auto -p COM3 firmware.hex
    return cmds




# ==================== Linux 开发配置 ====================
def linux_init():
    """Linux平台初始化烧录命令"""
    serial_ports = get_serial_ports()
    if not serial_ports:
        return []  # 无串口返回空列表

    # 参数配置
    # 虚拟环境python可执行文件（路径）
    python = ".venv/bin/python"
    # 烧录工具（脚本）
    upload_tool = "stcgal"
    # BSL通信协议版本
    BSL = "auto"
    # 固件路径
    bin_path = ".pio/build/STC89C52RC/firmware.hex"


    # 为每个串口生成独立的烧录命令
    cmds = []
    for port in serial_ports:
        cmd = [
            python,
            "-m", upload_tool,  # 让python以模块方式运行stcgal，即执行stcgal包内的__main__.py
            "-P", BSL,  # BSL通信协议版本
            "-p", port, # 绑定当前串口
            bin_path    # 固件路径
        ]
        cmds.append(cmd)

    # 命令示例
    # .venv/bin/python -m stcgal -P auto -p /dev/ttyUSB0 .pio/build/STC89C52RC/firmware.hex
    return cmds




# ==================== 主程序入口 ====================

if __name__ == '__main__':
    # 根据系统选择初始化函数
    if sys.platform.startswith('win'):
        cmds = Windows_init()
    elif sys.platform.startswith('linux'):
        cmds = linux_init()
    else:
        print(f"不支持的操作系统: {sys.platform}")
        sys.exit(1)

    # 校验命令列表
    if not cmds:
        print("无可用烧录命令，退出")
        sys.exit(1)

    # 遍历执行所有烧录任务
    for idx, cmd in enumerate(cmds, 1):
        target_port = cmd[cmd.index("-p") + 1]  # 提取当前命令的串口号

        print(f"\n----- 执行第 {idx}/{len(cmds)} 个任务，目标串口: {target_port} -----")

        try:
            run_cmd(cmd)
            print(f"串口 {target_port} 烧录完成")
        except subprocess.CalledProcessError:
            print(f"串口 {target_port} 烧录失败，继续下一个")

    print("\n===== 所有烧录任务执行完毕 =====")
