import os
from faker import Faker


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

    Starts creating files at level 0.
    Folders and files are created in the last folder of the previous level.

    :levels: number of folder levels (ie 3 -> 3 levels of folders)
    :nb_folders: number of folders at each level
    :nb_files: number of files at each level
    """

    fake = Faker()

    if levels > 0 and nb_folders == 0:
        nb_folders = 1
        print(f"nb_folders changed to 1 to allow creation of {levels} levels.")

    os.mkdir("generated_tree")
    os.chdir("generated_tree")

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


if __name__ == "__main__":
    create_files_folders(levels=5, nb_folders=0, nb_files=0)






    #screate_file("my_file", "txt")
