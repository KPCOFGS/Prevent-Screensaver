# Prevent Screensaver

This Python script prevents the screensaver from activating by periodically moving the mouse. It uses the `pynput` library to simulate mouse movements and `argparse` to allow customization of the interval between movements.

## Requirements
- Python 3.x
- `pynput` library

## Installation

First clone the repository and install needed packages:
```
git clone https://github.com/KPCOFGS/Prevent-Screensaver.git
cd Prevent-Screensaver
python -m pip install -r requirements.txt
```
## Usage
To run the script, use the following command:
```bash
python prevent_screensaver.py <interval>
```
Replace `<interval>` with the number of seconds you want between each mouse movement.

## Example
```bash
python prevent_screensaver.py 120
```
This command will move the mouse every 120 seconds to prevent the screensaver from activating.
### Script Details

The script uses the `pynput` library to control the mouse and simulate small movements. It will continuously move the mouse slightly and then pause for the specified interval.

## Termination

To stop the script, you can interrupt it by pressing `Ctrl+C` in the terminal. The script will handle the interruption gracefully and terminate.
## License

This script is provided under the Unlicense. See the [LICENSE](LICENSE) file for details.
