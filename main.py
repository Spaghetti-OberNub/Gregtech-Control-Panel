from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QProgressBar, QLabel
import sys
from interpret_sample import get_sample
from interpret_reactor_sample import get_reactor_sample
from get_redstone import RedstoneSignal
from PyQt6.QtCore import QTimer, QStringListModel
from config import lapo_sample_path, reactor_sample_path
from get_redstone import RedstoneSignal
from main_ui import Ui_MainWindow

class ThoriumWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("thorium_widget.ui", self) 

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)


        self.thorium_widgets = []
        for i in range(8):
            current_widget = ThoriumWidget()
            self.thorium_widgets.append(current_widget)
            self.fuel_rod_container.addWidget(current_widget, i // 4 , i % 4)

        self.redstone_list_model = QStringListModel([])
        self.redstone_list_view.setModel(self.redstone_list_model)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_values)
        self.timer.start(250)

    def update_values(self):
        # Lapo Stats
        lapo_stats = get_sample(lapo_sample_path)
        self.capacitorPercent.setValue(round(float((str(lapo_stats["used_capacity"]))[:-1])))
        self.EU_IN.setText(lapo_stats["eu_input"] + " EU/t")
        self.EU_OUT.setText(lapo_stats["eu_output"] + " EU/t")
        self.eu_stored.setText(lapo_stats["eu_stored"][0] + " / " + lapo_stats["total_capacity"][0])

        # Redstone Stats
        signals = []
        for signal in RedstoneSignal.get_active_redstone_list():
            signals.append(f"{signal.active_redstone_id}: {signal.active_redstone_name}")
        self.redstone_list_model.setStringList(signals)


        # Reactor Stats
        reactor_sample = get_reactor_sample(reactor_sample_path)

        reac_activity= f"{reactor_sample["isRunning"]}"
        
        self.reac_activity_label.setText(reac_activity)
        if reac_activity == "Running":
            self.reac_activity_label.setStyleSheet("color: green;")
        else:
            self.reac_activity_label.setStyleSheet("color: red;")

        self.fuel_rod_name.setText(reactor_sample["item_name"])

        for i, widget in enumerate(self.thorium_widgets):
            container = widget.verticalWidget

            rod_name = f"Fuel Rod #{i}"
            container.findChild(QLabel, "rod_name_label").setText(rod_name)

            durability = f"Durability: {reactor_sample[f"{i}-durability"]}%"
            container.findChild(QLabel, "durability_label").setText(durability)

            try:
                container.findChild(QProgressBar, "damage_progress").setValue(int(reactor_sample[f"{i}-durability"]))
            except TypeError:
                print("Could not convert durability to int")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())