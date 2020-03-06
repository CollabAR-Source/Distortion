# MobileDistortion dataset
[![Website shields.io](https://img.shields.io/badge/opencv--python-4.1-lightgrey)](http://shields.io/)

To quantify the extent of image distortion in real-world mobile augmented scenarios, we use commodity AR devices, i.e., the Nokia 7.1 smartphone and the MagicLeap One head-mounted AR set, to record videos in different real-world environments (at 30 frames per second). The collected videos comprise the **MobileDistortion** dataset and can be downloaded via https://1drv.ms/u/s!Aqyf-lNI69G1gkdZUz5J6D5jzv4D?e=nILsiW.

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
│   └───Nokia7.1 - Underwater.mp4
|
└───Gaussian Noise
│   │
│   └───Nokia7.1 - Camera zoom In.mp4
│   └───Nokia7.1 - Dark Room.mp4
```

## Extract frames from videos

Follow the procedure below to extract image frames from the videos:  
1. Install the open-cv library before running the python script "*extract_frames.py*".
2. Runing the script by: `python .\extract_frames.py -source_video`

   replace the field `-source_video` by the `PATH of the video` from which you want to extract the frames.
   For instance:  
   `python .\extract_frames.py .\Distortion\Motion Blur\MotionBlur Outdoor.mp4`
4. You should be able to see the generated folder that contains extracted images in the folder "frames".

  
 
