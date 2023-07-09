import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QPushButton, QTextEdit, QMessageBox, QMainWindow, QDialog, QToolBar, QFileDialog

class NewFileDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create new files")
        self.create_file()
    
    def create_file(self):
        folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'projects')
        new_folder_path = os.path.join(folder_path, 'new_folder')

        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print("The 'new_folder' directory has been created successfully!")
        else:
            print("The 'new_folder' directory already exists!")

        file_path = os.path.join(new_folder_path, 'prompt')
        with open(file_path, 'w') as file:
            file.write('')
        

def delete_directory(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            os.remove(os.path.join(root, file))
    
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))

def delete_files():
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'projects')

    delete_directory(folder_path)

    print("Files and folders have been deleted successfully!")

def create_new_file_dialog():
    dialog = NewFileDialog(window)

class EditPromptWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Prompt")

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'projects', 'new_folder', 'prompt')
        self.load_content()

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_content)

        toolbar = QToolBar()
        toolbar.addWidget(self.save_button)
        self.addToolBar(toolbar)

    def load_content(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                content = file.read()
            self.text_edit.setPlainText(content)

    def save_content(self):
        content = self.text_edit.toPlainText()
        with open(self.file_path, 'w') as file:
            file.write(content)
        self.close()

    def showEvent(self, event):
        super().showEvent(event)
        self.load_content()

def edit_prompt_file():
    global edit_window

    if not edit_window:
        edit_window = EditPromptWindow()
    edit_window.show()

    print("Edit Prompt window opened.")

def export_files():
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'projects')
    
    save_dialog = QFileDialog()
    save_dialog.setFileMode(QFileDialog.DirectoryOnly)
    save_dialog.setWindowTitle("Choose Export Location")
    if save_dialog.exec_():
        export_path = save_dialog.selectedFiles()[0]
        
        subprocess.Popen(['cp', '-r', folder_path, export_path])

    print("Files exported successfully.")

def start_main_script():
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'main.py')
    
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'projects', 'new_folder')

    subprocess.Popen(['python3', script_path, folder_path])

    print("Main script started.")

def remove_colons():
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'projects', 'new_folder', 'workspace')
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if ":" in file:
                new_file = file.replace(":", "")
                os.rename(os.path.join(root, file), os.path.join(root, new_file))
                print(f"Renamed {file} to {new_file}")

    print("Folder names have been corrected successfully.")

def open_workspace_folder():
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'projects', 'new_folder', 'workspace')
    subprocess.Popen(['open', folder_path])

    print("Workspace folder opened.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    app.setStyleSheet("""
        QWidget {
            background-color: #303030;
            color: #F0F0F0;
        }
        QTreeView {
            background-color: #202020;
            border: none;
            color: #F0F0F0;
        }
        QPushButton {
            background-color: #404040;
            color: #F0F0F0;
            border: 1px solid #707070;
            padding: 5px;
        }
        QTextEdit {
            background-color: #202020;
            color: #F0F0F0;
            border: none;
        }
    """)

    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'projects')

    model = QFileSystemModel()
    model.setRootPath(folder_path)

    tree_view = QTreeView()
    tree_view.setModel(model)
    tree_view.setRootIndex(model.index(folder_path))
    tree_view.setColumnWidth(0, 300)
    tree_view.setHeaderHidden(False)

    tree_view.setExpanded(model.index(folder_path), True)

    delete_button = QPushButton("Delete files")
    delete_button.clicked.connect(delete_files)

    create_dialog_button = QPushButton("Create new files")
    create_dialog_button.clicked.connect(create_new_file_dialog)
    
    edit_button = QPushButton("Edit Prompt")
    edit_button.clicked.connect(edit_prompt_file)

    start_script_button = QPushButton("Start Script")
    start_script_button.clicked.connect(start_main_script)

    open_workspace_button = QPushButton("Open Workspace")
    open_workspace_button.clicked.connect(open_workspace_folder)

    remove_colons_button = QPushButton("Name folder Correction")
    remove_colons_button.clicked.connect(remove_colons)

    export_button = QPushButton("Export files")
    export_button.clicked.connect(export_files)

    edit_window = None  # Global variable to hold the EditPromptWindow instance

    window = QWidget()
    window.resize(800, 600)
    layout = QVBoxLayout()
    layout.addWidget(tree_view)
    layout.addWidget(delete_button)
    layout.addWidget(create_dialog_button)
    layout.addWidget(edit_button)
    layout.addWidget(start_script_button)
    layout.addWidget(open_workspace_button)
    layout.addWidget(remove_colons_button)
    layout.addWidget(export_button)
    window.setLayout(layout)
    window.setWindowTitle("Free GPT Engineer Manager")
    window.show()

    print("Application started.")

    sys.exit(app.exec_())

#https://github.com/arkadawa
