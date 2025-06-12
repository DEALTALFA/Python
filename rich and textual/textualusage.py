
from textual.app import App
from textual.widgets import Static
from textual.containers import Container
import psutil
import time

class SystemMonitor(App):
    def __init__(self):
        super().__init__()
        self.cpu_widget = Static()
        self.memory_widget = Static()

    def compose(self):
        yield Container(
            self.cpu_widget,
            self.memory_widget
        )

    async def on_mount(self):
        self.set_interval(1, self.update_stats)

    def update_stats(self):
        # Get CPU usage
        cpu_percent = psutil.cpu_percent()
        self.cpu_widget.update(f"CPU Usage: {cpu_percent}%")

        # Get memory usage
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        memory_used = memory.used / (1024 * 1024 * 1024)  # Convert to GB
        memory_total = memory.total / (1024 * 1024 * 1024)  # Convert to GB
        
        self.memory_widget.update(
            f"Memory Usage: {memory_percent}%\n"
            f"Used: {memory_used:.2f}GB / {memory_total:.2f}GB"
        )

if __name__ == "__main__":
    app = SystemMonitor()
    app.run()