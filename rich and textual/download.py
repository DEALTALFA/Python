
from rich.progress import Progress, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn
import requests

def download_file(url, filename):
    # Create custom progress columns
    progress = Progress(
        "[progress.description]{task.description}",
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
    )

    with progress:
        # Create download task
        download_task = progress.add_task("[cyan]Downloading...", total=None)
        
        # Send GET request with stream enabled
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        
        # Update total size for progress bar
        progress.update(download_task, total=total_size)
        
        # Open file and write chunks
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    progress.update(download_task, advance=len(chunk))

# Example usage
url = "https://example.com/file.zip"
filename = "downloaded_file.zip"
download_file(url, filename)