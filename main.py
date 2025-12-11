import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from database import create_tables, seed_initial_data_if_empty


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Accessory Store - Project")
        self.setGeometry(100, 100, 800, 600)
        
        


if __name__ == "__main__":
    create_tables()
    seeded = seed_initial_data_if_empty()
    if seeded:
        print("Seeded initial data (customers/products).")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

