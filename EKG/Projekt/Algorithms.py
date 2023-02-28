

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import scipy.signal
import wfdb

class Algorithms:
    def __init__(self):
        self.range=[5000,6500]
        self.Fs=250
        self.wfdb=0
        self.resetParameters()
      
        
        
    def resetParameters(self):
        self.MeanBMP=0
        self.MeanR_R=0
        self.NN50=0
        self.SDNN=0
        self.RMSSD=0
        
        
         
    def loadFileCsv(self,path):
        self.wfdb=0
        self.dataCSV=pd.read_csv(path)
        self.CSVFile=np.array(self.dataCSV.T)
        self.csvTime=self.CSVFile[0]/self.Fs
        self.csvSignal=self.CSVFile[-1]
        self.range=[0,len(self.csvTime)]
        self.showPlot(self.csvTime, self.csvSignal, self.range)
        
    def loadFilePkl(self,path):
        self.wfdb=0
        self.dataPKL=pd.read_pickle(path)
        time=np.array([i for i in range(len(self.dataPKL.cs))])
        self.pklTime=time/self.Fs
        self.pklSignal=self.dataPKL.cs
        #self.range=[0,len(self.pklTime)]
        self.showPlot(self.pklTime, self.pklSignal, self.range)
        
        
    def loadFileWfbd(self,path):
        self.wfdb=1
        record = wfdb.rdrecord(path) 
        ar1=[record.p_signal[i][0] for i in range(record.sig_len)]
        ar2=[record.p_signal[i][1] for i in range(record.sig_len)]
        time=np.array([i for i in range(record.sig_len)])
       # self.range=[0,len(ar2)]
        self.wfdbSignal=np.array(ar2[self.range[0]:self.range[1]])
        self.wfdbTime=time/self.Fs
        
        self.showPlot(self.wfdbTime, self.wfdbSignal, self.range)
       
        
    def showPlot(self,timeArray,signalArray,range):
        plots=2
        timeArray=np.array(timeArray)
        self.signalArrayR=np.array(signalArray)
        self.timeArrayR=timeArray[range[0]:range[1]]
        if(self.wfdb==1):
            print("2")
        else:
            self.signalArrayR=self.FiltSignal(signalArray[range[0]:range[1]])
        self.fig,self.ax=plt.subplots(plots,1,figsize=(20,10))
        self.filSig=self.signalArrayR
        temp=self.calcdoublesquare(self.timeArrayR, self.signalArrayR)
        self.signalArrayR=temp[0]
        self.timeArrayR=temp[1]
        self.EKGsignal=self.filSig[:len(self.signalArrayR)]
        self.ax[0].plot(self.timeArrayR,self.EKGsignal,label="ECG")
        self.ax[0].set_xlabel("TIME [s]")
        self.ax[0].set_ylabel("ECG ")
        self.ax[0].legend(loc='best')
        self.ax[0].set_title("ECG")
        
        self.squaredSignal=self.signalArrayR 
        self.signalArrayR=self.normalizeSignal(self.signalArrayR)
        self.signalArrayR=self.setTreshold(self.signalArrayR, 0.03)
        self.QRSwindow=self.windowQRS(self.signalArrayR)
       # self.Peaks=self.calcRpeaks(self.EKGsignal,self.QRSwindow)
        self.Peaks=self.calcRpeaks(self.squaredSignal,self.QRSwindow)
        self.ax[0].plot(self.timeArrayR[self.Peaks],self.EKGsignal[self.Peaks],"x",label="Peaks")
        self.ax[0].legend(loc='best')
        self.QRSindex=self.getBoundarypoints(self.indexOfWindow(self.QRSwindow))
        self.QRSindex=self.oneDimArrayToTwoDim(self.QRSindex)
        self.plotQRS() 
        self.HeartRate=self.calcHearRate(self.Peaks)
        self.plotHR(self.Peaks,self.HeartRate)
        self.R_R=self.calcR_R(self.Peaks)
        #HVR
        self.MeanR_R=self.calcMeanHeartRate(self.R_R)
        self.MeanBMP=60000/self.MeanR_R
        self.SDNN=self.calcSDNN(self.R_R,self.MeanR_R)
        self.RMSSD=self.calcRMSSD(self.R_R)
        self.NN50=self.calcNN50(self.R_R)
        self.NN50Dif=self.calcDifR_R_50ms(self.R_R)
        
        
        self.plotHistogram()
        plt.show()
    
   
   
    def oneDimArrayToTwoDim(self,signalindex):
        plotindex=[]
        for i in range(int(len(signalindex)/2)):
            plotindex.append([signalindex[2*i],signalindex[2*i+1]])
        return plotindex
   
    def plotQRS(self):
        for i in range(len(self.QRSindex)):
            self.ax[0].plot(self.timeArrayR[self.QRSindex[i][0]:self.QRSindex[i][1]],self.EKGsignal[self.QRSindex[i][0]:self.QRSindex[i][1]],"r",label="QRS")
            if(i<1):
                self.ax[0].legend(loc='best')
                
                
    def FiltSignal(self,signalArray):
        W=15/125
        b,a=scipy.signal.butter(7,0.2,btype ='low',analog=False)
        return scipy.signal.filtfilt(b,a,signalArray,padlen=len(signalArray)-1)
        
    def calcdoublesquare(self,timeArray,signalArray):
        data1=[]
        data2=[]
        for i in range(len(signalArray)-1):
           data1.append(signalArray[i+1]-signalArray[i])
        for i in range(len(data1)-1):
           data2.append(data1[i+1]-data1[i])
        return   [np.square(data2),timeArray[:len(data2)]]
    
    def normalizeSignal(self,signalArray):
        return signalArray/np.max(signalArray)
    
    def setTreshold(self,signalArray,Treshold):
        for i in range(len(signalArray)):
            if signalArray[i]<(Treshold):
                signalArray[i]=0
        return signalArray
    
    def windowQRS(self,signalArray):
        for i in range(len(signalArray)):
            if signalArray[i]>0:
                signalArray[i]=1
        filtr=4
        counter=0
        for i in range(len(signalArray)):
            if signalArray[i]==1:
                for j in range(filtr):
                    if signalArray[i+j+1]==0:
                        counter=counter+1
                if counter<4:
                    signalArray[i+1]=1   
            counter=0        
        while(i<len(signalArray)):
            if signalArray[i]==1:
                j=0
                while(signalArray[i+j]==1): 
                    j+=1         
                if j<15:
                    for h in range(j):
                        signalArray[i+h]=0
                else:
                    i=i+j
            i+=1
        return signalArray
    
    
    def calcRpeaks(self,signalArray,windowSignal):
        squareddataWindow=[]
        for i in range(len(signalArray)):
            squareddataWindow.append(abs(signalArray[i]*windowSignal[i]))
        count=0
        
        for i in squareddataWindow:
            if i>0:
                count+=1 
        windowStartPoints=self.getBoundarypoints(self.indexOfWindow(windowSignal))
        windows=[]
        for i in range(int(len((windowStartPoints))/2)):
            windows.append([windowStartPoints[2*i] , windowStartPoints[2*i+1]])
        R_peaks=[]
        for j in range(len(windows)):
            OnewindowSignal=squareddataWindow.copy()
            for i in range(len(OnewindowSignal)):
                if(not(i>=windows[j][0] and i<=windows[j][1])):
                    OnewindowSignal[i]=0
            R_peaks.append(np.argmax(OnewindowSignal))
            
        return R_peaks

    def getWindowedSignal(self,signalArray,windowSignal):
        return signalArray*windowSignal
    
    def indexOfWindow(self,windowSignal):
        return [i for i, e in enumerate(windowSignal) if e == 1]
    
    def getBoundarypoints(self,indexArray):
        windowStartPoints=[]
        windowStartPoints.append(indexArray[0])
        start=indexArray[0]
        for i in range(len(indexArray)-1):
            if((indexArray[i+1]-indexArray[i])>2):
                windowStartPoints.append(indexArray[i])
                windowStartPoints.append(indexArray[i+1])
        windowStartPoints.append(indexArray[-1])  
        
        return windowStartPoints
        
    
    def calcHearRate(self,R_peaks):
        R_R=[]
        for i in range(len(R_peaks)-1):
            R_R.append((R_peaks[i+1]-R_peaks[i])*4)
        HR=[]
        for i in range(len(R_R)):
            HR.append((1/R_R[i])*60000)       
        return HR 
   
    def calcR_R(self,R_peaks):
        R_R=[]
        for i in range(len(R_peaks)-1):
            R_R.append((R_peaks[i+1]-R_peaks[i])*4)
        return R_R
        
    def plotHR(self,Peaks,HR):
        HRindex=[]
        for i in range(len(Peaks)-1):
            HRindex.append([Peaks[i],Peaks[i+1]-1])
        tempHR=[]
        for i in range(len(HRindex)):
            for j in range(HRindex[i][1]-HRindex[i][0]):
                tempHR.append(HR[i])
            self.ax[1].plot(self.timeArrayR[HRindex[i][0]:HRindex[i][1]],tempHR,"r")
            
            tempHR.clear()
            
        self.ax[1].set_xlabel("TIME [s]")
        self.ax[1].set_ylabel("HEART RATE [bpm]") 
        self.ax[1].legend(loc='best')
        self.ax[1].set_title("Heart Rate")
       

    
    def calcMeanHeartRate(self,R_R):
        
        return sum(R_R)/len(R_R)
    
    def calcSDNN(self,R_R,MeanR_R):
        r_r_temp=0
        for i in range(len(R_R)):
            r_r_temp=r_r_temp+(R_R[i]-MeanR_R)
        r_r_temp=r_r_temp/len(R_R)
        return np.sqrt(abs(r_r_temp))
    
    
    def calcRMSSD(self,R_R):
        r_temp=0
        for i in range(len(R_R)-1):
            r_temp=r_temp+((R_R[i+1]-R_R[i])*(R_R[i+1]-R_R[i]))
        r_temp=r_temp/(len(R_R)-1)
        return np.sqrt(r_temp)
    
    def calcNN50(self,R_R):
        nn_temp=0
        
        for i in range(len(R_R)-1):
            if abs(R_R[i+1]-R_R[i])>50:
                #nn_temp=nn_temp+abs(R_R[i+1]-R_R[i])
                nn_temp=nn_temp+1
        return nn_temp
    
    def calcDifR_R_50ms(self,R_R):
        nn_temp=[]
        for i in range(len(R_R)-1):
            nn_temp.append(abs(R_R[i+1]-R_R[i]))
        return nn_temp
    
    def plotHistogram(self):
        n_bins=10
        self.fig, self.axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
        self.axs[0].hist(self.HeartRate, bins=n_bins,label="Heart Rate") 
        self.axs[0].set_xlabel("Heart Rate [bpm]")
        self.axs[0].set_title("Heart Rate")
        self.axs[0].legend(loc='best')
        self.axs[1].hist(self.NN50Dif, bins=n_bins)
        self.axs[1].set_xlabel("time duration [ms]")
        self.axs[1].set_title("R-R peak difference")

       
     