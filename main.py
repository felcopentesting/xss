#!/usr/bin/env python3
"""
XSS Pentesting GUI - Main Entry Point
"""
import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()