# Applied deep learning project
Alina Jaud - 12209471

## Idea and project type
I want to create an application that can measure the performance of drummers practicing on a drum pad. The application should track sticks on a video where a drummer is playing on a drum pad. The tracked sticks can be used to record the playing and calculate some metrics, for example the stick height on left and right hand, the straightness of the hits or the angle of the hits. These metrics can help the player to improve their drumming.
For this project I chose the project category “bring your on data”.
## Background research
There are several approaches in tracking drumsticks with deep learning technologies. The majority of the methods are built to enable air drumming, which means moving sticks in the air without an actual drumset. Hong et al. [1] propose a framework that can detect drumsticks with markes on the tip using YOLOv8 (todo quelle). Yadid et al. [2] provide a markerless approach with the YOLOv5 model. Both approaches give valuable insights in their dataset creation and network training but have not published their datasets. Since they both focus on air drumming, they did not train their networks on frames of people drumming on an actual drum pad.
Additional to stick tracking, hand pose tracking can generate valuable metrics for drum performance analytics. Therefore OpenPose [3] and MediaPipe [4] are considered to be used in the application.
## Approach
A major part of the project will be dataset creation. I plan to use a smartphone camera and a tripod to record videos from different angles. The dataset will then be split into frames and annotated with Roboflow [5] or CVAT [6]. Rotation and brightness change will be applied to reduce the number of necessary samples and introduce robustness. For training, I will use a pre-trained network. In a final application, a platform to upload a video will be provided. Th application can then calculate some easy metrics like stick height.
## Schedule
* Now – 1. 11: Recording videos
* 2.11 – 10. 11: preprocess videos for data annotation
* 11.11 – 1. 12: Create annotations
* 1.12 – 17.12: Use a pre-trained model and test against a minimal dataset (deadline assignment 2)
* 18.12.-6.1. Improve quality of dataset, adjust model
* 7.01-21.01. Build application around model (deadline assignment 2)
## References
[1]	S. Hong, K. Stephen, and T. Kenji, “Virtual Drum System Development using Motion Detection,” IIAI Letters on Informatics and Interdisciplinary Research, vol. 5, p. 1, 2024, doi: 10.52731/liir.v005.263.

[2]	H. Yadid, A. Algranti, M. Levin, and A. Taitler, “A2D: Anywhere Anytime Drumming,” 2023.

[3]	Z. Cao, G. Hidalgo, T. Simon, S.-E. Wei, and Y. Sheikh, “OpenPose: Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields,” 2018.

[4]	Mediapipe: A framework for perceiving and processing reality, 2019.

[5]	F. Ciaglia, F. S. Zuppichini, P. Guerrie, M. McQuade, and J. Solawetz, “Roboflow 100: A Rich, Multi-Domain Object Detection Benchmark,” 2022.

[6]	CVAT, CVAT Documentation. [Online]. Available: https://docs.cvat.ai/docs/

