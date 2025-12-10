import os
import zipfile

from worlds.Files import APPlayerContainer


class MhwContainer(APPlayerContainer):
    game = "Monster Hunter World"
    compression_method = zipfile.ZIP_DEFLATED
    patch_file_ending = ".zip"

    def __init__(self, base_path: str, output_directory: str, player, player_name, content):
        container_path = os.path.join(output_directory, base_path + ".zip")
        super().__init__(container_path, player, player_name)
        self.content = content

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        opened_zipfile.writestr("Settings.txt", self.content)
        super().write_contents(opened_zipfile)
