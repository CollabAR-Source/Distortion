# MobileDistortion dataset
[![Website shields.io](https://img.shields.io/badge/opencv----python-4.1-green)](http://shields.io/)

To quantify the extent of image distortion in real-world mobile augmented scenarios, we use commodity AR devices, i.e., the Nokia 7.1 smartphone and the MagicLeap One head-mounted AR set, to record videos in different real-world environments (at 30 frames per second). The collected videos comprise the **MobileDistortion** dataset and can be downloaded via https://1drv.ms/u/s!Aqyf-lNI69G1gkdZUz5J6D5jzv4D?e=nILsiW.

**Summary**:

* [Extract frames from videos](#1)
* [Citation](#2)
* [Acknowledgments](#3)


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
└───Noise
│   │
│   └───Nokia7.1 - Camera zoom In.mp4
│   └───Nokia7.1 - Dark Room.mp4
```

## 1. <span id="1">Extract frames from videos</span>

Follow the procedure below to extract image frames from the videos:  
1. Install the open-cv library before running the python script "*extract_frames.py*".
2. Running the script by: `python .\extract_frames.py -source_video`

   replace the field `-source_video` by the `PATH of the video` from which you want to extract the frames.
   For instance:  
   `python .\extract_frames.py .\Distortion\Motion Blur\MotionBlur Outdoor.mp4`.
4. You should be able to see the generated folder that contains extracted images in the folder "frames".

## 2. <span id="2">Citation</span>

Please cite the following paper in your publications if the dataset helps your research.

     @inproceedings{Liu20CollabAR,
      title={{CollabAR}: Edge-assisted collaborative image recognition for mobile augmented reality },
      author={Liu, Zida and Lan, Guohao and Stojkovic, Jovan and Yunfan, Zhang and Joe-Wong, Carlee and Gorlatova, Maria},
      booktitle={Proceedings of the 19th ACM/IEEE Conference on Information Processing in Sensor Networks},
      year={2020}
    }
  
## 3. <span id="3">Acknowledgments</span>

The authors of this dataset are [Zida Liu](https://zidaliu.github.io/), [Guohao Lan](https://guohao.netlify.com/), and [Maria Gorlatova](https://maria.gorlatova.com/). This work was done in the [Intelligent Interactive Internet of Things Lab](https://maria.gorlatova.com/) at [Duke University](https://www.duke.edu/).

Contact Information of the contributors: 

* zida.liu AT duke.edu
* guohao.lan AT duke.edu
* maria.gorlatova AT duke.edu

This work is supported by the Lord Foundation of North Carolina and by NSF awards CSR-1903136 and CNS-1908051.  
 
