**Author: Runshi Gao(002793874) and Yueyan Li(002190756)**
# Introduction
This project is a LSM-tree based key-value storage. We use LSM-tree as its index. Currently it is a memory-only version. 
# Getting Started
First download the project by:  
`git clone https://github.com/RunshiGao/My-LSMT.git`  

To run the program, you just need python3 installed.  
`python3 main.py`  

Then you will be prompted to input commands, you can type help for more information.  
# Limitation
As mentioned before, currently this is just a memory version. We don't have OOM detection and we assume on integer keys. For file input, we assume keys are seperated by comma.