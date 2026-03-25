# lib/

This folder contains external CircuitPython libraries.

## Setting up libraries

Download libraries from the **Adafruit CircuitPython Bundle** and place the required `.mpy` files
(or folders) here:

- Download: https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases
- Copy only the libraries you need (conserve flash storage!)

## Currently required

From `sw.md`:

| Library                  | File in Bundle                         |
|--------------------------|----------------------------------------|
| `adafruit_neopixel`      | `src/lib/neopixel.mpy`                 |

## Tip

Use [circup](https://github.com/adafruit/circup) to manage libraries automatically:

```bash
pip install circup
circup install neopixel
```
