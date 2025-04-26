# Height Map Visualization with Shading Techniques

This Python project visualizes height map data using two shading techniques: simple and advanced shading. It generates clear, colorful, and intuitive representations of elevation data, making it suitable for geographic, educational, and graphical applications.

## Features

- **Simple Shading:** Quickly illustrates elevation differences by comparing neighboring height values.
- **Advanced Shading:** Uses normal vector calculations and realistic lighting effects to simulate natural terrain lighting.
- **Color Mapping:** Translates height data into RGB colors using HSV color space for intuitive elevation visualization.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

Install dependencies with:
```bash
pip install numpy matplotlib
```

## Usage

1. **Prepare Data**:
   - Height data file (`.dem`) must have dimensions (width, height) and distance between points on the first line.
   - Subsequent lines contain height values.

   Example (`big.dem`):
   ```
   100 100 1
   10 12 13 ...
   ...
   ```

2. **Run the script:**
   ```bash
   python heightmap_shading.py
   ```

## Example Results

The script outputs two plots:

- **Simple Shading:** Visual differences in elevation are highlighted clearly.
- **Advanced Shading:** Provides realistic visual effects by simulating directional lighting.

