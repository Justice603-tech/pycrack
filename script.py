import minecraft_launcher_lib
import subprocess

options = options = minecraft_launcher_lib.utils.generate_test_options()
gamedir = "./.pycrack"
def install(version):
    minecraft_launcher_lib.install.install_minecraft_version(version,gamedir)
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, gamedir, options)
    subprocess.call(minecraft_command)











options["gameDir"] = "./.pycrackdir"
user = input("username>")
options["username"] = user

version = input("version>")
install(version)
