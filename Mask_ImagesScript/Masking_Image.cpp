#include <iostream>
#include <vector>
#include <mutex>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

void load_images(int start,int end){
   vector<Mat>img_lst;
   mutex mtx;

#pragma omp parallel for
   for(size_t i=start;i<=end;i++){
      char filename[16];
      sprintf(filename,"%d.jpg",i);
      Mat img = imread(filename);
      if (img.empty()){
         cerr << "ERROR: Failed to load " << filename << endl;
      }
      mtx.lock();
      img_lst.push_back(img);
      mtx.unlock();
   }
   mtx.lock();
   cout << "INFO: Loaded " << img_lst.size() << endl;
   mtx.unlock();
}

int
main(int argc,char*argv[])
{
    load_images(1,122000);
}