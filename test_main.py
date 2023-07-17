"""Test the message box example"""
from pytestqt.qt_compat import qt_api
from PySide6.QtWidgets import QMessageBox
from main import MainWindow
def test_clicked_noinput(qtbot, monkeypatch):
    """Test the info button"""
    widget = MainWindow()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.button, qt_api.QtCore.Qt.MouseButton.LeftButton)
    assert widget.msgBox.text()=="enter an expression"

def test_clicked_exp_nominmax(qtbot, monkeypatch):
    """Test the info button"""
    widget = MainWindow()
    qtbot.addWidget(widget)
    widget.EXP.setText("x^5")
    qtbot.mouseClick(widget.button, qt_api.QtCore.Qt.MouseButton.LeftButton)

    assert widget.msgBox.text()=="enter a minimum value"
def test_clicked_exp_min_nomax(qtbot, monkeypatch):
    """Test the info button"""
    widget = MainWindow()
    qtbot.addWidget(widget)
    widget.EXP.setText("x^5")
    widget.MIN.setText("50")
    qtbot.mouseClick(widget.button, qt_api.QtCore.Qt.MouseButton.LeftButton)

    assert widget.msgBox.text()=="enter a maximum value"
def test_clicked_exp_min_lrg_max(qtbot, monkeypatch):
    """Test the info button"""
    widget = MainWindow()
    qtbot.addWidget(widget)
    widget.EXP.setText("x^5")
    widget.MIN.setText("50")
    widget.MAX.setText("25")
    qtbot.mouseClick(widget.button, qt_api.QtCore.Qt.MouseButton.LeftButton)

    assert widget.msgBox.text()=="minimum should be smaller then maximum"
def test_clicked_badexp(qtbot, monkeypatch):
    """Test the info button"""
    widget = MainWindow()
    qtbot.addWidget(widget)
    widget.EXP.setText("x^5+6^^")
    widget.MIN.setText("25")
    widget.MAX.setText("50")
    qtbot.mouseClick(widget.button, qt_api.QtCore.Qt.MouseButton.LeftButton)

    assert widget.msgBox.text()=="wrong Expression at <b style=\"color:red;\">x^5+6^</b>"
def test_clicked_badmin(qtbot, monkeypatch):
    """Test the info button"""
    widget = MainWindow()
    qtbot.addWidget(widget)
    widget.EXP.setText("x^5+6^4")
    widget.MIN.setText("2ttsh")
    widget.MAX.setText("50")
    qtbot.mouseClick(widget.button, qt_api.QtCore.Qt.MouseButton.LeftButton)

    assert widget.msgBox.text()=="enter a number for minimum input"
def test_clicked_badmax(qtbot, monkeypatch):
    """Test the info button"""
    widget = MainWindow()
    qtbot.addWidget(widget)
    widget.EXP.setText("x^5+6^4")
    widget.MIN.setText("2")
    widget.MAX.setText("50erre")
    qtbot.mouseClick(widget.button, qt_api.QtCore.Qt.MouseButton.LeftButton)
    assert widget.msgBox.text()=="enter a number for maximum input"

def test_clicked_badmaxandmin(qtbot):
    """Test the info button"""
    widget = MainWindow()
    qtbot.addWidget(widget)
    widget.EXP.setText("x^5+6^4")
    widget.MIN.setText("2ttsh")
    widget.MAX.setText("50tfrd")
    qtbot.mouseClick(widget.button, qt_api.QtCore.Qt.MouseButton.LeftButton)
    assert widget.msgBox.text()=="enter a number for minimum input and maximum input"

def test_clear(qtbot):
    """Test the info button"""
    widget = MainWindow()
    qtbot.addWidget(widget)
    widget.EXP.setText("x^5+6^4")
    widget.MIN.setText("2")
    widget.MAX.setText("50")
    qtbot.mouseClick(widget.button, qt_api.QtCore.Qt.MouseButton.LeftButton)
    assert widget.EXP.text()==widget.MIN.text()==widget.MAX.text()