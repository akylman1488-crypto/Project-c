include <cstdlib>

extern "C" {
    int detect_change(unsigned char* img1, unsigned char* img2, int size) {
        int diff = 0;
        for(int i=0; i<size; i++) {
            if (abs(img1[i] - img2[i]) > 20) diff++;
        }
        return diff;
    }
    
    bool is_dark(unsigned char* img, int size) {
        long sum = 0;
        for(int i=0; i<size; i++) sum += img[i];
        return (sum / size) < 50;
    }
}
