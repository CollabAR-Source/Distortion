# Distortion

Here is the link for distortion video: https://1drv.ms/u/s!Aqyf-lNI69G1gkdZUz5J6D5jzv4D?e=fskXOy

We use two commodity mobile devices, ie., the Nokia7.1 smart phone and the MagicLeap One head-mounted AR set, to record videos(at 30 fps) in different evironments that suffer three types of image distortion.

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



## Extract frames

You can extract frames by running the script "extract_frames.py".

1. you need to install open-cv, running the script.
2. runing the script: python .\extract_frames.py -source_video <br>
   -source_video -- the original video from which you want to get frames<br>
   
   **ex: python .\extract_frames.py .\Distortion\Motion Blur\MotionBlur Outdoor.mp4**
4. you will see the generated folder that contains distortion images in the folder "frames".

  
 
