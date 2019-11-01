# Real-world Distortion Image Set

To quantify the extent of image distortion in real-world mobile augmented scenarios, we use commodity AR devices, i.e., the Nokia 7.1 smartphone and the MagicLeap One head-mounted ARset, to record videos in different real-world environments. The collected videos comprise the **MobileDistortion** dataset and can be downloaded via: ***[Link will be made available after acceptance]***

The tree structure of the video set is:
```
Distortion
└───Motion Blur
│   │
│   └───MagicLeap One - MotionBlur Outdoor.mp4
│   └───MagicLeap One - MotionBlur Corridor.mp4
│   └───Nokia7.1 - MotionBlur Outdoor.mp4
│   └───Nokia7.1 - MotionBlur Corridor.mp4
│   
└───Gaussian Blur
│   │
│   └───Nokia7.1 - Foggy.mp4
│   └───Nokia7.1 - Underwater
|
└───Gaussian Noise
│   │
│   └───Nokia7.1 - Camera zoom In.mp4
│   └───Nokia7.1 - Dark Room.mp4
```
The videos are recorded at 30 frames per second.

## Extract frames from videos

To extract image frames from the videos, one can follow the procedure below: simply run the script .

1. Install the open-cv library before running the python script "*extract_frames.py*".
2. Runing the script by: `python .\extract_frames.py -source_video'
   replace `-source_video` by the `PATH` of the video from which you want to extract the frames.
   For instance:   
   `**python .\extract_frames.py .\Distortion\Motion Blur\MotionBlur Outdoor.mp4**'
4. you will see the generated folder that contains distortion images in the folder "frames".

  
 
