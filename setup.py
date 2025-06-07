import os, json


class Setup:
    def __init__(self) -> None:
        self.mainDir = os.path.dirname(os.path.realpath(__file__))
        self.settings_file_path = os.path.join(self.mainDir, "settings.json")
        self.settings = dict(json.load(open(self.settings_file_path)))

        self.dependencies = self.settings['dependencies']
        self.verbose = self.settings['verbose']

    def ChecknInstall(self, pkgs: dict):
        status = dict()

        for pkg, pkg_src in pkgs.items():
            try:
                exec(f"import {pkg}")
                status[pkg] = True

            except ImportError as e:
                if self.verbose:
                    print(f'\033[31;1m[-] ModuleNotFoundError:\033[0m \033[31mNo module named \'\033[1m{pkg}\033[0m\033[31m\'.\033[0m')
                    print(f'\033[33mInstalling \'\033[1m{pkg}\033[0m\033[33m\'...\033[0m')

                try:
                    import pip
                    pip.main(['install', pkg_src])

                except ModuleNotFoundError:
                    print(f"\033[1;31m[-] InstellationError:\033[0m \033[1m'pip' not found, please install 'pip' and try again.\033[0m")
                    exit(1)

        return status
    
    def main(self):
        self.ChecknInstall(self.dependencies)
