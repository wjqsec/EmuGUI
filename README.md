# Ubuntu
update: `sudo apt-get update && sudo apt-get upgrade`
install QEMU: `sudo apt-get install qemu`

## Install Dependencies:
python: `sudo apt install python3 -y`
pip: `python3 -m pip install --upgrade pip`
安装Qemu: `sudo apt install qemu -y` (更高版本的Ubuntu: `sudo apt install qemu-system -y`)
安装 EmuGUI 所需的 Python 包: `pip3 install PyQt6 PySide6 python-magic requests python-dateutil psutil pyqtdarktheme`

安装 python3-venv, 为了创建虚拟环境，需要安装 python3-venv(Ubuntu 24.04 及更高版本):
`sudo apt install python3-venv -y`
创建虚拟环境(名称为emugui-venv) `python3 -m venv ~/emugui-venv`
激活虚拟环境: `source ~/emugui-venv/bin/activate`


这个错误是 Ubuntu（基于 Debian 的系统）在较新版本（如 Ubuntu 22.04 或更高版本）中引入的 **externally-managed-environment** 限制，防止直接使用 `pip3` 在系统级 Python 环境中安装包。这是为了避免破坏系统依赖的 Python 环境。以下是解决方法，基于错误提示和 EmuGUI 的要求，我推荐使用虚拟环境来安装依赖，这样既安全又不会干扰系统 Python。

### 解决方法：使用虚拟环境安装依赖

1. **确保 Python 和 pip 已安装**
   检查 Python 和 pip 是否已安装：
   ```bash
   python3 --version
   pip3 --version
   ```
   如果未安装 pip，安装它：
   ```bash
   sudo apt install python3-pip -y
   ```

2. **安装 python3-venv**
   为了创建虚拟环境，需要安装 `python3-venv`：
   ```bash
   sudo apt install python3-venv -y
   ```

3. **创建虚拟环境**
   在你的主目录或项目目录中创建一个虚拟环境（例如命名为 `emugui-venv`）：
   ```bash
   python3 -m venv ~/emugui-venv
   ```

4. **激活虚拟环境**
   激活虚拟环境以使用隔离的 Python 环境：
   ```bash
   source ~/emugui-venv/bin/activate
   ```
   激活后，你的终端提示符会变化（例如显示 `(emugui-venv)`），表示你现在在虚拟环境中。

5. **升级虚拟环境中的 pip**
   在虚拟环境中升级 pip：
   ```bash
   pip install --upgrade pip
   ```

6. **安装 EmuGUI 所需的 Python 依赖**
   在虚拟环境中安装所有需要的包：
   ```bash
   pip install PyQt6 PySide6 python-magic requests python-dateutil psutil pyqtdarktheme
   ```

7. **安装 QEMU 和 libxcb-cursor0**
   这些是系统级依赖，不能通过 pip 安装，使用 apt 安装：
   ```bash
   sudo apt install qemu-system libxcb-cursor-dev -y
   ```

8. **验证依赖安装**
   检查 Python 包是否安装成功：
   ```bash
   pip list
   ```
   确认 `PyQt6`、`PySide6`、`python-magic`、`requests`、`python-dateutil`、`psutil` 和 `pyqtdarktheme` 出现在列表中。

9. **运行 EmuGUI**
     - 克隆仓库：
       ```bash
       git clone https://github.com/wjqsec/EmuGUI.git
       cd EmuGUI
       ```
     - 确保仍在虚拟环境中（如果已退出，重新激活：`source ~/emugui-venv/bin/activate`）。
     - 运行主脚本：
       ```bash
       python3 emugui.py
       ```
