# Pneumonia-Detection-Challenge

 The goal is to build a pneumonia detection system, to locate the position of inflammation in an image.  
 
Tissues with sparse material, such as lungs which are full of air, do not absorb the X-rays and appear black in the image. Dense tissues such as bones absorb X-rays and appear white in the image. 
 
While we are theoretically detecting “lung opacities”, there are lung opacities that are not pneumonia related. 
 
In the data, some of these are labeled “Not Normal No Lung Opacity”. This extra third class indicates that while pneumonia was determined not to be present, there was nonetheless some type of abnormality on the image and oftentimes this finding may mimic the appearance of true pneumonia. 
 
Dicom original images: - Medical images are stored in a special format called DICOM files (*.dcm). They contain a combination of header metadata as well as underlying raw image arrays for pixel data. 
