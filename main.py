from PIL import Image
import numpy as np
import bettercam
import win32api
import win32con
import time

# Initialize the camera and start capturing
cam = bettercam.create()
cam.start((int(1920 / 2 - 200), int(1080 / 2 - 200), int(1920 / 2 + 200), int(1080 / 2 + 200)))

while True:
    # Get the latest frame as an image
    frame = cam.get_latest_frame()

    # Convert the frame to a PIL Image (if not already)
    image = Image.fromarray(frame)  # Adjust if `frame` is already a PIL Image or needs conversion.

    # Convert image to NumPy array for pixel analysis
    image_array = np.array(image)

    # Define the threshold for "close to white"
    threshold = 240

    # Check for pixels where all RGB values are >= threshold
    white_pixels = np.all(image_array >= threshold, axis=-1)

    # Get the coordinates of all "white" pixels
    white_pixel_coords = np.argwhere(white_pixels)
    if (white_pixel_coords.size > 0) and win32api.GetAsyncKeyState(0xA4) != 0:
        print(f"Moving mouse by dx={(white_pixel_coords[0][1])}")
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int((white_pixel_coords[0][1] - 200)), int(((white_pixel_coords[0][0] - 190))), 0, 0)
        # time.sleep(0.00001)
        # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # Mouse down
        # time.sleep(0.00001)
        # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)    # Mouse up
    # Calculate the center of the image
    # center = np.array([image_array.shape[0] / 2, image_array.shape[1] / 2])

    # # Find the closest white pixel to the center
    # if white_pixel_coords.size > 0:
    #     distances = np.linalg.norm(white_pixel_coords - center, axis=1)
    #     closest_pixel_index = np.argmin(distances)
    #     closest_pixel_coords = white_pixel_coords[closest_pixel_index]

    #     print(f"Moving mouse by dx={(closest_pixel_coords[0] - 200)}")
        # win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int((closest_pixel_coords[0] - 200)/10), int(-((closest_pixel_coords[1] - 200)/10)), 0, 0)
        # time.sleep(1)
        # Move the mouse based on relative positions
        # if closest_pixel_coords[0] > 200:
        #     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(-1), int(0), 0, 0)
        # elif closest_pixel_coords[0] < 200:
        #     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(1), int(0), 0, 0)
        # if closest_pixel_coords[1] > 200:
        #     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(0), int(1), 0, 0)
        # elif closest_pixel_coords[1] < 200:
        #     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(0), int(-1), 0, 0)
    # else:
    #     # print("No white pixels found within the threshold.")
    #     pass