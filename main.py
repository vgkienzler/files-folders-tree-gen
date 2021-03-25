import os
import shutil

from faker import Faker


def folder_overwrite(path: str) -> str:
    """Create folder if it does not exist, if it exists deletes it and recreate.

    :path: path of the folder to create/overwrite
    :return: path to the folder created
    """
    if os.path.exists(path):
            shutil.rmtree(path)
    os.mkdir(path)

    return path


def create_file(file_name: str, extension: str="", validate: bool=False) -> None:
    """ Creates a file and closes it.

    :file_name: name of the file to create
    :extension: extension to add to file_name (optional)
    :validate: to indicate if the extension must be validated against valid_extensions
    list
    """

    valid_extensions = [
        "txt",
        "jpg",
        "xlsx",
        "doc",
        "pdf",
    ]

    try:
        if validate and extension not in valid_extensions:
            raise ValueError
        # Only if extension provided append extension to file_name
        if extension:
            file_name = file_name + "." + extension
    except ValueError:
        print("The extension provided is not in the list of valid extensions.")
    else:
        f=open(file_name, "w+")
        f.close()


def create_files_folders(levels: int, nb_folders: int, nb_files: int) -> None:
    """Creates files and folders in folder "generated_tree"

    Starts creating files and folders inside generated_tree, then Folders and
    files are created in the last folder of the previous level until level = 0.

    :levels: number of folder levels (ie 3 -> 3 levels of folders)
    :nb_folders: number of folders at each level
    :nb_files: number of files at each level
    """

    fake = Faker()

    if levels > 0 and nb_folders == 0:
        nb_folders = 1
        print(f"nb_folders changed to 1 to allow creation of {levels} levels.")

    os.chdir(folder_overwrite("generated_tree"))

    for _ in range(levels):

        for fi in range(nb_files):
            create_file(fake.file_name())

        for fo in range(nb_folders):
            new_dir_name = fake.word()
            if fo == (nb_folders - 1):
                new_dir_name = new_dir_name + "_"
            os.mkdir(new_dir_name)

        os.chdir(new_dir_name)
        print(os.getcwd())


def recursive_create_files_folders(levels: int, nb_folders: int, nb_files: int, fake: Faker) -> None:
    """Creates files and folders recursively"

    Starts creating files at level 0.
    Folders and files are created in all the newly created folders, until level 0
    is reached.

    :levels: number of folder levels (ie 3 -> 3 levels of folders)
    :nb_folders: number of folders at each level
    :nb_files: number of files at each level
    """
    if levels > 0 and nb_folders == 0:
        nb_folders = 1
        print(f"nb_folders changed to 1 to allow creation of {levels} levels.")

    print(f"Creating {nb_folders} folders and {nb_files} files over {levels} levels.")

    for fi in range(nb_files):
        create_file(fake.file_name())

    if levels > 0:
        for fo in range(nb_folders):
            new_dir_name = fake.word()
            os.mkdir(new_dir_name)
            os.chdir(new_dir_name)
            recursive_create_files_folders(levels - 1, nb_folders, nb_files, fake)
            os.chdir("..")


if __name__ == "__main__":
    # create_files_folders(levels=5, nb_folders=0, nb_files=0
    fake = Faker()
    os.chdir(folder_overwrite("generated_tree"))
    recursive_create_files_folders(levels = 2,
                                    nb_folders = 2,
                                    nb_files = 2,
                                    fake = fake)
