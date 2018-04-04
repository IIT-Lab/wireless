# 
Rate Control Algorithm:
We have proposed 2 algorithms, both using a fuzzy controller. To run the below files we need the Fuzzy Logic Designer toolbox to be installed in matlab. It is enough to have the .fis file in the same folder and run the .m file.
RateControlAlgorithm_Algorithm1.m and RateControlAlgorithm_Algorithm1.fis files use algorithm 1 (using SNR and BER)
RateControlAlgorithm_Algorithm2.m and RateControlAlgorithm_Algorithm2.fis files use algorithm 2 (using SNR)

Literature Assignment:
We have written a critical review of the paper 'On Robust Neighbor Discovery in Mobile Wireless
Networks' 

Wireshark: W14
Wireshark_W14.py - The script is used to run Tshark in monitoring mode. It extracts the frame information and length and add increases the value of the counter based on the frame type. The code is encapsulated in a for loop as the wifi disconnects after recording around 13k frames.

wireless - SDR
The file for the SDR assignment has been uploaded.
rtl_sdr -s 2400000 -f 101500000 -g25 capture.bin -> This command is used to capture the audio and we stop recording in 5 seconds.
101.5MHz is the frequent of Sky Radio.
We can call the function with the bellow parameters:
FM_demod(loadFile('capture1.bin'),60000,10,15000,5,2400000);
